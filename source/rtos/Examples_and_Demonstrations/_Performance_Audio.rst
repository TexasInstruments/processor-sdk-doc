.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_Performance_Audio

Introduction
============

This page describes the performance audio demo, developed within Processor SDK RTOS on 66AK2Gx platform.
This demo implements and integrates audio I/O, framework, auto-detection, decoding, audio stream
processing (ASP) and encoding - the foundational building blocks of any performance audio application.
The system block diagram below shows the structure of the demo.

.. Image:: /images/pa_k2g_layout.png
	:scale: 100 %

This demo utilizes Processor SDK features/components:

-  **SYS/BIOS** application utilizing TI-RTOS features for DSP-C66x core and ARM-A15 core
-  **McASP LLD** from PDK for audio input/output
-  **IPC** for inter-processor communications between DSP and ARM
-  **UIA** for instrumentation logging

Requirements
============

Hardware

-  `66AK2Gx Evaluation Module (EVMK2G) <http://www.ti.com/tool/evmk2g>`__
-  `66AK2Gx Audio Daughter Card (AUDK2G) <http://www.ti.com/tool/AUDK2G>`__
-  `Momentum Data Systems (MDS) HDMI repeater kit <http://www.mds.com/products/hdmivideo/>`__ (optional).
   Contact contactsales@mds.com for more information.

Software

-  Code Composer Studio (CCS)
-  Python 2.7.14 and Sed 4.2.1 for Windows only

How to Run the Demo
===================

Hardware Setup
--------------

-  Setup K2G EVM according to the `Quick Start Guide <http://www.ti.com/lit/pdf/sprw292>`__
-  Setup Audio Daughter Card according to the `Quick Start Guide <http://www.ti.com/lit/pdf/sprw287>`__ and attach it to the K2G EVM.
   The Audio Daughter Card connects to the EVM through the JP1 “Audio Expansion” and J12 “Serial Expansion” connectors on EVM.
-  Connect an analog player output to the ADC_IN0-3 input jacks on the Audio Daughter Card.
-  Connect a DVD/Blue-Ray player digital output (S/PDIF) to the MOD1 Digital Input (Optical) connector on the Audio Daughter Card.
-  Connect speakers to DAC_OUT0-3 output jacks on the Audio Daughter Card.
-  Connect a COM port on PC to UART0 port on K2G EVM using a RS-232 cable.
-  Connect XDS2xx USB Onboard Debug Probe to a PC USB port using the USB cable delivered with the EVM.

.. Image:: /images/pa_k2g_EVM_DC_setup.png
	:scale: 70 %

Optional Setup for HDMI
-----------------------

-  Connect the MDS HSR41P to the MDS IFB.

   -  Connect HSR41P J4 “Main” header to the IFB J5 “Main” header using the short 26-wire ribbon cable. Ensure the red wire on the ribbon
      cable is connected between HSR41P J4 Pin1 and IFB J5 Pin1.
   -  Connect HSR41P J7 “Sec” header to the IFB J2 “Sec” header using the short 34-wire ribbon cable. Ensure the red wire on the ribbon
      cable is connected between HSR41P J7 Pin1 and IFB J2 Pin1.

-  Connect the MDS IFB to the Audio Daughter Card. Connect IFB J3 “McASP0” header to Audio Daughter Card “I2S Header” using the supplied
   long 34-wire ribbon cable. Ensure the red wire on the ribbon cable is connected between IFB J3 Pin1 and Audio Daughter Card “I2S Header”
   Pin1 (note the “I2S Header” is only 32 pins, so the two wires on the ribbon cable opposite Pin1 are unused).
-  Connect HDMI cable from audio source (e.g. Blu-ray player) to HSR41P J6 “IN”. Connect HDMI cable to audio sink (e.g. HDMI enabled monitor)
   from HSR41P J8 “HDMI OUT”.
-  Connect 5V AC to USB power supply to IFB power connector J1.

.. Image:: /images/pa_k2g_EVM_DC_HDMI_setup.png
	:scale: 70 %

Software and Tools Setup
------------------------
CCS is required to load the binaries and run the demo. Sed and Python are required for run time reselection of input/output, control and reconfiguration
of decoding and/or audio stream procesing, etc. One may choose to run the demo first and then install Sed and Python for run-time reconfiguration.

-  Download and Install CCS (download link available at Processor SDK download page)
-  Obtain Sed 4.2.1 from http://gnuwin32.sourceforge.net/packages/sed.htm,
   executable installer, sed-4.2.1-setup.exe (click on Setup next to "Complete package, except sources" and download will start).
   Install it to c:/PA_Tools/GnuWin32 (or change installation location in
   <process-sdk installation root>/demos/performance-audio/src/setup_build_env/setup_env.bat.
-  Obtain Python 2.7.14 from https://www.python.org/downloads/release/python-2714/ (click on
   Windows x86 MSI installer, and the installer python-2.7.14.msi will be downloaded automatically).
   Install it to c:/PA_Tools/Python27 (or change installation location in
   <process-sdk installation root>/demos/performance-audio/src/setup_build_env/setup_env.bat.
-  Once Python is installed, open a Command Prompt and go to <process-sdk installation root>/demos/performance-audio/src/setup_build_env. Run setup_env.bat,
   and then go to <process-sdk installation root>/demos/performance-audio/tools/ and run setup.bat
   to install PyAlpha dependencies. Note: since tools/setup.bat will download Python packages from the web, one needs to
   make sure that the proxy environment variables are set properly.

Load and Run Pre-built Binaries
-------------------------------

This demo can be run by loading and running the DSP and ARM binaries through CCS:

#.  Click View -> Target Configurations.
#.  In the Target Configurations window, right click and then click Import Target Configurations.
#.  Browse to <process-sdk installation root>/demos/performance-audio/src/pasrc/test_dsp/targetConfigs, click K2GEVM.ccxml and then click Open.
#.  In the Target Configurations window, right-click on K2GEVM.ccxml and select Launch Selected Configuration.
#.  In the Debug window, right-click on the C66x and select Connect Target. The output from the GEL code invoked on the target connection can be observed in the Console output window. The final line of this output should read "C66xx: GEL Output: DDR3A initialization complete".
#.  In the Debug window, right-click on the CortexA15 and select Connect Target. The output from the GEL code invoked on the target connection can be observed in the Console output window. The final line of this output should read "CortexA15: GEL Output: A15 non secure mode entered".
#.  In the Debug Window, click on the C66x. Then open Run->Load->Load Program. In the Load Program window, click on Browse and double click <process-sdk installation root>/demos/performance-audio/prebuilt-binaries/test_dsp.xe66. Then click OK to load the C66x binary.
#.  In the Debug Window, click on the CortexA15. Then open Run->Load->Load Program. In the Load Program window, click on Browse and double click <process-sdk installation root>/demos/performance-audio/prebuilt-binaries/test_arm.xa15fg. Then click OK to load the CortexA15 binary.
#.  In the Debug window, click on the C66x. Then Open Run->Resume to execute the C66x code.
#.  In the Debug window, click on the CortexA15. Then Open Run->Resume to execute the CortexA15 code.
#.  The CIO Console output window should display memory usage statistics. The final line of output should display the memory usage summary for the EXT NC SHM heap.
#.  Default input interface is S/PDIF. Play music on the media player with S/PDIF output. Sound should come out of speakers connected to analog out DAC_OUT0.

Limitations:

-  If code needs to be reload and rerun, one must terminate the CCS debugging session,
   power cycle the EVM, and start a new CCS debugging session. Then repeat from step 4 listed above.

Run-time Reconfiguration (in Windows only)
------------------------------------------
Please make sure src/setup_build_env/setup_env.bat and tools/setup.bat have both been run to setup the tools path.

Output volume can be changed at run-time via Python scripts through UART:

-  Open a windows command prompt, go to tools folder and use the following command to change output volume:

   -  python.exe pyalpha -I alpha -h pa_i13_evmk2g_io_a -p COM1 writeVOLControlMasterN(<volume level>),
      where <volume level> is level adjustment from default in units of 0.5dB. For example,
      python.exe pyalpha -I alpha -h pa_i13_evmk2g_io_a -p COM1 writeVOLControlMasterN(-24)
      lowers the level by 12dB from default.

Input interface is S/PDIF by default and can be reslected at run-time (Note: interface can be reselected
only when playing is stopped):

-  Switch to HDMI input:

   -  Stop playing
   -  Issue command to change to HDMI input:
      python.exe pyalpha -I alpha -h pa_i13_evmk2g_io_a -p COM1 execPAIInHDMI
   -  Play again using digital player with HDMI output

-  Switch to analog input:

   -  Stop playing
   -  Issue command to change output to ADC slave:
      python.exe pyalpha -I alpha -h pa_i13_evmk2g_io_a -p COM1 execPAIOutAnalogSlave
   -  Issue command to change input to analog:
      python.exe pyalpha -I alpha -h pa_i13_evmk2g_io_a -p COM1 execPAIInAnalog
   -  Play again using analog player

Limitations of run-time reconfiguration as of this release:

-  Input interface reselection can only be done when input is mute.
-  Once analog input is selected, S/PDIF can NOT be selected anymore. One
   must reload the code and rerun the demo.

How to Rebuild the Demo
=======================

The performance audio demo can be rebuilt from the source code, following the
instructions given below.

Setup Environment Variables in Linux
------------------------------------
A bash shell script, <process-sdk installation root>/demos/performance-audio/src/setup_build_env/setup_env.sh,
can be used to set up the environment variables:

-  set the TI tools path and performance audio demo path in setup_env.sh properly.
-  set version numbers of each component to what's going to be used for the build (default is what's delivered in PRSDK).
-  run the shell script using command "source setup_env.sh".

Setup Environment Variables in Windows
--------------------------------------
Batch file <process-sdk installation root>/demos/performance-audio/src/setup_build_env/setup_env.bat can be
used to set up the environment variables.

-  set variable TI_TOOLS_DIR in setup_env.bat properly (default is C:\ti).
-  set version numbers of each component to what's going to be used for the build (default is what's delivered in PRSDK).
-  go to folder <process-sdk installation root>/demos/performance-audio/src/setup_build_env and run setup_env.bat (Note: this
   script MUST be run in the setup_build_env folder.)
-  after running setup_env.bat, run setup_paf.bat in the same folder (Note: setup_env.bat MUST be run before setup_paf.bat).

Rebuild the Demo
----------------

-  Go to source folder: <process-sdk installation root>/demos/performance-audio/src
-  Issue command "make clean" and "make install" for Linux
-  Issue command "gmake clean" and "gmake install" for Windows
-  The rebuilt binaries are placed in src/install/pasdk/debug. They can also be
   found at src/pasdk/test_dsp/bin/debug and src/pasdk/test_arm/bin/debug

Trouble Shooting
================

Problems may be encountered when setting up or running the demo. Here are some common problems and the corresponding solutions:

1.  Sound doesn't come out of the speakers:

   -  Make sure the audio daughter card (and HDMI repeater card if used) is connected well. The `PDK addon audio loopback test
      <index_examples_demos.html#k2g-audio-dc-addon>`__ can be run to verify the setup of EVM and audio daughter card.
   -  In CCS Expressions window, enter variable "asipLoopCount1" and check if it is incrementing. If not, terminate the debug session, power cycle
      the EVM, and restart.

2.  The Python command times out:

   -  Make sure to use UART0 COM port on the EVM. The Python scripts may not work well if J23 USB connector is used for UART communications.

3.  The source code doesn't build:

   -  Make sure the environment variables are set correctly. The default tools location in setup.env may not be where the tools are installed.
      Change TI_TOOLS_DIR to where tools and Proc-SDK components are installed.

4.  Python setup can't install PyAlpha dependencies.

   - Make sure proxy environment variables, HTTP_PROXY and HTTPS_PROXY, are set properly.
