.. http://processors.wiki.ti.com/index.php/Processor_Linux_SDK_CCS_Installation_Guide
.. rubric:: Overview
   :name: overview-linux-CCS-Installation

Code Composer Studio (CCS) is the IDE integrated with the Processor
Linux SDK and resides on your host Ubuntu machine. This wiki article
covers the CCS basics including installation, importing/creating
projects and building projects. It also provides links to other CCS wiki
pages including debugging through GDB and JTAG and accessing your target
device remotely through Remote System Explorer.

CCS is an optional tool for the SDK, and may be downloaded and installed
at the same time that the SDK is installed or at a later date. For
instructions on how to download the Processor Linux SDK, please see
`Processor SDK Linux
Installer <../../Overview/Download_and_Install_the_SDK.html>`__.

CCS uses the Eclipse backend and includes the following plugins:

-  Remote System Explorer - provides tools which allow easy access to
   the remote target board
-  Cross-compile for GCC- allows easy access to the ARM GCC-based
   compiler included in the Processor Linux SDK

.. note::

   You should download CCS from the Processor Linux SDK Download page
   because it comes with the above plug-ins already installed. Otherwise,
   you will have to install the plug-ins yourself in order to take
   advantage of all the features covered in the wiki help pages and wiki
   training pages.

|

.. rubric:: Prerequisites
   :name: prerequisites-ccs-install

If you wish to use CCS along with the Processor Linux SDK, there are
requirements to consider before you attempt to install and run CCS. To
be prepared for development, you should have already setup your host
Linux machine and you should already have your target board up and
running. Additionally, you should be able to communicate from the host
to the target with serial and Ethernet communication.

For more information on setting up your development environment, see the
`Processor SDK Linux Getting Started
Guide <../../Overview/Processor_SDK_Linux_Getting_Started_Guide.html#start-your-linux-development>`__.

|

.. rubric:: Toolchain
   :name: toolchain

The Processor Linux SDK comes with an integrated ARM GCC toolchain
located on your Ubuntu host. CCS is integated with the SDK allowing you
to build, load, run and debug code on the target device. In more recent
SDK versions (v06.00, v08.00, v01.00.00.00, v02.00.00.00, etc) for
non-ARM 9 devices, a new ARM based toolchain is used and the location
of the toolchain has changed. For more information on the GCC toolchain,
please see `Processor Linux SDK GCC
Toolchain <../../Overview/GCC_ToolChain.html>`__.

Latest SDK toolchains use a prefix of **arm-linux-gnueabihf-**. Versions
older than Processor Linux SDK 06.00 and AM18x users may still use the
prefix **arm-arago-linux-gnueabi-**.

|

.. rubric:: Locating the CCS Installer
   :name: locating-the-ccs-installer

.. rubric:: Using the SD Card Provided with the EVM
   :name: using-the-sd-card-provided-with-the-evm

When the SD card provided in the box with the EVM is inserted into an SD
card reader attached to a Linux system three partitions will be mounted.
The third partition, labeled START\_HERE, will contain the CCS installer
along with the Processor Linux SDK installer. The CCS installer is
located inside of the CCS directory and there is a helper script called
ccs\_install.sh available to help call the installer.

.. rubric:: Downloading from the Web
   :name: downloading-from-the-web

The CCS installer is available for download for Linux as a compressed
tarball (tar.gz) file. It is also available for Windows. The installer
can be located by browsing to `SDK for Sitara
Processors <http://www.ti.com/tool/linuxezsdk-sitara>`__ and selecting
the device being used. The CCS installer can be found on the device's
SDK installer page under the Optional Addons or directly from the
`Download CCS <https://www.ti.com/tool/download/CCSTUDIO>`__ page.

.. Image:: /images/SDK_download_page.png

Clicking this link will prompt you to fill out an export restriction
form. After filling out the form, you will be given a download button to
download the file and you will receive an e-mail with the download link.
Download the tarball and save it to your Linux host development system.

|

.. rubric:: Starting the CCS Installer
   :name: starting-the-ccs-installer

.. rubric:: Installing CCS from the Linux Command Line
   :name: installing-ccs-from-the-linux-command-line

If you want to install CCS apart from the Processor Linux SDK installer,
or if you decided not to install it as part of the SDK install and want
to install it now, you can install CCS using the following commands:

#. Open a Linux terminal and change directory to the location where the
   CCS tarball is located. This may be the START\_HERE partition of the
   SD card or the location where you downloaded the file from ti.com or
   the wiki page.
#. If the CCS files are still in a compressed tarball, extract them.
   <version> is the version string of the CCS installer.
   **tar -xzf CCS<version>\_web\_linux.tar.gz**
#. Begin the installer by executing the binary (.bin) file extracted.
   **./ccs\_setup\_<version>.bin**

|

.. rubric:: CCS Installation Steps
   :name: ccs-installation-steps

.. note::

   The "Limited 90-day period" language in the CCS installer license
   agreement applies only for the case of using high-speed JTAG emulators
   (does not apply to use of the XDS100v2 JTAG emulator or an on-board
   emulator). If a debug configuration is used that requires a high-speed
   JTAG emulator, you will be prompted to register your software for a fee.
   All use of CCS (excluding use of high-speed JTAG emulators) is free and
   has no 90-day time limit.

When the CCS installer runs, you can greatly reduced the install time
and installed disk space usage by taking the defaults as they appear in
this CCS installer. The screen captures below show the default
installation options and the recommended settings when installing CCS.

#. The *License Agreement* screen will prompt you to accept the terms of
   the license agreement. Please read these terms and if you agree,
   select **I accept the terms of the license agreement**. If not, then
   please exit the installation.
#. At the *Choose Installation Location* just hit "Next" to install at
   the default location. If you want the SDK installed at a different
   location then select "Browse" and pick another location.

.. Image:: /images/Sitara_Linux_CCS_Install_Directory.png

#. At the *Processor Support* screen make sure to select the **Sitara
   ARM 32-bit processors** option. You should not select "GCC ARM
   Compiler" or "TI ARM Compiler", because you will be using the ARM
   toolchain that comes with the Processor Linux SDK installation.

.. Image:: /images/Sitara_Linux_CCS_Choose_Sitara.png

#. At the *Select Emulators* screen, select any emulators that you have
   and want to use. This is an optional feature you can use for
   debugging via JTAG.

.. Image:: /images/Sitara_Linux_CCS_emulator.png

#. At the *APP Center* screen none of the options should be selected,
   click **Finish** to begin installation.

.. Image:: /images/Sitara_Linux_CCS_Finish_and_install.png

#. Now the installation process starts and this can take some time.

.. Image:: /images/Sitara_Linux_SDK_CCS_installing.png

#. After installation is complete, you should see the following screen,
   hit finish and installation is complete.

.. Image:: /images/Sitara_Linux_SDK_finished.png

|

.. rubric:: Installing Emulator Support
   :name: installing-emulator-support

If during the CCS installation you selected to install drivers for the
Blackhawk or Spectrum Digital JTAG emulators, a script must be run with
administrator privileges to allow the Linux Host PC to recognize the
JTAG emulator. The script must be run as "sudo" with the following
command:

**sudo <CCS\_INSTALL\_PATH>/ccsv6/install\_scripts/install\_drivers.sh**
where <CCS\_INSTALL\_PATH> is the path that was chosen when the CCS
installer was run.

|

.. rubric:: Launching CCS
   :name: launching-ccs

#. **Double-Click the Code Composer Studio v6 icon on the desktop**. You
   will see a splash screen appear while CCS loads.

.. Image:: /images/CCSv6_splash.png

#. The next window will be the *Workspace Launcher* window which will
   ask you where you want to locate your CCSv6 workspace. Use the
   **default** value.

.. Image:: /images/CCS_workspace_launcher.png

#. CCS will load the workspace and then launch to the default *TI
   Resource Explorer* screen.

.. Image:: /images/CCS_getting_started.png

#. **Close the TI Resource Explorer screen**. This screen is useful when
   making TI CCS projects which use TI tools. The Processor Linux SDK
   uses open source tools with the standard Eclipse features and
   therefore does not use the TI Resource Explorer. You will be left in
   the Project Explorer default view.

.. Image:: /images/CCS_project_explorer.png

|

.. rubric:: Enabling CCS Capabilities
   :name: enabling-ccs-capabilities

Each time CCS is started using a new workspace, perspectives for
additional capabilities will need to be enabled. These are selectable in
the **Window -> Open Perspectives** list.

After opening CCS with a new workspace:

#. Open the **Window -> Preferences** menu.

.. Image:: /images/Sitara-Linux-CCS-window-preferences.png

#. Go to the **General -> Capabilities** menu.

.. Image:: /images/Sitara-Linux-CCS-general-capabilities.png

#. Select the **RSE Project** Capability.

.. Image:: /images/Sitara-Linux-CCS-enable-rse.png

#. Click **Apply** and then **OK**. This enables the perspectives in the
   **Window -> Open Perspective -> Other** menu, as shown below, and is
   needed to make the Remote System Explorer plug-ins selectable.

.. Image:: /images/Sitara-Linux-CCS-open-perspective.png

|

.. rubric:: Importing C/C++ Projects
   :name: importing-cc-projects

.. rubric:: Importing the Projects
   :name: importing-the-projects

#. Launch CCSv6 and load the default workspace.
#. From the main CCSv6 window, select **File -> Import...** menu item to
   open the import dialog.
#. Select the **General -> Existing Projects into Workspace** option.

.. Image:: /images/CCS_import.png

#. Click **Next**.
#. On the *Import Projects* page click **Browse**.

.. Image:: /images/CCS_import_browse.png

#. In the file browser window that is opened navigate to the **<SDK
   INSTALL DIR>/example-applications** directory and click **OK**.

.. Image:: /images/CCS_example_apps.png

#. The *Projects:* list will now be populated with the projects found.
#. Uncheck the following projects. They are Qt projects and are imported
   using a different method.

   -  matrix\_browser
   -  refresh\_screen

#. Select the projects you want to import. The following screen capture
   shows importing all of the example projects for an ARM-Cortex device,
   excluding the matrix\_browser project.

.. Image:: /images/CCS_example_uncheck.png

#. Click **Finish** to import all of the selected projects.
#. You can now see all of the projects listed in the *Project Explorer*
   tab.

.. Image:: /images/CCS_projects_added.png

.. rubric:: Building the C/C++ Projects
   :name: building-the-cc-projects

In order to build one of the projects, use the following steps. For this
example we will use the *mem-util* project.

#. Right-Click on the **mem-util project** in the *Project Explorer*.
#. Select the build configuration you want to use.

   -  For Release builds: **Build Configurations -> Set Active ->
      Release**
   -  For Debug builds: **Build Configurations -> Set Active -> Debug**

#. Select **Project -> Build Project** to build the highlighted project.
#. Expand the mem-util project and look at the mem\_util.elf file in the
   Debug or Release directory (depending on which build configuration
   you used). You should see the file marked as an [arm/le] file which
   means it was compiled for the ARM.

   .. Image:: /images/CCS_build_memutil.png

   .. note::

      You can use **Project -> Build All** to build all of the projects in
      the *Project Explorer*.

.. rubric:: Installing C/C++ Projects
   :name: installing-cc-projects

There are several methods for copying the executable files to the target
file system:

#. Use the top-level Makefile in the SDK install directory. See
   `Processor Linux SDK Top-Level
   Makefile <../../Overview/Top_Level_Makefile.html>`__ for
   details of using the top-level Makefile to install files to a target
   file system. This target file system can be moved via an SD card
   connected to the host machine and then to the target board,
   transferred via TFTP, or some other method. For more information on
   setting up a target filesystem, see `Processor SDK Linux Setup
   Script <../../Overview/Run_Setup_Scripts.html>`__.

   .. note::

      The top-level Makefile uses the install commands in the component
      Makefiles and can be used as a reference for how to invoke the
      install commands.

#. For all file system types, you can also transfer the file using the
   drag-and-drop method of Remote System Explorer. See the `Remote
   System Explorer <#remote-system-explorer-ccs-install>`__ section below for more
   details.
#. Files can also be moved from the Linux command line. Typically,
   executable files are stored in the project's Debug folder in the
   workspace.

|

.. rubric:: Creating a New Project
   :name: creating-a-new-project-ccs-install

This section will cover how to create a new cross-compile project to
build a simple *Hello World* application for the target.

.. rubric:: Configuring the Project
   :name: configuring-the-project-ccs-install

#. From the main CCSv6 window, select **File -> New -> Project...** menu
   item.
#. In the *Select a wizard* window, select the **C/C++ -> C Project**
   wizard.

   .. Image:: /images/CCS_new_project.png

#. Click **Next**.
#. In the *C Project* dialog set the following values:
   Project Name: **helloworld**
   Project type: **Executable -> Empty Project**
   Toolchains: **Cross GCC**

   .. Image:: /images/CCS_C_project.png

#. Click **Next**.
#. In the *Select Configurations* dialog, you can take the default
   *Debug* and *Release* configurations or add/remove more if you want.

   .. Image:: /images/CCS_config.png

#. Click **Next**.
#. In the *Command* dialog, set the following values:
   Tool command prefix: **arm-linux-gnueabihf-**.

   .. note::

      The prefix ends with a "-". This is the prefix of the cross-compiler
      tools as will be seen when setting the *Tool command path*.

   Tool command path:
   **/home/sitara/ti-sdk-<machine>-<version>/linux-devkit/sysroots/<Arago
   Linux>/usr/bin**
#. Use the *Browse..* button to browse to the Sitra Linux SDK
   installation directory and then to the **linux-devkit/sysroots/<Arago
   Linux>/usr/bin** directory. You should see a list of tools such as
   *gcc* with the prefix you entered above.

   .. Image:: /images/CCS_gcc_command.png

#. Click **Finish**.
#. After completing the steps above you should now have a *helloworld*
   project in your CCS *Project Explorer* window, but the project has no
   sources.

   .. Image:: /images/CCS_pe_helloworld.png

.. rubric:: Adding Sources to the Project
   :name: adding-sources-to-the-project-ccs-install

#. From the main CCS window select **File -> New> Source File** menu
   item.
#. In the *Source File* dialog set the *Source file:* setting to
   **helloworld.c**

   .. Image:: /images/CCS_new_source.png

#. Click **Finish**.
#. After completing the steps above you will have a template
   **helloworld.c** file. Add your code to this file like the image below:

   .. Image:: /images/CCS_helloworld.png

#. Compile the **helloworld** project by selecting **Project -> Build
   Project**
#. The resulting executable can be found in the *Debug* directory.

   .. Image:: /images/CCS_helloworld_build.png

|

.. rubric:: Remote System Explorer
   :name: remote-system-explorer-ccs-install

CCS as installed with this SDK includes the Remote System Explorer (RSE)
plugin. RSE provides drag-and-drop access to the target file system as
well as remote shell and remote terminal views within CCS. Refer to
`Processor Linux SDK CCS Remote System Explorer
Setup <../../Foundational_Components/Tools/Code_Composer_Studio.html#remote-explorer-setup-with-ccs>`__
to establish a connection to your target EVM and start using RSE. There
is also a more detailed training using RSE with the SDK at `Processor
SDK Linux Training: Hands on with the Linux
SDK <http://processors.wiki.ti.com/index.php/Processor_SDK_Linux_Training:_Hands_on_with_the_Linux_SDK>`__.

|

.. rubric:: Using GDB Server in CCS for Linux Debugging
   :name: using-gdb-server-in-ccs-for-linux-debugging

In order to debug Linux code using Code Composer Studio, you first need
to configure the GDB server on both the host and target EVM side.

Please refer to `Processor Linux SDK CCS GDB
Setup <../../Foundational_Components/Tools/Code_Composer_Studio.html#gdb-setup-with-ccs>`__ for more
information.

