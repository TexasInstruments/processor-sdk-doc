.. _display-cluster-user-guide:

############################
Display Cluster - User Guide
############################

Overview
========

AM62Px supports display sharing between A53 and MCU R5 cores. Refer :ref:`How to enable display sharing between remote core and Linux <display-sharing-between-remotecore-and-linux>` for more details.
The Display Cluster Demo helps evaluate the display sharing feature out of the box without any manual changes in the filesystem.

Hardware Prerequisites
======================

  - `SK-AM62P-LP <https://www.ti.com/tool/SK-AM62P-LP>`__

  - Microtips LVDS Panel

  - SD card (minimum 16GB)

  - PC (Windows or Linux) to flash wic image onto an SD Card

  - :file:`tisdk-display-cluster` wic image (Available at |__SDK_DOWNLOAD_URL__|)

Steps to validate Display Cluster Demo
======================================

#. Flash an SD card with the :file:`tisdk-display-cluster` wic image. Please follow the instructions provided at :ref:`Create SD Card <processor-sdk-linux-create-sd-card>` guide.

#. Insert the flashed SD card to `SK-AM62P-LP <https://www.ti.com/tool/SK-AM62P-LP>`__, connect the Microtips LVDS Panel and power on both the display panel and TI SK-AM62P-LP.

#. As soon as the device is powered on, MCU R5 will display the Texas Instruments logo which slowly fades away and then starts displaying the Tell Tales before the Linux boots.

#. Once after the Linux is fully booted, it will launch the ti-demo binary which mimics an Automotive Display Cluster.

#. The entire screen is controlled by the A53 displaying the Cluster except the region where MCU R5 is overlaying the Tell Tales.

    .. figure:: /images/AM62P-display-cluster.png
      :width: 500
      :height: 400

#. Now even if Kernel or the application crashes for some reason, the MCU will still be displaying the Tell Tales with it's own pipeline.
   To demonstrate it, try crashing the Kernel by running the following:

   .. code-block:: console

       root@am62pxx-evm:~# echo c > /proc/sysrq-trigger

How to build Display Cluster Demo
=================================

Building Display Cluster wic image from Yocto
---------------------------------------------

    #. To build the display cluster wic image, please refer :ref:`Processor SDK - Building the SDK with Yocto <building-the-sdk-with-yocto>`

Building the Display Cluster Demo from source
---------------------------------------------

    #. The source code for Display Cluster demo is available as part of the `ti-apps-launcher <https://github.com/TexasInstruments/ti-apps-launcher>`__.
    #. Display Cluster Demo does not require building the source code.
    #. The demo can run provided that the app source code and Qt 6's  ``qmlscene`` utility are present.

    #. To start the demo, issue the following command
       .. code-block:: console

          qmlscene --fullscreen apps/auto_cluster.qml

Building the MCU Firmware from sources
--------------------------------------

    #. Please refer to the `MCU+ SDK Documentation <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62PX/11_01_01_08/exports/docs/api_guide_am62px/group__DRV__DSS__MODULE.html>`__
