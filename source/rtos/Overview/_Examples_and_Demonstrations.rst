.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_Examples_and_Demonstrations

The SDK comes with some simple *examples* to get started using the
software and IDE. The *demonstrations* contain a richer set of software
and perform more complex features. If new to the SDK, it is suggested to
go through the examples and demos before writing your application.

|

Application

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Description

AM335x EVM

AM437x EVM

AM57x EVM

K2x EVM

C66x EVM

OMAPL13x EVM

GP

ICE

SK

BBB

GP

IDK

SK

GP

IDK

K2H

K2E

K2L

K2G

C665x

C667x

OMAPL137x/C6747x

OMAPL138x/C6748x

:ref:`Image Processing Demo <Demo-RTOS-Image-Processing-Demo-label>`

The image processing demonstration utilizes SDK features such as
multi-core A15 and DSP, optimized C66x IMGLIB, IPC, and UIA logging.

X

X

X

X

:ref:`POSIX-SMP Demo <-RTOS-POSIX-SMP-Demo-label>`

The Posix-SMP demonstration uses Posix APIs together with a simple
benchmark (Dhrystone) to automatically calculate the effective
throughput of all the cores in each SMP cluster. *(**NOTE:** SMP mode
only applies to devices with ARM-A15 multiple cores.)*

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

`Audio Benchmark Starterkit <index_examples_demos.html#audio-benchmark-starterkit>`__

The Audio Benchmark starter-kit demonstration provides quick and easy
way to run core-benchmarks on the DSP for algorithms that are commonly
used in audio applications.

X

X

X

X

X

`Audio Pre-Processing Demo <index_examples_demos.html#audio-pre-processing-demo>`__

The Audio Pre-Processing demonstration provides an example for speech
recognition application development by illustrating the integration of
Beamforming (BF), Adaptive Spectrum Noise Reduction (ASNR), and Multiple
Source Selection (MSS) components.

X

X

X

`Big Data IPC Example <index_examples_demos.html#big-data-ipc-example>`__

The big data ipc examples are created mainly to show exchange of big
data buffers between cores in a multi core system.

X

X

X

X

X

X

`TI-RTOS Kernel Example <index_examples_demos.html#ti-rtos-kernel-example>`__

The RTOS examples gets user started with development of code using the
TI-RTOS real-time operating system. These are simple examples that does
not get into details of software components provided in the SDK.

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

`No OS (Bare Metal) Example <index_examples_demos.html#no-os-bare-metal-example>`__

The bare-metal examples gets user started with development of code
without an operating system. These are simple examples that does not get
into details of software components provided in the SDK. *(**NOTE:**
This example does not require the SDK to be installed, only the CCS IDE
to communicate with the target.)*

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

`Gravity Simulator Demo <index_examples_demos.html#gravity-simulator-demo>`__

The RTOS Gravity Simulator Demo demonstrates the usage of an open
sourced library combined with RTOS drivers to create a vibrant display.
This showcases the usage of VPS LLD with CPU-generated display that is
both variable and updated continuously.

X

`Template Application <index_examples_demos.html#rtos-template-application>`__

The Template Application is intended for customers to use as a
starting point during software development using Processor SDK RTOS
software. The template application can be quickly brought up by
importing the included CCS project into CCS development environment.

X

X

|
| The source files for the demonstrations can be found in the **demos**
  folder of the top-level RTOS SDK directory:

::

     [SDK Install Path]/processor_sdk_rtos_<platform>_<version>/

The default SDK Install Path is ``C:\TI`` for Windows and
``/home/[user]/ti`` for Linux.

.. Image:: /images/Processor-SDK-RTOS-directory-top.png

|

