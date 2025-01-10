Video Graphics Test
===================

Introduction
------------

The video graphics test application demonstrates various video processing, graphics and display capabilities using VIP, GC320, SGX and DSS IPs. Many embedded applications need multiple displays with multiple videos and graphics planes rendered on different screens. Such applications can be developed with or without using a windowing system like Wayland. Using a windowing system demands more system resources like CPU, GPU and DDR bandwidth and increases system complexity. When the system resources are in a crunch and there is no real need to use a windowing system, many users prefer to use no windowing system (alternately called as NULL window or full-screen mode). The video graphics test application demonstrates such application development in full-screen mode using QT.

QT framework is a popular tool to draw the software or hardware accelerated graphics contents. It can manage the display backend of embedded Linux system to render the contents in full-screen mode.  It provides creation of a full-screen window by platform-specific means, known as QT Platform Abstraction (QPA).  EGLFS is a platform plugin for running Qt5 applications on top of EGL and OpenGL ES 2.0 without an actual windowing system. When having multiple displays connected, QT provides another plugin named eglfs_kms to render the content on multiple displays. In eglfs_kms QPA, DRM Linux Kernel Mode Setting (KMS) API is used to set DSS mode. By default, eglfs_kms provided by QT doesn’t take advantage of the advance capabilities of DSS IP such as scaling, overlaying and alpha-blending of the videos/graphics planes.

To enable optimal usage of all the IPs on the AM57x8 devices and to deliver the best performance while running the QT application, we have enhanced the eglfs_kms QPA to leverage the DSS IP advance capabilities.  The QPA exposes many callback functions through QPlatformNativeInterface to allow the users to set DSS IP advance properties. This enhanced QPA is packaged in PSDK Linux filesystem.

GC320 Usage for Rotation, Composition, Overlaying and Alpha-Blending
----------------------------------------------------------------------

GC320 is the 2D graphics accelerator from the Vivante Corporation and the IP is capable of performing tasks such as scaling, bit-blitting, rotation, composition, alpha-blending and many other 2D processing. Please refer to the Technical Reference Manual for the SOCs to learn about the capabilities of the GC320 accelerator.

DSS IP can accept up to 4 videos and graphics planes as input and send them individually or as overlaid/composed frames to different display monitors. If the application needs to display more planes than what DSS can accept, then it is recommended to use GC320 for composition/overlaying of some of those planes before sending to DSS. In the video graphics test application, we demonstrate GC320 usage for video scaling, rotation and overlaying/composition feature.

Application Description
------------------------

In the video graphics test application, we have demonstrated embedded application displaying two different videos and graphics contents rendered on two different display monitors in full-screen mode. One of the video sources comes from camera input hooked to parallel capture port VIP. Captured video is submitted to QT eglfs_kms QPA to be rendered on Display1 device. Next, the application takes the relevant information from the camera input and passes two copies of the same image to the GC320. The GC320 takes one copy and does not modify the image. For the second copy, the GC320 will rotate the image by 90 degrees. Then, the GC320 will stitch both images together and the output is submitted to QT plugin for rendering on Display2 device. QT framework is also used to draw analog clock and Maroon game using QT QML. The analog clock is set to be rendered on Display1 and Maroon game to be rendered on Display2. QT uses OpenGL APIs to render the graphics contents using 3D graphics accelerator SGX544. The users submit the properties of video planes like scaling, overlaying, alpha-blending, number of display monitors and etc using the APIs exposed through QPlatformNativeInterface. It sets the video planes to blend with graphics planes and the resulting output renders to the size of the display on both the monitors. QT uses DSS hardware accelerator to accelerate the overlaying, alpha blending and scaling processing.

**Video Graphics Test Block Diagram**

.. Image:: /images/video_graphics_test1.png

eglfs-kms QPA User Exposed APIs
-------------------------------

As part of eglfs_kms QPA enhancement, following APIs are exposed via QPlatformNativeInterface to allocate DSS hardware planes, to set the plane properties supported by DSS and to submit the buffer for display.

.. code-block:: html

    1. create_plane: Secure DSS hardware planes for overlay from QT QPA
    2. distroy_plane: Free the reserved DSS hardware planes
    3. export_buffer: Export user allocated buffer to the QT QPA
    4. distroy_buffer: Free the buffers
    5. set_plane_properties: Set the DSS plane properties for scaling of video planes and blending it with graphics planes. Properties can be set for both DRM plane type Primary and Overlay planes.
    6. get_plane_property: Read default/pre-set property value of a plane
    7. queue_plane: Queue the video buffer to a QPA plane to be overlayed/displayed
    8. start_disp_plane: Begin displaying of the queued buffers
    9. user_call_back_handle: Pass callback function pointer to the QT eglfs_kms QPA. The QPA will call this function to notify user the display completion of the overlay buffer

The APIs required to achieve scaling, overlaying and alpha-blending using the DSS IP owned by eglfs_kms QPA are demonstrated inside disp_obj.cpp and video_graphics_test.cpp file. An example of the software flow is shown below:

.. Image:: /images/video_graphics_test2.png

Running the Test
----------------
In order for the users to run the video graphics test, please type the following commands on the EVM:

::

    target # insmod /lib/modules/<kernel_version>/extra/galcore.ko baseAddress=0x80000000 physSize=0x80000000
    target # /etc/init.d/weston stop
    target # export QT_QPA_EGLFS_INTEGRATION=eglfs_km
    target # video-graphics-test -platform eglfs
