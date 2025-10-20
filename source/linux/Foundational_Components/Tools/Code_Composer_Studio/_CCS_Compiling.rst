.. http://processors.wiki.ti.com/index.php/Processor_Linux_SDK_CCS_Compiling_Guide
.. rubric:: Overview

Code Composer Studio (CCS) v6.0 is the IDE integrated with the Sitara
SDK and resides on your host Ubuntu machine. This wiki article covers
the CCS basics including installation, importing/creating projects and
building projects. It also provides links to other CCS wiki pages
including debugging through both GDB and JTAG and accessing your target
device remotely through remote system explorer.

.. rubric:: Prerequisites
   :name: prerequisites-ccs-compiling

If you wish to use CCS along with the Sitara Linux SDK, there are some
setup steps required before you attempt to install and run CCS.

#. You need to be prepared for development. This means you should have
   already setup your host linux machine and you should already have
   your target up and running. Additionally you should be able to
   communicate from host to target with both the following:

   #. Serial communication for linux boot and linux debug
   #. Ethernet communication for utilizing some of the CCS debug file
      sharing capabilities

See this link to meet the above requirements:
`Sitara\_Linux\_SDK\_Getting\_Started\_Guide#Start\_your\_Linux\_Development <../../Overview/Processor_SDK_Linux_Getting_Started_Guide.html#start-your-linux-development>`__

.. rubric:: Building Qt Applications
   :name: building-qt-applications

Although the Processor Linux SDK includes several Qt example
applications using Code Composer Studio to build or debug these
applications isn't recommended. QT Creator is the official IDE designed
to be used when developing or debugging Qt applications.

|

.. rubric:: Importing Existing C/C++ Projects
   :name: importing-existing-cc-projects

The Processor Linux SDK includes several example applications that
already includes the appropriate CCS Project files. The following
instructions will help you to import the example C/C++ application
projects into CCS.

.. rubric:: Importing the Project
   :name: importing-the-project

#. From the main CCS window, select **File -> Import...** menu item to
   open the import dialog
#. Select the **General -> Existing Projects into Workspace** option

   .. Image:: /images/Import_C_projects-1.png

#. Click **Next**
#. On the **Import Projects** page click **Browse**

   .. Image:: /images/Sitara-Linux-CCS-import-c.png

#. In the file browser window that is opened navigate to the **<SDK
   INSTALL DIR>/example-applications** directory and click **OK**

   .. Image:: /images/Example-applications.png

Select the projects you want to import. The following screen capture
shows importing all of the example projects for an ARM-Cortex device,
excluding the Qt projects.

   .. Image:: /images/Import-Qt.png

#. Click **Finish** to import all of the selected projects.
#. You can now see all of the projects listed in the **Project Explorer**
   tab.

.. Image:: /images/Projects-imported.png

.. rubric:: Creating a New Project
   :name: creating-a-new-project-ccs-compiling

This section will cover how to create a new cross-compile project to
build a simple **Hello World** application for the target.

.. rubric:: Configuring the Project
   :name: configuring-the-project-ccs-compiling

#. From the main CCS window, select **File -> New -> Project...** menu
   item
#. in the **Select a wizard** window select the **C/C++ -> C Project**
   wizard

   .. Image:: /images/Sitara-Linux-CCS-new-c-project.png

#. Click **Next**
#. In the **C Project** dialog set the following values:
   Project Name: **helloworld**
   Project type: **Cross-Compile Project**

   .. Image:: /images/Sitara-Linux-CCS-cross-compile.png

#. Click **Next**
#. In the **Command** dialog set the following values:
   Tool command prefix: **arm-linux-gnueabihf-**. Note the the prefix
   ends with a "-". This is the prefix of the cross-compiler tools as
   will be seen when setting the **Tool command path**
   Tool command path: **<SDK INSTALL
   DIR>/linux-devkit/sysroot/i686-arago-linux/usr/bin**. Use the
   **Browse..** button to browse to the Sitra Linux SDK installation
   directory and then to the **linux-devkit/bin** directory. You should
   see a list of tools such as **gcc** with the prefix you entered above.

   .. Image:: /images/Sitara-Linux-CCS-command-setup.png

#. Click **Next**
#. In the **Select Configurations** dialog you can take the default
   **Debug** and **Release** configurations or add/remove more if you want.

   .. Image:: /images/Sitara-Linux-CCS-select-configurations.png

#. Click **Finish**

.. rubric:: Adding Sources to the Project
   :name: adding-sources-to-the-project-ccs-compiling

#. After completing the steps above you should now have a **helloworld**
   project in your CCS *Project Explorer* window, but the project has no
   sources.

   .. Image:: /images/Sitara-Linux-CCS-empty-helloworld.png

#. From the main CCS window select **File -> New -> Source File** menu
   item
#. In the **Source File** dialog set the *Source file:* setting to
   **helloworld.c**

   .. Image:: /images/Sitara-Linux-CCS-helloworld-c-file.png

#. Click **Finish**

#. After completing the steps above you will have a template
   **helloworld.c** file. Add your code to this file like the image
   below:

   .. Image:: /images/Sitara-Linux-CCS-helloworld.png

.. rubric:: Compiling C/C++ Projects
   :name: compiling-cc-projects

#. Right-Click on the project in the *Project Explorer*
#. Select the build configuration you want to use

   -  For Release builds: **Build Configurations -> Set Active ->
      Release**
   -  For Debug builds: **Build Configurations -> Set Active -> Debug**

   .. Image:: /images/Code_Composer_Studio_Changing_Build_Configuration.png

#. Select **Project -> Build Project** to build the highlighted project

   .. Image:: /images/Code_Composer_Studio_Compiling_Project.png

#.

   -  **NOTE:** You can use **Project -> Build All** to build all of the
      projects in the *Project Explorer*

|
| Now that you have built your application you are ready to run and or
  debug the executable.

|

.. rubric:: Next Steps
   :name: next-steps-ccs-compiling

.. rubric:: Copying Binaries to the File system
   :name: copying-binaries-to-the-file-system

There are several methods for copying the executable files to the target
file system:

-  Copying files manually to the SD card root file system
-  If NFS is being used, copying the files manually to the NFS file
   system
-  Using Code Composer Studio to automatically copy the executable to
   the target evm using `Remote System
   Explorer <../../Foundational_Components/Tools/Code_Composer_Studio.html#remote-explorer-setup-with-ccs>`__

|

.. rubric:: Remote System Explorer
   :name: remote-system-explorer-ccs-compiling

CCS v6 by default includes the Remote System Explorer (RSE) plug-in. RSE
provides drag-and-drop access to the target file system as well as
remote shell and remote terminal views within CCS. It also provides a
way for Code Composer Studio to automatically copy and run or debug an
executable using a single button. Refer to `How to Setup and Use Remote
System
Explorer <../../Foundational_Components/Tools/Code_Composer_Studio.html#remote-explorer-setup-with-ccs>`__ to
learn how to use this feature.

|

.. rubric:: Debugging Source Code using Code Composer Studio
   :name: debugging-source-code-using-code-composer-studio-ccs-compiling

In order to debug user-space Linux code using Code Composer Studio v6,
you first need to configure your project to use gdb and gdbserver
included within the SDK.

Please refer to `Debugging using GDB with Code Composer
Studio <../../Foundational_Components/Tools/Code_Composer_Studio.html#gdb-setup-with-ccs>`__ for more
information.

