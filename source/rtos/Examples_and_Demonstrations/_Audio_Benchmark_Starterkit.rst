.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_Audio_Benchmark_Starterkit

Introduction
============

The Audio Benchmark Starterkit is intended to provide an easy and quick
way to benchmark key audio functions on C66x and C674x DSP devices. This
package is intended for users who are new to the TI DSP development
environment and provides an easy path to compare core audio benchmarks
to other implementations. For the purposes of benchmarking we have
selected the following signal processing functions

-  Complex Fast Fourier transform (FFT)
-  Real Block FIR filters with 128 samples, 16 coefficients
-  Cascaded Biquad (2 channels, 3 stages) IIR filter for 128 Samples

The package is also a great way to get familiar with benchmarking
functions on TI DSP with or without TI`s Code Composer Studio
environment. It also intends to provide guidance on the compiler options
and code/data memory placement that allows developers to obtain optimal
performance on TI DSP architecture. The package also demonstrates use of
signal processing functions from TI C6000 DSPLIB which contains several
kernels optimized for TI DSP architectures.

Software Features
=================

-  Benchmark applications for core signal processing functions
-  Makefile and CCS Project scripts to build applications
-  SD card bootable binaries [Supported on SOCs that support SD boot]

Directory Structure
===================

The audio benchmark starterkit is located in the Processor SDK RTOS
release under the directory path

::

    <SDK_INSTALL_PATH>\processor_sdk_rtos_<soc>_x_xx_xx_xx\demos\audio-benchmark-starterkit

|
| The directory structure for the audio benchmark starterkit is shown in
  the image below.

Detailed description of the directory structure is given below:
.. Image:: /images/Audben_dirStructure.png

-  prebuilt-binaries - directory contains prebuilt out files to run the benchmarks.
-  bootimages - SD card boot files to run the benchmarks using SD boot.
-  docs - directory contains ReadMe, Quick start guide and the software manifest for the package.
-  scripts - directory contains .txt script files that is used by BenchmarkProjectCreate
   script to create CCS projects
-  src
   -  common - Contains linker command file and logging functions used by all benchmark tests.
   -  singlePrecision_FFT - Source files for benchmark app for FFT
   -  singlePrecision_FIR - Source files for benchmark app for FIR
   -  singlePrecision_IIR - Source files for benchmark app for IIR

Software Dependencies
=====================

-  `Processor SDK RTOS v3.3 and later <index_overview.html#processor-sdk-for-rtos>`__
-  `Code Composer Studio IDE Environment v7 and later <index_overview.html#code-composer-studio>`__

.. note::
   For correct version of Code Composer Studio to download, please refer
   to the :ref:`Release Notes <processor-sdk-rtos-release-notes>`
   corresponding to the Processor SDK RTOS version that you have
   installed

Supported Hardware
==================

**Platforms supported in Processor SDK RTOS 3.3 and later**

-  `K2G EVM <http://www.ti.com/tool/EVMK2G>`__
-  `AM572x GP EVM <http://www.ti.com/tool/tmdsevm572x>`__
-  `AM571x IDK <http://www.ti.com/tool/TMDXIDK5718>`__

**Platforms planned in Processor SDK RTOS 4.0**

-  `OMAPL138/C6748 LCDK <http://www.ti.com/tool/tmdslcdk6748>`__
-  `K2H EVM rev 1.1 and
   later <http://www2.advantech.com/Support/TI-EVM/EVMK2HX.aspx>`__
-  `K2E EVMs rev 1.0.2.0 and
   later <https://www.einfochips.com/index.php/partnerships/texas-instruments/k2e-evm.html>`__
-  `C6678 EVM <http://www.ti.com/tool/tmdsevm6678>`__
-  `C6657 EVM <http://www.ti.com/tool/tmdsevm6657>`__

QuickStart with How-To-Video
============================

For an easy and visual experience to build and run the benchmark tests,
we have created a short How to video that demonstrates how the Benchmark
Starterkit can be built and run on C66x DSP on the K2G EVM which you can
check out from the link provided below:

-  `Demonstration of Audio Benchmark starterkit demo on 66AK2G02 GP
   EVM <https://training.ti.com/66ak2gx-gp-evm-audio-benchmark-starter-kit-demo>`__

How to Build the Benchmarks
===========================

The benchmark starterkit is designed to build with makefiles as well as
with Code Composer Studio (CCS) IDE Environment. Both the approaches
requires developers to setup the Processor SDK RTOS development
environment. Developers can use either approach based on their
familiarity with the chosen build environment. Let us take a closer look
at both approaches.

Using Makefile
--------------

**Step1 : Setup Processor SDK RTOS build Environment.**

Developers are required to setup the Processor SDK RTOS build
environment as described in :ref:`Processor SDK RTOS Setup environment <Build-The-SDK-Setup-Environment-label>`

#. **set SDK_INSTALL_PATH = C:\\ti\\<Install directory>**
#. **setupenv.bat**

.. note::
   If developers install CCS or Processor SDK RTOS under Custom path then
   they need to refer to the setup instructions described under
   :ref:`Setup environment when installing to a custom path <Processor-SDK-RTOS-Install-In-Custom-Path-label>`

|
**Step2 : Invoke Make from root directory**

The make file in the root director of the audio-starterkit can be used
to build the entire package. To build the benchmark examples:

#. **cd <PROC_SDK_INSTALL_PATH>/demos/audio-benchmark-starterkit**
#. **make all**

.. note::
   The build picks up the SOC information from the SDK setup. Also, in the
   make environment the benchmark application is built to send benchmark
   logs to UART console so that there is no dependency on the CCS IDE
   environment

|
For Other supported options, please type

**For Windows:**

::

    gmake help

**For Linux :**

::

    make help

All available options are provided below:

.. Image:: /images/Make_help.png

Using CCS Projects
------------------

The audio benchmark starterkit does not provide pre-canned CCS Projects
as it is difficult to set up projects to be portable across various
developer build environments. To create CCS Projects with the
benchmarks, developers are required to run the BenchmarkProjectCreate
script provided in the root directory of the starterkit.

**Step1 : Setup Processor SDK RTOS build Environment.**

#. **set SDK_INSTALL_PATH = C:\\ti\\<Install directory>**
#. **set TOOLS_INSTALL_PATH = C:\\ti\\<CCS Install directory>**
#. **setupenv.bat**

.. note::
   CCS by default is installed in the path C:\\ti\\ccsv7 so
   TOOLS_INSTALL_PATH=C:\\ti

Developers are required to setup the Processor SDK RTOS build
environment as described in :ref:`Processor SDK RTOS Setup environment <Build-The-SDK-Setup-Environment-label>`

.. note:: If developers install CCS or Processor SDK RTOS under a Custom path
   then they need to refer to the setup instructions described under :ref:`Setup
   environment when installing to a custom path
   <Processor-SDK-RTOS-Install-In-Custom-Path-label>`

|

**Step 2: Run BenchmarkProjectCreate script to generate CCS Projects**

To generate the CCS Projects

#. **cd $PROC_SDK_INSTALL_PATH/demos/audio-benchmark-starterkit**
#. **BenchmarkProjectCreate [Options]**

The Project create script can be run using the following syntax

::

     BenchmarkProjectCreate.bat <soc> <board> <all>

Description of arguments:

-  **soc** - **K2G (Default)** / K2H/ K2E/ C6678/ C6657/ AM572X/ AM571x/
   OMAPL138
-  **board** - **all (Default)** / <SOC supported EVMs>
-  **module** - **all** / (FFT / FIR / IIR)

::

    Example:
     a) BenchmarkProjectCreate.bat
                 - Creates all module projects for the K2G soc for evmK2G platform
     b) BenchmarkProjectCreate.bat AM572x
                 - Creates all module projects for AM572x soc for evmAM572x and idkAM572x platform
     c) BenchmarkProjectCreate.bat C6657 evmC6657
                 - Creates all modules for C6657 DSP for evmC6657 platform
     d) BenchmarkProjectCreate.bat K2H evmK2H FFT
                 - Creates FFT module project for K2H soc for evmK2H

.. note::
   **Known issue with Processor SDK RTOS 3.3**
   The BenchmarkProjectCreate script uses text files .txt from scripts
   folder to generate the CCS projects. The name for the demo folder was
   updated from "audio-benchmark-kit" to "audio-benchmark-starterkit". This
   will require CCS users to update the name in the .txt file before
   generating the scripts.

   For Example if you are using K2G platform locate file
   Benchmark_FFT_evmK2G_c66ExampleProject.txt,
   Benchmark_FIR_evmK2G_c66ExampleProject.txt and
   Benchmark_IIR_evmK2G_c66ExampleProject.txt and update the demo name in
   the text files from "audio-benchmark-kit" to
   "audio-benchmark-starterkit"

**Step 3: Import Generated CCS Projects in CCS Workspace**

Launch CCS and Import the CCS Project using the Project->Import Existing
CCS Project and browse to the audio-benchmark-starterkit folder

.. Image:: /images/CCS_Project_Browse.png

**Step 4: Build Imported CCS Benchmark Projects**

Right click on the Benchmark Project File and Build the project as shown
below:

.. Image:: /images/Build_Benchmark.png

How to Run the Benchmarks
=========================

The benchmark examples can be run by loading the built out files with an
emulator using the CCS Debug functionality or the examples can be run on
the DSP by creating SD card bootable images using out files. Let us take
a look at both these approaches.

Using CCS
---------

**Step 1: Connect Emulator and UART to Hardware**

-  Refer to the :ref:`Hardware Setup guide <RTOS-SDK-Supported-Platforms>`
   and connect the onboard or external emulator to the Hardware and Host
   machine with CCS installed.

-  Connect the UART cable from the EVM to the Host machine and configure
   the Serial console with following settings:

   -  **Baud Rate**: 115200
   -  **Data Bits**: 8
   -  **Parity**: None
   -  **Flow Control**: Off

**Step 2: Create Target configuration and connect to the DSP**

To connect to the SOC, developers need to create a Target configuration
by following the procedure described in wiki
:ref:`Create_Target_Configuration_File_for_EVM <Create-Target-Configuration-File-for-EVM-label>`

|
Instructions specific to supported EVMs:

-  `K2G GP EVM CCS
   Setup <http://processors.wiki.ti.com/index.php/66AK2G02_GP_EVM_Hardware_Setup#Connect_without_a_SD_card_boot_image>`__
-  `AM572x GP EVM CCS
   Setup <http://processors.wiki.ti.com/index.php/AM572x_GP_EVM_Hardware_Setup#Connect_without_a_SD_card_boot_image>`__

.. note::
   Please refer to :ref:`Hardware User Guide <RTOS-SDK-Supported-Platforms>`
   corresponding to each supported EVM so setup the boot switches to No
   boot if available

|
**Step 3: Loading and Running Benchmark application on the DSP**

-  Load the out file using **Run -> Load -> Load Program** and browse to
   the output binary.
-  After loading the out file, run the benchmark app by Pressing **F8**
   or **Run -> Resume**

|

Using SD card (Supported only on AM57xx and K2G)
------------------------------------------------

**Step 1: Run Create SD script to generate SD bootable binaries**

The root directory in the audio-benchmark-starterkit contains a
create-sd.bat file that will convert the .out files installed int the
bin folder into SD bootable images which will be installed in the path
bin/sd_card_files/<EVM>

The syntax to run the create-sd script is as follows:

::

    create-sd.bat <EVM>

**EVM** : refers to evaluation platfom on which the binaries are meant
to be run

Eg: create-sd evmK2G - Creates SD bootable images for K2G EVM.

**Step 2 : Format and copy the SD card binaries to the SD card**

Create an SD card using the procedure described in :ref:`Creating SD card in Windows <Tools-Create-SD-Card-Windows-label>`
and :ref:`Create SD card in Linux <Tools-Create-SD-Card-Linux-label>`

Copy the "MLO" and "Singleprecision_<Module>_app" to the boot partition
on the SD card.

**Step 3: Boot the Benchmark app by configuring SD boot on the EVM**

-  Configure the boot switches on the evaluation hardware to SD boot.
-  Insert the SD card in the microSD or SD card slot on the board.
-  Connect the UART on the hardware to the Host and configure the host
   to **Baud Rate**\ = 115200, **Data Bits**\ = 8 , **Parity**\ = None,
   **Flow Control**\ = Off
-  Power on the EVM to view the output on the Serial console on the host

Benchmark App output on UART console
====================================

.. Image:: /images/FFTbenchmark_sdBoot.png

Benchmark Starterkit Implementation
-----------------------------------

.. rubric:: Signal Processing functions used in Starterkit
   :name: signal-processing-functions-used-in-starterkit

.. rubric:: Single Precision FFT: DSPF_sp_fftSPxSP (Mixed Radix Forward
   FFT )
   :name: single-precision-fft-dspf_sp_fftspxsp-mixed-radix-forward-fft

The audio benchmark kit uses the FFT implementation(DSPF_sp_fftSPxSP)
from the `TI DSP
Library <http://processors.wiki.ti.com/index.php/Software_libraries#DSPLIB>`__.
The DSPF_sp_fftSPxSP kernel calculates the discrete Fourier transform of
complex input array ``ptr_x`` using a mixed radix FFT algorithm. The
result is stored in complex output array ``ptr_y`` in normal order. Each
complex array contains real and imaginary values at even and odd
indices, respectively. DSPF_sp_fftSPxSP kernel is implemented in
assembly to maximize performance, but a natural C implementation is also
provided. The demonstration app for this kernel includes the required
bit reversal coefficients, ``brev``, and additional code to calculate
the twiddle factor coefficients, ``ptr_w``.

|

.. note::
   -  For implementation details of this FFT computation refer to
      documentation provided in `Additional resources <index_examples_demos.html#additional-resources>`__
   -  For Real input sequences, efficient FFT Implementation is described
      here
      `Efficient_FFT_Computation_of_Real_Input <http://processors.wiki.ti.com/index.php/Efficient_FFT_Computation_of_Real_Input>`__

.. rubric:: Single Precision FIR: DSPF_sp_fir_cplx (Complex FIR Filter)
   :name: single-precision-fir-dspf_sp_fir_cplx-complex-fir-filter

The audio benchmark kit uses the FFT implementation(DSPF_sp_fftSPxSP)
from the `TI DSP
Library <http://processors.wiki.ti.com/index.php/Software_libraries#DSPLIB>`__.
The DSPF_sp_fir_cplx kernel performs complex FIR filtering on complex
input array x with complex coefficient array h. The result is stored in
complex output array y. For each complex array, real and imaginary
elements are respectively stored at even and odd index locations.

The API reference and the implementation details can found in the TI
DSPLIB documentation included in the Processor SDK.

.. rubric:: Single Precision IIR : tisigCascadeBiquadSP_2c_3s_kernel
   (Cascade Biquad Filter for Multichannel input)
   :name: single-precision-iir-tisigcascadebiquadsp_2c_3s_kernel-cascade-biquad-filter-for-multichannel-input

The Cascade biquad filtering function in the audio benchmark starterkit
is an improved biquad infinite impulse response filter `Patent
US20160112033
Pending <http://appft1.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PG01&p=1&u=/netahtml/PTO/srchnum.html&r=1&f=G&l=50&s1=20160112033.PGNR.>`__.
The new filter structure modifies the feedback path in the filter,
resulting in a significant reduction in execution cycles. One of the
most-used digital filter forms is the biquad. A biquad is a second order
(two poles and two zeros) Infinite Impulse Response (IIR) filter. It is
high enough order to be useful on its own, and because of the
coefficient sensitivities in higher order filters the biquad is often
used as the basic building block for more complex filters. For instance,
a biquad low pass filter has a cutoff slope of 12 dB/octave, useful for
tone controls; if a 24 dB/octave filter is needed, you can cascade two
biquads and it will have less coefficient sensitivity problems than a
single fourth-order design.

For implementation details please check the `USTO
link <http://appft1.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PG01&p=1&u=/netahtml/PTO/srchnum.html&r=1&f=G&l=50&s1=20160112033.PGNR.>`__

API reference:

::

    int tisigCascadeBiquad32f_2c_3skernel(CascadeBiquad_FilParam *pParam)

where CascadeBiquad_FilParam is defined as

.. code-block:: c

     CascadeBiquad_FilParam {
          float *restrict pin1;    // Input Data Channel 1
          float *restrict pin2;    // Input Data Channel 2
          float  *restrict pOut1;  // Output Data Channel 1
          float  *restrict pOut2;  // Output Data Channel 1
          float  *restrict pCoef;  // Filter Coefficients a, b for 3 stages
          float  *restrict pVar0;  // Filter Variables d0, d1 for 3 stages channel 0
          float  *restrict pVar1;  // Filter Variables d0, d1 for 3 stages channel 1
          int      sampleCount;    // Number of samples
     }  CascadeBiquad_FilParam;

Memory placement of Instruction and Data
========================================

The best performance of the DSP can be obtained by placing all the data
and instructions in L2 SRAM. Please refer to the linker command files
include in the src/common folder to see how the instructions and data
can be place in DSP internal L2 memory.

.. note::
   In application use cases where audio data needs to be place in onchip
   shared memory (OCMC or MSMC) and DDR memory, we recommend that users
   move data from external memory to L2 for processing using EDMA or enable
   DSP cache using CSL to optimize performance.

Compiler Optimization Flags
===========================

All the projects in the Audio Benchmark starterkit are built using C6000
compiler with -o3 optimization that allows the source code to be
compiled with highest compiler optimization settings. User can refer to
the compiler Build settings in the Makefiles or go to Build Settings in
CCS Project settings to modify the compiler options.

|

.. note::
   For more Details on recommended C6000 Compiler options refer
   `C6000_Compiler:_Recommended_Compiler_Options <http://processors.wiki.ti.com/index.php/C6000_Compiler:_Recommended_Compiler_Options>`__

   -  C6000 compiler documentation: `C6000 Compiler v8.x User
      Guide <http://www.ti.com/lit/ug/sprui04a/sprui04a.pdf>`__

SOC Integration and Optimization
================================

Configuring device clocks
-------------------------

Every SOC with TI DSP requires users to enable the DSP clocks by setting
up the PLL and or enabling the DSP through Power Sleep Controller or
Power and Control (PRCM) module. The way the clocks are set up differs
depending on the environment setup

-  **Development environment with emulator:**\ In this case the SOC
   clocks are setup using GEL files which are added to the target
   configuration file. For audio benchmark starterkit, this done using
   GEL files setup explained in the Hardware Setup section

-  **Application Boot from boot media**\ If you are booting application
   from a boot media like SD/MMC or flash device, the ROM bootloader or
   a secondary level bootloader performs the clock configuration. For
   audio starterkit, this initialization is done using board library
   which is linked to the secondary bootloader and the benchmark tests.

.. note::
   If the clocks are not configured the DSP will run at speed of the input
   clock rather than at the device speed grade. Hence if the clocks are not
   configured correctly the benchmarks will run much slower than
   anticipated but the cycle count will show the same.

Benchmarking using DSP TSCH/TSCL registers
==========================================

For C66x+ and C674x members of the C6000 family, there is a pair of
registers, TSCL and TSCH, which together provide a 64-bit clock value.
You can create your own clock function to take advantage of these
registers. Simply add this function to your program and it will override
the clock function from the library.

The Bench mark test application, use the following functions to capture
cycle count using the TSCH and TSCL regsiters.

.. code-block:: c

           /* ---------------------------------------------------------------- */
           /* Initialize timer for clock */
           TSCL= 0,TSCH=0;
           /* Compute the overhead of calling _itoll(TSCH, TSCL) twice to get timing info */
           /* ---------------------------------------------------------------- */
           t_start = _itoll(TSCH, TSCL);
           t_stop = _itoll(TSCH, TSCL);
           t_overhead = t_stop - t_start;


           t_start = _itoll(TSCH, TSCL);
           <Algorithm to be bechmarked>
           t_stop = _itoll(TSCH, TSCL);
           t_measured = (t_stop - t_start) - t_overhead;

Benchmark logging
=================

The Audio benchmarks demonstrates two ways to log benchmark numbers. One
approach that can be used when code is loaded and run from Code composer
studio is to use standard printf messages from the standard IO RTS
libraries and the other approach is to use UART based logging that can
send the benchmark logs to serial console on the host at the baud rate
of 115.2 kbps.

All the benchmark test application include a file Benchmark_log.h and
Benchmark_log.c, that are used to log messages based on the definition
of macro **IO_CONSOLE**. If IO_CONSOLE is defined the output will be
directed to CCS console. If it is not defined, the logs are sent to the
UART console.

Makefiles and scripts that build binaries to boot from SD card will not
have IO_CONSOLE defined hence the benchmark logs will be directed to the
UART serial console. In the CCS projects, we define the IO_CONSOLE macro
so that the output can be observed on the CCS console.

Cache configuration for Code/data sections in SRAM/DDR
======================================================

The best performance of the DSP can be obtained by placing all the data
and instructions in L2 SRAM. If developer application use cases places
audio data in onchip shared memory (OCMC or MSMC) and DDR memory then
the user will need to enable L1 and L2 cache using CSL API.

To enable and utilize cache in the application, please refer to the
csl_cacheAux.h file in the pdk_<soc>_x_x_x/packages/ti/csl folder in the
SDK and link the CSL library for the soc into the application code.

Benchmark results
=================

+-----------------------+-----------------------+-----------------------+
| Algorithm\DSP         | C66x DSP              | C674x DSP             |
| Architecture          |                       |                       |
+=======================+=======================+=======================+
| Single Precision FFT  | 1808 cycles           | 2314 cycles           |
| (256 samples)         |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Single Precision FIR  | 2652 cycles           | 4465 cycles           |
| (128 samples, 16      |                       |                       |
| coefficients)         |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Single Precision IIR  | 8258 cycles           | 12381 cycles          |
| (1k samples from 2    |                       |                       |
| channel with 3 stage  |                       |                       |
| cascade biquad)       |                       |                       |
+-----------------------+-----------------------+-----------------------+

.. note::

   -  All code and data for the benchmark tests is placed in L2 Memory.
   -  C6000 compiler version used was CGTools v8.1.3
   -  Bench marks were obtained from C66x DSP on K2G and C674x DSP on
      OMAPL138 LCDK
   -  FFT and FIR benchmarks were obtained using the DSPLIB functions.

Support
=======

For questions, feature requests and bug reports, please use the TI E2E
Forum provided below:

-  `E2E Processor Support
   <https://e2e.ti.com/support/processors/>`__

Additional resources
====================

**White papers:**

-  `Introduction to TMS320C6000 DSP
   Optimization <http://www.ti.com/lit/an/sprabf2/sprabf2.pdf>`__
-  `TI DSP
   Benchmarking <http://www.ti.com/lit/an/sprac13/sprac13.pdf>`__
-  `Optimizing Loops on
   C66x <http://www.ti.com/lit/an/sprabg7/sprabg7.pdf>`__
-  `TI’s new TMS320C66x fixed and floating-point DSP core conquers the
   ‘Need for Speed’ <http://www.ti.com/lit/wp/spry147/spry147.pdf>`__
-  `Efficient fixed- and floating-point code execution on the
   TMS320C674x core delivers faster code development and reduces system
   cost with improved
   performance <http://www.ti.com/lit/wp/spry127/spry127.pdf>`__

