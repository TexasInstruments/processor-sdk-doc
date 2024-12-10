.. http://processors.wiki.ti.com/index.php/Processor_Linux_SDK_CCS_GDB_Setup
.. rubric:: Prerequisites
   :name: prerequisites-ccs-gdb-setup

Before you configure RSE you should make sure the following
prerequisites are met:

#. Installed the Processor Linux SDK
#. You have ran the `SDK's Setup
   Scripts <../../Overview/Run_Setup_Scripts.html>`__
#. Installed Code Composer Studio
#. Created or imported a C/C++ Project. This project should be already
   open. For this guide a helloworld project will be used as an example.
#. Connected your host PC and evm to the same network. Your PC and EVM
   should be on the same subnet.
#. `Remote System
   Explorer <../../Foundational_Components/Tools/Code_Composer_Studio.html#remote-explorer-setup-with-ccs>`__
   has already been setup and your
   `connected <../../Foundational_Components/Tools/Code_Composer_Studio.html#connecting-to-the-target>`__
   to the board.
#. The project you want to debug is already opened. Its important that
   the debug version of the executable is built.

.. rubric:: Debugging using GDB and GDB Server
   :name: debugging-using-gdb-and-gdb-server

.. rubric:: Creating the Debug Configuration for the Project
   :name: creating-the-debug-configuration-for-the-project

#. In CCS, select the project you wish to work with by clicking on it
   and highlighting it.
#. Select the Run -> Debug Configurations menu item.  This opens a
   dialog box as shown below.

   .. Image:: /images/Initial-debug-configurations.png

3. Double click C/C++ Remote Application.  You should then see a new
   debug configuration named "helloworld Debug" as shown below.

   Select your target connection from the Connection drop-down
   box.  In the example the target connection is called My Target EVM.

   .. Image:: /images/Hello_World_Debug_Configuration.png

4. Click the Search Project button to open the Program Selection dialog
   box below.  Click on the "armle - /helloworld/Debug/helloworld" item and
   click OK.

   .. Image:: /images/Debug-config-2.png

5. Click the "Browse..." button for "Remote Absolute File Path for C/C++
   Application".  Navgate to the executable file on the remote file system.
   For this example, the executable file is found at "/usr/bin/helloworld".

   .. Image:: /images/Auto-debug-config-main-tab.png

6. Click the Debugger tab.  On the Debugger page, the Main tab should
   be selected.

Click Browse next to "GDB debugger" and browse to the GDB executable.
GDB should be located at:
<sdk-path>/linux-devkit/sysroot/i686-arago-linux/usr/bin/arm-linux-gnueabihf-gdb

|
| Click browse next to "GDB command file" and browse to the .gdbinit
  file in the SDK install directory.
| GDB init file should be located at : <sdk-path>/.gdbinit

| When you try to browse to the .gdbinit file, you will need to right
  click and select Show Hidden Files to see the file.

  .. Image:: /images/Show_Hidden_Files.png

|

The .gdbinit file is used by GDB to locate source files and library
files on the target. The .gdbinit file is created when the SDK
environment script runs. Here is an example of a .gdbinit file.

.. Image:: /images/Gdbinit.png

|

Click Ok button in the browse window and then click the Close button in
the Debug Configuration window.

You are now ready to debug the application!

.. rubric:: Running the Debug Session
   :name: running-thedebug-session

1. Make sure that you are setup for the debug build configuration which
   contains symbol information.  In the C/C++ perspective, click on the
   helloworld project to select it and

   Project -> Build Configurations -> Set Active -> Debug.

2. Click the green "bug" icon to build the executable, transfer the
   executable to the target, start gdbserver and and start debugging.

   CCS will change to the CCS Debug perspective. The debug tab will
   show the running threads and their status. The source code window will
   show the program halted at the first executable source code line in the
   main() function. The Variables window will show the local variables and
   their current values.

   .. Image:: /images/Auto-debugging.png

3. To toggle a breakpoint, highlight the line of code in the source code
   window. Then click the Run -> Toggle Breakpoint menu item.

6. Use the debugger "Step Over" and "Step Into" icons to step through
   the source code.

7. To resume program execution, click the Run -> Resume menu item.

   NOTE: Do not click the Run -> Debug menu item, as that will attempt
   to start a new debug session.

   From here, you can make changes to the C source files, save the
   changes and then just click the green "Bug" icon again and you will be
   debugging the new executable on the target.

   (Each time you start the debugger the executable is built,
   automatically transferred to the target board and the gdbserver
   program is started for you.)

.. rubric:: Stopping the Debug Session
   :name: stopping-the-debug-session

When finished debugging the helloworld application, click the Run ->
Resume menu item.   To terminate the program,  click the Terminate icon
in CCS (this icon is a red square).

.. rubric:: Manually Terminating Gdbserver
   :name: manually-terminating-gdbserver

If the program being debugged ends abnormally or crashes CCS may be
unable to automatically stop the application and or kill gdbserver. If
this happens you may need to manually terminate gdbserver.

Note: These steps should only be followed if stop the application and
gdbserver has failed when hitting the stop button discussed above.

Once setup, you can follow these steps to terminate gdbserver:

1) Change to the Remote System Explorer perspective. Right click on
   Shell Processes in the target connection tree and select Show in Table
   to open a Remote System Details window.

2) Double-click on "All Processes" in the table to display the list of
   processes runnning on the target system.

3) Click on "Executable Name" in the table headers to sort the list by
   executable name.

4) Find the gdbserver process.  Right click on it and select Kill.  This
   will open a "Send a Kill Signal" dialog box.  Click the Kill button.

   .. Image:: /images/Shell-processes.png

   .. Image:: /images/Kill-gdbserver.png

