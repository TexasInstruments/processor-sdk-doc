.. http://processors.wiki.ti.com/index.php/Processor_Linux_SDK_CCS_Debug
.. rubric:: Updated Toolchain
   :name: updated-toolchain

Starting with Sitara Linux SDK 6.0 the location of the toolchain has
changed and for non ARM 9 devices a new Linaro based toolchain will be
used. Details about the change in toolchain location can be found
:ref:`here <overview-getting-started>`.
Also details about the switch to Linaro can be found
:ref:`here <overview-getting-started>`.

AM18x users are not affected by the switch to Linaro. Therefore, any
references to the Linaro toolchain prefix "**arm-linux-gnueabihf**-"
should be replaced with "**arm-arago-linux-gnueabi-**".

.. rubric:: Background
   :name: background

.. rubric:: Linux Debug Overview
   :name: linux-debug-overview

CCSv5 supports run mode debug (a.k.a. remote GDB debug, agent-based
debug, application debug)and stop mode debug (a.k.a. JTAG debug,
low-level debug). For Linux aware debug support (an extension of the
stop mode debug), please read the section `Linux Aware
Debug <http://processors.wiki.ti.com/index.php/Linux_Debug_in_CCSv5#Linux_Aware_Debug>`__ below.

-  In run mode debug, the user can debug one or more Linux processes. On
   the host side, CCSv5 launches a cross platform GDB debugger to
   control the target side agent (a GDB server process). The GDB server
   launches or attaches to the process to be debugged and accepts
   instructions from the host side over a serial or TCP/IP connection.
   The Linux kernel remains active during the debug session. The user
   can only examine the state of the processes being debugged.
-  In the stop mode debug, CCSv5 halts the target using a `JTAG
   emulator <http://processors.wiki.ti.com/index.php/Emulation>`__. The Linux kernel and all
   processes are suspended completely. The user can examine the state of
   the target and the execution state of the current process.

**IMPORTANT!** This page refers to CCS version 6.0.0 and newer.

-  For CCSv5.1.x - CCSv5.5.x check `this
   page <http://processors.wiki.ti.com/index.php/Linux_Debug_in_CCSv5>`__
-  For CCSv5.0.x check `this
   page <http://processors.wiki.ti.com/index.php/Linux_Debug_in_CCSv5_0>`__.

.. rubric:: Run Mode Debug
   :name: run-mode-debug

.. rubric:: Dependencies
   :name: dependencies

The following dependencies apply to Run Mode Debug:

-  CCS versions: CCSv5.3 or greater
-  Devices: any core that is capable of running Linux: Cortex-A, ARM9,
   C66x.
-  Host requirement: a cross platform GDB debugger (typically part of a
   GCC package like CodeSourcery or Arago)
-  Target requirement: a GDB server that is compatible with the GDB
   debugger located on the host (typically part of a SDK package like
   EZSDK, DVSDK, etc.)
-  A GCC project (see `How to create GCC projects in
   CCSv5 <http://processors.wiki.ti.com/index.php/How_to_create_GCC_projects_in_CCSv5>`__).

   The run mode debug requires two connections to the target system:
   **1.** One connection to the target console is used to execute Linux
   commands.

-  If using a serial port (common in all TI's EVMs and low-cost boards
   like Beagleboard and Pandaboard), this connection can be done using a
   simple terminal program like Hyperterminal, Putty, TeraTerm or even a
   `CCSv5 terminal
   plug-in <http://processors.wiki.ti.com/index.php/How_to_install_the_terminal_plugin_in_CCSv5>`__.
-  If using Ethernet, this connection must be done using one of the
   programs above and configuring it for telnet or SSH. Keep in mind
   that the linux running on the target board requires a telnet or SSH
   server running on it.

   **2.** The other connection is used by the gdb debugger to communicate
   with the gdb server running on the target.

-  This connection can be done either via Ethernet or serial port. Keep
   in mind the speed of a serial connection can be a lot slower and
   timeouts may occur.

.. rubric:: Procedure
   :name: procedure

**IMPORTANT!** In certain versions CCSv5 does not enable "CDT GDB
Debugging" configurations. You need to enable them from the
Capabilities tab in the Preference dialog (select **Window** -->
**Preferences** --> **General** --> **Capabilities**).

1. Bring up the Debug Configurations dialog by selecting menu
   **Run** --> **Debug Configurations**

2. Select **C/C++ Remote Application**

3. Click on the icon **New launch configuration** (Top left of the pane)

4. Set the fields  **C/C++ Application:** and\ **Project:**
   respectively to the existing project in the workspace and the binary
   executable file

   Note: If the project is already in focus (Active or highlighted) in
   the **Project Explorer** view, these fields will be already populated.

5. In tab **Main**, click on the link **Select Other** at the bottom
   where it says **Using GDB (ASF) Automatic Remote Debugging Launcher**.
   Check **Use configuration specific settings** and select **GDB (DSF)
   Manual Remote Degugging Launcher**. Click **OK**.

   .. Image:: /images/Linux_debug_v5_GDB_config.png


   Note: It is possible to set up CCSv5 to automatically connect and
   launch the debugger in the target by leaving the settings above
   untouched. Check section 8 of the `Eclipse CDT
   FAQ <http://wiki.eclipse.org/index.php/CDT/User/FAQ>`__.

   **Note:** Other options like *Enable auto build*, *arguments* and others
   can be modified at this time.

   .. Image:: /images/Linux_debug_v5_tab_main.png


6. Select the **Debugger** tab and specify the GDB debugger as well
   as the GDB command file. In this case the GDB debugger from Arago is
   being used, but it is possible to use also CodeSourcery or other
   toolchain.

   Click browse next to "GDB command file" and browse to the .gdbinit
   file in the SDK install directory.  When you try to browse to the
   .gdbinit file, you will need

   to R-Click -> Show Hidden Files to see the file.   Click the Close
   button and you are now ready to debug the application!

   -  In this example of the 06.00.00.00 SDK, the path is:
      /home/user/AM335X/SDK/ti-sdk-am335x-evm-06.00.00.00/linux-devkit/sysroot/i686-arago-linux/usr/bin/arm-linux-gnueabihf-gdb
   -  The GDB init file is located:
      /home/user/AM335X/SDK/ti-sdk-am335x-evm-06.00.00.00/.gdbinit

   .. Image:: /images/Linux_debug_v5_tab_dbg_main.png


7. On the Debugger **Connection** tab, specify the IP address and
   port of the GDB server running on the target.

   **Note:** the port number is arbitrary and is specified when the
   gdbserver is launched - unless you have a strong reason to change it,
   the value of 10000 is just fine.

   **Note:** the IP address of the target can be determined from the target
   linux console.

   **IMPORTANT!** Some SDKs do not have gdbserver installed by default in
   the supplied filesystem. Check the SDK documentation for details on how
   to install it.

   .. Image:: /images/Linux_debug_v5_ifconfig.png

   .. Image:: /images/Linux_debug_v5_tab_dbg_connection.png


8. On the target console, start the GDB server specifying the
   application file and the port number.

   **Note:** make sure the port number matches the one specified in the
   Debugger Connection tab (10000 by default).

   **Note:** the application under debug must be located on the target
   filesystem. This can be done in multiple ways: either copying it to the
   shared NFS directory, to the SD card being used to boot linux, etc.

   .. Image:: /images/Linux_debug_v5_gdbserver.png

9. Launch the debug configuration by clicking the Debug button.

   -  CCSv5 will launch the GDB debugger to connect to the GDB server.
   -  After the connection is established, you can step, set breakpoints
      and view the memory, registers and variables of the application
      process running on the target.

   .. Image:: /images/Linux_debug_v5_debugger.png

10. You may need to set the shared library (object) search path in a
    cross compile debug enviroment.

    -  Under **Debug Configuration** -> **Debugger** tab -> **Shared Libraries**
       tab enter the path to the target filesystem lib directory
    -  You may need a copy of the target filesystem on the local debug host

.. rubric:: Stop Mode Debug
   :name: stop-mode-debug

.. rubric:: Dependencies
   :name: dependencies-1

| The following dependencies apply to Stop Mode Debug:

-  CCS version 5.3.0 or greater. This facilitates working on either a
   Windows host, or a Linux host.

In addition to the procedure below, a short video clip is located
`here <http://software-dl.ti.com/sdo/sdo_apps_public_sw/CCSv5/Demos/Linux_kernel_debugging/Linux_kernel_debugging.html>`__.

-  Devices: any core that is capable of running Linux: Cortex-A, ARM9,
   C66x.
-  Host system requirements:
-  Target system requirements: a Linux distribution running on the
   target. Kernel releases 2.6.x and 3.1.x were tested.

|
| The stop mode debug requires a JTAG connection to the target system.
  It supports either a standalone JTAG emulator (XDS100, XDS510, XDS560)
  or an embedded emulator on the development board (OMAPL137EVM,
  Beaglebone, etc.)
| An additional connection to the target console is helpful to monitor
  the Linux boot procedure and the integrity during the debug session.

.. rubric:: Procedure
   :name: procedure-1

| Although it is possible to connect to the device using the JTAG
  emulator without any reference to the source code, this makes the
  debugging process very difficult as the information in the debugger
  will consist in pure assembly code. In order to perform low-level
  debugging with complete visibility of the Linux kernel source code, a
  few steps are necessary:
| **1.** Compile the kernel with the appropriate debug symbols (EABI
  executable file ``vmlinux``).
| **2.** Create a project in the CCS workspace that contains all Linux
  kernel source code.
| **3.** Create a debug configuration that loads the debug symbols to
  the debugger and references the source code in the Linux kernel tree.

.. rubric:: Compiling the Linux kernel with debug information
   :name: compiling-the-linux-kernel-with-debug-information

| The Linux kernel must be built with debugging information, otherwise
  no source code correlation can be made by the debugger.
| In order to add or verify if the debug symbols are properly added to
  the configuration, the step *make menuconfig* must be performed before
  the kernel is built, and the options below must be enabled:

-  Enable *Kernel hacking* --> *Compile the kernel with debug info*

Also, if the kernel is in experimental mode, you should enable the
option below:

-  *Kernel hacking* ---> *Enable stack unwinding support*

To check if the kernel is in this mode, check if the option below is
enabled.

-  *General Setup* ---> *Prompt for development and/or incomplete
   code/drivers*

**Note:** for kernel 3.1.0 and above, there is an additional option that
must be set:

-  *Kernel Hacking* ---> *Enable JTAG clock for debugger connectivity*

**Note:** for kernel 3.2.0, the option *Enable stack unwinding support*
shown above is only available if the kernel is built with ARM EABI
support. To enable it, go to:

-  *Kernel Features* ---> *Use the ARM EABI to compile the kernel*

**Note:** for kernel 3.2.0, the option *Compile the kernel with debug
info* shown above is only available if the option *Kernel Debugging* is
enabled. To do it, go to:

-  *Kernel hacking* ---> *Kernel Debugging*

| **Note:** the building process depends on the Linux distribution being
  used, therefore it is recommended to read the SDK documentation
  regarding this step.

.. rubric:: Creating a source code project for the kernel
   :name: creating-a-source-code-project-for-the-kernel

1. Create a new C/C++ project by selecting *File* --> *New* -->
   *Project* and select *Makefile Project with Existing Code*. Click
   *Next*.

   .. Image:: /images/Linux_debug_v5_kernel_pjt_wizard.png


2. In the section *Existing Code Location*, click on *Browse...* and
   point to the root directory of the Linux kernel source tree. Leave the
   toolchain as *<none>* and click *Finish*.

   .. Image:: /images/Linux_debug_v5_kernel_pjt_new.png

   .. Image:: /images/Linux_debug_v5_kernel_pjt_tree.png


3. To prevent CCS from building the Linux kernel automatically
   before launching the debugger, this option must be disabled. Highlight
   the Linux kernel project in the *Project Explorer* view, right click and
   select *Build Options...*, then select *C/C++ Build* in the left tree
   and the tab *Behaviour*. Uncheck all the build rules boxes and click
   *OK*.

   .. Image:: /images/Linux_debug_v5_kernel_build_set.png

**Note:** it is possible the C-syntax error checker built into Eclipse
is also activated, which may throw errors while launching the debugger.
It can be configured by right-clicking on the project --> *Build
Options...* --> click on *Show Advanced Settings* --> *C/C++ General*
--> *Code Analysis*. It can also be completely disabled by going to the
submenu Launching and then unchecking the box *Run as you type (selected
checkers)*.
|

.. rubric:: Associating the Kernel Project with the Target
   :name: associating-the-kernel-project-with-the-target

At this point, a target configuration file (.ccxml) that corresponds to
your emulator and board must be ready.

In this example a Beaglebone (AM3359) was used, together with the Sitara
support package available at the `CCS download
page <https://www.ti.com/tool/download/CCSTUDIO>`__.
**Note:** check the `Getting Started
Guide <http://processors.wiki.ti.com/index.php/GSG:Debugging_projects_v5#Creating_a_Target_Configuration_File>`__
to learn how to create one.
**Important!** When debugging a target running any High-level OS (Linux,
WinCE, Android, etc.) or its support/initialization routines (u-boot,
WinCE bootloader, etc.) you should not rely on GEL files in the target
configuration (.ccxml) for device and peripheral initializations that
will disrupt your environment. Details on how to add/remove GEL files
are shown in the section *Advanced target configurations* --> *Adding
GEL files to a target configuration* of the `CCSv5 Getting Started
Guide <http://processors.wiki.ti.com/index.php/CCSv5_Getting_Started_Guide>`__.

1. Select menu *Run* --> *Debug Configurations*
2. Select *Code Composer Studio - Device Debugging* and click on the
   button *New Launch configuration* at the top left.

   .. Image:: /images/Linux_debug_v5_jtag_tab_main.png

3. Click on the button **File System...** near the box **Target
   Configuration** to select the target configuration file (.ccxml) for your
   hardware.

   **Optional:** give a meaningful name for the Debug Configuration at the
   box *Name:*

   **Optional:** depending on the target configuration, at this point a
   list of cores will be shown and can be disabled to improve the debugger
   performance.

   .. Image:: /images/Linux_debug_v5_jtag_target_assign.png

4. Select the tab *Program* to assign the Linux kernel source code
   to the Debug configuration.

5. On the drop-down menu *Device* select the core where the Linux is
   running. In this example the core **Texas Instruments XDS100v2 USB
   Emulator\_0/CortxA8** was selected

6. Click on the button *Workspace...* near the box *Project* to
   select the Linux kernel project

   -  In this example it was used the project ``linux-3.1.0-psp04.06.00.03.sdk``
   -  For the latest version, use ``/home/user/AM335X/SDK/ti-sdk-am335x-evm-06.00.00.00/board-support/linux-3.2.0-psp04.06.00.11``

7. Click on the button *File System...* near the box *Program* to
   select the EABI executable ``vmlinux`` that contains the debug symbols

   **Note:**\ If the Linux kernel was rebuilt, the location of this file is
   usually in the main directory of the Linux kernel source tree.
   /home/nick/AM335X/SDK/ti-sdk-am335x-evm-06.00.00.00/board-support/linux-3.2.0-*psp04.06.00.11*

   **Important!** It is common that a file ``vmlinux`` is also provided in
   the boot partition of the SD card shipped with the development board
   (where the file ``uImage`` is also located). However, check its size; if
   it is relatively small when compared to uImage (3, 4 times larger) it is
   possible it does not carry debug information. A typical size for the
   ``vmlinux`` file usually starts at 30~40MB.

8. At last, check the box *Load symbols only*. Click *Apply*.

   .. Image:: /images/Linux_debug_v5_jtag_vmlinux.png

9. Now the debug session is ready to be launched. At this point, the
   emulator must be connected, the target board powered up and Linux
   running (typically in the command prompt). Click on the *Debug* button.

   .. Image:: /images/Linux_debug_v5_jtag_debugger_launching.png

   .. Image:: /images/Linux_debug_v5_jtag_debugger.png

.. rubric:: Mixed Mode Debug
   :name: mixed-mode-debug

The stop mode debug can be used concurrently with the run mode debug.
The user can set breakpoints in the user process using the run mode
debug and breakpoints in the kernel using the stop mode debug.
To demonstrate this, a call to the function ``sleep()`` is added to the
Linux application used earlier in the Run mode debug and a breakpoint is
added to the function ``sys_nanosleep()`` (file <kernel/hrtimer.c>).
This will provoke a halt on the breakpoint set in the Stop Mode debug
caused by a function call from the Linux application in the Run mode.
**1.** Search for the function call ``hrtimer_nanosleep()`` on the file
<kernel/hrtimer.c> that belongs to the Linux kernel project.
**2.** With the Stop mode debug session still running, halt the target.
Right-click on the line of the call, select *Breakpoint (Code Composer
Studio)* then *Hardware Breakpoint*. Resume the target execution.
**3.** Start a Run mode debug session with the application that has the
``sleep()`` function call. After launching, the *Debug* view should show
two debug sessions as in the screen below:

.. Image:: /images/Linux_debug_v5_mixed_app_startup.png


**4.** Put the target to run. When the application calls ``sleep()`` the
Stop mode debug session should halt at the breakpoint, as shown in the
screen below:

.. Image:: /images/Linux_debug_v5_mixed_kernel_halted.png

**Important!** Keep in mind that halting the Linux kernel while
GDB/GDBserver are running may cause communication timeouts, clock skews
or other glitches inherent from the fact that the host system and other
peripherals are still running.
|

.. rubric:: Linux Aware Debug
   :name: linux-aware-debug

| This feature was not ported to CCSv5.1 due to compatibility break with
  the standard Eclipse (required significant changes that would penalize
  other debug features), lack of popularity and overall performance
  (speed and memory usage to refresh and store all processes at every
  breakpoint).
| To date there is not estimate to implement an "add-on" tool to
  CCSv5.1. Please check back regularly for updates.

.. rubric:: Limitations and Known Issues
   :name: limitations-and-known-issues

**1.** When performing Run Mode debug, by default Eclipse looks in the
host PC root directory for runtime shared libraries, thus failing to
load these when debugging the application in the target hardware. The
error messages are something like:

warning: .dynamic section for "/usr/lib/libstdc++.so.6" is not at the
expected address (wrong library or version mismatch?)
warning: .dynamic section for "/lib/libm.so.6" is not at the expected
address (wrong library or version mismatch?)
warning: .dynamic section for "/lib/libgcc\_s.so.1" is not at the
expected address (wrong library or version mismatch?)
warning: .dynamic section for "/lib/libc.so.6" is not at the expected
address (wrong library or version mismatch?)
When SDKs setup.sh script, it should automatically generate a .gdbinit
file for you in the base directory of the SDK.

The file will contain the line: set sysroot <SDK-PATH>/targetNFS.

An example would be

| *set sysroot
  /home/user/AM335X/SDK/ti-sdk-am335x-evm-06.00.00.00/targetNFS*

I

| Close any GDB debugging sessions. Open the *Debug Configurations* as
  shown in the Run Time debugging and then browse to this file in the
  *Debugger* tab --> box *GDB command file*.

