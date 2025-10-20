.. http://processors.wiki.ti.com/index.php/Processor_Linux_SDK_CCS_Remote_Explorer_Setup
.. rubric:: Overview
   :name: overview-ccs-remote-explorer

Remote System Explorer (RSE) is an Eclipse plug-in that provides:

-  Drag-and-drop access to the remote file system
-  Remote shell execution
-  Remote terminal
-  Remote process monitor

.. rubric:: Prerequisites
   :name: prerequisites-ccs-remote-setup

Before you configure RSE you should make sure the following
prerequisites are met:

#. Installed the Processor Linux SDK
#. Installed Code Composer Studio
#. Created or imported a C/C++ Project. This project should be already
   open.
#. Connected your host PC and evm to the same network. Your PC and EVM
   should be on the same subnet.
#. Know the IP of your evm.

   -  You can obtain the IP address of the EVM by connecting over
      the serial console and using the **ifconfig** command.

.. rubric:: Opening the Remote System Explorer Perspective
   :name: opening-the-remote-system-explorer-perspective

#. Go to **Window -> Open Perspective -> Other...**
#. In the menu window select **Remote System Explorer** to open this
   perspective.

.. Image:: /images/Sitara-Linux-CCS-rse-perspective.png

#. Click **OK**
#. You will now have the RSE view opened

.. Image:: /images/Sitara-Linux-CCS-rse-view.png

.. rubric:: Creating a New Connection
   :name: creating-a-new-connection

To establish a new connection with the target EVM you must run the New
Connection Wizard.

#. Click **File -> New -> Other...**
#. In the **Select a wizard** window select **Remote System Explorer ->
   Connection**

.. Image:: /images/New-connection.png

#. Click **Next**
#. In the **Select Remote System Type** window select the **Linux**
   system type

.. Image:: /images/Remote-system-type.png

#. Click **Next**
#. In the **Remote Linux System Connection** window enter
   **Host name:** Enter the IP address of your target EVM. This can be
   determined as detailed in the `**Prerequisites** <#prerequisites-ccs-remote-setup>`__
   section above
   **Connection name:** The default value is the same as the host name,
   but this can be changed to a more human readable value like *Target
   EVM*
   You can un-check **Verify host name** or leave it checked depending
   on whether you want to verify the IP address you entered for the
   *Host name* field.

.. Image:: /images/X-New_Connection.png

#. Do NOT click the Finish button.  Click **Next**
#. Check **ssh.files** to use the *Secure Shell* protocol for
   communication

.. Image:: /images/Ssh-files.png

#. Do NOT click the Finish button.  Click **Next**
#. Check **processes.shell.linux** to use a shell to work with processes
   on the remote system

.. Image:: /images/Processes_.png

#. Do NOT click the Finish button.  Click **Next**
#. Check **ssh.shells** to use *Secure Shell* to work will shell
   commands

.. Image:: /images/Shells.png

#. Do NOT click the Finish button.  Click **Next**
#. Check **ssh.terminals** to use *Secure Shell* to work with terminals

.. Image:: /images/Terminals.png

#. Click **Finish**
#. You will now see your EVM configuration in the RSE view

.. Image:: /images/Sitara-Linux-CCS-target-view.png

.. rubric:: Re-Opening the C/C++ View
   :name: re-opening-the-cc-view

If when you enabled RSE and opened the RSE perspective your C/C++ view
disappeared you can re-open it using the following commands. This is
useful to get back to your projects list to enable copying and pasting
files to transfer to the remote system.

#. Select **Window -> Show View -> Other...**
#. In the **Show View** dialog select **C/C++ -> C/C++ Projects**

.. Image:: /images/Sitara-Linux-CCS-c-view.png

#. Click **OK**

   -  **NOTE:** If you do not like the location of the C/C++ Projects
      view you can drag it to another location in CCS my dragging and
      dropping the Tab.

.. rubric:: Re-Opening the Remote System Explorer View
   :name: re-opening-the-remote-system-explorer-view

If you have closed the RSE view and wish to re-open it you can use these
steps:

#. Select **Window -> Show View -> Other...**
#. In the **Show View** dialog select **Remote Systems -> Remote
   Systems**

.. Image:: /images/Show-view-remote-systems.png

#. Click **OK**

   -  **NOTE:** If you do not like the location of the Remote Systems
      view you can drag it to another location in CCS my dragging and
      dropping the Tab.

#. A Remote Systems tab appears in the CCS perspective. The target
   connection named Target EVM is shown in a tree structure with
   branches for the various Remote System functions which communicate
   with the target EVM using a secure SSH connection.
   Sftp Files - Provides a drag and drop GUI interface to the target
   file system.
   Shell Processes - Provides a listing of processes running on the
   remote system and allows processes to be remotely killed.
   Ssh Shells - Provides a Linux shell window for the remote system
   within CCS.
   Ssh Terminals - Provides a terminal window for the remote system
   within CCS.

.. Image:: /images/Sitara-Linux-CCS-target-view.png

|

.. rubric:: Configuring with a Proxy
   :name: configuring-with-a-proxy

In the case that you are behind a proxy (most corporate networks) you
may need to configure CCS to bypass all proxies. You want to make sure
you also bypass the proxy for your target devices so that your
connection does not attempt to go out the proxy and then come back in
through the proxy.

To bypass your proxy follow the below steps:

#. Click the **Window -> Preferences** menu item
#. Go to **General -> Network Connections**
#. Change the **Active Provider** from **Native** to **Manual**
#. Highlight the **HTTP** item and click the **Edit** button
#. enter your company's *host proxy URL* and *port number*
#. Do the same for the **HTTPS** item. Both items should be checked as
   shown below.

.. Image:: /images/X-network-Connections-top.jpeg

#. In the **Proxy Bypass** section click **Add Host...**
#. Add the **IP address** of target board (in place of xx.xx.xx.xx)
#. Click OK.

.. Image:: /images/X-network-Connections-bottom.jpeg

|

.. rubric:: Connecting to the Target
   :name: connecting-to-the-target

After the New Connection Wizard has been completed and the Remote System
Explorer view has been opened, the new connection must be configured to
communicate with the target EVM.

#. Right-Click the **Target EVM** node and select **Connect**
#. A dialog like the one shown below will appear

.. Image:: /images/X-login.png

The Arago distribution that is used for our SDK is configured to use
root as the usernamr and no password.

When prompted for a login use **root** for the *user ID* and leave the
*password* blank. **NOTE:** you can save the user ID and password values
to bypass this prompt in the future

The first time the target EVM file system is booted a private key and a
public key is created in the target file system. Before connecting to
the target EVM the first time, the public key must be exported from the
target EVM to the Linux host system. To configure the key do

.. Image:: /images/Setup-ssh-editted-1.png

::

    Click Yes to accept the key

Under certain circumstances a warning message can appear when the
initial SSH connection is made as shown below. This could happen if the
user deletes the target file system and replaces it with another target
file system that has a different private RSA SSH key established (and
the target board IP address remains the same). This is normal. In this
case, click Yes and the public key from the target board will be
exported to the Ubuntu host overwriting the existing public key.

.. Image:: /images/Nasty-Warning-2.PNG

|

At this point, all Remote System Explorer functions will be functional.

.. rubric:: Target File System Access
   :name: target-file-system-access

Expand the **Sftp Files -> Root** node. The remote system file tree
should now show the root directory. You can navigate anywhere in the
remote file system down to the file level. Files can be dragged and
dropped into the remote file tree. A context menu allows you to create,
rename or delete files and folders.

.. Image:: /images/Expand-root-small.jpeg

|

.. rubric:: SSH Terminals
   :name: ssh-terminals

To open an SSH Terminal view

#. Right-Click the **Ssh Terminals** node under the target EVM
   connection
#. Select **Launch Terminal** from the context menu
#. Type shell commands at the prompt in the terminal window. Below is a
   sample command to list the contents of the remote /usr folder.

.. Image:: /images/MyTerminalView-small.jpeg

|

.. rubric:: Next Steps
   :name: next-steps-ccs-remote-setup

.. rubric:: Debugging Source Code using Code Composer Studio
   :name: debugging-source-code-using-code-composer-studio-ccs-remote-setup

In order to debug user-space Linux code using Code Composer Studio v6,
you first need to configure your project to use gdb and gdbserver
included within the SDK.

Please refer to `Debugging using GDB with Code Composer
Studio <../../Foundational_Components/Tools/Code_Composer_Studio.html#gdb-setup-with-ccs>`__ for more
information.

|

