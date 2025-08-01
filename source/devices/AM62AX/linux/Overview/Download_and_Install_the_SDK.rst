.. _download-and-install-sdk:

Download and Install the SDK
============================

The |__SDK_FULL_NAME__| Installer will install the necessary components
to start Linux development on the TI microprocessor.

**The** |__SDK_FULL_NAME__| **Release supports installer only for Linux machine.**

+--------------------------------------------+-------------------------+
| **Installer Details**                      | **Installers Name**     |
+--------------------------------------------+-------------------------+
| PSDK Linux AM62A Installer (Linux version) | |__SDK_INSTALL_FILE__|  |
+--------------------------------------------+-------------------------+

Use Linux installer for complete source package, tools, prebuilt-image, filesystems,
etc for product development.

From a windows machine, you can only flash a SD card. This can be done without
installing the SDK. Use balenaEtcher to flash SD card from windows machine.

The |__SDK_FULL_NAME__| includes the ARM GCC toolchain.
The |__SDK_FULL_NAME__| was built and tested against a specific Linux
Distribution name and version, Ubuntu |__LINUX_UBUNTU_VERSION_SHORT__|.
Note that this **does not** prevent the user from installing the SDK on other Linux
distributions.

.. rubric:: Downloading the SDK installer
   :name: downloading-the-sdk-installer

You can download the latest |__SDK_FULL_NAME__| installer from the
|__SDK_DOWNLOAD_URL__|.

.. rubric:: How to Run the SDK Installer in Linux
   :name: how-to-run-the-sdk-installer-linux

Make sure that the execute permissions are set. Bring up a terminal
window and change directories to where the installer is located
(probably the Downloads directory) and run the following commands:

.. parsed-literal::

    chmod +x ./|__SDK_INSTALL_FILE__|
    ./|__SDK_INSTALL_FILE__|

Alternatively, you can give execute permissions and run the "|__SDK_INSTALL_FILE__|"
by double clicking on it within your Linux host PC.

.. rubric:: How to Run the SDK Installer in Windows
   :name: how-to-run-the-sdk-installer-windows

Double click on the installer to begin installation.

.. note::

   As a part of the installation, the installer will run a script to configure your
   environment and extract the Linux devkit. This will cause the installation to
   continue for roughly a minute even after it shows that it has reached 100%.

.. note::

   If nothing seems to happen, your computer may be running a 32-bit version of
   its operating system. The installer is 64-bit, and will not execute properly.

**Package Overview**

This AM62A Software development kit contains Linux device drivers, sample examples and
application specific demos.  The SDK has the below folder structure


+----------------------+---------------------------------------------------------+
| **Folder Name**      | **Description**                                         |
+----------------------+---------------------------------------------------------+
| bin                  | set-up scripts, SD card image creation script           |
|                      |                                                         |
+----------------------+---------------------------------------------------------+
| board-support        | Linux board supported packages (prebuilt-images, tools, |
|                      | Linux kernel and u-boot in source)                      |
+----------------------+---------------------------------------------------------+
| licenses             | Software Licenses                                       |
|                      |                                                         |
+----------------------+---------------------------------------------------------+
| manifests            | Software Manifests                                      |
|                      |                                                         |
+----------------------+---------------------------------------------------------+
| filesystem           | Prebuilt Filesystems (both tar and wic images)          |
|                      |                                                         |
+----------------------+---------------------------------------------------------+
| linux-devkit         | Linux development kit (tools, compilers etc.)           |
|                      |                                                         |
+----------------------+---------------------------------------------------------+
| k3r5-devkit          | RTOS (R5F) development kit (tools, compilers etc.)      |
|                      |                                                         |
+----------------------+---------------------------------------------------------+
| example-applications | Sample examples and application specific demos          |
|                      | (GUI composer of benchmark demos)                       |
+----------------------+---------------------------------------------------------+

Refer :ref:`Release Notes <Release-note-label>` for complete feature-set and further details


**MCU+ SDK for RTOS/NO-RTOS**

.. note::

   Processor SDK Linux AM62A contains only the Linux specific source and application intended
   to runs on A53/Linux core. For R5F and RTOS/NO-RTOS side source and applications, refer **MCU+ SDK**
   package `[Use Link] <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62AX/11_01_00_16/exports/docs/api_guide_am62ax/index.html>`__.

**Instructions to set-up CCS**

-  Refer `[Use Link] <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62AX/11_01_00_16/exports/docs/api_guide_am62ax/CCS_SETUP_PAGE.html>`__
