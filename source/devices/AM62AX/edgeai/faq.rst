.. _pub_edgeai_FAQs:

====
FAQs
====

.. _pub_edgeai_multiple_usb_cams:

Getting Error when trying to capture from multiple USB cameras simultaneously
=============================================================================

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

#. Download and install `Processor SDK Linux <https://software-dl.ti.com/processor-sdk-linux/esd/AM62AX/10_01_00/exports/docs/devices/AM62AX/linux/Overview/Download_and_Install_the_SDK.html>`__
#. Get the patch to add `bandwidth_cap` parameter to `uvcvideo` kernel module `uvcvideo patch <https://www.spinics.net/lists/linux-media/msg175596.html>`_
#. Apply the patch to kernel source in Processor SDK Linux Install path. Please refer to `PSDK building kernel <https://software-dl.ti.com/processor-sdk-linux/esd/AM62AX/10_01_00/exports/docs/linux/Foundational_Components_Kernel_Users_Guide.html#overview>`_
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
