************************************
Processor SDK Technical Support
************************************

Technical support is a broad term. Our desire is to provide a solid
product, good documentation, and useful training that defines a clear
path for developing a product based on the Linux/RTOS/Android SDKs.
However, we know we'll never cover everything that can be done, and
occasionally we even make mistakes <gasp>. So, when you can't seem to
find what you need, there's a good place to search through previously
answered questions and ask a new one - The E2E Support Forums.

There is an active community of TIers and other customers like you
already using a TI Processor, on these forums. You may find your
question has already been answered with a quick Search of the Forums. If
not, a quick post will likely provide you the answers you need.

-  `E2E Processor Support
   <https://e2e.ti.com/support/processors/>`__

Open Source Software Support Disclaimer
=======================================

.. ifconfig:: CONFIG_sdk in ('SITARA')

    Processor SDK Linux integrates various free and open source software (FOSS) to demonstrate the hardware capabilities of Sitara devices. The FOSS offers many advantages to the customers such as flexibility, interoperability, robustness, reduced development time and support from the respective FOSS community.

.. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational')

    Processor SDK Linux Automotive integrates various free and open source software (FOSS) to demonstrate the hardware capabilities of Jacinto devices. The FOSS offers many advantages to the customers such as flexibility, interoperability, robustness, reduced development time and support from the respective FOSS community.


TI uses Yocto Project to integrate various software components and to build |__SDK_FULL_NAME__|. Yocto Project has two releases per year in April and October. TI’s Long-term Support (LTS) build for next year is based on current year’s October release of the Yocto Project. During a given year, TI’s LTS version migration only happens once per year and it occurs towards the end of the second quarter. The LTS migration usually signifies newer version of Kernel, U-boot, Toolchain, Yocto Project and etc. For more information on the current release, please refer to the Release Notes in the "Release Specific" section of respective platform. Therefore, the various open source components included in the |__SDK_FULL_NAME__| are only updated once per year.

While TI integrates the FOSS in |__SDK_FULL_NAME__|, TI does not own, maintain and support the entire FOSS. If users have educational queries, feature enhancement requests or discover a bug on any components, TI encourages the users to reach out to the respective FOSS community for any additional support. Below are helpful resources to seek support on a few of the individual FOSS components. Please keep in mind that we are only showing a few of the components below but the same concept applies to all of the FOSS integrated in the |__SDK_FULL_NAME__|.


.. ifconfig:: CONFIG_part_family not in ('AM64X_family')

    **Gstreamer Framework**

    - https://gstreamer.freedesktop.org/documentation/
    - Gstreamer application tutorials: https://gstreamer.freedesktop.org/documentation/tutorials/

    **QT Framework**

    - https://www.qt.io
    - https://doc.qt.io
    - https://forum.qt.io

    **Wayland Weston**

    - https://wayland.freedesktop.org

    .. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational')

        **Robot Operating System (ROS)**

        - http://www.ROS.org
        - For meta-ros (embedded version of ROS, that runs on our ARM): https://github.com/bmwcarit/meta-ros

    .. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational')

        **V4L2**

        For programming external video devices, a V4L2 sub-device driver is needed to be used in conjunction with the V4L2 driver. It also uses some of the helper kernel libraries videobuf2 (VB2) for common buffer operations, queue management and memory management.

        - https://www.kernel.org/doc/html/v5.10/admin-guide/media/index.html
        - https://www.kernel.org/doc/html/v5.10/userspace-api/media/v4l/v4l2.html
        - https://www.kernel.org/doc/html/v5.10/driver-api/media/v4l2-videobuf2.html
        - https://www.kernel.org/doc/html/v5.10/driver-api/media/v4l2-subdev.html

    **Graphics**

    - Direct Rendering Infrastructure (DRI): https://dri.freedesktop.org/wiki/Documentation/
    - Direct Rendering Manager (DRM): http://dri.freedesktop.org/wiki/DRM/
    - Kernel Mode Setting (KMS): https://www.kernel.org/doc/html/v5.10/gpu/drm-kms.html
    - Graphics Execution Manager (GEM): https://www.kernel.org/doc/html/v5.10/gpu/drm-mm.html#the-graphics-execution-manager-gem


    .. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational')

        Example applications:

        - https://github.com/tomba/kmsxx
        - http://git.ti.com/sitara-linux/dual-camera-demo/trees/master
        - The modetest tool is available inside git://anongit.freedesktop.org/git/mesa/drm

        **OpenCV**

        - OpenCV: https://opencv.org/
        - Documentation, tutorials and examples of how to use OpenCV 3.1: https://docs.opencv.org/3.1.0/#gsc.tab=0
        - OpenCL offload through OpenCV 3.1 transparent API: https://opencv.org/opencl/

