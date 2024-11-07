.. http://processors.wiki.ti.com/index.php/Processor_SDK_Demos_Video_Analytics

Video Analytics
===============

.. rubric:: Overview
   :name: overview-video-analytics

The Video Analytics demo shipped with the Processor SDK Linux for AM57xx
showcases how a Linux Application running on Cortex A-15 cluster can
take advantage of C66x DSP, 3D SGX hardware acceleration blocks to
process a real-time camera input feed and render the processed output on
display - all using open programming paradigms such as OpenCV, OpenCL,
OpenGL, and Qt and standard Linux drivers for capture/display.

A hand gesture is detected using morphological operators from OpenCV
library. The gesture is used to control a parameter (wind speed) used in
physical simulation of water waves. Result of simulation is visualized
in real-time via 3D rendering of water surface. The hardware IP blocks,
such as IVAHD, M4 cores, are not utilized for this demo.

.. rubric:: Setup
   :name: setup

In order to re-create the demo, user would need a standard `AM572x GP
EVM <http://www.ti.com/tool/TMDXEVM5728>`__ and `Processor SDK Linux
package <http://www.ti.com/tool/PROCESSOR-SDK-AM57X>`__. The demo is
integrated into the Matrix GUI and can be launched by touching the
"Video Analytics" icon on the LCD. The sources to the demo are packaged
in the Processor SDK Linux Installer, under "example-applications"
folder and can be compiled using the SDK's top-level Makefile

.. rubric:: Building Blocks
   :name: building-blocks

-  **Camera Capture**: The camera module on AM572x GP EVM acquires color
   frames of 640x480 resolution. The images are received by the OpenCV
   framework using camera capture class, that depends on the standard
   V4L2 Linux driver (/dev/video1).
-  **Gesture Recognition**: The first 30 frames captured are used to
   estimate the background, and later subtracted to extract the hand
   contour, using erode and dilute operations available in the OpenCV
   Library. Analysis of largest contour is performed to find convex
   hulls. Hand gesture classification is based on ratio of outer and
   inner contour. Several discrete values are sent to wave simulation
   algorithm.
-  **Wave Simulation**: Wave simulation is done in two stages:
   calculation of initial (t=0)) Phillips spectrum followed by spectrum
   updates per each time instant. Height map is generated in both steps
   using 2D IFFT (of spectrum). The Gesture inputs are used to vary the
   wind direction for wave simulation
-  **Graphics Rendering**: Finally, 2D vertex grid is generated with the
   above height map. Fragment rendering uses user-defined texture and
   height dependent coloring.
-  **Display**: The displayed content includes - Camera feed, overlayed
   with the contour detection, and the generated water surface

.. rubric:: Block diagram
   :name: block-diagram

|

.. raw:: html

   <div class="center">

.. raw:: html

   <div class="floatnone">

.. Image:: /images/Va_demo_diagram.png

.. raw:: html

   </div>

.. raw:: html

   </div>

|

.. rubric:: Demo Internals
   :name: demo-internals

.. rubric:: Programming Paradigm
   :name: programming-paradigm

-  Code running on A15 Linux platform is written in C++ and links with
   QT5, OpenCV and OpenCL host side libraries.
-  Code running on DSP C66x is written in OpenCL C
-  Code running on GPU is written in GLSL.
-  Standard V4L2 Linux driver is used for camera capture
-  The demo uses OpenCV 3.1, OpenCL 1.2, OpenGL ES 2.0/GLSL and QT 5.5

.. rubric:: OpenCV (running on ARM A15s)
   :name: opencv-running-on-arm-a15s

| *FLOW: camera color frames from V4L2 driver -> OpenCV based algorithms
  -> single float converted to 4 discrete values*

Video analytics functionality includes simple algorithm to extract
contours of hand, and detect how widely opened the hand is. A parameter
which indicates ratio between convex hull and contours is used to
control physical simulation of waves.This is an output argument
converted to wind speed, in 2.5-10 ms range (4 discrete values).
Initially image background is estimated (for 30 frames) using MOG2
(Mixture Of Gaussians), standard OpenCV algorithm. Later, the background
is subtracted from camera frames, before morphological operations: erode
and dilute are performed.Next two steps include contour detection (which
is also presented in camera view window) and convex hull estimation.
Ratio between outer and inner contour indicates (in 1.1-1.8 range) can
be correlated with number of fingers and how widely are they spread. If
they are more widely spread, parameter is converted to higher wind speed
and waves become higher.

.. rubric:: OpenCL (running on ARM A15s + C66x)
   :name: opencl-running-on-arm-a15s-c66x

| *FLOW: 4 discrete values of wind speed (2.5, 4, 7, 10m/s)  -> OpenCL
  based algorithms -> 256x256 float height map matrix (-1, ..., +1 range
  of vertex heights)*

Wave surface simulation is based on generation of Phillips (2D) spectrum
followed by 2D IFFT (256x256). Both operations are executed by OpenCL
offload to single DSP core. Many details on this algorithm can be found
in
`graphics.ucsd.edu/courses/rendering/2005/jdewall/tessendorf.pdf <http://graphics.ucsd.edu/courses/rendering/2005/jdewall/tessendorf.pdf>`__.
This stage is controlled by wave speed (output of gesture detection
algorithm) using fixed wind direction *(an idea for improvement: wind
direction can be controlled using hand gesture).*

Height map in form of 256x256 float matrix is generated on output and
used by OpenGL based vertex renderer (performed in next step). Wave
surface simulation consists of two steps:

-  initial setup defining starting conditions (wind speed and wind
   direction are used as input in this stage only)
-  update of wave surface height map (Phillips spectrum modification
   generated at t=0, along time axe and 2D IFFT for each time step).

.. rubric:: OpenGL ES (running on ARM A15s + GPU/SGX)
   :name: opengl-es-running-on-arm-a15s-gpusgx

*FLOW: 256x256 float height map matrix + fixed texture -> OpenGL ES
based algorithm -> rendered frame buffers*

OpenGL ES is a subset of Open GL for desktop devices. Important
difference (for this project) is requirement to use vertex buffers and
only triangle strips. Also Qt provides wrapper functions (QOpenGL
functions) created with intention to hide differences between different
OpenGL versions and also to slightly simplify programming. On the
downside, it involves Qt specific syntax (not far from original OpenGL
ES functions). Height Map data (256x256, but sub-sampled by 4x4, hence
64x64 vertices) received from previous stage, are rendered specific
coloring and user supplied JPEG image. Fragment shader does mixing of
texture and color derived from interpolated height giving more natural
visualization. Currently lighting effects are not used (Implementing
this can significantly improve the quality of rendering).

.. rubric:: QT 5 (running on ARM A15)
   :name: qt-5-running-on-arm-a15

*FLOW: user input (mouse and keyboard) -> QT application -> windowing
system and control of above threads*

| qt-opencv-multithreaded
  (`github.com/devernay/qt-opencv-multithreaded <https://github.com/devernay/qt-opencv-multithreaded>`__
  ) is skeleton GUI application providing camera input and some basic
  image processing algorithms. Additional algorithm (w.r.t baseline) is
  hand gesture which starts OpenCV thread and OpenCL simulation thread.
  Wave surface window (detached, 600x400) appears only if hand is put
  (at 2-3ft) in front of EVM camera. Intensity of waves is defined by
  how much fingers are spread.
| Please wait for 2-3 seconds (after start of Gesture detection) before
  putting hand in front of camera, to allow good background estimation.
  Wave display window can be closed by pressing [x] in top right corner,
  and some other algorithm selected or gesture detection restarted (e.g.
  to estimate new background).

.. rubric:: Directory Structure
   :name: directory-structure

The functionality is organized as shows in the files/description below.

+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|      | file name                                                           |  description                                                                                                                                                                                                                                                                                                      |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1    | CameraConnectDialog.cpp/CameraConnectDialog.h                       |                                                                                                                                                                                                                                                                                                                   |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2    | CameraGrab.cpp/CameraGrab.h                                         | Auxilliary camera frame acquisition functions to achieve full FPS                                                                                                                                                                                                                                                 |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 3    | CameraView.cpp/CameraView.h                                         | Major class instantiated after connecting to camera. This class creates processing thread, wavesimulation thread and also instantiates wave display (3D graphics) widget.                                                                                                                                         |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 4    | CaptureThread.cpp/CaptureThread.h                                   | Input (camera) frame buffering.                                                                                                                                                                                                                                                                                   |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 5    | FrameLabel.cpp/FrameLabel.h                                         |                                                                                                                                                                                                                                                                                                                   |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 6    | GeometryEngine.cpp/GeometryEngine.h                                 | Height map mash creation, vertex updates                                                                                                                                                                                                                                                                          |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 7    | Gesture.cpp/Gesture.h                                               | Hand gesture (OpenCV) detection algorith,                                                                                                                                                                                                                                                                         |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 8    | ImageProcessingSettingsDialog.cpp/ImageProcessingSettingsDialog.h   | Settings of parameters used by image processing algorithms.                                                                                                                                                                                                                                                       |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 9    | main.cpp                                                            | main function                                                                                                                                                                                                                                                                                                     |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 10   | MainWindow.cpp/MainWindow.h                                         |                                                                                                                                                                                                                                                                                                                   |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 11   | MatToQImage.cpp/MatToQImage.h                                       | Conversion from OpenCV Mat object to QT QImage object                                                                                                                                                                                                                                                             |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 12   | ProcessingThread.cpp/ProcessingThread.h                             | Main processing thread, frame rate dynamics, invokes variois image processing algorithms                                                                                                                                                                                                                          |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 13   | SharedImageBuffer.cpp/SharedImageBuffer.h                           |                                                                                                                                                                                                                                                                                                                   |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 14   | WaveDisplayWidget.cpp/WaveDisplayWidget.h                           | Wave surface 3D rendering (invokes methods from GeometryEngine.cpp)                                                                                                                                                                                                                                               |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 15   | WaveSimulationThread.cpp/WaveSimulationThread.h                     | Wave surface physical simulation thread - host side of OpenCL dispatch.                                                                                                                                                                                                                                           |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 16   | Buffers.h                                                           |                                                                                                                                                                                                                                                                                                                   |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 17   | Structures.h                                                        |                                                                                                                                                                                                                                                                                                                   |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 18   | Config.h                                                            |                                                                                                                                                                                                                                                                                                                   |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 19   | phillips.cl                                                         | DSP OpenCL phillips spectrum generation kernels and 2D IFFT kernel (invoking dsplib.ae66 optimized 1D FFT). After compilation (by clocl) phillips.dsp\_h is generated, and included in WaveSimulationThread.cpp (ocl kernels are compiled and downloaded in this thread, before run-time operation is started).   |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 20   | vshader.glsl                                                        | Vertex shader (gets projection matrix, position and texture position as input arguments; generates texture coordinate and height for fragment shader                                                                                                                                                              |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 21   | fshader.glsl                                                        | Fragment shader doing linear interpolation of textures and mixing texture with height dependent color, and adds ambient light                                                                                                                                                                                     |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 22   | shaders.qrc                                                         | Specify shader filenames                                                                                                                                                                                                                                                                                          |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 23   | textures.qrc                                                        | Specify texture file (2D block which is linearly interpolated in fragment shader, using position arguments provided by vertex shader)                                                                                                                                                                             |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 24   | qt-opencv-multithreaded.pro                                         | Top level QT make file: phi                                                                                                                                                                                                                                                                                       |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 25   | ImageProcessingSettingsDialog.ui                                    | User interface definition file for modification of algorithm parameters.                                                                                                                                                                                                                                          |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 26   | CameraView.ui                                                       | Camera view user interface definition file - right click mouse action brings up image processing algorithm selection                                                                                                                                                                                              |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 27   | CameraConnectDialog.ui                                              |                                                                                                                                                                                                                                                                                                                   |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 28   | MainWindow.ui                                                       |                                                                                                                                                                                                                                                                                                                   |
+------+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

|

|

|

|

|

|

|

|

|

|

|

|

|

|

|

|

|

|

|

|

|

|

|

|

|

|

|

|

|

|

|

|

.. rubric:: Performance
   :name: performance

The hand gesture detection/wave surface simulation/wave surface
rendering demo pipeline runs at 18-20 fps. For other algorithms (e.g.
smoothing, canny) the pipeline runs at 33-35 fps.

.. rubric:: Licensing
   :name: licensing

The demo code is provided under BSD/MIT License

.. rubric:: FAQ/Known Issues
   :name: faqknown-issues

-  Brighter lighting conditions are necessary for noise-free camera
   input, to allow good contour detection. In poor lighting conditions,
   there would be false or no detection.
-  OpenCV 3.1 version shows low FPS rate for Camera Capture. Hence, a
   custom solution based on direct V4L2 ioctl() calls is adopted
   (cameraGrab.cpp file) to boost the FPS

