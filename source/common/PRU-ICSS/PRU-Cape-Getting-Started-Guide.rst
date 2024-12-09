.. _pru_cape_getting_started_guide:

PRU Cape Getting Started Guide
------------------------------

.. note::

    The PRU Cape continues to be an excellent hardware tool for enabling PRU
    development on AM335x. Note that the demo software referenced in this
    document is legacy code that is no
    longer supported on the TI forums (AM335x Starterware).

.. rubric:: Introduction

This guide is intended to walk through the basic instructions on how to
get started with your PRU Cape using the available demo software.

The PRU Cape is a test, development, and evaluation module system that
enables developers to write software and develop hardware around the PRU
subsystem. The diagram below shows the basic features supported by the
cape. For more details about the PRU Cape hardware, please refer to the
:ref:`pru_cape_hardware_user_guide`.

|

.. image:: /images/Pru_cape-wiki-blockdiagram.png

|

.. rubric::  Prerequisites

The hardware and software prerequisites needed to run the getting
started demo are listed below.

.. rubric::  Hardware

-  BeagleBone or BeagleBone Black `(Can be ordered from
   beagleboard.org) <https://www.beagleboard.org/boards/beaglebone-black>`__
-  BeagleBone PRU Cape `(Can be ordered from
   ti.com) <https://www.ti.com/tool/PRUCAPE>`__
-  MicroSD card formatted as FAT32
-  USB cable to power BeagleBone or BeagleBone Black
-  FTDI cable for BeagleBone Black serial debug port *(not required for
   original BeagleBone)*
-  Speakers or headphones for audio demo
-  RS-232 serial cable for hardware UART demo

.. rubric::  Software

The **PRU Cape Demo Software** is available in the `PRU Software
Support
Package <https://git.ti.com/pru-software-support-package/pru-software-support-package/>`__
hosted on git.ti.com. To download this package, select the "Source Tree"
button from the PRU Software Support Package webpage and then click
"Download master as tar.gz." In Windows, a program such as 7-zip can be
used to open the downloaded file and extract the software package.
