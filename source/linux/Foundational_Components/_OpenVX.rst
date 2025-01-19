.. http://processors.wiki.ti.com/index.php/Processor_SDK_TIOVX

**********************************
OpenVX
**********************************

.. rubric:: OpenVX
   :name: openvx

OpenVX is an open, Khronos (https://www.khronos.org/openvx/) defined
standard for cross platform acceleration of computer vision
applications. OpenVX enables performance and power-optimized computer
vision processing, with emphasis on embedded and real-time use cases:

-  advanced driver assistance systems (ADAS)
-  face, body and gesture tracking
-  smart video surveillance
-  object and scene reconstruction
-  augmented reality
-  visual inspection
-  robotics and more.

Though originally intended for vision only embedded applications, it may
be extended in future to non-vision applications suitable for data flow
representation.

.. rubric:: TIOVX
   :name: tiovx

TIOVX is TI's implementation of OpenVX Standard.

TIOVX allows users to create vision and compute applications using
OpenVX API. These OpenVX applications can be executed on TI SoCs like
AM57xx (including A15 and C66 cores), following OpenVX 1.1 standard.
TIOVX also provides optimized OpenVX kernels for C66x DSP. An extension
API allows users to integrate their own natively developed custom
kernels and call them using OpenVX APIs.

.. Image:: /images/Tiovx.PNG

|

.. rubric:: TIOVX software
   :name: tiovx-software

+--------------------------------------+--------------------------------------+
| Module/Block                         | Description                          |
+======================================+======================================+
| OpenVX API                           | OpenVX API as defined by Khronos     |
+--------------------------------------+--------------------------------------+
| TIOVX API                            | TI extensions and additional APIs in |
|                                      | order to efficiently use OpenVX on   |
|                                      | TI platforms                         |
+--------------------------------------+--------------------------------------+
| TIOVX Framework                      | TI's implementation of OpenVX spec.  |
|                                      | This layer is agnostic of underlying |
|                                      | SoC, OS platform                     |
+--------------------------------------+--------------------------------------+
| TIOVX Platform                       | This layer binds TIOVX framework to  |
|                                      | a specific platform. Ex, Processor   |
|                                      | Linux SDK for AM57xx SOCs. This      |
|                                      | layer also binds TIOVX framework to  |
|                                      | a specific OS like Linux or TI-RTOS  |
+--------------------------------------+--------------------------------------+
| TIOVX Kernel Wrapper                 | Kernel wrappers allow TI and         |
|                                      | customers to integrate a natively    |
|                                      | implemented kernel into the TIOVX    |
|                                      | framework.                           |
+--------------------------------------+--------------------------------------+
| TIOVX Conformance tests              | OpenVX conformance test from Khronos |
|                                      | to make sure an implementation       |
|                                      | implements OpenVX according to       |
|                                      | specification.                       |
+--------------------------------------+--------------------------------------+

There are two versions of VXLIB kernels: without BAM framework, and
with BAM framework. BAM is a low level framework representing directed
acyclic graph, where EDMA transfers are heavily utilized to bring 2D
memory objects to higher speed L2 memory, thus improving performance
almost twofold.

Current release has kernels with BAM framework. This framework
achieves higher performance via heavy use of EDMA, which brings blocks
of data from remote DDR memory to local L2, while DSP does the
processing. List of these kernels can be checked in
https://git.ti.com/processor-sdk/tiovx/trees/master/kernels/openvx-core/c66x/bam.

.. rubric:: TIOVX DSP Kernels (in VXLIB)
   :name: tiovx-dsp-kernels-in-vxlib

There are 44 kernels in current release of VXLIB (typically there are
multiple implementations for different data types).

Here is complete list of DSP kernel wrappers (wrappers are part of TIOVX):

-  AbsDiff
-  AccumulateSquare
-  Accumulate
-  AccumulateWeighted
-  Add
-  BitwiseAnd
-  BitwiseNot
-  BitwiseOr
-  BitwiseXor
-  Box3x3
-  CannyEd
-  ChannelCombine
-  ChannelExtract
-  ColorConvert
-  ConvertDepth
-  Convolve
-  Dilate3x3
-  EqHist
-  Erode3x3
-  Gaussian3x3
-  HalfscaleGaussian
-  HarrisCorners
-  Histogram
-  IntegralImage
-  Lut
-  Magnitude
-  MeanStdDev
-  Median3x3
-  MinMaxLoc
-  Multiply
-  NonLinearFilter
-  Phase
-  Sobel3x3
-  Subtract
-  Threshold

|

.. rubric:: TIOVX in Processor Linux SDK on AM57xx EVM
   :name: tiovx-in-processor-linux-sdk-on-am57xx-evm

Following TIOVX components are present in EVM filesystem:

+--------------------------+--------------------------+--------------------------+
| Type                     | File path                | Description              |
+--------------------------+--------------------------+--------------------------+
| application              | /usr/bin/tiovx-app\_host | Statically linked Linux  |
|                          |                          | application running      |
|                          |                          | several thousands test   |
|                          |                          | cases, with all          |
|                          |                          | available kernels and    |
|                          |                          | using different test     |
|                          |                          | vectors                  |
+--------------------------+--------------------------+--------------------------+
| DSP firmware             | /lib/firmware/dra7-dsp1- | DSP firmware including   |
|                          | fw.xe66.openvx,          | DSP side of TIOVX        |
|                          |                          | framwork implementation, |
|                          | /lib/firmware/dra7-dsp   | IPC implementation,      |
|                          | 2-fw.xe66.openvx         | DSP kernels (part of     |
|                          |                          | VXLIB DSP library) - for |
|                          |                          | DSP1. This firmware is   |
|                          |                          | loaded at boot time, or  |
|                          |                          | using procedure          |
|                          |                          | mentioned below (to      |
|                          |                          | switch from OCL firmware |
|                          |                          | to TIOVX firmware)       |
+--------------------------+--------------------------+--------------------------+

TIOVX release 1.0.0.0 runs exclusively wrt OpenCL, as both firmwares use
common resources DSP cores and CMEM memory. That is: application can be
either TIOVX-based, or OpenCL -based. Future releases may remove this
limitation and use static split in resources (between OpenCL and
OpenVX). **TIOVX needs CMEM memory with two blocks**: block 0 is big DDR
block for exchange of big buffers (>100MB) and block 1 (~1MB) which is
used as shared memory visible from all cores to exchange shared data
objects (typically in OCMC)

.. rubric:: Switch from OpenCL to OpenVX firmware:
   :name: switch-from-opencl-to-openvxfirmware

Run the command below to switch from OpenCL to OpenVx firmware:

::

    reload-dsp-fw.sh tiovx                   # load openvx firmware and restart dsps

.. rubric:: Run TIOVX test application
   :name: run-tiovx-test-application

First, it is necessary to copy test vectors from
https://git.ti.com/processor-sdk/tiovx/trees/master/conformance_tests/test_data
to EVM filesystem (e.g. ~/tiovx/test\_data).Then run following
commands:

::

    export VX_TEST_DATA_PATH=/home/root/tiovx/test_data  # Set environment variable to point to location of test vectors on EVM
    tiovx-app_host 2>&1 | tee log.txt                    # Run test application, and log output to log.txt

At the end of test (taking roughly 24mins) you can expect report like
this:

::

    ...
    [ N7 ] Execution time for    307200 pixels (avg =    3.584000 ms, min =    3.584000 ms, max =    3.584000 ms)
    [ N8 ] Execution time for    307200 pixels (avg =  171.797000 ms, min =  171.797000 ms, max =  171.797000 ms)
    [ N9 ] Execution time for    307200 pixels (avg =  366.952000 ms, min =  366.952000 ms, max =  366.952000 ms)
    [ G4 ] Execution time for    307200 pixels (avg =  500.146000 ms, min =  500.146000 ms, max =  500.146000 ms)
    [ N1 ] Execution time for       256 pixels (avg =    0.278000 ms, min =    0.278000 ms, max =    0.278000 ms)
    [ N2 ] Execution time for       256 pixels (avg =    0.230000 ms, min =    0.230000 ms, max =    0.230000 ms)
    [ N3 ] Execution time for       256 pixels (avg =    0.281000 ms, min =    0.281000 ms, max =    0.281000 ms)
    [ N4 ] Execution time for       256 pixels (avg =    0.303000 ms, min =    0.303000 ms, max =    0.303000 ms)
    [ N5 ] Execution time for       256 pixels (avg =    0.285000 ms, min =    0.285000 ms, max =    0.285000 ms)
    [ G5 ] Execution time for       256 pixels (avg =    2.169000 ms, min =    2.169000 ms, max =    2.169000 ms)
    [ N1 ] Execution time for       256 pixels (avg =    0.243000 ms, min =    0.243000 ms, max =    0.243000 ms)
    [ N2 ] Execution time for       256 pixels (avg =    0.301000 ms, min =    0.301000 ms, max =    0.301000 ms)
    [ G6 ] Execution time for       256 pixels (avg =    0.871000 ms, min =    0.871000 ms, max =    0.871000 ms)
    [ N1 ] Execution time for       256 pixels (avg =    0.352000 ms, min =    0.352000 ms, max =    0.352000 ms)
    [ N2 ] Execution time for       256 pixels (avg =    0.246000 ms, min =    0.246000 ms, max =    0.246000 ms)
    [ N2 ] Execution time for       256 pixels (avg =    0.324000 ms, min =    0.324000 ms, max =    0.324000 ms)
    [ G7 ] Execution time for       256 pixels (avg =    1.502000 ms, min =    1.502000 ms, max =    1.502000 ms)
    [ N1 ] Execution time for       256 pixels (avg =   75.37000  ms, min =   75.37000  ms, max =   75.37000  ms)
    [ G8 ] Execution time for       256 pixels (avg =   60.474000 ms, min =   60.474000 ms, max =   60.474000 ms)
    [     DONE ] tivxMaxNodes.MaxNodes/0/few_strong_corners/MIN_DISTANCE=3.0/SENSITIVITY=0.10/GRADIENT_SIZE=3/BLOCK_SIZE=5/k=3/VX_INTERPOLATION_NEAREST_NEIGHBOR
    [ -------- ] 1 tests from test case tivxMaxNodes

    [ ======== ]
    [ ALL DONE ] 6217 test(s) from 110 test case(s) ran
    [ PASSED   ] 6217 test(s)
    [ FAILED   ] 0 test(s)
    [ DISABLED ] 7397 test(s)

    To be conformant 6217 required test(s) must pass. Disabled 7397 test(s) are optional.

    #REPORT: 20170927134830 ALL 13614 7397 6217 6217 6217 0 (version 1.1-20170301)
    <-- main:

Please note that last ~3000 lines of test log include performance data
(execution time and number of pixels processed) useful for further
evaluation.

.. rubric:: Switch from OpenVX, back to OpenCL firmware:
   :name: switch-from-openvx-back-to-openclfirmware

After finishing running the TIOVX test application, switch the firmware back to the default for OpenCL:

::

    reload-dsp-fw.sh opencl        # load opencl firmware and restart dsps

.. rubric:: Recompile TIOVX (using Yocto build)
   :name: recompile-tiovx-using-yocto-build

| TIOVX framework implementation is available at
  https://git.ti.com/processor-sdk/tiovx/trees/master
| TIOVX sample application including IPC implementation based on
  standard MessageQ, as well as application running conformance tests,
  can be found at
  https://git.ti.com/processor-sdk/tiovx-app/trees/master
| Additional documentation can be found at
  https://git.ti.com/processor-sdk/tiovx/trees/master/docs
| TIOVX framework and TIOVX-APP can be recompiled like any other
  component, as described in
  http://processors.wiki.ti.com/index.php/Processor_SDK_Building_The_SDK.
  Optionally you can do full rebuild with:

::

    MACHINE=am57xx-evm bitbake tisdk-core-bundle

| For modifying individual components in SDK, please refer to: to
  http://processors.wiki.ti.com/index.php/Processor_SDK_Building_The_SDK#Recipes
| If there is a need to modify source code of TIOVX host library
  (framework) files (A15 side), please do that in:
  tisdk/build/arago-tmp-external-arm-toolchain/work/am57xx\_evm-linux-gnueabi/tiovx-lib-host/01.00.00.00-r1/git/
  folder.
| For example, to modify list of tests executed: update file
  ./tiovx/conformance\_tests/test\_tiovx/test\_main.h, or
  ./tiovx/conformance\_tests/test\_conformance/test\_main.h
| After the source modification, force compile the Library (Linux host
  side), and rebuild the package using:

::

    MACHINE=am57xx-evm bitbake tiovx-lib-host  -f -c compile

::

    MACHINE=am57xx-evm bitbake tiovx-lib-host

| Similarly application code can be modified in:
  ./tisdk/build/arago-tmp-external-arm-toolchain/work/am57xx\_evm-linux-gnueabi/tiovx-app-host/01.00.00.00-r1/git,
  and then force-recompiled and rebuilt using:

::

    MACHINE=am57xx-evm bitbake tiovx-app-host -f -c compile

::

    MACHINE=am57xx-evm bitbake tiovx-app-host

