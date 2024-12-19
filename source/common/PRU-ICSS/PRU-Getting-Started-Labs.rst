.. _pru_getting_started_labs:

PRU Getting Started Labs
========================

* :ref:`pru_getting_started_labs_lab_1`
* :ref:`pru_getting_started_labs_lab_2`
* :ref:`pru_getting_started_labs_lab_3`
* :ref:`pru_getting_started_labs_lab_4`
* :ref:`pru_getting_started_labs_lab_5`


Introduction
------------

The PRU Getting Started Labs demonstrate:

#. How to create a PRU project in Code Composer Studio (CCS), or from the Linux
   terminal

#. How to write PRU firmware in C, assembly, or mixed C and assembly

#. How to compile PRU firmware from CCS, or from the Linux terminal

   * CCS shows how to compile binaries that can be loaded by CCS, another core
     running Linux, or another core running RTOS or NORTOS (NORTOS is also known
     as "bare metal" or "no OS")

   * Linux terminal shows how to compile binaries that can be loaded by another
     core running Linux

#. How to initialize the PRU from CCS, or another core running Linux

#. How to debug the PRU from CCS, or another core running Linux

.. note::

   These labs reference the Processor SDK and MCU+ SDK documentation. To find
   the SDK documentation:

   #. Go to the processor's product page. (AM64x example:
      https://www.ti.com/product/AM6442)

   #. Go to section "Design & Development" -> "Software development" ->
      "MCU-PLUS-SDK" or "PROCESSOR-SDK-LINUX".

   #. Select "Download options" -> "Documentation". Click the link to the
      latest SDK documentation. (AM64x example for MCU+ SDK 10.1:
      https://software-dl.ti.com/mcu-plus-sdk/esd/AM64X/10_01_00_32/exports/docs/api_guide_am64x/index.html)

   #. If using an SDK that is not the latest SDK, it is suggested to use that
      release's SDK documentation instead of the latest SDK documentation.

.. note::

   This lab documentation is under active development. It will be updated between
   SDK releases. If there are any questions, please reach out on the TI e2e
   forums.

.. note::

   Steps to initialize the PRU from another core running an OS from an MCU+ SDK
   (i.e., RTOS or NORTOS) will be
   added at a later time. Not all cores running RTOS or NORTOS can initialize
   the PRU. Reference the MCU+ SDK release notes to see which cores support
   initializing the PRU with the **PRUICSS** driver.

.. note::

   These labs do **not** cover cores running an OS from a Processor SDK RTOS
   (i.e., TI-RTOS). Steps to initialize the PRU from a core running TI-RTOS
   are provided as a resource for customers using AM335x, AM437x, and
   AM57xx. However, the TI-RTOS steps have **not** been tested. See
   :ref:`pru_getting_started_labs_last_tested_config` for more information.

.. note::

   Steps to debug the PRU from a core running an OS from an MCU+ SDK (i.e.,
   RTOS or NORTOS) will be added at a later time.


Supported Processors
^^^^^^^^^^^^^^^^^^^^

* PRU-ICSS processors: AM335x, AM437x, AM57xx

* PRU-SS processors: AM62x

* PRU_ICSSG processors: AM64x, AM65x


Required Hardware and Software
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following hardware and software are required to complete the PRU Getting
Started Labs:

.. rubric::  Hardware

* EVM board: Any TI EVM for a supported processor, or BeagleBone Black

* Power supply for the board

* Debug connector: JTAG emulator, FTDI cable, or micro USB cable for UART port
  depending on the board. Some EVMs have an onboard debugger, while some EVMs
  require a separate JTAG emulator

* Computer running Linux or Windows


.. rubric::  Software

* A Processor SDK for the processor. Install the Linux or MCU+
  Processor SDK as appropriate.

* The PRU Software Support Package (PSSP)

  * The PSSP is included in the **example-applications/pru-icss-x.y.z/** folder of
    many Linux Processor SDK releases.

  * If using an MCU+ SDK, a Linux SDK without the PSSP installed,
    or if running Windows on the computer, download the PSSP from the
    git repository
    `here <https://git.ti.com/cgit/pru-software-support-package/pru-software-support-package>`__.
    The notation **<PSSP_PATH>** will be used throughout the labs to reference
    the PSSP installation location.

* `Code Composer Studio (CCS) <https://www.ti.com/tool/CCSTUDIO>`__

* `PRU Code Generation
  Tools <https://software-dl.ti.com/codegen/non-esd/downloads/download.htm#PRU>`__
  (also available through the CCS App Center)

.. note::

   If using a Linux Processor SDK, check which version of the PSSP is used:

    * SDK 7.x (Linux kernel 5.4): compatible with PSSP tags v5.7.0 - v5.9.0

    * SDK 8.x (Linux kernel 5.10): compatible with PSSP tags v6.0.0 onwards

   If using the PSSP packaged within the Linux Processor SDK, x.y.z in the
   folder name is the version number. e.g.,
   'example-applications/pru-icss-6.0.1/' uses tag v6.0.1. The tag can also
   be viewed in the PSSP files ReadMe.txt and Release_Notes.txt.


.. _pru_getting_started_labs_last_tested_config:

Last Tested Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

The PRU Getting Started Labs were last tested with:

* CCSv11.2

* AM335x Processor SDK Linux 7.3 with BeagleBone Black

* AM62x Processor SDK Linux 8.3 with AM62x SK EVM

* AM64x Processor SDK Linux 8.1 with AM64x General Purpose EVM

.. note::

   These labs do not cover cores running an OS from a Processor SDK RTOS (i.e.,
   TI-RTOS running on AM335x, AM437x, AM57xx, AM65x). Some legacy information is
   provided for initializing the PRU from TI-RTOS cores on AM335x, AM437x, and
   AM57xx. This information was written using PROCESSOR-SDK-RTOS 6.3. However,
   this information has not been tested or validated in several years. These
   sections are not supported by TI, and are marked **legacy**.

   TI no longer provides support for TI-RTOS / baremetal SW development for
   AM335x & AM437x. `See this notice for more information.
   <https://e2e.ti.com/support/processors-group/processors/f/processors-forum/1071334/notice-regarding-processor-sdk-ti-rtos-for-am335x-am437x-omap-l13x-c674x-k2g-devices>`__
