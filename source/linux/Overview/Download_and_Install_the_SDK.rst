.. _download-and-install-sdk:

Download and Install the SDK
============================

.. http://processors.wiki.ti.com/index.php/Processor_SDK_Linux_Installer
.. rubric:: Overview
   :name: download-and-install-sdk-overview

The |__SDK_FULL_NAME__| Installer (|__SDK_INSTALL_FILE__|)
will install the necessary components to start your development on the
TI microprocessor.

The SDK consists of a development filesystem, a
target filesystem, example applications, toolchain and board support
package, ease of use scripts and documentation.

The |__SDK_FULL_NAME__| now includes the ARM GCC toolchain.
The |__SDK_FULL_NAME__| was built and tested against a specific Linux
Distribution name and version, Ubuntu |__LINUX_UBUNTU_VERSION_SHORT__|.
Note this **does not** prevent the user from installing the SDK on other Linux
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

.. ifconfig:: CONFIG_sdk in ('SITARA')

    .. rubric:: How to Get the SDK Installer
       :name: how-to-get-the-sdk-installer

    There are two ways you can get the installer:

    1. From a file downloaded from the |__SDK_DOWNLOAD_URL__|.
       This will always host the latest version of SDK.

       .. note::
          The second way below is not applicable to K2H/K2K, K2E, and K2L
          platforms, which are using SD card.

    2. From the SD Card included with a TI EVM. This may not be the latest
       version of the SDK. We recommend checking the above site and using the
       latest version if at all possible. Before running the SDK Installer from
       the SD card, the SD Card from the EVM box needs to be mounted to your
       Linux Host PC (using a USB SD Card reader).  The SDK Installer is found
       in the START\_HERE partition of the SD card.

.. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational')

    .. rubric:: Downloading the SDK installer
       :name: downloading-the-sdk-installer

    You can download the latest |__SDK_FULL_NAME__| installer from the
    |__SDK_DOWNLOAD_URL__|.

.. rubric:: How to Run the SDK Installer
   :name: how-to-run-the-sdk-installer

.. ifconfig:: CONFIG_sdk in ('SITARA')

    Make sure that the execute permissions are set. Bring up a terminal
    window and change directories to where the installer is located
    (probably the Downloads directory if downloaded or the START\_HERE
    partition mounted from the SD Card) and run the following commands:

.. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational')

    Make sure that the execute permissions are set. Bring up a terminal
    window and change directories to where the installer is located
    (probably the Downloads directory) and run the following commands:

.. parsed-literal::

    chmod +x ./|__SDK_INSTALL_FILE__|
    ./|__SDK_INSTALL_FILE__|

Alternatively, you can give execute permissions and run the "|__SDK_INSTALL_FILE__|"
by double clicking on it within your Linux host PC.

.. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational')

    .. note::
       As a part of the installation, the packaging will run a script to configure your
       environment and download the Linux devkit.  This will cause the installation to
       continue for roughly a minute even once it shows that it has reached 100%.

.. note::
   If nothing seems to happen, you are probably running a 32-bit version of
   Linux. The installer is 64-bit, and will not execute properly.

.. rubric:: Additional Installer Options
   :name: additional-installer-options

Invoking the installer with argument --help will list available options
for the installer (e.g. text installer, etc.):

.. parsed-literal::

    ./|__SDK_INSTALL_FILE__| --help

.. rubric:: SDK Installer Execution Steps
   :name: sdkinstaller-execution-steps

1. **Confirm**
   User is to confirm if loading the |__SDK_FULL_NAME__| is ok. This is
   important to note if the user is trying to over-install on an existing
   directory and has made changes to the directory.
2. **Directory Install Location**
   The user will be prompted for a location on where to put the |__SDK_FULL_NAME__|.
   An example is given below.
3. **Installation of software**
   The software is installed.

.. rubric:: Where to install the Processor SDK package
   :name: where-to-install-the-processor-sdk-package

The default selection of where to install is the user's home directory.

.. ifconfig:: CONFIG_sdk in ('SITARA')

    In this particular example the name of the user is 'sitara'.

    .. Image:: /images/Processor_sdk_select_directory.png

.. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational')

    .. Image:: /images/Processor_sdk_jacinto_select_directory.png


After the installation, refer to section `Setting up host environment <Run_Setup_Scripts.html>`__ for next steps.

