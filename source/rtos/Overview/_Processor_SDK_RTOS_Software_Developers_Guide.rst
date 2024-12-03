**********************************************
Processor SDK RTOS Software Developer's Guide
**********************************************

.. note::
   | Processor SDK documentation is now created from reStructuredText sources using
     Sphinx, and hosted on ti.com instead of processors wiki - starting
     4.3 release.
   |
   | We intend to retain the look and feel of the content
     to make this transition seamless, and yet provide the users with the benefits of
     consuming the content generated with emergent documentation tools.
   |
   | Wiki content will be left for reference during this migration process to find any missing old content. Feel free to drop us a note using the
     forums listed at :ref:`Technical Support <overview-technical-support>`, and we would love to hear from you.
   |
   | Old Wiki Documentation links from previous releases:
   |    - `Wiki Software Developer's Guide <http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_Software_Developer_Guide>`__.
   |    - `Wiki Getting Started Guide <http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_Getting_Started_Guide>`__.
   |

.. rubric:: Introduction
   :name: introduction

The Texas Instruments Processor Software Development Kit (Processor-SDK)
is a single scalable software platform that offers streamlined development
across different TI `Sitara/DSP Processors <http://www.ti.com/lsds/ti/processors/overview.page>`__.
The Processor-SDK for RTOS provides fundamental platform software and tools
for development, deployment and execution of RTOS-based applications.
It includes the following, though not all features are applicable across
all supported platforms:

-  TI-RTOS kernel, a light-weight real-time embedded operating system for TI devices
-  Chip support libraries, drivers, and basic board-support utilities
-  Interprocessor communication for communication across cores and devices
-  Basic networking stack and protocols
-  Optimized C66x algorithm libraries
-  Debug and instrumentation utilities
-  Bootloaders and boot utilities
-  Demonstrations and examples

Combined with TI Code Composer Studio integrated development environment (IDE),
the Processor-SDK provides the core foundational building blocks that facilitate
application software development on TI's embedded processors.

.. rubric:: Scope
   :name: scope

The purpose of this guide is to quickly provide the information you need most while
evaluating and developing applications on a TI embedded processor, specifically
running embedded real-time operating system. It is not intended to be a thorough
design document. As such, the focus is on application programming interfaces (API),
build information, and examples to use as a template to start development.

.. rubric:: Guides
   :name: guides

+------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Processor SDK RTOS**                                                                                                                                 |
+========================================================================+===============================================================================+
| |__Getting Started Guide__|  <-- **Start Here**                        | |__Release Notes__|                                                           |
+------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| |__Examples and Demonstrations__|                                      | |__RTOS Software Stack__|                                                     |
+------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| |__Directory Structure Overview__|                                     | |__Building the SDK__|                                                        |
+------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `Training <https://training.ti.com/processor-sdk-training-series>`__   | |__Migration Guide__|                                                         |
+------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| |__Technical Support__|                                                | |__How To Guides__|                                                           |
+------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| |__Related Software__|                                                 | |__Frequently Asked Questions (FAQ)__|                                        |
+------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| |__Supported Platforms and Versions__|                                                                                                                 |
+------------------------------------------------------------------------+-------------------------------------------------------------------------------+


.. |__Getting Started Guide__| replace:: :ref:`Getting Started Guide <overview-getting-started-guide>`
.. |__Release Notes__| replace:: :ref:`Release Notes <processor-sdk-rtos-release-notes>`
.. |__Examples and Demonstrations__| replace:: :ref:`Examples and Demonstrations <index-examples-demos>`
.. |__RTOS Software Stack__| replace:: :ref:`RTOS Software Stack <overview-rtos-software-stack>`
.. |__Directory Structure Overview__| replace:: :ref:`Directory Structure Overview <overview-directory-structure>`
.. |__Building the SDK__| replace:: :ref:`Building the SDK <overview-building-the-sdk>`
.. |__Migration Guide__| replace:: :ref:`Migration Guide <RTOS-SDK-Migration-Guide-label>`
.. |__Technical Support__| replace:: :ref:`Technical Support <overview-technical-support>`
.. |__How To Guides__| replace:: :ref:`How To Guides <index-how-to-guides>`
.. |__Related Software__| replace:: :ref:`Related Software <overview-related-software>`
.. |__Frequently Asked Questions (FAQ)__| replace:: :ref:`Frequently Asked Questions (FAQ) <index-faq>`
.. |__Supported Platforms and Versions__| replace:: :ref:`Supported Platforms and Versions <RTOS-SDK-Supported-Platforms>`

+---------------------+---------------------+--------------------------+-------------------+
| **Board/EVM Abstration**                                                                 |
+=====================+=====================+==========================+===================+
| |__Diagnostics__|   | |__Board Support__| | |__Power-On Self Test__| |                   |
+---------------------+---------------------+--------------------------+-------------------+

.. |__Diagnostics__| replace:: :ref:`Diagnostics <index-board-diagnostics>`
.. |__Board Support__| replace:: :ref:`Board Support <board-board-support>`
.. |__Power-On Self Test__| replace:: :ref:`Power-On Self Test <board-power-on-self-test>`

+---------------------+-------------------+--------------------+--------------------+
| **Foundational Components**                                                       |
+=====================+===================+====================+====================+
| |__TI-RTOS Kernel__|| |__Boot__|        | |__IPC__|          | |__MPM__|          |
+---------------------+-------------------+--------------------+--------------------+
| |__OpenMP__|        | |__FC__|          | |__OpenCL__|       | |__Network__|      |
+---------------------+-------------------+--------------------+--------------------+
| |__XDAIS__|         | |__PKTLIB__|      | |__NWAL__|         | |__Tools__|        |
+---------------------+-------------------+--------------------+--------------------+

.. |__TI-RTOS Kernel__| replace:: :ref:`TI-RTOS Kernel <foundational-components-ti-rtos-kernel>`
.. |__Boot__| replace:: :ref:`BOOT <foundational-components-boot>`
.. |__IPC__| replace:: :ref:`IPC <foundational-components-IPC>`
.. |__MPM__| replace:: :ref:`MPM <foundational-components-mpm>`
.. |__OpenMP__| replace:: :ref:`OpenMP <foundational-components-openmp>`
.. |__FC__| replace:: :ref:`FC <foundational-components-fc>`
.. |__OpenCL__| replace:: :ref:`OpenCL <foundational-components-opencl>`
.. |__Network__| replace:: :ref:`Network <foundational-components-ndk>`
.. |__XDAIS__| replace:: :ref:`XDAIS <foundational-components-xdais>`
.. |__PKTLIB__| replace:: :ref:`PKTLIB <foundational-components-pktlib>`
.. |__NWAL__| replace:: :ref:`NWAL <foundational-components-nwal>`
.. |__Tools__| replace:: :ref:`Tools <foundational-components-tools>`


+---------------------+-------------------+--------------------+--------------------+
| **DSP Optimized Libraries**                                                       |
+=====================+===================+====================+====================+
| |__MATHLIB__|       | |__IMGLIB__|      | |__DSPLIB__|       | |__FFTLIB__|       |
+---------------------+-------------------+--------------------+--------------------+
| |__LINALG__|        |                   |                    |                    |
+---------------------+-------------------+--------------------+--------------------+

.. |__MATHLIB__| replace:: :ref:`MATHLIB <dsp-sw-dsp-optimized-libraries>`
.. |__IMGLIB__| replace:: :ref:`IMGLIB <dsp-sw-dsp-optimized-libraries>`
.. |__DSPLIB__| replace:: :ref:`DSPLIB <dsp-sw-dsp-optimized-libraries>`
.. |__FFTLIB__| replace:: :ref:`FFTLIB <dsp-sw-dsp-optimized-libraries>`
.. |__LINALG__| replace:: :ref:`LINALG <dsp-sw-dsp-optimized-libraries>`


+---------------------+-------------------+--------------------+--------------------+
| **DSP Debug and Trace**                                                           |
+=====================+===================+====================+====================+
| |__CToolsLib__|     | |__UIA__|         | |__Trace__|        |                    |
+---------------------+-------------------+--------------------+--------------------+
| |__Fault Mgt__|     | |__WDT__|         |                    |                    |
+---------------------+-------------------+--------------------+--------------------+

.. |__CToolsLib__| replace:: :ref:`CToolsLib <dsp-sw-ctoolslib>`
.. |__UIA__| replace:: :ref:`UIA <dsp-sw-uia>`
.. |__Trace__| replace:: :ref:`Trace <dsp-sw-trace>`
.. |__Fault Mgt__| replace:: :ref:`Fault Mgt <dsp-sw-fault-management>`
.. |__WDT__| replace:: :ref:`WDT <dsp-sw-wdt>`

+-----------------------------+----------------------------+----------------------------+----------------------------+
| **Device Drivers**                                                                                                 |
+=============================+============================+============================+============================+
| |__CSL__|                   | |__UART__|                 | |__USB__|                  | |__PCIe__|                 |
+-----------------------------+----------------------------+----------------------------+----------------------------+
| |__GPIO__|                  | |__I2C__|                  | |__McSPI-QSPI-OSPI__|      | |__EDMA3__|                |
+-----------------------------+----------------------------+----------------------------+----------------------------+
||__ICSS-EMAC__|              | |__PRUSS__|                | |__FATFS__|                | |__MMCSD__|                |
+-----------------------------+----------------------------+----------------------------+----------------------------+
| |__QMSS__|                  | |__CPPI__|                 | |__PA__|                   | |__SA__|                   |
+-----------------------------+----------------------------+----------------------------+----------------------------+
| |__SRIO__|                  | |__HYPLNK__|               | |__TSIP__|                 | |__MCBSP__|                |
+-----------------------------+----------------------------+----------------------------+----------------------------+
| |__EMAC__|                  | |__MCASP__|                | |__PM__|                   | |__RM__|                   |
+-----------------------------+----------------------------+----------------------------+----------------------------+
| |__GPMC__|                  | |__VPS Drivers__|          | |__DSS__|                  | |__CAL__|                  |
+-----------------------------+----------------------------+----------------------------+----------------------------+
| |__UDMA__|                  | |__SCICLIENT__|            |  |__IOLINK__|              |                            |
+-----------------------------+----------------------------+----------------------------+----------------------------+

.. |__CSL__| replace:: :ref:`CSL <device-driver-csl>`
.. |__UART__| replace:: :ref:`UART <device-driver-uart>`
.. |__USB__| replace:: :ref:`USB <device-driver-usb>`
.. |__PCIe__| replace:: :ref:`PCIe <device-driver-pcie>`
.. |__GPIO__| replace:: :ref:`GPIO <device-driver-gpio>`
.. |__I2C__| replace:: :ref:`I2C <device-driver-i2c>`
.. |__McSPI-QSPI-OSPI__| replace:: :ref:`McSPI-QSPI-OSPI <device-driver-mcspi-qspi-ospi>`
.. |__EDMA3__| replace:: :ref:`EDMA3 <device-driver-edma3>`
.. |__ICSS-EMAC__| replace:: :ref:`ICSS-EMAC(DRIVER,FIRMWARE) <device-driver-icss-emac>`
.. |__PRUSS__| replace:: :ref:`PRUSS <device-driver-pruss>`
.. |__FATFS__| replace:: :ref:`FATFS <device-driver-fatfs>`
.. |__MMCSD__| replace:: :ref:`MMCSD <device-driver-mmcsd>`
.. |__QMSS__| replace:: :ref:`QMSS <device-driver-qmss>`
.. |__CPPI__| replace:: :ref:`CPPI <device-driver-cppi>`
.. |__PA__| replace:: :ref:`PA <device-driver-pa>`
.. |__SA__| replace:: :ref:`SA <device-driver-sa>`
.. |__SRIO__| replace:: :ref:`SRIO <device-driver-srio>`
.. |__HYPLNK__| replace:: :ref:`HYPLNK <device-driver-hyplnk>`
.. |__TSIP__| replace:: :ref:`TSIP <device-driver-tsip>`
.. |__MCBSP__| replace:: :ref:`MCBSP <device-driver-mcbsp>`
.. |__EMAC__| replace:: :ref:`EMAC <device-driver-emac>`
.. |__MCASP__| replace:: :ref:`MCASP <device-driver-mcasp>`
.. |__PM__| replace:: :ref:`PM <device-driver-pm>`
.. |__RM__| replace:: :ref:`RM <device-driver-rm>`
.. |__GPMC__| replace:: :ref:`GPMC <device-driver-gpmc>`
.. |__VPS Drivers__| replace:: :ref:`VPS Drivers <device-driver-vps-drivers>`
.. |__DSS__| replace:: :ref:`DSS <device-driver-dss>`
.. |__CAL__| replace:: :ref:`CAL <device-driver-cal>`
.. |__UDMA__| replace:: :ref:`UDMA <device-driver-udma>`
.. |__SCICLIENT__| replace:: :ref:`SCICLIENT <device-driver-sciclient>`
.. |__IOLINK__| replace:: :ref:`IOLINK <device-driver-iolink>`


+-----------------------------+----------------------------+----------------------------+----------------------------+
| **Device Driver Utilities**                                                                                        |
+=============================+============================+============================+============================+
| |__OSAL__|                  | |__Profiling__|            |                            |                            |
+-----------------------------+----------------------------+----------------------------+----------------------------+

.. |__OSAL__| replace:: :ref:`OSAL <device-driver-osal>`
.. |__Profiling__| replace:: :ref:`Profiling <device-driver-profiling>`


+-----------------------------+----------------------------+----------------------------+----------------------------+
| **PRU-ICSS Firmware**                                                                                              |
+=============================+============================+============================+============================+
| |__Dual EMAC and Switch__|  | |__PRU-ICSS SORTE__|       | |__PRU-ICSS I2C__|         | |__PRU-ICSS IOLINK__|      |
+-----------------------------+----------------------------+----------------------------+----------------------------+

.. |__Dual EMAC and Switch__| replace:: :ref:`Dual EMAC and Switch <pru-icss-fw-dual-emac-and-switch>`
.. |__PRU-ICSS SORTE__| replace:: :ref:`PRU-ICSS SORTE <pru-icss-fw-pru-icss-sorte>`
.. |__PRU-ICSS I2C__| replace:: :ref:`PRU-ICSS I2C <pru-icss-fw-pru-icss-i2c>`
.. |__PRU-ICSS IOLINK__| replace:: :ref:`PRU-ICSS IOLINK <pru-icss-fw-pru-icss-iolink>`


+-----------------------------+----------------------------+----------------------------+----------------------------+
| **Compilers**                                                                                                      |
+=============================+============================+============================+============================+
| |__TI C6000__|              | |__TI ARM__|               | |__TI PRU__|               | |__Linaro GCC ARM__|       |
+-----------------------------+----------------------------+----------------------------+----------------------------+

.. |__TI C6000__| replace:: :ref:`TI C6000 <compilers-ti-c6000>`
.. |__TI ARM__| replace:: :ref:`TI ARM <compilers-ti-arm>`
.. |__TI PRU__| replace:: :ref:`TI PRU <compilers-ti-pru>`
.. |__Linaro GCC ARM__| replace:: :ref:`Linaro GCC ARM <compilers-linaro-gcc-arm>`
