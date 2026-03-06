.. http://processors.wiki.ti.com/index.php/Processor-sdk-MultiWay-of-ARM-DSP-Communication

This document describes the ways of communication on TI multicore devices. The individual cores in an applicatioin can assume the roles of Host/Device or Master/Slave. This discussion here assumes the Host/Master is ARM® cluster running SMP/Linux and the Device/Slave is the C6xx DSP cluster running TI-RTOS.

.. rubric:: OpenCL
   :name: opencl

OpenCL is a framework for writing programs that execute across
heterogeneous systems, and for expressing programs where parallel
computation is dispatched across heterogeneous devices. It is an open,
royalty-free standard managed by Khronos consortium. On a heterogeneous
SoC, OpenCL views one of the programmable cores as a host and the other
cores as devices. The application running on the host (i.e. the host
program) manages execution of code (kernels) on the device and is also
responsible for making data available to the device. A device consists
of one or more compute units. On the ARM and DSP SoCs, each C66x DSP is
a compute unit. The OpenCL runtime consists of two components: (1) An
API for the host program to create and submit kernels for execution and
(2) A cross-platform language for expressing kernels – OpenCL C – which
is based on C99 C with some additions and restrictions OpenCL supports
both data parallel and task parallel programming paradigms. Data
parallel execution parallelizes the execution across compute units on a
device. Task parallel execution enables asynchronous dispatch of tasks
to each compute unit. For more info, please refer to `OpenCL User’s
Guide <http://downloads.ti.com/mctools/esd/docs/opencl>`__

.. rubric:: Use Cases
   :name: use-cases

-  Offload computation from ARM running Linux or RTOS to the DSPs

.. rubric:: Examples
   :name: examples

Please see `OpenCL
examples <http://downloads.ti.com/mctools/esd/docs/opencl/examples/overview.html>`__

.. rubric:: Benefits
   :name: benefits

-  Easy porting between devices
-  No need to understand memory architecture
-  No need to worry about MPAX and MMU
-  No need to worry about coherency
-  No need to build/configure/use IPC between ARM and DSP
-  No need to be an expert in DSP code, architecture, or optimization

.. rubric:: Drawbacks
   :name: drawbacks

-  Don't have control on system memory layout, etc. to handle optimize
   DSP code

|

.. rubric:: DCE (Distributed Codec Engine)
   :name: dce-distributed-codec-engine

DCE Framework provides an easy way for users to write applications on
devices, such as AM57xx, having hardware accelerators for image and
video. It eanbles and provides remote access to hardware acceleration
for audio and video encoding and decoding on the slave cores. The ARM
user space GStreamer based multimedia application uses GStreamer library
to load and interface with TI GStreamer plugin which handles all the
details specific to use of the hardware accelerator. The plugin
interfaces libdce module that provides the ARM user space API. Libdce
uses RPMSG framework on the ARM which communicates to the counterpart on
the slave core. On the slave core, it uses Codec engine and Frame
Component for the video/image codec processing on IVA.

.. Image:: /images/Mm_software_overview_v3.png

**Overview of the Multimedia Software Stack using DCE**
AM57xx as an example has the following accelerators

-  Image and Video Accelerator (IVA)
-  Video Processing Engine (VPE)
-  C66x DSP cores for offloading certain image/video and/or voice/audio
   processing

Users can leverate open source elements that provide functionality such
as AVI stream demuxing, and audio codec, etc. These along with the ARM
based GStreamer plugins in TI's Processor Linux SDK provide the
abstracts for the accelerator offload.

In AM57xx, the hardware accelerators are capable of the following

-  IVA for multimedia enconding and decoding

   -  Video Decode: H264, MPEG4, MPEG2, and VC1
   -  video Encode: H264, and MPEG4
   -  Image Decode: MJPEG

-  VGE for video operations such as scaling, color space conversion, and
   deinterlacing of the following formats:

   -  Supported Input formats: NV12, YUYV, UYVY
   -  Supported Output formats: NV12, YUYV, UYVY, RGB24, ARGB24, and
      ABGR24

-  DSP for offloading signal processing

   -  Sample Image Processing Kernels integrated in the DSP gstreamer
      plugin: Median2x2, Median3x3, Sobel3x3, Conv5x5, Canny

For more info, please refer to the `DCE Developer’s
Guide <http://processors.wiki.ti.com/index.php/DRA7xx_GLSDK_Software_Developers_Guide>`__

.. rubric:: Use Cases
   :name: use-cases-1

-  audio/video or proprietary codecs processing offload to slave core

.. rubric:: Examples
   :name: examples-1

-  Please see `sample
   application <http://processors.wiki.ti.com/index.php/DRA7xx_GLSDK_Software_Developers_Guide#Running_DSP_sample_applications>`__

.. rubric:: Benefits
   :name: benefits-1

-  Accelerated multimedia codec processing
-  Simplifies the development of multimedia application when interfacing
   with Gstreamer and TI Gstreamer plugin

.. rubric:: Drawbacks
   :name: drawbacks-1

-  Not suitable for non-codec algorithm
-  Need work to add new codec algorithm
-  Need knowledge of DSP programming

|

.. rubric:: Big Data IPC
   :name: big-data-ipc

Big Data is a special use case of TI IPC implementation for High
Performance Computing applications and other Data intensive applications
which often require passing of big data buffers between the multi-core
processors in an SoC. The Big Data IPC provides a high level abstraction
to take care of address translation and Cache sync on the big data
buffers

.. rubric:: Use Cases
   :name: use-cases-2

-  Message/Data exchange for size greater than 512 bytes between ARM and
   DSP

.. rubric:: Examples
   :name: examples-2

-  Please see `Big Data IPC example
   <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/
   index_examples_demos.html#big-data-ipc-example>`__

.. rubric:: Benefits
   :name: benefits-2

-  Capable of handling data greater than 512 bytes

.. rubric:: Drawbacks
   :name: drawbacks-2

-  Need knowledge of DSP memory architecture
-  Need knowledge of DSP configuration and programming
-  TI proprietary API

|

.. rubric:: IPC
   :name: ipc

Inter-Processor Communication (IPC) is a set of modules designed to
faciliate inter-process communication. The communication includes
message passing, streams, and linked lists. The modules provides
services and functions which can be used for communication between ARM
and DSP processors in a multi-processor environment.

-  IPC Module initialized the various subsystems of IPC and synchronizes
   multiple processors.
-  MessageQ Module supports the structured sending and receiving of
   variable length messages.
-  ListMP Module is a linked-list based module designed to provide a
   mean of communication between different processors. It uses shared
   memory to provide a way for multiple processors to share, pass or
   store data buffers, messages, or state information.
-  HeapMP Module provides 3 types of memory management, fixed-size
   buffers, multiple different fixed-size buffers, and variable-size
   buffers.
-  GateMP Module enforces both local and remote context protection
   through its instance.
-  NOtify Module manages the multiplexing/demultiplexing of software
   interrupts over hardware interrupts.
-  SharedRegion Module is designed to be used in a multi-processor
   environment where there are memory regions that are shared and
   accessed across different processors.
-  List Module provides support for creating doubly-linked lists of
   objects
-  MultiProc Module centralizes processor ID management into one module
   in a multi-processor environment.
-  NameServer Module manages local name/value pairs which enables an
   application and other modules to sotre and retrieve values based on a
   name.

| For more info, please refer to `IPC User's Guide
  <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/
  rtos/index_Foundational_Components.html#ipc>`__

.. rubric:: User Cases
   :name: user-cases

-  Message/Data exchange between ARM and DSP

.. rubric:: Examples
   :name: examples-3

-  Please see `IPC Examples
   <Foundational_Components_IPC.html#build-ipc-linux-examples>`__

.. rubric:: Benefits
   :name: benefits-3

-  suitable for those who are familiar with DSP programming
-  DSP code optimization

.. rubric:: Drawbacks
   :name: drawbacks-3

-  Need knowledge of DSP memory architecture
-  Need knowledge of DSP configuration and programming
-  message size is limited to 512 bytes
-  TI proprietary API

|

.. rubric:: Pros and Cons
   :name: pros-and-cons

+------------+----------------------------------------------------------+-----------------------------------------------------------------------------------+
|            | Pros                                                     | Cons                                                                              |
+============+==========================================================+===================================================================================+
| OpenCL     | Easy porting                                             | Customer don’t have control over memory layout etc. to handle optimize DSP code   |
|            | No DSP programming                                       |                                                                                   |
|            | Standard OpenCL APIs                                     |                                                                                   |
+------------+----------------------------------------------------------+-----------------------------------------------------------------------------------+
| DCE        | Accelerated multimedia codec handling                    | Not meant for non-codec algorithms                                                |
|            | Simplifies development when interfacing with GStreamer   | Need work to add new codec algorithms                                             |
|            |                                                          | Codec like APIs                                                                   |
|            |                                                          | Require knowledge of DSP programming                                              |
+------------+----------------------------------------------------------+-----------------------------------------------------------------------------------+
| Big Data   | Full control of DSP configuration                        | Need to know memory architecture                                                  |
|            | Capable of DSP code optimization                         | Need to know DSP configuration and programming                                    |
|            | Not limited to the 512 byte buffer size                  | TI proprietary API                                                                |
|            | Same API supported on multiple TI platforms              |                                                                                   |
+------------+----------------------------------------------------------+-----------------------------------------------------------------------------------+
| IPC        | Full control of DSP configuration                        | Need to know memory architecture                                                  |
|            | Capable of DSP code optimization                         | Need to know DSP configuration and programming                                    |
|            | Same API supported on multiple TI platforms              | Limited to small messages (less than 512 bytes)                                   |
|            |                                                          | TI proprietary API                                                                |
+------------+----------------------------------------------------------+-----------------------------------------------------------------------------------+

|

.. rubric:: Decision Making
   :name: decision-making

The following simple flow chart is provided as a reference when making
decision on which methods to use for ARM/DSP communication. Hardware
capability also need to be considered in the decision making process,
such as if Image and Video Accelerator exists when using DCE.

.. Image:: /images/ARM-DSP_DecisionMaking.jpg

