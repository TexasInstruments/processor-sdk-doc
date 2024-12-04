*****************************************
Processor SDK RTOS Getting Started Guide
*****************************************

.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_Getting_Started_Guide

Overview
=========

The **Processor Software Development Kit (Processor-SDK)** provides the core
foundation and building blocks that facilitate application software development
on TI's embedded processors. This *Getting Started Guide* focuses on the
Real-Time Operating System (RTOS) and provides information on acquiring the
software and running basic examples/demonstrations bundled in the SDK.

For anyone that is new to Processor-SDK RTOS, traversing through all the
resources we provide in the right order is important. Here is a sequence
to follow that introduces the SDK structure and gets you started with
writing applications using the SDK.

|

Introduction to Processor SDK RTOS
===================================

First, start with watching introductory Processor SDK training videos
that are relevant to RTOS:

+------+-----------------------+-----------------------+
|  ID  |         Name          |      Description      |
+======+=======================+=======================+
| 1.2  | `Introduction to      | This module is the    |
|      | Processor SDK RTOS    | first installment of  |
|      | Part                  | a two-part overview   |
|      | 1 <http://training.ti | of the Processor SDK  |
|      | .com/introduction-pro | from the TI-RTOS      |
|      | cessor-sdk-rtos-part- | perspective. It       |
|      | 1?cu=519268>`__       | introduces the        |
|      | (40 min)              | functional elements   |
|      |                       | that may be included  |
|      |                       | in the installation   |
|      |                       | for an SoC, and then  |
|      |                       | looks at these        |
|      |                       | elements in more      |
|      |                       | detail: TI-RTOS       |
|      |                       | kernel,               |
|      |                       | Inter-Processor       |
|      |                       | Communication (IPC),  |
|      |                       | Network Developer's   |
|      |                       | Kit (NDK), algorithm  |
|      |                       | libraries, and        |
|      |                       | diagnostic software.  |
+------+-----------------------+-----------------------+
| 1.3  | `Introduction to      | This module is the    |
|      | Processor SDK RTOS    | second installment of |
|      | Part                  | a two-part overview   |
|      | 2 <http://training.ti | of the Processor SDK  |
|      | .com/introduction-pro | from the TI-RTOS      |
|      | cessor-sdk-rtos-part- | perspective. It       |
|      | 2?cu=519268>`__       | examines the          |
|      | (30 min)              | functional elements   |
|      |                       | that may be included  |
|      |                       | in the installation   |
|      |                       | for an SoC: Low-level |
|      |                       | Drivers (LLD), Chip   |
|      |                       | Support Library       |
|      |                       | (CSL), OS Abstraction |
|      |                       | Layer (OSAL), board   |
|      |                       | library, Secondary    |
|      |                       | Boot Loader (SBL),    |
|      |                       | and board             |
|      |                       | diagnostics.          |
+------+-----------------------+-----------------------+

After going through these videos, you will have a good understanding of

-  how the software is organized for portability across platforms
-  software API hierarchy within a platform, from chip support to
   low-level driver to middleware
-  where to customize software for different use cases

|

Basic examples
================
Next, it is beneficial to start with executing simple examples.

Since we want to do this on the actual hardware target, you will need
Code Composer Studio (CCS) and an Evaluation Module (EVM). See sections
below for information to configure CCS and EVM for development. This is
a top-level starting point, but you may need to go to your specific EVM
hardware setup guide for some steps (e.g., connecting external JTAG). A
cross reference to all hardware users guide can be found on the :ref:`Supported
Platforms <RTOS-SDK-Supported-Platforms>`
page.

“Hello World” example with no operating system
------------------------------------------------
The simplest example that you can write is a “Hello World” example that
runs in bare metal or no operating system. CCS comes with templates of a
semi-hosted program for the different device and core. Using this
template allows standard output to be displayed on the host PC using the
debugger. This is a good way to start learning basic configurations such
as the memory map of your device. Specific instructions for each
platform bundled in the Processor SDK RTOS can be found at
`Processor SDK Bare-Metal Examples <index_examples_demos.html#no-os-bare-metal-example>`__

Simple examples with an operating system
------------------------------------------
The next level of complexity is the take that same “Hello World” example
and run it over the TI-RTOS kernel. Besides a template for the simple
four-line “Hello World” example, CCS comes with templates for other
features of the kernel such as clock, error, event, log, SWI, and task.
You will also learn how to configure the TI-RTOS kernel for such things
as enabling semi-host support. Specific instructions for each platform
bundled in the Processor SDK RTOS can be found at
`Processor SDK RTOS Examples <index_examples_demos.html#ti-rtos-kernel-example>`__

|

Advanced examples
==================
Next, you can get familiar with peripheral drivers.

Peripheral driver example
---------------------------
The next level of complexity is to start using peripherals of your
device. There are low-level driver examples that are provided in the
Processor SDK RTOS package. These are CCS projects that can be used to
test an individual peripheral. Some of the examples use multiple low
level drivers; for example, the GPIO example will use I2C driver for
reading EVM board ID to auto configure the software and UART driver to
display status messages.

For simplicity and flexibility, the CCS project information are captured
in configuration files that you can use to generate CCS projects for
your platform, EVM, endian, and core. Once CCS projects are created,
they are loaded and run on the EVM via JTAG. Instructions to create and
run the CCS projects can be found at
`Rebuilding The PDK <index_how_to_guides.html#rebuild-drivers-from-pdk-directory>`__

|

Application development
========================
We now take the leap to put together parts of the SDK and create a more
complex application.

Template Application Workshop
----------------------------------
Take a look at the `workshop`__ for the RTOS/Bare-metal Template Application. This
workshop will cover the basics of navigating the SDK and its documentation and
using CCS. The Template Application is a good
starting point to learn how to use drivers, the OSAL layer, and Board Library.
It pulls portions of the SDK software into one application which can serve
as the starting point for creating your first application.

__ index_examples_demos.html#rtos-template-application

.. note::
   The template application currently supports Sitara EVMs (AM335x EVM,
   AM437x EVM, AM572x EVM, and AM654x EVM) only.

Demonstrations in Processor SDK RTOS
--------------------------------------
Start with running the demonstrations that are part of Processor SDK
RTOS package. These demonstrations can be run “out of box” since
pre-build binaries are provided, but also contain source to that you can
set breakpoints and step through the code. The demonstrations contain a
richer set of software and perform more complex features such as audio
and graphics.

Not all demonstrations are applicable to all platforms. The following
page has a list of all demonstrations and supported platform:
`Processor SDK_RTOS Examples and Demonstrations <index_examples_demos.html>`__

Custom application
--------------------
Next, watch the following training video on guidelines to write a custom
application using the SDK.

+------+-----------------------+-----------------------+
|  ID  |         Name          |      Description      |
+======+=======================+=======================+
| 1.4  | `Application          | This presentation     |
|      | Development Using     | provides a detailed   |
|      | Processor SDK         | overview of the       |
|      | RTOS <https://trainin | application           |
|      | g.ti.com/application- | development process   |
|      | development-using-pro | using the Processor   |
|      | cessor-sdk-rtos?cu=51 | SDK RTOS release. It  |
|      | 9268>`__              | walks through each    |
|      | (1 hr 40 min)         | step of the a typical |
|      |                       | development flow,     |
|      |                       | including setup of    |
|      |                       | the evaluation module |
|      |                       | (EVM), getting        |
|      |                       | started with the EVM, |
|      |                       | running out-of-box    |
|      |                       | examples, developing  |
|      |                       | application code,     |
|      |                       | porting applications  |
|      |                       | to custom hardware,   |
|      |                       | and customization of  |
|      |                       | application software. |
+------+-----------------------+-----------------------+

This video has a lot of content, as you can see from the duration. It is
broken down into the following sections:

-  **Setup** development environment including download software,
   configure target EVM
-  **Start** with basic software examples and basic connectivity of EVM
-  **Run** demo applications provided in SDK
-  **Develop** application using drivers in SDK
-  **Port** software to custom hardware by changing the board support
   package
-  **Customize** application for certain use cases

If you have custom hardware, the SDK software is organized to ease
porting to a new hardware. All EVM-specific software is kept in the
board support package, Board Library. Functions include unlocking MMR
registers, initializing PLL, configuring clock, configuring PinMux,
initialing DDR, and creating a UART instance for console output.
Individual examples, unit tests, and demonstrations call the Board
Library so that each of these applications can be migrated to a custom
hardware by modifying the Board Library. You may want to also port the
EVM diagnostics to your custom hardware and ensure the test suite
passes.

The customize module provides information to create a new application.
This includes configuring TI-RTOS kernel to link required driver
libraries, memory map, RTSC platform definition, and task creation.

|

Download and install software
===============================
There are three software packages that make up the Processor SDK RTOS
development ecosystem:

-  Code Composer Studio (if using JTAG, IDE)
-  Latest CCS Emulation package (for connecting to target using JTAG)
-  Processor-SDK RTOS software

See the :ref:`Release Notes <processor-sdk-rtos-release-notes>`
for information on minimum requirements for host PC.

The size of the installer is large since we want to provide one bundle
for all the components. The bad side of this is that if you are manually
downloading the Processor-SDK installer, you may run into issues such as
download stall or slow download. One simple solution is to run a
download manager/accelerator such as
http://www.freedownloadmanager.org/.

.. _overview-code-composer-studio:

Code Composer Studio
-----------------------

.. Image:: /images/Ccsv7splash.jpg

The Processor-SDK RTOS uses *Code Composer Studio* as the host
integrated development environment for development and debug. All
compilers are packaged with the SDK installer. This allows compilation
of software without needing to install CCS. You only need CCS if you are
using CCS projects, using JTAG to communicate with target, or need an
Integrated Development Environment (IDE) for development and debug.

To download CCS, use the installer specified on the Processor-SDK
download page for your platform (see links in below section).


.. Attention::
   See the :ref:`Release Notes <processor-sdk-rtos-release-notes>` for the
   recommended version of CCS. This is the version that was validated with
   the software in the SDK and will provide the best user experience.
   Occasionally, there may be compatibility issues if different versions
   are used.
|

When installing CCS, you can choose to control what is installed for
processor architecture.

.. Image:: /images/Processor-SDK_CCSv7-Setup-Processor-Support.png

The minimum required for the SDK are the following items

-  **Sitara AMx Processors** for AM335x, AM437x, AM57x
-  **66AK2x multicore DSP + ARM Processors & C66x KeyStone multicore
   DSP** for K2E, K2G, K2H, K2K, K2L, C665x, C667x
-  **OMAP-L1x DSP + ARM9 Processor** for OMAP-L1x
-  **C6000 Power-Optimized DSP** for C674x

.. note::
   If you plan to use emulators other than the XDS100 class or XDS200 class
   of emulators, please select the appropriate emulation drivers at the
   time of install. Code composer studio does not allow upgrades on drivers
   that were not installed during the first install.

|

Emulator support
-----------------
The support for connecting a JTAG to the EVM to debug software is
included in the CCS package. In some cases, additional modifications to
configuration GEL files are provided separately. To get the latest
version, perform a `CCS Check for
Updates <http://software-dl.ti.com/ccs/esd/documents/ccsv7_updates.html>`__.

The relevant update will be named

-  **Sitara Device Support** for AM335x, AM437x, AM57x
-  **Keystone2 Device Support** for K2E, K2G, K2H, K2K, K2L
-  **Keystone1 Device Support** for C665x, C667x
-  **OMAPL/Integra Device Support** for OMAP-L1x
-  **C6000 Device Support** for C674x

For example, an update for Sitara devices will look like:

.. Image:: /images/Processor-SDK_CCS-Emu-Update.png

Processor-SDK for RTOS
------------------------
The final step is to download and install the Processor-SDK RTOS. See
the software product page for your device to get the latest version of
this software:

-  `Processor SDK for
   AM335x <http://www.ti.com/tool/processor-sdk-am335x>`__
-  `Processor SDK for
   AM437x <http://www.ti.com/tool/processor-sdk-am437x>`__
-  `Processor SDK for
   AM57xx <http://www.ti.com/tool/processor-sdk-am57x>`__
-  `Processor SDK for
   AMIC110 <http://www.ti.com/tool/PROCESSOR-SDK-AMIC110>`__
-  `Processor SDK RTOS for
   C665x <http://www.ti.com/tool/PROCESSOR-SDK-C665X>`__
-  `Processor SDK RTOS for
   C667x <http://www.ti.com/tool/PROCESSOR-SDK-C667X>`__
-  `Processor SDK RTOS for
   C6747/OMAP-L17 <http://www.ti.com/tool/processor-sdk-omapl137>`__
-  `Processor SDK RTOS for
   C6748/OMAP-L138 <http://www.ti.com/tool/processor-sdk-omapl138>`__
-  `Processor SDK RTOS for
   K2E <http://www.ti.com/tool/PROCESSOR-SDK-K2E>`__
-  `Processor SDK RTOS for
   K2G <http://www.ti.com/tool/PROCESSOR-SDK-K2G>`__
-  `Processor SDK RTOS for
   K2H/K2K <http://www.ti.com/tool/PROCESSOR-SDK-K2H>`__
-  `Processor SDK RTOS for
   K2L <http://www.ti.com/tool/PROCESSOR-SDK-K2L>`__

From the appropriate software product page, go to the download page by
clicking "Get Software" for the RTOS package.

.. note::
    -  When Installing on linux (Ubuntu 16.04 and above) the following packages need to be installed before the Procsdk RTOS installer is installed

       **sudo apt install diffstat texinfo gawk chrpath dos2unix unzip socat doxygen libc6:i386 libncurses-dev:i386 libstdc++6:i386 libz1:i386**

    -  To avoid configuring CCS "Tool Discovery Path" to search for
       components in different directories, it is recommended to install the
       SDK in the same directory as CCS. This is *C:/TI* for Windows and
       */home/[user]/ti* for Linux.
    -  Once installer has started, the Cancel button may not work properly.
    -  On Ubuntu 14.04 Linux Host, if you are installing Processor SDK RTOS
       and observe that the installer exits immediately after you try to run
       from command line then you need resolve dependencies using
       instructions provided here :ref:`Processor SDK RTOS_Release Notes <processor-sdk-rtos-release-notes>`

|

Setup EVM hardware
===================

.. Attention::
   The EVM board is sensitive to electrostatic discharges
   (ESD). Use a grounding strap or other device to prevent damaging the
   board. Be sure to connect communication cables before applying power to
   any equipment.

|

The EVM provides the ability to utilize a variety of capabilities of the
SoC. Follow instructions in the included *EVM Quick Start Guide* for
information on hardware configuration and other pertinent information.
This guide is included in the EVM kit and also available for download
from the software download page for your particular device. The list of
supported EVMs are provided in the :ref:`Release Notes <RN-Supported-Platforms-label>`.

If you connect to the EVM UART, use the following host configuration:

-  **Baud Rate**: 115200
-  **Data Bits**: 8
-  **Parity**: None
-  **Flow Control**: Off

For more information beyond what is covered in the *EVM Quick Start
Guide*, see :ref:`EVM Hardware User Guides <RTOS-SDK-Supported-Platforms>`

|

Setting up CCS for EVM and Processor-SDK RTOS
==============================================
After the Processor SDK is installed, launch Code Composer Studio and
make sure that the components inside Processor SDK are discovered by the
CCS eclipse environment. If you installed the SDK in the same directory
as CCS, this is as simple as starting CCS and it will auto-detect the
newly installed components.

.. note::
   If you installed the SDK and CCS in different paths, see the
   `Custom Installation Path <index_how_to_guides.html#update-environment-when-installing-to-a-custom-path>`__
   **How To** page that provides instructions to configure for a custom
   installation path.

The next step is to make a connection between CCS and your EVM (or
*target*). If you need help with this step, see the `Setup CCS <index_how_to_guides.html#setup-ccs-for-evm-and-processor-sdk-rtos>`__
**How To** page explaining this further.

At this point, you should be able to connect to target using CCS and
start development!

|

Useful links
==============

- :ref:`Developer Guide <Index-Processor-SDK-RTOS-label>`
.. note::
   This is a good landing page to bookmark since all links below can be
   found in the Developer Guide.


- `Training Videos <https://training.ti.com/processor-sdk-training-series>`__
- `Getting Started Guide <index_overview.html#getting-started-guide>`__

- :ref:`Supported Platforms <RTOS-SDK-Supported-Platforms>`

- `Landing Page to All Processor SDK RTOS Packages <http://www.ti.com/tool/ti-rtos-proc>`__
- :ref:`Release Notes <processor-sdk-rtos-release-notes>`
- `Examples and Demonstrations <index_examples_demos.html>`__
- `FAQ <index_faq.html>`__
|

Archived
==========
- `Processor-SDK RTOS 4.0 <http://processors.wiki.ti.com/index.php?title=Processor_SDK_RTOS_Getting_Started_Guide&oldid=230434>`__
- `Processor-SDK RTOS 3.2 <http://processors.wiki.ti.com/index.php?title=Processor_SDK_RTOS_Getting_Started_Guide&oldid=225568>`__

|

