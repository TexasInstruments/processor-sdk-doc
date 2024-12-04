.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_VPS_DRIVERS

Overview
--------

Introduction
^^^^^^^^^^^^

VPS (Video Processing SubSystem) video Drivers allow users to make use
of all video hardware features like 1080P capture, HDMI/LCD/SDTV
display, deinterlacing, scaling. A user can use the drivers in many
different ways like multi-channel capture, memory to memory processing,
display and so on. This document has detailed API description that
user's can use to make use of the VPS drivers.

VPS consists of following modules

-  Video Input Port (VIP) - for video capture functions for the device
-  Video Processing Engine (VPE)- for video operations such as color
   space convertion, deinterlacing, scaling and chroma upsampling
   features.
-  Display SubSystem (DSS) - for LCD outputs on three parallel
   interfaces (DPI1, DPI2, and DPI3) and HDMI

User Interface
--------------

Driver Configuration
^^^^^^^^^^^^^^^^^^^^^

.. rubric::  **Board Specific Configuration**
   :name: board-specific-configuration

All board specific configurations eg:enabling clock and pin-mux for
UART/display/vip pins are required before calling any driver APIs. The
board specific configurations are implemented under
<pdk>/ti/drv/vps/src/boards/src folder.

.. rubric::  **VPS Configuration Structure**
   :name: vps-configuration-structure

For details about individual fields of VPS library structure, see the
Doxygen help by opening
PDK_INSTALL_DIR\\packages\\ti\\drv\\vps\\docs\\doxygen\\html\\index.html.

APIs
^^^^^

The VPS driver API can be broadly divided into the following categories

-  FVID2 API - API used to create, control and use the different VPS
   drivers
-  VPS (Video Processing Sub-system) API - API for all video drivers
-  VPS Control Driver API
-  VPS Capture API - API for video capture drivers
-  VPS VIP Capture API - API specific to VIP capture driver
-  VPS DSSWB Capture API - API specific to DSS WB capture driver
-  VPS Display API - API for video display drivers
-  VPS Display Controller API - API for controlling and configuring
   VENCs in the display subsystem
-  VPS Memory to Memory (M2M) API - API for memory to memory drivers
-  M2M VPE API - API specific to VPE M2M driver
-  External Device API - API for controlling external video devices like
   video decoders, video encoders, video filters, IO expanders,
   Ultra-sonic sensors
-  Platform Specific API - API for platform/board specific control, like
   setting pin muxes, clocks etc
-  Board Specific API - API for board specific features.

In addition to above drivers the VPS package also includes many sample
examples which show how to use the drivers in different ways. Many of
these sample examples use a common set of APIs which a user may find
useful to refer to for use in their final application.

API reference for application:

::

    #include <ti/drv/vps/include/vps_<func>.h>

Application
------------

Examples
^^^^^^^^

+-----------------------+-----------------------+-----------------------+
| Name                  | | Description         | | Expected Results    |
+=======================+=======================+=======================+
| Display Dss           | | Example             | | Application prompts |
| application           |   demonstrating       |   user to select the  |
|                       |   *simple* display    |   test case input in  |
|                       |   yuyv or bgr frames  |   CCS console.        |
|                       |   to the LCD use      |                       |
|                       |   case. Reference     |                       |
|                       |   example for         |                       |
|                       |   developers          |                       |
+-----------------------+-----------------------+-----------------------+
| Display Dss           | | Example             | | Application prompts |
| application (Bare     |   demonstrating       |   user to select the  |
| Metal)                |   *simple* display    |   test case input in  |
|                       |   yuyv or bgr frames  |   CCS console.        |
|                       |   to the LCD use case |                       |
|                       |   for bare metal use  |                       |
|                       |   cases. Reference    |                       |
|                       |   bare metal example  |                       |
|                       |   for developers      |                       |
+-----------------------+-----------------------+-----------------------+
| Display Dss WB        | | Example             | | Application prompts |
| application           |   demonstrating       |   user to select the  |
|                       |   *simple* display    |   test case input in  |
|                       |   Write Back (WB)     |   CCS console.        |
|                       |   yuyv or bgr frames  |                       |
|                       |   to the LCD use      |                       |
|                       |   case. Reference     |                       |
|                       |   example for         |                       |
|                       |   developers          |                       |
+-----------------------+-----------------------+-----------------------+
| Loopback application  | | Example             | | Application prompts |
| (Capture and Display  |   demonstrating       |   user to select the  |
| application)          |   *simple* capture    |   test case input in  |
|                       |   and display yuyv    |   CCS console, please |
|                       |   frames from camera  |   select ov2659       |
|                       |   to the LCD use      |   camera for idkAM57x |
|                       |   case. Reference     |   and OV1063x for     |
|                       |   example for         |   evmAM572x test      |
|                       |   developers          |   cases.              |
+-----------------------+-----------------------+-----------------------+
| Loopback application  | | Example             | | Application prompts |
| Bare metal(Capture    |   demonstrating       |   user to select the  |
| and Display           |   *simple* capture    |   test case input in  |
| application)          |   and display yuyv    |   CCS console, please |
|                       |   frames from camera  |   select ov2659       |
|                       |   to the LCD use case |   camera for idkAM57x |
|                       |   for bare metal.     |   and OV1063x for     |
|                       |   Bare Metal          |   evmAM572x test      |
|                       |   reference example   |   cases.              |
|                       |   for developers      |                       |
+-----------------------+-----------------------+-----------------------+

.. note::

   ::

        * Starting from Processor SDK 4.2 release, idkAM574x support is added for VPS.
        * Starting from Processor SDK 4.2 release, oV1063x camera part support is added for AM572x - GP evm (older Aptina MT9T11 camera is never supported).
        * Starting from Processor SDK 3.2 release, osd101t2587 lcd panel is supported (new part) along with osd101t2045 lcd panel (old part) on idkAM572x
          and idkAM571x boards for all display subsystem examples.
        * The bare metal examples are added starting from Processor SDK 4.0 release
        * Some of the clocks such as 32KHz Sync clock are directly tied to A15 core and need that core to be running. Hence while testing the code on other cores
          such as DSP/IPU, please make sure to disconnect the ARM core after connecting the ARM core & running the GEL files to enable the other cores and before
          loading the executable on that core.


Additional References
---------------------

+-----------------------------------+----------------------------------------+
| **Document**                      | **Location**                           |
+-----------------------------------+----------------------------------------+
| API Reference Manual              | $(TI_PDK_INSTALL_DIR)\\packages\\ti    |
|                                   | \\drv\\vps\\docs\\doxygen\\html\\index.|
|                                   | html                                   |
+-----------------------------------+----------------------------------------+

Building VPS examples
---------------------

-  VPS examples and dependent libraries are built from the top level pdk
   makefile after the environment setup is done using the
   pdksetupenv.sh(bat) file.
-  cd <pdk>/packages
-  pdksetupenv.bat (sh)
-  make vps  : to build vps examples under **<pdk>/ti/packages/binary**
   folder
-  make vps_clean : to clean the vps and vps examples.

VPS examples
------------

Display DSS Example
^^^^^^^^^^^^^^^^^^^

.. rubric::  *Description*
   :name: description

The example exploits the DISPC (Display Controller) and LCD/HDMI outputs
available in the SoC. When run, the test outputs multiple options to
select between to demonstrate the various capacity of the display
subsystem. There is also option to select "Auto Run", when selected runs
all the tests in sequential manner. The example works on outputing a
pre-loaded video frames of YUV422I and BGR888 formats to DP1, DP2 and
DP3 parallel interfaces and also to HDMI output observed on TV set, from
VID1, VID2, VID3 and GFX pipelines. The example also demonstrates
displaying videos combined from GFX and other VID pipelines to DPI1 LCD
output. The example is also enhanced to show the display controler
scaling features. Test that exploits the scalar unit to show all
possible allowed scaling. Maximum scaling ratio supported is the ratio
of the dss functional clock / pixel clk. Please refer to section
"11.2.4.10.4.2 DISPC Scaling limitations" of AM57x Technical Reference
manual for minimum ratio allowed when using the scalar unit.

|

.. rubric::  **Running the Display DSS example**
   :name: running-the-display-dss-example

**Configuring Display**:

-  Make sure the LCD panel is connected to the base EVM before running
   the example binary.
-  Make sure the HDMI is connected to TV from the EVM for HDMI display
   options.
-  For AM571x IDK EVM, installing a shunt on header J51 to short those
   pins

**CCS connection**:

-  Load the generated executable file in CCS
-  Run the application, Select any of the option and load the buffer as
   suggested.
-  Content will be displayed on the LCD panel or HDMI TV connected to
   EVM for test options

.. note::

   -  Test Input files for Display Sample application will be in
      "<pdk>\drv\vps\docs\test_inputs\dss_input_files.rar"

The rar file can be unrar-ed to get the test files using utilities such
as http://www.7-zip.org Please download the latest version of 7-zip from
this website. The command to unrar is: 7z x {file_to_unrar}

When the test program expects the yuyv422 file, please load
**display_yuyv422_prog_packed_1920_1080.tigf** file and when the test
program expects the bgr888 file, please load
**display_gbr888_prog_packed_1920_1080.tigf** file. Each video has 4
frames. Below shows the first frame. If GP EVM is used, only the left
upper corner of the video is displayed as it only has an 800x480 LCD.

.. Image:: /images/488px-Yuyv422.png
.. Image:: /images/488px-Gbr888.png

The test runs bunch of test cases as shown in the test example menu.

**Warning** : Due to A15 MMU protection, memory load while CPU is
running is not possible. Hence below workaround needs to be done for
loading the test files.

#. Power up the board
#. Connect to A15 Core
#. Load both tigf files into memory
#. Do a CPU reset on A15
#. Load example code for core type
#. Run example code

Display DSS WB example
^^^^^^^^^^^^^^^^^^^^^^

.. rubric::  *Description*
   :name: description-1

The WB pipeline allows the use of the hardware processing available
inside the DISPC, such as color space conversion, rescaling, and
compositing to perform memory-to-memory transfer with data processing or
capturing a displayed frame.

.. rubric::  *Running Display DSS WB example*
   :name: running-display-dss-wb-example

The test connection and procedure for this example is very much same as
the running the Display DSS example. In this example, the display output
that is sent to the output is captured and sent to the WriteBack
pipeline.

.. rubric::  **Loopback (Capture and Display) example**
   :name: loopback-capture-and-display-example

.. rubric::  *Description*
   :name: description-2

This is the capture and display example that demonstrates the VIP
captures functions for the devices. VIP incorporates a multi-channel raw
video parser, various video processing blocks, and a flexible Video Port
Direct Memory Access (VPDMA)engine to store incoming video in various
formats. This example demonstrates the video capture of 720P, YUY422
format from the camera sensor (OV2659 for idkAM57x and OV1063x for
evmAM572x) to DPI1 LCD output.

.. rubric::  *Running Loopback example*
   :name: running-loopback-example

-  Make sure OV sensor and LCD Panel is connected to to the board before
   running the binary.

**CCS connection**:

#. Power up the board
#. Connect to the Core
#. Run the application, Select any of the option.
#. Captured Content will be displayed on the LCD panel connected to EVM

|

FAQ
---

.. rubric::  How to reduce the VPS test examples build time using
   makefile?
   :name: how-to-reduce-the-vps-test-examples-build-time-using-makefile

Please refer to `Rebuilding The PDK <index_how_to_guides.html#rebuild-drivers-from-pdk-directory>`__
on how to invoke the build for specific core and specific platform, to save the
build time.

.. rubric::  How to create a CCS project other than VPS loopback
   example?
   :name: how-to-create-a-ccs-project-other-than-vps-loopback-example

To create a CCS project for other VPS examples, please use the existing
text file under
PDK_INSTALL_PATH\packages\ti\drv\vps\examples\ccsprojects\am57xx\bios as
a template:

-  Copy the .txt with desired processor then rename it to a new test
   project name accord to CCS project create convention, see
   `PDK Example and Test Project Creation <index_how_to_guides.html#pdk-example-and-test-project-creation>`__
-  Update the linked source files and include paths
-  The common configuration file and build options can be kept
-  Update pre-defined symbol -D<soc_name> to match your SOC, like
   -DSOC_AM571x, -DSOC_AM572x or -DSOC_AM574x
-  Update the configuration .bld file "-b
   ${PDK_INSTALL_PATH}/ti/build/<soc>/config_<soc>_<core>.bld" to match
   your soc
-  In rtsc.setConfiguroOptions, add -DBOARD=<board_name>, which can be
   idkAM571x, idkAM572x, evmAM572x or idkAM574x
-  Save the file and re-run pdkProjectCreate to create the new added CCS
   project

Below is example for vps_dssExample_evmAM572x_armExampleProject.txt:

``-ccs.linkFile "PDK_INSTALL_PATH/ti/drv/vps/examples/dss/displayDss/src/DisplayDss_main.c"``

-ccs.linkFile
"PDK_INSTALL_PATH/ti/drv/vps/examples/ccsprojects/common/bios/utils/bspCommonBIOS_a15.cfg"

-ccs.setCompilerOptions "-c -mcpu=cortex-a15 -mtune=cortex-a15 -marm
-mfloat-abi=hard -DMAKEFILE_BUILD -DNDEBUG -DTRACE_ENABLE
-DASSERT_ENABLE -DVPS_VIP_BUILD -DVPS_VPE_BUILD -DVPS_DSS_BUILD
-UVPS_ISS_BUILD -UVPS_SIMCOP_BUILD -UVPS_ISS_ISP_DEF -DVPS_VIP1_BUILD
-DVPS_VIP2_BUILD -DVPS_VIP3_BUILD -DVPS_CAPT_BUILD -DVPS_DISP_BUILD
-DSOC_AM572x -Dxdc_target_types__=gnu/targets/arm/std.h
-Dxdc_target_name__=A15F -g -gstrict-dwarf -gdwarf-3 -Wimplicit -Wall
-Wunused -Wunknown-pragmas -ffunction-sections -fdata-sections -MMD -MP
-I${PDK_INSTALL_PATH}/ti/drv/vps
-I${PDK_INSTALL_PATH}/ti/drv/vps/examples/dss/displayDss/src"
-rtsc.enableRtsc

-ccs.setLinkerOptions " -lrdimon -lgcc -lm -lnosys -nostartfiles -static
-Wl,--gc-sections
-L$(BIOS_INSTALL_PATH)/packages/gnu/targets/arm/libs/install-native/arm-none-eabi/lib/fpu
" -rtsc.setConfiguroOptions "-b
${PDK_INSTALL_PATH}/ti/build/am572x/config_am572x_a15.bld
-DBOARD=evmAM572x"

.. rubric::  Can I load any jpeg file into the memory to display through
   DSS?
   :name: can-i-load-any-jpeg-file-into-the-memory-to-display-through-dss

The display uses video, not static image as input. There is no JPEG
decoder so it will not work.

.. rubric::  In DSS example, two input video files are loaded for
   testing, what is their format and how to play them?
   :name: in-dss-example-two-input-video-files-are-loaded-for-testing-what-is-their-format-and-how-to-play-them

The two files are with .tigf extension. Tigf is a local convention that
TI development team followed. The file name (before the extension) shows
what you are attempting to decode: e.g., 24 bit RGB or yuyv422 video
file with 1920x1080 resolutions. To play them:

-  In Linux, use avplay with syntax: avplay -video_size <wxh>
   -pixel_format <format> -f rawvideo <video file>, where wxh is
   1902x1080 and pixel_format is rgb24 or yuyv422

-  In Windows, use yuv player from:
   https://sourceforge.net/projects/raw-yuvplayer/

|
