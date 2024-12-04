.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_Directory_Structure

Overview
===========
The Processor SDK for RTOS contain a number of software components,
including a top-level RTOS SDK directory. These components are all
installed in one common install path specified when running the
installer.

.. note::
   Not all components are applicable on all platforms.
|

Software Component Directories
================================
Here is a sample directory layout for the AM57x RTOS SDK:

.. Image:: /images/Processor-SDK-RTOS-directories.png

|

Processor-SDK Directory
========================
The Processor SDK for RTOS contains a top-level RTOS SDK directory:

::

     [SDK Install Path]/processor_sdk_rtos_<platform>_<version>/

The default SDK Install Path is ``C:\TI`` for Windows and
``/home/[user]/ti`` for Linux.

This directory contains the following top-level directories and files;
here is an example for AM57x:

.. Image:: /images/Processor-SDK-RTOS-directory-top.png

These directories contain the collateral and tools applicable for RTOS:

-  **bin** - Contains the helper scripts for configuring the host system
   and target device. Based on EVM capability, examples include scripts
   to create an SD card with an RTOS application, script to flash EVM
   with bootable application

-  **demos** - Contains demonstrations that implements interesting
   features. Additionally, these demonstrations serve as a template to
   start writing an application

-  **docs** - Contains various documentation such as the software
   manifest and release notes

-  **prebuilt-sdcards** - Contains prebuilt SD card images that can be
   copied to an SD card and used to load the EVM (AM3, AM4, AM5 only)

-  **prebuilt-images** - Contains prebuilt images to flash images to
   write to EVM flash (K2x only)

-  **makefile** - Provides build targets for SDK components from the
   top-level of the SDK

-  **setupenv.bat** - Configures the user Windows host system to prepare
   to invoke the makefile

-  **setupenv.sh** - Configures the user Linux host system to prepare to
   invoke the makefile

|

Components Included in SDK
============================
The following is a list of all components that may be included in the
Processor-SDK RTOS SDK installer. See :ref:`Release Notes <release-notes-component-version>`
for applicable components for a specific platform.

Development Host Content
--------------------------

-  **CG_XML** - Perl scripts used to process the XML files that come
   from the TI code generation tools

-  **XDC Tools** - XDCtools contains all of the tools for reusable
   software components, optimized for real-time embedded systems

-  **ARM GCC Compiler** - GNU GCC ARM contains runtime libraries and
   cross-compilers used for ARM development

-  **TI ARM Compiler** - TI ARM code generation tools, including C/C++
   compiler, linker, and run-time-support libraries

-  **TI C6000 Compiler** - TI C6X code generation tools, including C/C++
   compiler, linker, and run-time-support libraries

-  **TI PRU Compiler** - TI PRU code generation tools, including C/C++
   compiler, linker, and run-time-support libraries

Target Content
---------------

-  **CTOOLSLIB** - C6x DSP software libraries to use
   trace/instrumentation hardware blocks on SOC (e.g., ETB, AET, STM)

-  **DSPLIB** - Optimized C6x DSP function library for C programmers

-  **EDMA3-LLD** - EDMA3 low level driver that supports data transfers
   between two memory mapped devices

-  **FC**: Framework Components is comprised of XDAIS algorithm resource
   managers and functional interfaces

-  **FFTLIB** - Optimized C6x DSP Fast Fourier Transform function
   library for C programmers

-  **IMGLIB** - Optimized C6x DSP image and video processing function
   library for C programmers

-  **IPC** - InterProcess Communication mechanisms including message
   passing, streams, and linked lists, which work transparently in both
   uniprocessor and multiprocessor configurations

-  **LIBARCH** - Library architecture framework used by other C6x DSP
   optimized libraries

-  **LINALG** - Optimized C6x DSP dense linear algebra function library
   for C programmers

-  **MATHLIB** - Optimized C6x DSP floating-point math function library
   for C programmers

-  **MPM** - Multiproc Manager C6x DSP component provides services to
   MPM Linux module to load and manage remote processors

-  **NDK** - Network Development Kit package provides an example network
   stack that runs on the TI-RTOS kernel

-  **OPENCL** - OpenCL is a framework for writing programs that execute
   across heterogeneous systems

-  **OPENMP** - OpenMP Runtime implements support for the OpenMP API
   specification, a standard for shared memory parallel programming

-  **PDK** - Platform Development Kit that includes Chip Support
   Libarary (CSL), Low Level Drivers (LLD), Boot, Diagnostics, and other
   functions

-  **SYS/BIOS** - TI-RTOS kernel, a real-time operating system that
   provides pre-emptive deterministic multithreading

-  **UIA** - Unified Instrumentation Architecture (UIA) APIs and
   transports allow embedded software to log trace/event instrumentation
   data that can be visualized in CCS

-  **XDAIS** - XDAIS (eXpress DSP Algorithm Interoperability Standard)
   provides the rules and guidelines necessary to enable integration and
   execution of algorithms

|

