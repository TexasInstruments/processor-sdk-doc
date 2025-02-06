
Dual Camera
===========

Below diagram illustrates the video data processing flow of dual camera demo.

.. Image:: /images/Dual_camera_demo.png

**Dual camera example demo demonstrates the following**

#. Video capture using V4L2 interface from up to two cameras.
#. QT QWidget based drawing of user interface using linuxfb plugin, where linuxfb is an fbdev based software drawn QPA.
#. Hardware accelerated scaling of input video from primary camera to display resolution using DSS IP.
#. Hardware accelerated scaling of input video from secondary camera (if connected) to lower resolution using DSS IP.
#. Hardware accelerated overlaying of two video planes and graphics plane using DSS IP.
#. Scaling of two video planes and overlaying with graphics plane happens on the fly in single pass inside DSS IP using DRM atomic APIs.
#. Snapshot of the screen using JPEG compression running on ARM. The captured images are stored in filesystem under the :file:`/usr/share/camera-images/` folder
#. The camera and display driver shares video buffer using DMA buffers. The capture driver writes content to a buffer which is directly read by the GPU and potentially the display without copying the content locally to another buffer (zero copy involved).
#. The application also demonstrates allocating the buffer from either omap_bo (from omapdrm) memory pool or from cmem buffer pool. The option to pick omap_bo or cmem memory pool is provided runtime using cmd line.
#. If the application has need to do some CPU based processing on captured buffer, then it is recommended to allocate the buffer using CMEM buffer pool. The reason being omap_bo memory pool doesn't support cache read operation. Due to this any CPU operation involving video buffer read will be 10x to 15x slower. CMEM pool supports cache operation and hence CPU operations on capture video buffer are fast.
#. The application runs in nullDRM/full screen mode (no compositors like Weston) and the linuxfb QPA runs in fbdev mode. This gives application full control of DRM resource DSS to control and display the video planes.

**Instructions to run dual camera demo**

* Since the application need control of DRM resource (DSS) and there can be only one master, make sure that the wayland/weston is not running.
* Run the dual camera application ``dual-camera -platform linuxfb <0/1>``
* When last argument is set as 0, capture and display driver allocates memory from omap_bo pool.
* When it is set to 1, the buffers are allocated from CMEM pool.
