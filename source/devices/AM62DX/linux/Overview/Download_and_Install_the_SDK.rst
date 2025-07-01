.. _download-and-install-sdk:

Download and Install the SDK
============================

The |__SDK_FULL_NAME__| Installer will install the necessary components
to start Linux development on the TI microprocessor.

**The** |__SDK_FULL_NAME__| **Release supports installer only for Linux machine.**

+----------------------------------------------+----------------------------------------------------------------------+
| **Installer Details**                        | **Installers Name**                                                  |
+----------------------------------------------+----------------------------------------------------------------------+
|  AM62D Linux SDK Installer (Linux version)   | ti-processor-sdk-linux-am62dxx-evm-<version>-Linux-x86-Install.bin   |
+----------------------------------------------+----------------------------------------------------------------------+

Use Linux installer for complete source package, tools, prebuilt-image, filesystems,
etc for product development.

From a windows machine, you can only flash a SD card. This can be done without
installing the SDK. Use balenaEtcher to flash SD card from windows machine.

The |__SDK_FULL_NAME__| includes the ARM GCC toolchain.
The |__SDK_FULL_NAME__| was built and tested against a specific Linux
Distribution name and version, Ubuntu |__LINUX_UBUNTU_VERSION_SHORT__|.
Note that this **does not** prevent the user from installing the SDK on other Linux
distributions.

Download & Install the SDK Installer Inside a Container
-------------------------------------------------------

TI provides a Ubuntu 22.04 based docker image with all the packages that are required to install the SDK Installer.

The Docker image is hosted on `ghcr.io/texasinstruments <https://github.com/TexasInstruments/ti-docker-images/pkgs/container/ubuntu-distro>`__.

Refer `Steps to Run SDK Installer inside a Container <https://github.com/TexasInstruments/ti-docker-images?tab=readme-ov-file#steps-to-run-sdk-installer-inside-container>`__ for a comprehensive guide.

.. note::

    Before starting the container, ensure that you have completed all the Pre-Requisites as mentioned `here <https://github.com/TexasInstruments/ti-docker-images?tab=readme-ov-file#pre-requisites>`__.

Download & Install the SDK Installer on Host
--------------------------------------------

You can download the latest |__SDK_FULL_NAME__| installer from the
|__SDK_DOWNLOAD_URL__|.

.. rubric:: Required Host Packages to Install the SDK Installer in Linux
   :name: required-host-packages-to-install-the-sdk-installer-linux

Please run the following command to install all packages required to Install the SDK Installer on Ubuntu |__LINUX_UBUNTU_VERSION_SHORT__|.

.. code-block:: console

    host# sudo apt-get install file fdisk dosfstools

.. rubric:: How to Run the SDK Installer in Linux
   :name: how-to-run-the-sdk-installer-linux

Make sure that the execute permissions are set. Open the terminal
window and change directories to where installation program is located
(probably the Downloads directory) and run the following commands:

.. parsed-literal::

    # For AM62D (am62dxx-evm) Installer
    chmod +x ./ti-processor-sdk-linux-am62dxx-evm-<version>-Linux-x86-Install.bin
    ./ti-processor-sdk-linux-am62dxx-evm-<version>-Linux-x86-Install.bin

Alternatively, you can give execute permissions and run the SDK Installer
by double clicking on it within your Linux host PC.

.. note::
   As a part of the installation, installation program will run a script to configure
   your environment and extract the Linux devkit. This will cause the installation to
   continue for roughly a minute even after it shows that it has reached 100%.

.. note::
   If nothing seems to happen, your computer may be running a 32-bit version of
   its operating system. The installation program is 64-bit, and will not execute properly.


**MCU+ SDK for RTOS/NO-RTOS**

.. note::
   AM62D Linux SDK contains only the Linux specific source and application intended
   to run on A53/Linux core. For A53 based FreeRTOS side source and applications, refer **MCU+ SDK**


**Instructions to set-up CCS**


