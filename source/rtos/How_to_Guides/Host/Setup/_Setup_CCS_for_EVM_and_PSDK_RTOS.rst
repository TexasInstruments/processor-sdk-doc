Setup CCS for EVM and Processor-SDK RTOS
------------------------------------------

.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_Setup_CCS

Overview
^^^^^^^^^

This page provides information on configuring CCS to work with both the
EVM and the Processor-SDK for RTOS.

Discovering SDK products
^^^^^^^^^^^^^^^^^^^^^^^^^

CCS and SDK installed in same directory
""""""""""""""""""""""""""""""""""""""""

After installing the Processor-SDK RTOS, start CCS and it will
automatically detect the newly installed components (*products*):

.. Image:: /images/CCS-discovered-products.png
|
CCS and SDK installed in different directories
"""""""""""""""""""""""""""""""""""""""""""""""

If you chose to install the SDK package in a different folder from where
CCS is installed (e.g. C:\\TEMP\\RTOS-SDK\\am57x), then you will need to
add the path to the search path for CCS to locate the new packages. The
screenshots below demonstrate the process to setup the CCS environment;
the sequence for a Linux host is the same.

Go to product preference
'''''''''''''''''''''''''

From CCS, select "Window -> Preferences":

.. Image:: /images/CCS-GP57x-EVM-Custom-Preferences.png
|
Enter path to SDK
'''''''''''''''''''

In the Preferences window, select "Code Composer Studio -> RTSC ->
Products" in the panel on the left. Then, press the "Add" button on the
panel on the right:

.. Image:: /images/CCS-GP57x-EVM-Custom-Add.png
|
Verify components
''''''''''''''''''

Next, verify the newly discovered products. If everything is correct,
press the "Finish" button on the bottom:

.. Image:: /images/CCS-GP57x-EVM-Custom-Finish.png
|
Restart CCS
''''''''''''

When prompted, restart CCS for changes to take effect. You will see
newly discovered products from the custom path.

.. Image:: /images/CCS-GP57x-EVM-Custom-Confirm.png
|

Install Latest Emulation Package and Sitara Device Support Package
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
1. In CCS, navigate to Help -> Check for Updates and select "Sitara device support"
and "TI Emulators" and click Next.

 .. image:: /images/TMDX654_EVM_Hardware_Setup/CCS_Check_for_Updates.PNG

2. Click "Next" again, select "I accept the terms of the license agreements"
and click Finish to begin the installation.

 .. image:: /images/TMDX654_EVM_Hardware_Setup/CCS_Updating_Software.png

3. You may be prompted to restart CCS for the updates to take effect. Click "Restart Now" when
prompted to complete the installation.


Create Target Configuration File for EVM
""""""""""""""""""""""""""""""""""""""""""

In CCS, you need to create a *Target Configuration* for your EVM to be
able to connect to the target. This configuration defines your:

-  Connection to the target (XDS, FET, etc.)
-  Target device (AM437x GP EVM, AM57x GP EVM, etc.)
-  GEL file for hardware initialization. A GEL file is basically a
   “batch file” that sets up the CCS debug environment including memory
   map, PLL, clock, etc.

CCS comes with basic configuration that can be used to configure your
particular setup. In the example below, we provide details for a GP
AM437x EVM; configuration information for other supported EVMs are also
provided as needed.

For EVM specific instructions, refer to the **Hardware User's Guide**
for your :ref:`EVM <RTOS-SDK-Supported-Platforms>`

.. note::
   **Note for K2G devices:** If using CCS v6.1.2 and Keystone2 device
   support v1.1.7, 66AK2G02 would not show up in the list of devices when
   creating the target configuration. This is due to an incompatibility in
   the XML parser in CCS v6.1.2 with the K2G device xml. In order to
   work-around this issue, make the change in 66AK2G02.xml as illustrated
   below in order to have 66AK2G02 display in the device list. This problem
   does not exist in CCS v6.1.3 onwards as the XML parser has been updated.

   ::

	C:\ti\ccsv6\ccs_base\common\targetdb\devices\66AK2G02.xml

	Line #1

	<?xml version="1.1" encoding="UTF-8" standalone="no"?>
	to
	<?xml version="1.0" encoding="UTF-8" standalone="no"?>

Open new target configuration file
'''''''''''''''''''''''''''''''''''

From CCS, select "File -> New -> Target Configuration File":

.. Image:: /images/CCS-GP437x-EVM-New-Target.png
|
Select target configuration options
''''''''''''''''''''''''''''''''''''

The AM437x GP EVM supports embedded XDS100V2 USB Emulation through the
MicroUSB AB connector. Select

-  **Connection**: Texas Instruments XDS100v2 USB Debug Probe
-  **Board or Device**: EVMAM437X

.. Image:: /images/CCS-GP437x-EVM-Configure-Target.png
|
**Useful Tip**

If you enter the starting numbers of your device in the **Board or
Device** field, the list will show the relevant subset.

Here is a table showing configuration information for all supported
EVMs in the Processor-SDK RTOS:

+-----------------------+-----------------------+-----------------------+
| EVM                   | Connection            | Board                 |
+=======================+=======================+=======================+
| AM65x EVM             | Texas Instruments     | GPEVM_AM65x           |
|                       | XDS110 USB Debug      |                       |
|                       | Probe                 |                       |
|                       |                       |                       |
+-----------------------+-----------------------+-----------------------+
| AM65x IDK             | Texas Instruments     | IDK_AM65x             |
|                       | XDS110 USB Debug      |                       |
|                       | Probe                 |                       |
|                       |                       |                       |
+-----------------------+-----------------------+-----------------------+
| GP335x                | External Emulator     | EVMAM3358             |
|                       | Supplied by User. EVM |                       |
|                       | includes a TI 20 pin  |                       |
|                       | JTAG connector.       |                       |
+-----------------------+-----------------------+-----------------------+
| ICE335x               | Texas Instruments     | ICE_AM3359            |
|                       | XDS100v2 USB Debug    |                       |
|                       | Probe                 |                       |
+-----------------------+-----------------------+-----------------------+
| SK335x                | Texas Instruments     | SK_AM3358             |
|                       | XDS100v2 USB Debug    |                       |
|                       | Probe                 |                       |
+-----------------------+-----------------------+-----------------------+
| BBB                   | External Emulator     | BeagleBone_Black      |
|                       | Supplied by User. EVM |                       |
|                       | includes a TI 20 pin  |                       |
|                       | JTAG connector.       |                       |
+-----------------------+-----------------------+-----------------------+
| GP437x                | Texas Instruments     | EVMAM437X             |
|                       | XDS100v2 USB Debug    |                       |
|                       | Probe                 |                       |
+-----------------------+-----------------------+-----------------------+
| IDK437x               | Texas Instruments     | IDK_AM437X            |
|                       | XDS100v2 USB Debug    |                       |
|                       | Probe                 |                       |
+-----------------------+-----------------------+-----------------------+
| GP572x                | External Emulator     | GPEVM_AM572X          |
|                       | Supplied by User. EVM |                       |
|                       | includes a TI 20 pin  |                       |
|                       | JTAG connector.       |                       |
+-----------------------+-----------------------+-----------------------+
| X15                   | External Emulator     | GPEVM_AM572X          |
|                       | Supplied by User. EVM |                       |
|                       | includes a TI 20 pin  |                       |
|                       | JTAG connector.       |                       |
+-----------------------+-----------------------+-----------------------+
| IDK572x/IDK574x       | Texas Instruments     | IDK_AM572X/IDK_AM574X |
|                       | XDS100V2 USB Debug    |                       |
|                       | Probe                 |                       |
|                       | External Emulator     |                       |
|                       | Supplied by User. EVM |                       |
|                       | includes a 60-pin     |                       |
|                       | MIPI JTAG connector   |                       |
+-----------------------+-----------------------+-----------------------+
| C665x EVM             | Texas Instruments     | TMS320C6657           |
|                       | XDS2xx USB Onboard    |                       |
|                       | Debug Probe           |                       |
+-----------------------+-----------------------+-----------------------+
| C667x EVM             | L w/ XDC100: Texas    | TMS320C6678           |
|                       | Instruments XDS100v1  |                       |
|                       | USB Emulator          |                       |
|                       | LE/LXE with XDS560:   |                       |
|                       | Blackhawk             |                       |
|                       | XDS560v2-USB          |                       |
|                       | Mezzanine Emulator    |                       |
+-----------------------+-----------------------+-----------------------+
| K2E EVM               | Texas Instruments     | 66AK2E05              |
|                       | XDS2xx USB Onboard    |                       |
|                       | Debug Probe           |                       |
+-----------------------+-----------------------+-----------------------+
| K2H EVM               | Texas Instruments     | 66AK2H12              |
|                       | XDS2xx USB Onboard    |                       |
|                       | Debug Probe           |                       |
+-----------------------+-----------------------+-----------------------+
| K2L EVM               | Texas Instruments     | TCI6630K2L            |
|                       | XDS2xx USB Onboard    |                       |
|                       | Debug Probe           |                       |
+-----------------------+-----------------------+-----------------------+
| K2G GP EVM            | Texas Instruments     | 66AK2G02              |
|                       | XDS2xx USB Onboard    |                       |
|                       | Debug Probe           |                       |
+-----------------------+-----------------------+-----------------------+
| OMAPL137 EVM          | Spectrum Digital      | OMAPL137SK            |
|                       | XDS510USB Emulator    |                       |
+-----------------------+-----------------------+-----------------------+
| OMAPL138 LCDK         | External Emulator     | OMAPL138LCDK          |
|                       | Supplied by User. EVM |                       |
|                       | includes a TI 14 pin  |                       |
|                       | JTAG connector.       |                       |
+-----------------------+-----------------------+-----------------------+

|
Save target configuration
''''''''''''''''''''''''''

Next, save the target configuration by pressing the **Save** button:

.. Image:: /images/CCS-GP437x-EVM-Save-Target.png
|
Test target configuration
''''''''''''''''''''''''''

Next, test the target configuration by pressing the **Test Connection**
button. This will confirm that you have successfully created an emulator
connection with your board.

.. Image:: /images/AM4-GP-test-connection.png
|
View target configurations
'''''''''''''''''''''''''''

From CCS, select "View -> Target Configurations":

.. Image:: /images/CCS-GP437x-EVM-View-Target.png
|
Launch target configuration
''''''''''''''''''''''''''''

Open "User Defined" list and right click on the target configuration
file that was just saved and select "Launch Selected Configuration":

.. Image:: /images/CCS-GP437x-EVM-Launch-Target.png
|
Connect target
'''''''''''''''

After launch, you can connect to a core. For GP AM437x EVM, select
**Cortex A9** and select "Connect Target":

.. Image:: /images/CCS-GP437x-EVM-Connnect-Target.png

|

Success!
'''''''''

After connecting to target, check the console for status. Typically, the
end of the configuration will indicate success or failure. For GP AM437x
EVM, you will see the message "AM437x GP EVM Initialization is Done":

.. Image:: /images/CCS-GP437x-EVM-Run-Target.png
|
Additional Notes for AM57x
"""""""""""""""""""""""""""

Connect to AM57x Target Cores
'''''''''''''''''''''''''''''

After connecting to the boot master core -- typically the ARM core --
you may need to connect to a target core in order to run code. Depending
on your SOC, the target core can be

-  DSP C66x
-  ARM M4
-  PRUSS
-  IVAHD

Typically the target cores will wait in reset state until the master core
wakes up the target core to run code. To connect to the target core on
AM57x, go to **Scripts** menu in CCS Debug View and under **AM572x
MULTICORE Initialization** enable the corresponding sub system clock.
For example, enable ``DSP11SSClkEnable_API`` for the first DSP core.
After running the clock enable option, you can connect to the core.

.. Image:: /images/Multicore-Enable.jpg
|
Timer Suspend Control Options for DSP
'''''''''''''''''''''''''''''''''''''''

On AM57xx devices, all the timers on the chip have their suspend control
signal routed to the A15 core. Which means that if any of the target
cores are using these timers, the timers will continue to run even when
the target core has been paused. The timer will only pause when the A15
core is halted.

This is confusing while debugging code on target cores if you are relying
on timer for logging, inserting delays or if the timer keeps firing
interrupts even when the core is halted. One such scenario occurs with
*GPtimer5* when DSP developers are using SYS/BIOS. The OS uses
*GPtimer5* on the DSP and forces a frequency check to confirm the timer
configuration, however the OS can't gain access to the timer due to the
hook up of the suspend control signals.

Due to this issue the SYS/BIOS developers will need to configure an
additional CCS configuration check to connect the GPTimer suspend
control signal to the DSP as shown in the image below:

.. Image:: /images/GPtimer5_DSPConnect.png

|

Troubleshooting
""""""""""""""""

If you face any problems, first check these basic items:

-  **Power cycle your target.**
-  **Check the USB cable.** One simple way to do this is to connect
   another device to the USB and ensure the cable works.
-  **Check host driver.** Even with CCS turned off, your host should
   list the TI XDS as a USB device. If this does not work, try a
   different USB port.
-  **Latest emulation package.** Ensure that you have the latest
   emulation files as specified in the `Getting Started Guide <index_overview.html#emulator-support>`__.

If this does not resolve your problem, see these additional resources:

-  `Troubleshoot
   CCS <http://processors.wiki.ti.com/index.php/Troubleshooting_CCSv6>`__
-  `Troubleshoot
   XDS100 <http://processors.wiki.ti.com/index.php/XDS100#Troubleshooting>`__
-  `Troubleshoot
   XDS200 <http://processors.wiki.ti.com/index.php/XDS200#Troubleshooting>`__
-  `Troubleshoot
   XDS560 <http://processors.wiki.ti.com/index.php/XDS560#Frequently_Asked_Questions>`__

|

