.. _List-of-filesystems-in-SDK:

Filesystem
==========

The |__SDK_FULL_NAME__| provides a filesystem tarball that contains
programs, scripts, Linux user-space components that abstract various
hardware accelerators available in the SoC. The filesystem can be
built via Yocto, following the instructions
:ref:`Processor SDK - Building the SDK with Yocto <building-the-sdk-with-yocto>`

There are different filesystem tarballs provided in the SDK. You'll find them at
:file:`${PSDK_PATH}/filesystem/`


.. ifconfig:: CONFIG_sdk in ('SITARA')

    .. rubric:: tisdk-base-image

    This is the barebones images, intended to be a starting point for
    users to add packages and create a custom filesystem that suits their
    project needs.

    .. rubric:: tisdk-thinlinux-image

    This is a minimal system image enabled with containers to provide
    an environment to start the next level of complex systems up. Depending
    on the platform capabilities, graphics is enabled by default as well.


.. rubric:: tisdk-default-image

This is the complete filesystem image, that contains standard Linux
commands and features. This also contains the TI component libraries,
binaries and :ref:`TI Apps Launcher OOB Demo <TI-Apps-Launcher-User-Guide-label>`

.. only:: _comment

    [comment] current SDK 7.x build for 'PSDK' doesn't have docker/tiny image, so comment out the following section

    .. rubric:: tisdk-docker-rootfs-image

    This is a minimal image with support for Docker.
    See `Docker Linux Container Runtime <Foundational_Components/Virtualization/Docker.html>`__ for more information.

    .. rubric:: arago-tiny-image

    This is the absolute minimal filesystem. The boot files are omitted from this
    image and systemd has been replaced with sysvinit.


Following is a list of all filesystem images provided by TI which can be built via Yocto

.. code-block:: text

    Common targets are:

    From meta-arago[recommended]:
        tisdk-bootstrap-base-image:  Arago TI SDK bootstrap base image for initramfs
        tisdk-jailhouse-image:  Arago TI SDK image for Jailhouse Hypervisor
        tisdk-bootstrap-image:  Arago TI SDK bootstrap image usable for board bringup
        tisdk-tiny-initramfs:  Arago TI SDK super minimal base image for initramfs
        tisdk-core-bundle:  Installer package for TI SDK - NOT for direct use on target
        tisdk-base-image:  Arago TI SDK base image with test tools
        tisdk-thinlinux-image:  Arago TI SDK Thin Linux image
        tisdk-jailhouse-inmate:  Arago TI SDK super minimal base image for jailhouse linux demo
        tisdk-default-image:  Arago TI SDK full filesystem image
        tisdk-tiny-image:  Arago TI SDK super minimal base image for initramfs

    From meta-tisdk:
        tisdk-display-cluster-image:  Arago TI SDK full filesystem image showcasing display sharing in AM62P


.. note::

    Watchout for console logs while running `oe-layersetup <https://git.ti.com/cgit/arago-project/oe-layersetup/>`__
    to get an exhaustive list of target filesystem images that can be built using Yocto.
