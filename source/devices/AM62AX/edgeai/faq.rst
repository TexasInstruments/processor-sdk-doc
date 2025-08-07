.. _pub_edgeai_FAQs:

####
FAQs
####

.. _pub_edgeai_overlay:

*****************************************************************************************************************************************
Why does "ERROR: Unable to map memory @ 0xa2000000..." appear after applying a custom DTBO using name_overlays from SDK 11.1 with EdgeAI?
*****************************************************************************************************************************************

Background
==========

Starting with Processor SDK 11.1, the :file:`k3-am62a7-sk-edgeai.dtbo` overlay is automatically applied by default in the AM62A board environment (``ti-u-boot``).
This is set via the ``name_overlays`` variable in U-Boot, as seen in `board/ti/am62ax/am62ax.env <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tree/board/ti/am62ax/am62ax.env?h=11.01.05#n22>`__

Issue
=====

If you add or override overlays using :file:`uEnv.txt` (e.g. for enabling IMX219 camera support), you may unintentionally replace the default ``name_overlays`` value.
This means the essential EdgeAI memory carve-out overlay (:file:`k3-am62a7-sk-edgeai.dtbo`) is no longer applied.
As a result, EdgeAI applications may fail to allocate memory, showing errors such as:

.. code-block:: console

   APP_LOG: ERROR: Unable to map memory @ 0xa2000000 of size 3288576 bytes !!!

Who is affected?
================

EdgeAI users upgrading to SDK 11.1 (or newer) who apply custom device tree overlays and do not re-apply the EdgeAI carve-out overlay.

Solution
========

Always include :file:`k3-am62a7-sk-edgeai.dtbo` in your overlays when customizing ``name_overlays`` in :file:`uEnv.txt` or at the U-Boot prompt.
For example - To enable IMX219 camera support

.. code-block:: console

   name_overlays=ti/k3-am62a7-sk-edgeai.dtbo ti/k3-am62x-sk-csi2-imx219.dtbo

This ensures the memory region required by EdgeAI applications is reserved.

Summary Table
-------------

.. csv-table:: Summary
   :header: "SDK Version","Default EdgeAI Overlay","Action Needed When Customizing Overlays"

   "≤ 10.1", "None", "Only add your required overlays"
   "≥ 11.1", "EdgeAI overlay applied", "Must re-apply EdgeAI overlay when overriding `name_overlays`"

.. tip::

   If you encounter memory mapping errors after customizing overlays, verify that the EdgeAI carve-out overlay is present in your configuration.

.. _pub_edgeai_multiple_usb_cams:

*****************************************************************************
Getting Error when trying to capture from multiple USB cameras simultaneously
*****************************************************************************

This is a common issue faced in the industry with many USB cameras.
You may get errors like ``Failed to allocate required memory.`` when tying to
capture simultaneously from more than one usb cameras.

The root cause for this issue is that most of the USB cameras requests for more
BW than actually required. If the use case is to capture only from 2 USB cameras
, it can be done by connecting one of them to USB type-C port since it is
internally connected to a separate instance of USB controller. But if the use
case is to capture from more than 2 cameras, you need to modify the UVC driver
to override the BW allocation.

The root cause and work around is explained in detail in this
blog `Multiple UVC cameras on linux <https://www.thegoodpenguin.co.uk/blog/multiple-uvc-cameras-on-linux>`_

To apply the work around to our SDK, use below steps

#. Download and install `Processor SDK Linux <https://software-dl.ti.com/processor-sdk-linux/esd/AM62AX/11_01_07_05/exports/docs/devices/AM62AX/linux/Overview/Download_and_Install_the_SDK.html>`__
#. Get the patch to add `bandwidth_cap` parameter to `uvcvideo` kernel module `uvcvideo patch <https://www.spinics.net/lists/linux-media/msg175596.html>`_
#. Apply the patch to kernel source in Processor SDK Linux Install path. Please refer to `PSDK building kernel <https://software-dl.ti.com/processor-sdk-linux/esd/AM62AX/11_01_07_05/exports/docs/linux/Foundational_Components_Kernel_Users_Guide.html#overview>`_
#. Compile only `uvcvideo` module using below command

   .. code-block:: bash

      make ARCH=arm64 CROSS_COMPILE=aarch64-none-linux-gnu- am62ax_evm_a53_defconfig
      make ARCH=arm64 CROSS_COMPILE=aarch64-none-linux-gnu- ./drivers/media/usb/uvc/uvcvideo.ko
#. Copy `./drivers/media/usb/uvc/uvcvideo.ko` to sk
#. Remove `uvcvideo` module and install modified version using below commands

   .. code-block:: bash

      rmmmod uvcvideo
      insmod uvcvideo.ko
#. Set the desired BW cap as shown below

   .. code-block:: bash

      echo 1200 >  /sys/module/uvcvideo/parameters/bandwidth_cap

.. note::

   The unit of BW here is Bytes/125us, you can estimate the approximate BW
   requirement by multiplying fps with size/frame
