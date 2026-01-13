.. _EV_charging_Demo_User_Guide-label:

###########################################################
AM62L Electric Vehicle Supply Equipment (EVSE) - User Guide
###########################################################

************
Introduction
************

Electric Vehicle Supply Equipment (EVSE) systems require sophisticated control mechanisms to support multiple charging standards and protocols.
The `TIDA-010939`_ reference design addresses this complexity by providing a comprehensive front-end controller solution that serves as the central
communication module for EV charging operations.

This reference design combines the `AM62L MPU`_ with the `MSPM0 MCU`_ to create a versatile platform supporting both AC and
DC charging across global standards including Combined Charging System (CCS), Guobiao/Tuijian (GB/T), and Charge de Move (CHAdeMO).

The `AM62L MPU`_ runs the EV charging software stack on Linux, handling digital communication with electric vehicles,
Ethernet and wireless connectivity for backend communications, and display capabilities for human-machine interface (HMI) integration.
The `MSPM0 MCU`_ manages critical analog handshakes with electric vehicles and safety functions, including control pilot signaling,
proximity detection, and temperature monitoring of charging connectors.

The reference design provides multiple communication interfaces—CAN, RS-485, RS-232, and Ethernet—enabling control of power conversion units,
external metering devices, and other peripherals.

The `TIDA-010939`_ reference design is referred to as **AM62L-EVSE-DEV-EVM** throughout this documentation.

.. note::

   For complete hardware setup, testing procedures, and system architecture details, refer to the `AM62L-EVSE-DEV-EVM Software User Guide`_.

This guide is intended for software engineers and system integrators who are:

* Porting existing EV charging solutions to the `AM62L-EVSE-DEV-EVM`_ platform
* Developing custom EV charging applications using the |__SDK_FULL_NAME__|
* Integrating the platform with existing charging infrastructure

This documentation assumes you have an existing EV charging software stack ready for integration. If you do not have a charging stack,
consider evaluating `EVerest`_, an open-source EV charging software platform.


************
SDK Overview
************

|__SDK_FULL_NAME__| provides software support for the `AM62L-EVSE-DEV-EVM`_, enabling all communication interfaces
required for EV charging applications. The SDK facilitates rapid development and deployment of EV charging solutions on this hardware platform.

The EVSE-specific SDK image :file:`tisdk-evse-image` extends the standard TI SDK image :file:`tisdk-default-image` with additional
packages and configurations required for the `AM62L-EVSE-DEV-EVM`_ to function properly.


********************************
Quick Start with Pre-built Image
********************************

For quick evaluation and testing, download the latest pre-built WIC image: |__SDK_DOWNLOAD_URL__|

After downloading and flashing the image to your SD card, proceed directly to testing the communication interfaces by following the
procedures in the `AM62L-EVSE-DEV-EVM Software User Guide`_.


***************************
Building the SDK with Yocto
***************************

This section describes how to build the EVSE WIC image from source using the Yocto Project build system.
Follow the standard :ref:`Processor SDK - Building the SDK with Yocto <building-the-sdk-with-yocto>` and build for the EV charging Use case.


********************************
Testing Communication Interfaces
********************************

The `AM62L-EVSE-DEV-EVM`_ provides multiple communication interfaces essential for EV charging applications:

* **PLC (Power Line Communication)** - For ISO 15118 high-level communication
* **CAN** - For communication with power conversion units and vehicle networks
* **RS-485** - For industrial protocol communication with metering devices
* **RS-232** - For legacy device communication

Complete testing procedures, pinout information, and example configurations for all communication interfaces are documented in the `AM62L-EVSE-DEV-EVM Software User Guide`_.


**********************************
Using EVerest as EV charging stack
**********************************

Pre-Requisites
==============

Before you begin, ensure you have a working Yocto build for EV charging by following the steps given in :ref:`Processor SDK - Building the SDK with Yocto <building-the-sdk-with-yocto>`

Steps
=====

Follow the steps given below to add `EVerest`_ stack into the WIC image.

1. Edit :file:`sources/meta-tisdk/meta-ti-foundational/recipes-core/images/tisdk-evse-image.bb` and add ``everest-core`` & ``tida-010939-everest-config`` packages:

   .. code-block:: console

      IMAGE_INSTALL:append = " \
         everest-core \
         tida-010939-everest-config \
      "

   .. important::

      Find the existing ``IMAGE_INSTALL:append`` section in the file. **Do not remove or modify the existing packages**. Add the two new packages to the list.

2. Re-build the WIC image

   .. code-block:: console

      $ . conf/setenv
      $ MACHINE=am62lxx-evm ARAGO_RT_ENABLE=1 bitbake -k tisdk-evse-image

   Once the build is completed successfully, WIC image should include the `EVerest`_ stack.

3. Flash the WIC image on the device and run the command below to verify if `EVerest`_ stack is added.

   .. code-block:: console

      $ systemctl status everest


   If `EVerest`_ is added then the output should show ``Active: active (running)``, If it shows ``Unit everest.service could not be found.``
   then `EVerest`_ did not get added to the WIC image.

For further information on changing the `EVerest`_ configuration, refer `AM62L-EVSE-DEV-EVM Software User Guide`_.


********************
Additional Resources
********************

* `AM62L-EVSE-DEV-EVM Software User Guide`_ - Complete hardware setup, testing procedures, and system architecture
* `AM62L-EVSE-DEV-EVM`_ User Guide
* `TIDA-010939`_ Reference Design - Product page, specifications and resources
* `AM62L MPU`_ Product Page - AM62L MPU specifications and resources
* `AM62L Product Overview`_
* `AM62L Device Academy`_
* `EVerest`_ Open Source EV Charging Stack


.. _AM62L-EVSE-DEV-EVM Software User Guide: https://www.ti.com/lit/pdf/SLUUDH5

.. _AM62L-EVSE-DEV-EVM: https://www.ti.com/lit/ug/slvudn0/slvudn0.pdf

.. _TIDA-010939: https://www.ti.com/tool/TIDA-010939

.. _AM62L MPU: https://www.ti.com/product/AM62L

.. _EVerest: https://everest.github.io/

.. _AM62L Device Academy: https://dev.ti.com/tirex/explore/node?node=A__AEIJm0rwIeU.2P1OBWwlaA__AM62L-ACADEMY__6F61DO6__LATEST

.. _AM62L Product Overview: https://www.ti.com/lit/po/sprt790/sprt790.pdf

.. _MSPM0 MCU: https://www.ti.com/product/MSPM0G3507



Glossary
========

.. glossary::

   CCS
      Combined Charging System - A fast-charging standard for electric vehicles supporting both AC and DC charging.

   CHAdeMO
      Charge de Move - A DC fast-charging standard developed in Japan for electric vehicles.

   EVSE
      Electric Vehicle Supply Equipment - The infrastructure and equipment used to supply electric energy for charging electric vehicles.

   GB/T
      Guobiao/Tuijian - Chinese national standards for electric vehicle charging, including GB/T 20234 (connectors) and GB/T 27930 (communication protocol).

   PLC
      Power Line Communication - Technology that enables data transmission over existing power cables, used in ISO 15118 for vehicle-to-grid communication.
