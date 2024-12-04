.. http://processors.wiki.ti.com/index.php/Processor_SDK_Posix-SMP_Demo

Introduction
============

This page describes the SMP/Posix demo provided in the Processor-SDK for
RTOS and Linux. This demo uses Posix APIs together with a simple
benchmark (Dhrystone) to automatically calculate the effective
throughput of all the cores in each SMP cluster. SMP mode is only
supported on Coretex-A15 cores.

This demo runs on:

-  AM572x (A15, C66, M4)
-  AM437x (A9)
-  AM335x (A8)
-  K2H (A15, C66)
-  K2E (A15, C66)
-  K2G (A15, C66)
-  K2L (A15, C66)
-  C6678 (C66)
-  C6657 (C66)

The sections below provide details of the application as well as build
and run instructions.

Requirements
============

The following materials are required to run this demonstration:

Hardware

-  TI EVM (see list above)
-  Serial UART cable (provided in EVM kit)

Software

-  Processor-SDK RTOS
-  Code Composer Studio

|

Software Design
===============

The demo is based on Dhrystone 2.1 from
`link <http://fossies.org/linux/privat/old/dhrystone-2.1.tar.gz/>`__.

The purpose of the demo is two-fold. First, it is to show easy scaling
of throughput across cores in a SMP cluster when running TI-RTOS.
Second, it shows easy portability of Posix threads between TI-RTOS and
Linux.

The overall requirement is discover all parameters automatically without
user input, and to minimize the amount of code that must be customized
between TI-RTOS and Linux. This demonstrates that the same Posix threads
as well as their setup/control code can be run on either TI-RTOS or
Linux with minimal effort.

In order to accomplish this, several major modifications were made to
Dhrystone in order to "threadify" it. Some of these changes slightly
affect the results compared to an unmodified version. Thus this modified
version should be run on all processors where comparisons will be drawn.

-  **Removal of most printf() during normal operation.** Original code
   dumped all final values for the user to verify. Changed to
   programmatic verification. Only printf() for actual results (DMIPS
   and Dhrystones) preserved.
-  **Removal of all global variables.** They are accessed through an
   "inst" pointer instead.
-  **Adaptive discovery of iteration count.** Original code used a
   #define. This version doubles iteration count until execution time is
   about 10M timer ticks.
-  **Adaptive discovery of number of cores in SMP cluster.** Original
   code didn't use threads. This version doubled number of threads until
   cumulative DMIPS flattens out.

POSIX barriers are used inside the timed portion of the code. This is
not to time the performance of the barrier, but is instead used to time
how long all threads together take to complete. It is assumed the
execution times of the threads (> 0.1 second) are orders of magnitude
more than the barrier, so the barrier's effect on results is negligible.

Processor SDK uses makefiles for TI-RTOS and Yocto recipes for Linux for
the supported EVMs. The makefile can also be used to compile native
builds for Linux (both for EVMs and x86).

For more information on TI-RTOS Posix, see `POSIX
Support <http://processors.wiki.ti.com/index.php/SYS/BIOS_POSIX_Thread_(pthread)_Support>`__.

|

How to Run the Demo
===================

The processor SDK includes pre-built binaries which may be loaded and
run using the SBL with UART or using CCS with UART or ROV (UART display
for newer versions and ROV for older versions). To run using UART, hook
up to the board using UART and run the .out file.

.. Image:: /images/Posix-demo-uart.PNG

To run using CCS, use the following steps. Each binary has an associated
\\*.rov.xs file located in the same directory--enabling the CCS ROV tool.
Newer versions will display directly to the UART console and any steps
involving ROV may be skipped.

::

    <SDK_INSTALL_PATH>/processor_sdk_rtos_<platform>_2_00_xx_xx/demos/posix-smp/bin/<platform>/<core>/debug/dhry.out
    <SDK_INSTALL_PATH>/processor_sdk_rtos_<platform>_2_00_xx_xx/demos/posix-smp/bin/<platform>/<core>/debug/dhry_pa15fg.rov.xs

For all platforms and core types, the basic procedure for running the
demo will be the same:

#. Using CCS, launch the target configuration for the EVM `CCS-Target
   Configurations <http://processors.wiki.ti.com/index.php/Target_Configuration_-_Custom_Configurations>`__.
   Please ensure that the target configuration will load the appropriate
   CCS gel files found in the emupak. Make sure all Coretex-A15 cores in
   the SMP cluster have an appropriate CCS gel file.
#. The default ccxml file only loads a gel on connect for some of the
   cores. Modify the ccxml file to load the gel for all the
   corresponding cores.
#. In the CCS debug view, group and then connect to all cores of device
   that you wish to test on (i.e. - all of the clustered A15 cores).
#. For each, core load the dhry.out file. The principle core should halt
   at main while the SMP linked cores will begin auto-running upon load.
#. Once all cores have been loaded, run all the cores.
#. The output will be sent to the UART console in real time.
#. The demo should not take more than a few minutes to run. You must
   manually halt the cores to end the demo.

If using Processor-SDK 3.0 or later,

#. Open the ROV window (Tools > RTOS Object View (ROV)) and view the
   SysMin module to inspect the output of the demo. If you see the below
   message, please specify the XDC and SYSBIOS versions:

.. Image:: /images/Use_rov_1.jpg

.. Image:: /images/Use_rov_2.png

.. Image:: /images/Posix-smp2.png

The output buffer shown in the ROV contains the different stages of the
demo's progression:

#. The demo finds an appropriate number of iterations for the device.
#. The demo begins to add threads.
#. The demo concludes when adding additional threads does not further
   increase the DMIPS.

The output takes the form of: "xxxxxxx iterations \*n threads;
dhrystones xxxxxxxx, dmips = xxxx". In the screenshot above, moving from
two threads to four threads does not appreciably improve the DMIPS, so
the demo completes. This behavior is expected because the demo is only
running on two cores in this example.

.. note::
   -  A15 cores may usually be connected to directly; on the AM572x, the M4
      IPUs must first be initialized by the gel scripts (Scripts > AM572x
      MULTICORE initialization > IPUxSSClkEnable_API)
   -  If the K2 demo will not run, try updating to the latest emupack by
      doing "Help/Check For Updates" and selecting "Keystone2 device
      support" update (only). There are additional instructions for
      configuring groups, etc. at `SMP
      Debug <http://processors.wiki.ti.com/index.php/SMP_Debug>`__.
   -  If the primary core of an SMP group will not allow running after
      loading the demo, try pausing the linked cores and then running all
      the cores in a group
   -  For TI-RTOS documentation for enabling SMP, refer to
      `SMP/BIOS <http://processors.wiki.ti.com/index.php/SMP/BIOS>`__. The
      POSIX demo in the Processor SDK RTOS packages with C66x does not
      support SMP. This is a POSIX pthread demo intended to run Dhrystone
      on one C66x core without SMP.
   -  Some of the DMIPS values may not be accurate, but the values will
      increase proportionally with the number of cores

How to Build the Demo
=====================

Processor-SDK RTOS
------------------

To build the project manually, first navigate to the top level makefile:

::

     <SDK_INSTALL_PATH>/processor_sdk_rtos_<platform>_2_00_xx_xx/demos/posix-smp/makefile

Edit the makefile to include the paths to BIOS, XDC, PDK packages, and
the toolchains for the cores being used.

::

    #DEPOT = <ROOT_INSTALL_PATH>
    #### BIOS-side dependencies ####
    #BIOS_INSTALL_PATH ?= $(DEPOT)\bios_n_nn_nn_nn
    #XDC_INSTALL_PATH ?= $(DEPOT)\xdctools_n_nn_nn_nn_core
    #### BIOS-side toolchains ####
    #TOOLCHAIN_PATH_A15 ?= $(DEPOT)\ccsv6\tools\compiler\gcc-arm-none-eabi-n_n-xxxxqn
    #TOOLCHAIN_PATH_M4 ?= $(DEPOT)\ccsv6\tools\compiler\ti-cgt-arm_x.x.x

Navigate to the demo directory and run "make". The steps to run the demo
will be the same.

Processor-SDK Linux
-------------------

The Posix-SMP demo has been added to the Linux SDK matrix starting in
Processor-SDK 3.0. Simply run the example from the Matrix and the output
will be displayed on the console.

For the documentation on the Linux Matrix, please see:
`link <http://processors.wiki.ti.com/index.php/Matrix_Users_Guide>`__.

