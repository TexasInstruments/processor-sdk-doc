.. http://processors.wiki.ti.com/index.php/Sitara_Linux_Training:_Hands_on_with_QT
.. _hands-on-with-qt:
.. rubric:: Introduction
   :name: introduction-hands-on-qt

This lab is going to give you a hands on tutorial on QT, the GUI
devolpment tool, which is a component of the Sitara SDK. Each of the
following sections below will walk you through a particular Lab
exercise, the key points to take away, and the step-by-step
instructions to complete the lab. The labs in this section will
utilize both a command line build approach and a IDE approach using QT
Creator.

**Training:** - You can find the necessary code segments embedded
in the this article. You can cut and paste them from the wiki as
needed.

**Hands On Session:** - In the vmware image, there are cheater files:
/home/sitara/QT\_Lab You can cut and paste section of code from this
file rather than have to type them in. You can find a copy here, just
right click and select "Save Target As": `File:QT
Lab.tar.gz <http://processors.wiki.ti.com/index.php/File:QT_Lab.tar.gz>`__

**NOTE:** In this guide commands to be executed for each step will be
marked in **BOLD**

.. rubric:: Lab Configuration
   :name: lab-configuration

The following are the hardware and software configurations for this lab.
The steps in this lab are written against this configuration. The
concepts of the lab will apply to other configurations but will need to
be adapted accordingly.

.. rubric::
   Hardware
   :name: hardware

-  AM335x EVM-SK (TMDSSK3358) - `Order
   Now <https://estore.ti.com/TMDSSK3358-AM335x-Starter-Kit-P3110.aspx>`__

    .. raw:: html

       <div
       style="margin: 5px; padding: 2px 10px; background-color: #ecffff; border-left: 5px solid #3399ff;">

    **NOTE**
    All Sitara boards with an LCD display or HDMI/DVI out can be used
    for these labs, but the steps below related to serial and ethernet
    connections may differ.

    .. raw:: html

       </div>

-  Router connecting AM335x EVM-SK and Linux Host
-  USB cable connection between AM335x EVM-SK and Linux Host using the
   micro-USB connector (J3/USB0)

    .. raw:: html

       <div
       style="margin: 5px; padding: 2px 10px; background-color: #ecffff; border-left: 5px solid #3399ff;">

    **NOTE**
    The AM335x EVM uses a standard DB9 connector and serial cable. New
    Win7 based Host PCs may require a USB-to-Serial cable since newer
    laptops do not have serial ports. Additionally, since the serial
    connection is not required for these labs, you can telnet or ssh
    into the target over ethernet instead of using a serial terminal for
    target interaction.

    .. raw:: html

       </div>

-  5V power supply (typically provided with the AM335x EVM-SK)

.. rubric:: Software
   :name: software

-  A Linux host PC configured as per the `Linux Host
   Configuration <http://processors.wiki.ti.com/index.php/Sitara_Linux_Training:_Linux_Host_Configuration>`__
   page

   -  **\*\*PLEASE NOTE\*\*** currently the Linux Host Configuration
      page is under revision. Please download Ubuntu 14.04 rather than
      Ubuntu 12.04 at this link http://releases.ubuntu.com/14.04/

-  Sitara Linux SDK installed. This lab assumes the latest Sitara Linux
   SDK is installed in /home/sitara. If you use a different location
   please modify the below steps accordingly.
-  SD card with Sitara Linux SDK installed.

   -  For help creating a 2 partition SD card with the SDK content see
      the `create\_sdcard.sh
      script <Overview/Processor_SDK_Linux_create_SD_card.html>`__ page

-  QT Creator 5.7.0 installed on your Linux host.

   -  You can download Qt Creator from open source distribution version
      of Qt at http://download.qt.io/official_releases/qt/
   -  QT will download as a .run file. Make the file executable by
      running the **chmod + <qtfile>** command and **./<qtfile>**. These
      steps should launch the QT installer.
   -  Extract the package. Qt creator will be under Tools/Qt5.7.0
      folder. In some cases it may also be under the opt folder. Type
      **cd /opt/Qt5.7.0** into the command line to locate the file.
   -  The labs in this wiki page is validated with Ubuntu 14.04 on 64
      bit machine.

.. rubric:: Supported Platforms and revisions
   :name: supported-platforms-and-revisions

The following platforms are system tested to verify proper operation.

-  am335x
-  am37x
-  am35x
-  am180x
-  BeagleBoard XM

**This current version has been validated on ti-processor-sdk version
02.00.01.07 using QT Creator 3.6.0**

.. rubric:: LAB 1: Hello World Command Line
   :name: lab-1-hello-world-command-line

.. rubric:: Description
   :name: description

This LAB is optional, it introduces where to find QT components and
build tools in the Sitara SDK. Approximate time to complete this LAB: 15
minutes. This section will cover the following topics

-  Introduction to build tools
-  enviroment setup script
-  The QT component of the Sitara SDK

   -  where to find things in the Sitara SDK

.. rubric:: Key Points
   :name: key-points

-  Where in the SDK to find the build tools
-  Where in the SDK to find the QT components
-  How to setup your build environment
-  How to utilize the above points to create a Hello World application.

.. rubric:: Lab Steps
   :name: lab-steps

#. Connect the cables to the EVM. For details on where to connect these
   cables see the **Quick Start Guide** that came with your EVM.

   #. Connect the Serial cable to provide access to the console.
   #. Connect the network cable
   #. Insert the SD card into the SD connector
   #. Insert the power cable into the 5V power jack

#. Power on the EVM and allow the boot process to finish. You will know
   when the boot process has finished when you see the Matrix
   application launcher on the LCD screen

   .. raw:: html

      <div
      style="margin: 5px; padding: 2px 10px; background-color: #ecffff; border-left: 5px solid #3399ff;">

   **NOTE**
   You may be required to calibrate the touchscreen. If so follow the on
   screen instructions to calibrate the touchscreen.

   .. raw:: html

      </div>

#. Open a terminal window on your Linux host by double clicking the
   Terminal icon on the desktop
#. The cross-compiler is located in the linux-devkit/bin directory of
   the SDK installation directory. In the terminal window enter the
   following commands, replacing the <machine> and <sdk version> fields
   with the target machine you are using and the SDK version installed.

   .. raw:: html

      <div
      style="margin: 5px; padding: 2px 10px; background-color: #ecffff; border-left: 5px solid #3399ff;">

   **NOTE**
   You can use TAB completion to help with this

   .. raw:: html

      </div>

   -  **cd /home/sitara/AM335x/ti-processor-sdk-linux-<machine>-<sdk
      version>/linux-devkit/sysroots/x86\_64-arago-linux/usr/bin**
   -  **ls**

#. You should see a listing of the cross-compile tools available like
   the one below.

   .. Image:: /images/Sitara-linux-training-cross-tools-1.png

#. To locate the pre-built ARM libraries perform the following commands:

   -  **cd /home/sitara/AM335x/ti-processor-sdk-linux-<machine>-<sdk
      version>/linux-devkit/sysroots/cortexa8hf-vfp-neon-linux-gnueabi/usr/lib**
   -  **ls**

#. You should now see a listing of all the libraries (some are contained
   within their individual sub-directories) available as pre-built
   packages within the SDK.
#. Now list only the QT libraries from the same directory by listing all
   libs starting with libQt.

   -  **ls libQt\***

#. You should see a listing of QT related libraries that can be used to
   build and run QT projects.

   .. Image:: /images/Sitara_Linux_QT_library_listings_1.png

#. You can also find out where the QT header files are located. At the
   directory below are sub directories full of QT header files.

   -  **cd /home/sitara/AM335x/ti-processor-sdk-linux-<machine>-<sdk
      version>/linux-devkit/sysroots/cortexa8hf-vfp-neon-linux-gnueabi/usr/include/qt5**
   -  **ls**

#. In order to make it easier to perform cross-compilations and ensure
   linking with the proper cross-compiled libraries instead of the host
   system libraries the **environment-setup** script has been created in
   the linux-devkit directory. This script will configure many standard
   variables such as CC to use the cross-compile toolchain, as well as
   adding the toolchain to your PATH and configuring paths for library
   locations. To utilize the setting provided by the environment-setup
   script you will need to **source** the script. Perform the following
   commands to source the environment-setup script and observe the
   change in the QMAKESPEC variable:

   -  **echo $QMAKESPEC**
   -  **source /home/sitara/AM335x/ti-processor-sdk-linux-<machine>-<sdk
      version>/linux-devkit/environment-setup**
   -  **echo $QMAKESPEC**

#. You should see the changes that were applied by executing the setup
   script.

   .. Image:: /images/Sitara_Linux_QT_environment_setup_script.jpeg

#. You should have observed that the QMAKESPEC variable now contains the
   path to the QMAKESPEC files. Additionally your compile tools were
   added. There was also another change that occurred which was that
   your standard prompt changed from **sitara@ubuntu** to
   **[linux-devkit]**. The purpose of this change is to make it easy to
   identify when the environment-setup script has been sourced. This is
   important because there are times when you DO NOT want to source the
   environment-setup script. A perfect example is when building the
   Linux kernel. During the kernel build there are some applications
   that get compiled which are meant to be run on the host to assist in
   the kernel build process. If the environment-setup script has been
   sourced then the standard CC variable will cause these applications
   to be built for the ARM, which in turn will cause them to fail to
   execute on the x86 host system.

#. As mentioned above sometimes it is not appropriate to source the
   environment-setup script, or you only want to source it during a
   particular build but not affect your default environment. The way
   this is done in the SDK is to source the environment-setup script
   inside of the project Makefile so that it is used only during the
   build process.

#. Take a look at the enviroment setup file to see what all is going on
   there. Look through file to see where the compile tools variables
   such as CC and CPP and PATH are defined.

   -  **gedit /home/sitara/AM335x/ti-processor-sdk-linux-<machine>-<sdk
      version>/linux-devkit/environment-setup**

#. It is now time to build a Hello World project using QT. You need to
   create two files: helloworld.cpp and helloworld.pro

   -  **mkdir /home/sitara/AM335x/ti-processor-sdk-linux-<machine>-<sdk
      version>/example\_applications/helloworld**
   -  **cd /home/sitara/AM335x/ti-processor-sdk-linux-<machine>-<sdk
      version>/example\_applications/helloworld**
   -  **gedit helloworld.cpp** and add the following code

      .. raw:: html

         <div
         style="margin: 5px; padding: 5px 10px; background-color: #ffffec; border-left: 5px solid #ff6600;">

      **IMPORTANT**
      You can find pre-written files in the in the
      **/home/sitara/sitara-training-helper-files/QT\_Lab/lab1**
      directory. You can just copy those files to your directory instead
      of typing the contents if you want to

      .. raw:: html

         </div>

      `` #include <QApplication>``
      #include <QLabel>
      int main(int argc, char \*\*argv)
      {
      QApplication app(argc,argv);
      QLabel label("Hello World");
      label.show();
      return app.exec();
      }
   -  **gedit helloworld.pro** and add code

      .. raw:: html

         <div
         style="margin: 5px; padding: 5px 10px; background-color: #ffffec; border-left: 5px solid #ff6600;">

      **IMPORTANT**
      You can find pre-written files in the in the
      **/home/sitara/sitara-training-helper-files/QT\_Lab/lab1**
      directory. You can just copy those files to your directory instead
      of typing the contents if you want to

      .. raw:: html

         </div>

      ``QT += core gui widgets``
      SOURCES += helloworld.cpp

#. Now lets use qmake to create a Makefile

   -  **qmake helloworld.pro**

#. Notice how qmake automatically generated a Makefile for us, now lets
   build.

   -  **make**

#. Notice the build is using our cross-compiler-arm-linux-gnueabihf-g++

   .. Image:: /images/Sitara_Linux_QT_make_using_cross_compile.jpeg

#. Also notice we now have an executable, lets see what type of file we
   created

   -  **file helloworld**

#. You should see something similar to the following: helloworld: ELF
   32-bit LSB executable, ARM, version 1 (SYSV), dynamically linked
   (uses shared libs), for GNU/Linux 2.6.31,
   BuildID[sha1]=0x8569a0956d8efffcfde68fca5c883be5fa4f1c31, not
   stripped

#. Finally lets copy the helloworld over to our target file system and
   run it.

   -  If you have not already done so connect with **minicom** and type
      **ifconfig** to find your target's ip address

      .. raw:: html

         <div
         style="margin: 5px; padding: 2px 10px; background-color: #ecffff; border-left: 5px solid #3399ff;">

      **NOTE**
      You can also get your ip address from Matrix if it is running.
      **Select Settings->Network Settings**

      .. raw:: html

         </div>

   -  On your Linux host console issue the command **scp -r helloworld
      root@xx.xx.xx.xx:/home/root** replacing the xx.xx.xx.xx below with
      you target's ip address.
   -  When asked for password, just **hit return**
   -  **Type yes** when asked if you would like to continue
   -  Move back over to your minicom window and execute it. You should
      find the helloworld in your default /home/root directory on the
      target.

      -  **./helloworld**

#. You should see helloworld print on the LCD panel of your target
   board.


.. rubric:: LAB 2: QT Creator Hello World
   :name: lab-2-qt-creator-hello-world

.. rubric:: Description
   :name: description-1

This section will cover setting up QT Creator the integrated development
environment. We start to investigate how QT Creator aids in rapid GUI
development.

.. rubric:: Key Points
   :name: key-points-1

-  Setting up QT Creator to find your tools
-  Setting up QT Creator to communicate with the target platform
-  Creating hello world and run using QT Creator.

.. rubric:: Lab Steps
   :name: lab-steps-1

#. Source the enviroment setup file to ensure all the paths are setup
   correctly. This was done in the previous section. If you already see
   [linux-devkit]: as your prompt then you can skip this step.

   -  **source /home/sitara/AM335x/ti-processor-sdk-linux-<machine>-<sdk
      version>/linux-devkit/environment-setup**

#. Bring up Qt Creator

   -  **./home/sitara/Qt5.7.0/Tools/QtCreator/bin/qtcreator**

      .. raw:: html

         <div
         style="margin: 5px; padding: 5px 10px; background-color: #ffffec; border-left: 5px solid #ff6600;">

      **IMPORTANT**
      By bringing QT Creator up manually, you will pass in the
      environment setup. If you double click on the Qt Creator Icon from
      the Desktop, you will not have the enviroment setup correctly and
      your lab will not work later on.

      .. raw:: html

         </div>

#. QT creator should be up and running now

   .. Image:: /images/Sitara_Linux_QT_qtcreator.png

#. Now lets setup QT creator to configure qmake. From the QT creator
   main menu shown above select the following:

   -  **Tools -> Options...**
   -  On the left side vertical menubar click **Build & Run**
   -  Click the **Qt Versions** tab under Build & Run
   -  **Remove** any versions that may already exist to make sure you
      start with a clean configuration
   -  Click **Add...** on the right
   -  Navigate to
      **/home/sitara/AM335x/ti-processor-sdk-linux-<machine>-<sdk
      version>/linux-devkit/sysroots/x86\_64-arago-linux/usr/bin/qt5**
   -  **Select qmake** then **click on Open**
   -  Double click on **Version Name** and give the Qt Version a
      descriptive name such as **QT 5.5 Sitara** See image below.

   .. Image:: /images/Sitara_Linux_QT_options.jpeg

   .. raw:: html

      <div
      style="margin: 5px; padding: 5px 10px; background-color: #ffffec; border-left: 5px solid #ff6600;">

   **IMPORTANT**
   Notice there is a red ! icon. Don't worry, lets add in the toolchain
   next and it should change to yellow.

   .. raw:: html

      </div>

   -  Click **Apply** to save your changes

#. Now we will setup the toolchain

   -  Click the **Compiler** tab under Build & Run
   -  Click **Add** in the top right and add a **GCC**
   -  Change the name to **arm-linux-gnueabihf-gcc**. This can be done
      by editing the "Name" field.
   -  For Compiler Path **select Browse**

      -  Navigate to
         **/home/sitara/AM335x/ti-processor-sdk-linux-<machine>-<sdk
         version>/linux-devkit/sysroots/x86\_64-arago-linux/usr/bin**
      -  Select **arm-linux-gnueabihf-gcc** and **click on open**
      -  Make sure to click on **Apply** to save your changes.

   .. Image:: /images/Sitara-compilerAndDebugger.jpeg

#. Next, let’s setup the Debuggers.

   -  Click the Debuggers tab under Build and Run
   -  Click **Add** in the top right
   -  Change the name to **GDB Engine**. This can be done by editing the
      "Name" field.
   -  For Debugger Path **select Browse**

      -  Navigate to
         **/home/sitara/AM335x/ti-processor-sdk-linux-<machine>-<sdk
         version>/linux-devkit/sysroots/x86\_64-arago-linux/usr/bin**
      -  Select **arm-linux-gnueabihf-gdb** and **click on open**
      -  Make sure to click on **Apply** to save your changes.

   .. Image:: /images/Sitara-Debugger.png

#. Click the **Kits** tab under **Build & Run**

   -  Change the name to give the device a unique name: **AM335x EVM**
   -  Select Device type **Generic Linux Device** instead of Desktop.
   -  Select Compiler **arm-linux-gnueabihf-gcc** instead of the host
      gcc.
   -  For Debugger select **GDB Engine**.
   -  For QT Version select **Qt 5.5 Sitara**
   -  Click **Apply** to register the options.

   .. Image:: /images/Sitara-linux-kits.png

#. Now let's setup our Target. While still in the **Tools -> Options**
   menu

   -  On the left side of the window, select the **Devices tab**
   -  In Devices: click the **Devices tab**
   -  Click **Add...** in the top right

   .. Image:: /images/Sitara_Linux_QT_options_add_device.png

   -  Select **Generic Linux device** and click on **Start Wizard**

   .. Image:: /images/Sitara_Linux_QT_Device_Configuration_Wizard_Selection.jpeg

   -  The Device Configuration Wizard Selection Dialog box comes up

      -  Type in the name of the Device: **AM335x EVM**
      -  Type in the IP address of the Embedded Linux Device. Type the
         IP address for your board, not the one shown in the screen
         capture.

         .. raw:: html

            <div
            style="margin: 5px; padding: 2px 10px; background-color: #ecffff; border-left: 5px solid #3399ff;">

         **NOTE**
         This is the same IP address you obtained in the previous lab

         .. raw:: html

            </div>

      -  For Username type in **root** (Most Texas Instruments Boards
         have this username)
      -  Make sure Authentication type is Password, but **leave the
         password field blank**.
      -  Click **Next**

      .. Image:: /images/Sitara_Linux_options_Generic_Linux_Device_Configuration_Setup.jpeg

   -  Click **Finish**. You should see that the target test passed, so
      you can close that window.

   .. Image:: /images/Sitara_target_test.png

#. Now we need to setup an SSH key so that the host can communicate with
   the target

   -  Still under the Devices tab click **Create New** for Private key
      file

   .. Image:: /images/Sitara_Linux_QT_create_new_ssh_key.png

   -
      -  **Key algorithm RSA**
      -  Select **Key size: 1024**
      -  Then click **Generate and Save Key Pair...**

   .. Image:: /images/Sitara_Linux_QT_options_SSH_Key_Configuration.jpeg

   -
      -  Click **Do not Encrypt key file**

   .. Image:: /images/Sitara_Linux_QT_Password_for_Private_Key.jpeg

   -
      -  Just use the default name qtc\_id.pub and **Click Save** and
         **Click Close** to close the Generate SSH Key window.

   -  Under the Devices tab now click **Deploy Public Key...**

   .. Image:: /images/Sitara_Linux_QT_Deploy_Public_Key.png

   -
      -  Select the file just generated (should be under
         /home/sitara/.ssh)

         .. raw:: html

            <div
            style="margin: 5px; padding: 5px 10px; background-color: #ffffec; border-left: 5px solid #ff6600;">

         **IMPORTANT**
         You may need to right click and select **show hidden files**

         .. raw:: html

            </div>

      -  Select the file **qtc\_id.pub** and click on **Open**, shortly
         a window should show up saying "Deployment finished
         sucessfully"

   .. Image:: /images/Sitara_successful_deploy.png

   -  Close the window and **Click OK** to exit the Linux Devices
      Window.

   .. Image:: /images/Sitara_Linux_QT_ok_to_close_devices.png

#. Now that lets create a project build it and run it on the host

   -  Select **File -> New File or Project**
   -  Then select **Applications** under projects then select **QT
      Widgets Applicaton** on the top center
   -  Click on **Choose**

   .. Image:: /images/Sitara_Linux_QT_new_project.png

   -  Type in the name of the project as **terminal**. We will be
      building on this project in the next section.
   -  Change the **Create in** value to **/home/sitara**
   -  Click on **Next**

   .. Image:: /images/Sitarea_Linux_Qt_project_terminal.png

   -  Select the desired Kit for the target system
   -  Click on **Next**

   .. Image:: /images/Sitara_Linux_Qt_project_kits_select.png

   -  Type in **terminal** for the **Class name**
   -  Click **Next**

   .. Image:: /images/Sitara_Linux_QT_new_terminal_props.png

   -  Select **None** under version control
   -  Click **Finish**

   .. Image:: /images/Sitara_Linux_Qt_project_vc_select.png

#. Now we've setup a new project let's explore and add some code.

   -  Click on **Edit** on the **left hand menubar** and look at the
      project files including terminal.pro, main.cpp, terminal.cpp and
      terminal.ui

   .. Image:: /images/Sitara-terminal-pro.jpeg

   -  Under **Forms**, double click on **terminal.ui** This will bring
      up the widget editor.
   -  Remove the menuBar where it says Type Here on the top of the ui
   -  Right click on the menuBar and select **Remove MenuBar**
   -  Use the same procedure to remove the statusBar at the bottom of
      the ui. It is not that easy to see, but it is there and blank.
   -  Once again remove the ToolBar (mainToolBar). It is found at the
      top of the ui and is also hard to see.

   .. Image:: /images/RemoveMenubar.png

   -  Find the **label widget** in the category of *display widgets*,
      **left click and drag it on to the User Interface (UI).**
   -  Type **Hello World!!!** into the label widget and strech out the
      borders so you can see all the letters.

   .. Image:: /images/Sitara_hello_world_UI.png

#. Now we need to check and update the build and run settings:

   -  On the left side vertical menubar select **Projects**
   -  Select the **Build and Run** tab and select **Build** under
      AM335x.
   -  Uncheck **Shadow build** as shown in the screenshot below:

   .. Image:: /images/Sitara_Build_settings_1.png

   -  Now under the AM335x select the **Run** tab
   -  Under Method click **Add** and select **Add** and then **Deploy to
      Remote Linux Host**
   -  However you see the <Remote path not set> error under the Run
      secton.

   .. Image:: /images/Sitara_deploy_remote.jpeg

   -  To fix the <Remote path not set> error do the following:

      -  Click on **Edit** on the left side vertical bar and click on
         **terminal.pro**
      -  Add the two lines below to the bottom of terminal.pro as shown
         in the screen shot below

         .. raw:: html

            <div
            style="margin: 5px; padding: 5px 10px; background-color: #ffffec; border-left: 5px solid #ff6600;">

         **IMPORTANT**
         You can find pre-written files in the in the
         /home/sitara/sitara-training-helper-files/QT\_Lab/lab2
         directory. You can just copy those files to your directory
         instead of typing the contents if you want to

         .. raw:: html

            </div>

         ``target.path += /home/root``
         INSTALLS += target

      .. Image:: /images/Sitara_add_target_loc.jpeg

      -  Select **File -> Save**

   -  Click on **Projects** on the left side vertical bar and you should
      now see the error is gone and replaced with /home/root/terminal
   -  Now in the Run portion: **Select Add -> terminal (on Remote
      Generic Linux Host)**

   .. Image:: /images/Sitara_remote_host.jpeg

#. Finally we are ready to run

   -  Click the **Green Arrow** on the bottom left to run the project

      .. raw:: html

         <div
         style="margin: 5px; padding: 2px 10px; background-color: #ecffff; border-left: 5px solid #3399ff;">

      **NOTE**
      ti-processor-sdk-linux-<> version 02.00.00.00 and 02.00.01.07 has
      dropbear package that doesn't let the QT Creator to deploy the
      built image on the target board. dropbear version 2015.71 fixes
      this problem and the prebuilt binary can be download from
      `here <http://processors.wiki.ti.com/images/6/64/Dropbearmulti.tar.gz>`__.
      Replace the /usr/sbin/dropbearmulti on target board filesystem
      with the downloaded 2015.71 dropbearmulti binary. Change the
      copied file mode to executable. Restart the target board. QT
      Creator should be able to successfully deploy the binary now

      .. raw:: html

         </div>

   -  If you receive the error 'g++: Command not found', navigate to
      tools>options>build and run>kits. Add “linux-oe-g++” to the “Qt
      mkspec” text box

   .. Image:: /images/CompileErrorFix.PNG

   -  Save all files if asked

   .. Image:: /images/Sitara-linux-Terminal-hello.jpeg

#. Extra Investigation:

   -  From minicom: run **top** on the target while helloworld is
      running. Check out CPU utilization and memory utilization for this
      simple app.
   -  See how much memory is used by helloworld by itself, you may need
      to kill matrix **/etc/init.d/matrix-gui-2.0 stop**


.. rubric:: LAB 3: Terminal project
   :name: lab-3-terminal-project

.. rubric:: Description
   :name: description-2

This section shows how you can use QT Creator to create a GUI from
scratch.

.. rubric:: Key Points
   :name: key-points-2

-  Adding widgets to a an User Interface (ui).
-  Adding code to make the widgets do something meaningful.

.. rubric:: Lab Steps
   :name: lab-steps-2

#. We will continue on from the previous lab using the terminal project
   you created. First we will remove the Hello world widget and resize
   the ui.

   -  Click **terminal.ui** to bring up design mode.
   -  Click the **Hello World widget**, and **delete it** making the ui
      empty and clean

#. This next action is mainly for those with small displays, but will
   not adversely affect larger displays.

   -  **Select the entire ui** as shown below.
   -  **Edit the Geometry values to Width = 440 and Height = 230** as
      shown.

   .. Image:: /images/Sitara-Linux_QT_Resize_screen.png

#. Next we will add the Tab Widget. Just like the label widget, drag it
   over to the ui.

   .. Image:: /images/Sitara_tab_widget.png

   -  Select the tab widget layout. Currently, the tab widget is part of
      our ui, but it is just sitting at fixed location where we dragged
      it.

      -  On the upper right side right click on the **terminal QWidget
         and select Lay Out -> Lay Out Vertical** as shown below

   .. Image:: /images/Sitara_layout_vertically.png

   -  Now the tab widget should completely fill the ui.

#. Now let's ad

   -  Two **Push Button Widgets**
   -  One **Text Browser widget**
   -  One **Line Edit widget.**

      -  **Drag all of them up to the ui**

   -  Now lets set the TabWidget layout like we did with the terminal
      widget

      -  Right click on the upper right **QtabWidget -> Lay Out -> Lay
         Out in a Grid**
      -  Move them around so they look somewhat like the screen shot
         below

   .. Image:: /images/Sitara_ui_layout.jpeg

#. Lets Rename the Push Button widgets.

   -  Double click on the **PushButton text** in the ui
   -  Edit the upper push button to say **Send CMD**
   -  Edit the lower push botton to say **Exit**
   -  Depending on how the grid layout worked for you, lets stretch out
      the Text Browser widget and the bottom Push Button widget to take
      up the whole screen horizontally if needed.

      -  Just click on the widget and **drag the border to fill the
         screen** See screen shot below:

   .. Image:: /images/Sitara_adjust_widths.png

#. Now lets give our widget objects a unique name.

   -  Select the **Text Browser widget**
   -  Go over to properties on the bottom right and edit **ObjectName**

      -  Add the text **\_linuxshell** to the end of the textBrowser
         name as shown below:

   .. Image:: /images/Sitara_rename_objects.jpeg

#. Now create unique names for the other 3 widgets.

   -  For lineEdit: **lineEdit\_commandline**
   -  For the Send CMD push button: **pushButton\_sendcmd**
   -  For exit push button: **pushButton\_exit**

#. We are not done yet, but for fun lets run this application and see
   what it looks like on the target.

   -  **Push the Green Arrow** at the bottom left to launch on the
      target. Save all files if asked.

      .. raw:: html

         <div
         style="margin: 5px; padding: 5px 10px; background-color: #ffffec; border-left: 5px solid #ff6600;">

      **IMPORTANT**
      You can not start a new application on the target if your previous
      one is still running. To exit, push the "X" on the menubar at the
      top right of your target.

      .. raw:: html

         </div>

      .. raw:: html

         <div
         style="margin: 5px; padding: 2px 10px; background-color: #ecffff; border-left: 5px solid #3399ff;">

      **NOTE**
      It should appear just as we designed it, but pushing the buttons
      has no effect because we haven't added any code yet.

      .. raw:: html

         </div>

#. Now we are going to add code to make the buttons do what we wish them
   to do.

   -  Right click on the **Exit widget -> Go to slot**

   .. Image:: /images/Sitara_goto_slot.jpeg

   -  In the **Go to Slot selector**, select the first selection
      **clicked()** and hit OK

#. Notice this pops you over to your terminal.cpp file where some code
   has been automatically added for you.

   .. raw:: html

      <div
      style="margin: 5px; padding: 5px 10px; background-color: #ffffec; border-left: 5px solid #ff6600;">

   **IMPORTANT**
   The code additions below can also be found in the
   **/home/sitara/sitara-training-helper-files/QT\_Lab/lab3** directory
   and can be copied into your project

   .. raw:: html

      </div>

   -  Add the following line of code to
      **on\_pushButton\_exit\_clicked()**
      ``qApp->quit();``

   .. Image:: /images/Sitara_pushbutton.png

#. Now repeat the same process you did for the exit button on the send
   CMD button. We will add code to control that button press.

   .. raw:: html

      <div
      style="margin: 5px; padding: 2px 10px; background-color: #ecffff; border-left: 5px solid #3399ff;">

   **NOTE**
   You will need to go back to the ui file to do this

   .. raw:: html

      </div>

   -  Right click on the **Send CMD widget -> Go to slot**
   -  In the **Go to Slot selector**, select the first selection
      **clicked()** and hit OK
   -  Add the following line at the top of terminal.cpp to support
      QProcess.
      ``#include <QtGui>``
   -  Add the following code to **on\_pushButton\_sendCmd\_clicked()**
      ``QString LinuxTexttoSend = ui->lineEdit_commandline->text();``
      // QProcess used to binaries in /usr/bin
      QProcess process;
      // Merge Channels so the output of binaries can be seen
      process.setProcessChannelMode(QProcess::MergedChannels);
      // Start whatever command is in LinuxTexttoSend
      process.start(LinuxTexttoSend, QIODevice::ReadWrite);
      // Run the command and loop the output into a QByteArray
      QByteArray data;
      while(process.waitForReadyRead())
      data.append(process.readAll());
      ui->textBrowser\_linuxshell->setText(data.data());

   .. Image:: /images/Sitara_SendCMD_code.png

#. Finally since we don't have a keyboard to type a command lets add a
   predefined command to our **line Edit Widget** like shown below:

   -  Double click on the **line edit** and add the text: **date
      --help**

   .. Image:: /images/Sitara_add_command.png

#. Now run, you should see interaction with the Linux shell when you
   push sendCMD.


.. rubric:: LAB 4: Enhancing the project with a web viewer, soft
   keyboard, and Style Sheets
   :name: lab-4-enhancing-the-project-with-a-web-viewer-soft-keyboard-and-style-sheets

.. rubric:: Description
   :name: description-3

In this section we Enhance our GUI with a web browser, soft keyboard and
style sheets.

.. rubric:: Key Points
   :name: key-points-3

-  Adding a Web view.
-  Adding a softkeyboard.
-  How to adjust the look and feel

.. rubric:: Lab Steps
   :name: lab-steps-3

#. One of the first things we did in the Terminal Lab was to add a Tab
   widget which is a container widget. So far we added a Linux shell
   terminal to Tab 1, now lets add a Web View widget to Tab 2

   -  From the terminal.ui, **click on Tab 2** and notice it is empty.

      -  Drag over a **QWebView widget** to Tab 2
      -  Set the Layout of Tab 2 to a **vertical layout**

         .. raw:: html

            <div
            style="margin: 5px; padding: 2px 10px; background-color: #ecffff; border-left: 5px solid #3399ff;">

         **NOTE**
         Do you recall how we did this on the Terminal Lab? On the top
         right, right click tabWidget -> Lay Out -> Lay Out Vertically

         .. raw:: html

            </div>

   -  When complete with the above steps, it should look like the
      following:

   .. Image:: /images/Sitara_webview.jpeg

#. Now we can add a default URL. Since we are not connected to the
   internet, lets bring up matrix since it is running on a local server.

   -  Select the **WebView widget** and on the bottom right find the
      **url** property of **QWebView** near the bottom of the list.
   -  Type in: **http://localhost**

      .. Image:: /images/Sitara_default_url.png

      .. raw:: html

         <div
         style="margin: 5px; padding: 2px 10px; background-color: #ecffff; border-left: 5px solid #3399ff;">

      **NOTE**
      Notice how the Webview in your ui tries to display the webpage but
      can't since it is not local to your host. Some people see this
      error and some do not.

      .. raw:: html

         </div>

#. Now we need to add the webkit libraries to our project.

   -  Go to **Edit** mode and bring up the **terminal.pro** file
   -  Add **webkitwidgets** as shown below

   .. Image:: /images/Sitara_webkitwidgets.png

#. Give it a try and run it, you should see the Matrix displayed.

   .. raw:: html

      <div
      style="margin: 5px; padding: 5px 10px; background-color: #ffffec; border-left: 5px solid #ff6600;">

   **IMPORTANT**
   You will need to use the **Exit** button on **Tab1** to close this
   program

   .. raw:: html

      </div>

#. Now lets address a couple of cosmetic issues. Notice how our new GUI
   does not fill the entire screen.

   -  Change over to *Edit'* mode and bring up **main.cpp**.
   -  Find the line **w.show()**

      -  **Remove that line**
      -  **type w.** and notice how QT Creator will fill in all the
         possible options. Also notice that when you start to type it
         will jump the available options with the matching text.
      -  Select **w.showFullScreen();** see screen shot.

      .. Image:: /images/Sitara_fullscreen.png

#. Now re-run and notice how it takes up the full screen.

      .. Image:: /images/Sitara_matrix.PNG

      <div
      style="margin: 5px; padding: 5px 10px; background-color: #ffffec; border-left: 5px solid #ff6600;">

   **IMPORTANT**
   You will need to use the **Exit** button on **Tab1** to close this
   program


#. Now lets fix another issue back on Tab 1. We hard coded in a default
   command: **date --help**

   -  Since we did not provide a keyboard, lets add a soft keyboard.

      -  Download a keyboard class from this location: `Qt Keyboard
         Template
         wiki <http://processors.wiki.ti.com/index.php/Qt_Keyboard_Template>`__.
         These instruction assume you downloaded the tarball to the
         **/home/sitara** directory.

         .. raw:: html

            <div
            style="margin: 5px; padding: 5px 10px; background-color: #ffffec; border-left: 5px solid #ff6600;">

         **IMPORTANT**
         If you are using a TI laptop or followed the host configuration
         steps you can find these files in the
         **/home/sitara/sitara-training-helper-files/QT\_Lab/keyboard**
         directory and can skip these steps

         .. raw:: html

            </div>

         -  **cd /home/sitara**
         -  **tar -xzvf Keyboard.tar.gz**

      -  Copy the keyboard files to your terminal project directory

         -  **cd /home/sitara/terminal/**
         -  **cp -rf <keyboard extraction directory>/keyboard .**

   -  Now lets add keyboard into our project.

      -  Go to **Edit** mode and right click on **terminal -> Add
         Existing Files** as shown below.

      .. Image:: /images/Sitara_addexisting.png

      -  Navigate to the keyboard directory
         **/home/sitara/terminal/keyboard** and add all 4 files in that
         directory.

         .. Image:: /images/Sitara_addkeyboard.png

         .. raw:: html

            <div
            style="margin: 5px; padding: 2px 10px; background-color: #ecffff; border-left: 5px solid #3399ff;">

         **NOTE**
         Notice how all four keyboard files are now part of the Terminal
         project. Click on the **keyboard.ui** and take a look. It is
         made up mainly of QPushButtons and one QLineEdit and layout
         controls

         .. raw:: html

            </div>

   -  Now we need to hook in the keyboard to the terminal GUI.

      .. raw:: html

         <div
         style="margin: 5px; padding: 5px 10px; background-color: #ffffec; border-left: 5px solid #ff6600;">

      **IMPORTANT**
      As always you can find copy that you can copy into your project in
      the /home/sitara/sitara-training-helper-files/QT\_Lab/lab4
      directory

      .. raw:: html

         </div>

      -  Add some code to terminal.h

         -  At the top of the file add
            ``#include "keyboard/keyboard.h"``
         -  In **private slots:** add
            ``void open_keyboard_lineEdit();``
         -  In the section **private:** add
            ``Keyboard *lineEditkeyboard;``

         .. Image:: /images/Sitara_terminal_h.png

      -  Now add some code to **terminal.cpp**

         -  In the function **terminal::terminal**
            ``lineEditkeyboard = new Keyboard();``
            connect( ui->lineEdit\_commandline
            ,SIGNAL(selectionChanged()),this
            ,SLOT(open\_keyboard\_lineEdit()));
         -  Also add the function below to the bottom of terminal.cpp
            ``void terminal::open_keyboard_lineEdit()``
            {
            QLineEdit \*line = (QLineEdit \*)sender();
            lineEditkeyboard->setLineEdit(line);
            lineEditkeyboard->show();
            }

   .. Image:: /images/Sitara_terminal_cpp.jpeg

#. You are now ready to run your code.

   -  Run and verify when you touch the line edit widget, that the
      keyboard pops up.

      .. raw:: html

         <div
         style="margin: 5px; padding: 5px 10px; background-color: #ffffec; border-left: 5px solid #ff6600;">

      **IMPORTANT**
      Depending on your screen resolution you may need to double-tap the
      bar at the top of the keyboard to size it to full screen

      .. raw:: html

         </div>

#. Type in a linux command such as **ps** to list the running processes
   and verify that you get back the expected results.

#. Next lets add specific colors to the GUI components using style
   sheets.

   -  Go back to your ui in the upper right corner: right click on the
      **terminal widget -> Change styleSheet**

   .. Image:: /images/Sitara_stylesheet.jpeg

   -  Cut and paste from terminal sytle sheet settings at the end of
      this lab section to the Terminal stylesheet settings and Apply
      them

      .. raw:: html

         <div
         style="margin: 5px; padding: 5px 10px; background-color: #ffffec; border-left: 5px solid #ff6600;">

      **IMPORTANT**
      You can find this file in the
      **/home/sitara/sitara-training-helper-files/QT\_Lab/lab4/style\_sheet\_terminal.txt**
      file

      .. raw:: html

         </div>

   -  Do the same thing for the Tab Widget by cutting and pasting from
      the tab style sheet settings at the end of this Lab section

      .. raw:: html

         <div
         style="margin: 5px; padding: 5px 10px; background-color: #ffffec; border-left: 5px solid #ff6600;">

      **IMPORTANT**
      You can find this file in the
      **/home/sitara/sitara-training-helper-files/QT\_Lab/lab4/style\_sheet\_tab.txt**
      file

      .. raw:: html

         </div>

#. voila ... TI colors - your setup should now match the look and feel
   of the one below:

   .. Image:: /images/Sitara_tabStyle.jpeg

#. Run it!

#. Extra investigation: Run a debug session and set break points in
   keyboard.cpp. Notice how the each QPushbutton signals the
   keyboardHandler slot.

   -

      .. raw:: html

         <div
         style="margin: 5px; padding: 2px 10px; background-color: #ecffff; border-left: 5px solid #3399ff;">

      **NOTE**
      If breakpoints are not working for you, verify you have created a
      Debug version of terminal and not a Release version. Look under
      Projects and "Build Settings" and check Details under Build Steps.

      .. raw:: html

         </div>

**terminal style sheet settings**

.. code-block:: cpp

    QWidget {
        background-color: rgb(0, 0, 0);
    }

    QTabWidget::pane {
        position: absolute;
        border: 2px solid red;
    }

    QTabWidget::tab-bar {
        alignment: center;
    }


    QTabBar::tab {
        color: red;
        background-color: black;
        border: 2px solid red;
        border-radius: 0px;
        padding: 4px;
        margin-left: 0.25em;
        margin-right: 0.25em;
    }

    QTabBar::tab:selected, QTabBar::tab:hover {
        color: white;
        background: red;
    }

    QPushButton {
         /**font: bold 16pt;
         color: white ;

         border-image: url(:/pushblueup.png);
         background-color: transparent;
         border-top: 3px transparent;
         border-bottom: 3px transparent;
         border-right: 10px transparent;
         border-left: 10px transparent;**/
     }


**tab style sheet settings**

.. code-block:: cpp

    QWidget{
        background-color: red;
    }

    QTextBrowser{
        background-color: black;
        color: yellow;
    }

    QLineEdit{
        background-color: white;
        color: black;
    }

    QPushButton{
    }

    QWebView{
        background-color: white;
    }


.. rubric:: LAB 5: Exploring Existing Demos and Examples
   :name: lab-5-exploring-existing-demos-and-examples

.. rubric:: Key Points
   :name: key-points-4

-  Exploring existing projects in the QT SDK.
-  Using a SGX accelerated QT Demo

.. rubric:: Lab Steps
   :name: lab-steps-4

#. In a console window on your host:

   -  **gedit /home/sitara/AM335x/ti-processor-sdk-linux-<machine>-<sdk
      version>/example-applications/matrix-gui-browser-2.0/main.cpp**

      .. raw:: html

         <div
         style="margin: 5px; padding: 2px 10px; background-color: #ecffff; border-left: 5px solid #3399ff;">

      **NOTE**
      This is the QT application which displays matrix for all Sitara
      platforms. As you can see it uses a QWebView just like we did in
      the Terminal Enhancements Lab. The main differences are that you
      pass in the url as an argument, and all window framing was
      removed.

      .. raw:: html

         </div>

#. Now try this one using the minicom connection to your target, it may
   surpise some of you:

   -  **cd usr/share/qt5/examples**
   -  We are now in the target Filesystem provided with Sitara SDK. Lets
      search for how many QT project files we can find.

      -  **find . -name \*.pro**

   -  There are many QT project files here

      -  **find . -name \*.pro** \| wc

   -  Over 300 different projects already available in the SDK.

#. Lets take a look at one specific example **hellogl2**. This is an SGX
   accelerate QT demo. In your minicom window do

   -  **cd /usr/share/qt5/examples/opengl/hellogl2**
   -  run this **./hellogl2**

#. You should see an SGX accelerated demo

#. As mentioned there are many demos available. Some may not work due to
   how QT was configured when it was built.

#. Some additional demo of interest:

   #. **/usr/share/qt5/examples/webkitwidgets/browser** -- This is the
      broswer demo featured in matrix.

#. Extra Excercise: Pull in one the the demos or examples into QT
   Creator by opening it as a project. Build it and run it on the
   target.

   .. raw:: html

      <div
      style="margin: 5px; padding: 2px 10px; background-color: #ecffff; border-left: 5px solid #3399ff;">

   **NOTE**
   You may need to do some project setup to make sure you will run
   on the target

   .. raw:: html

      </div>

.. rubric:: Debugging QT Libraries
   :name: debugging-qt-libraries

For debugging QT application with source code to QT libraries,
corresponding QT library will need to be installed to the
<ti-processor-sdk-linux-xxx>/linux-devkit/sysroots/armv7ahf-neon-linux-gnueabi
location. The \*.ipk package can be found from the
:ref:`yocto build of PSDK <building-the-sdk-with-yocto>`
under build/arago-tmp-external-arm-toolchain/work/armv7ahf-neon-linux-gnueabi.
Linux "find" command can be used to refine the search for \*.ipk file.
For example, following steps to debug qtbase application

1. Copy and install the associated ipk packages into the sysroot
directory

# dpkg -x qtbase-dbg\_xxx\_armv7ahf-neon.ipk sysroots/armv7ahf-neon-linux-gnueabi/

2. Set sysroot in the QT Creator: Under Tools -> Options -> Debugger tab
of the QT Creator, go to the GDB tab and add these additional startup
commands, for example set sysroot
/home/sitara/ti-processor-sdk-linux-xxx/linux-devkit/sysroots/armv7ahf-neon-linux-gnueabi
set debug-file-directory
/home/sitara/ti-processor-sdk-linux-xxx/linux-devkit/sysroots/armv7ahf-neon-linux-gnueabi/usr/lib/.debug

|

