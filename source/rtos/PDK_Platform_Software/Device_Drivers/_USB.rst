.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_USB

Overview
--------

Driver Overview
^^^^^^^^^^^^^^^

PDK USB driver (USB LLD) provides the following USB class/functions
while isolating application from the complexity of low level USB and USB
class protocols:

-  USB device Mass Storage Class
-  USB host Mass Storage Class
-  USB device Audio Class
-  USB generic bulk device class

In rest of the page AM437x EVM is being refered as an example. Please
check Release Notes for list of supported EVMs for driver.

.. rubric:: Modes of Operation
   :name: modes-of-operation

-  **USB device Mass Storage Class**

   -  **USB device Mass Storage Class with RAM DISK**

In this mode, a user-selected USB instance of the EVM will be working in
device mode and will behave like a USB thumb drive. It uses part of the
EVM DDR memory and exposes it as a physical storage for another USB host
application. After the host PC enumerates this EVM-thumb drive, the PC
will see a USB storage device. This EVM-thumb drive is not yet formatted
with any file system and requires user to format it before use.

.. Image:: /images/USB_MSC_device.PNG

The following screen shots show what one would expect when running the
device mode demo application and plugging in a USB cable from the EVM
USB port #0 to a PC running Windows

Printout from demo application:

.. Image:: /images/Device_mode_printout.png

The MSC device is detected in Windows, and a FAT formatted USB drive
named "PDK-USBDEV" should be seen in the "Window Explorer". The content
of the drive is just a readme.txt file. This USB drive can be
manipulated like any other removable USB drive.

.. Image:: /images/Windows_pdk_usb.png

Windows might show a message saying it should be scanned and fixed. We
can just ignore it and just continue without scanning.

|

   -  **USB device Mass Storage Class with MMCSD card**

This example acts like a USB - MMCSD card reader. The example exposes
the EVM's MMCSD card to the Host PC via USB MSC. The Host PC can
manipulate files on the attached MMCSD card on the EVM. This is how it looks.
Its code is similar to that of the USB device MSC example but with the call back
functions calling MMCSD API's instead of RamDisk APIs

.. Image:: /images/Usb_device_mmcsd.PNG

|

-  **USB host Mass Storage Class**

In this mode, the USB instance will act as a USB host communicating with
a USB device that supports Mass Storage Class function (USB thumb drive
or a small USB hard drive). The demo example code utilizes a shell
interface via the EVM via UART for interaction with the example. The
shell provides some basic commands to manipulate the content of the
attached USB disk drive.

.. Image:: /images/USB_MSC_host.PNG

|

Screenshot of a MSC host mode example running in RTOS after plugging in
a USB thumb drive into USB port #1

.. Image:: /images/Host_shell_screen_shot.png

|

-  **USB device Audio Class**

In this mode, USB instance of the EVM will be working in device mode and
will behave like a USB headset with MIC. It uses audio codec on the EVM
for running playback and record initiated by the USB host. McASP module
will be used to transfer the data between USB device and audio codec on
the board. EVM will appear as a new USB audio device on the host PC.
Changing the default audio device on the host PC to EVM USB device will
allow the playback and record operations between EVM and USB host. This
mode of operation is currently supported on AM335X GP EVM, OMAP-L137 EVM
and OMAP-L138 LCDK.

|
.. Image:: /images/Am335x_usb_ac_bd.jpg

|

-  **USB generic bulk device class**

In this mode, a user-selected USB instance of the EVM will be working in
device mode. The mentioned USB device will show up in the host PC as a generic
USB bulk device with one single interface containing a bulk IN and a bulk OUT
endpoints. The configuration and interface descriptors published by the device
contain vendor-specific class identifiers, so an application on the host will
have to communicate with the device using either a custom driver or a subsystem
such as WinUSB or libusb-win32 on Windows (or just libusb on Linux) to read and
write to the device.


   -  **Running USB bulk device demo application**

The bulk demo application requires a host PC with USB host plugged to the USB device
port on the EVM. Depending on the platform, the USB device port might be USB port #0
or #1.

.. Image:: /images/USB_MSC_device.PNG

Please refer to PDK user guide for how to generate USB example projects. Once the demo
application is loaded and run, the EVM UART console shows the following:

.. Image:: /images/usb_dev_bulk_console.png

A Python host PC example application is provided in
ti/drv/usb/example/usb_dev/bulk/usb_dev_bulk_host_application.py

|

The example Python script requires PyUSB to run. On Linux host, proper UDEV rule is
also required in order to access the USB bulk device as non-sudo user.  The script
itself also lists the requirements to run it as well as what command options available.
The example UDEV rule is also placed in the same place where the Python script is located.
It does the following:

- The Python script looks for the USB device with the example PID:VID,
- Sends an ASCII text string to the USB bulk demo application running on the EVM
- Expects the same text string with reversed case letter returned back, and also
- Verifies the received data with the data that it has sent and report the test result.

A screen shot of what the Python test script outputs

.. Image:: /images/usb_dev_bulk_host_tool_output.png

The USB bulk demo application configures the USB endpoints as high speed endpoints with 512B packet size.

|
|

User Interface
--------------

Driver Configuration
^^^^^^^^^^^^^^^^^^^^^

-  **Data Structures**:

   -  **tUSBDMSCDevice**: Defined in usbdmsc.h. It is used in USB device
      mode application. This structure must be filled with the intended
      vendor and product ID as well as other product information and
      also the function pointers to functions that handle the disk
      functions (open/read/write/close, etc.). These product information
      will show up in the device and interface USB descriptors that are
      used during device enumeration. This device MSC class data is then
      assigned to the field usbClassData of the USB_Params bellow.
   -  **USB params**: USB_Params structure is declared in usb_drv.h.
      This structure must be provided to the USB driver. It must be
      initialized before the USB_open() function is called.
   -  **USB APIs**: main USB LLD and USB MSC API’s are declared in
      usb_drv.h and usbdmsc.h and usbhmsc.h provided in the root USB LLD
      directory.

|

-  **General USB LLD expectations**:

The USB LLD will setup appropriate USB clock and power domains for the
particular SOC being in used as part of its “device specific peripheral”
functions.

After the USB_open() is called, the driver expects the application code
to sets up USB interrupts with the interrupt handler being the USB LLD
provided interrupt handler. Then the application have to call the USB
LLD provided API USB_irqConfig() which enables USB module’s interrupts.
In device mode, both USB core and USB misc interrupts are used in the
USB device MSC application. In host mode, the USB host MSC only uses USB
core interrupts.

After these steps, application code then can expect to have USB
enumeration done and start USB transfer through the provided APIs.

Then handle reset function is called for the reconnecting of usb ,
and Usb_close() is called to disconnect the handle and it is called in
USB device bulk application.

API Call Flow
^^^^^^^^^^^^^

-  **USB Device MSC**

The example application code uses the USB library, configures it as a
USB device with MSC function. The example also provides functional codes
that access a RAM disk (included from the Utils library in the included
Starterware). The LLD calls these MSC back-ends functions to access the
RAM disk. User can replace these functions with other functions that
access other types of media or devices (MMCSD for example). The RAM disk
image provided in the example demo application is not currently
formatted. Thus the once enumerated, the PC will require the USB disc to
be formatted before use.

Below diagram is the sequence of API calls that starts the USB device
MSC application. All USB events are handled internally in the LLD and in
the interrupt context.

.. Image:: /images/USB_MSC_device_API_flow.PNG

User provided disk functions will be called from the LLD to handle the
actual physical disk access. The overview of USB Device MSC example
application:

.. Image:: /images/USB_MSC_device_example_blocks.PNG

The content of the file: usb_msc_structs.c can be replaced with customer
USB device information (PID/VID, device names, etc.)

-  **USB Host MSC**

The LLD also provides a USB host MSC example. The USB LLD is acting as a
USB host, waiting for a USB thumb drive/memory stick to be plugged in. A
console with a simple shell command is also provided so that the demo
example can display and manipulate content of the USB device.

The following is how the USB host MSC example demo is organized:

.. Image:: /images/USB_MSC_host_example_blocks.PNG

The following is the sequence of the APIs that were used:

.. Image:: /images/USB_MSC_host_API_flow.PNG

|

-  **USB Device Audio**

The example application code uses the USB library, configures it as a
USB device with Audio class function. USB LLD along with the application
enumerates as the USB audio class device and allows accessing the audio
ports on the EVM from USB host. It supports audio playback and record
operations.

Below diagram is the sequence of API calls that starts the USB device
audio application. All USB events are handled internally in the LLD and
in the interrupt context.

.. Image:: /images/USB_Audio_class_flowchart.jpg


|

-  **USB Device Bulk**

Sequence of API calls as long as what the example application looks like are
described bellow

.. Image:: /images/usb_device_generic_bulk_example_application.png

- Main APIs that are used to read/write from and to the USB bulk device are USBD_bulkRead() and USBD_bulkWrite().
These two functions will block the caller until they finish their operation.

- The main application should wait for about 500ms after the USB host sends the SetConfig request to make sure that the enumeration is completely finished before calling USBD_bulkRead/Write functions


Application
------------

Examples
^^^^^^^^

Examples are CCS projects. Generated with pdkProjectCreate scripts.
Please refer  `Processor SDK RTOS Getting Started Guide <index_overview.html#pdk-example-and-test-project-creation>`__
for how to create and build examples projects

+-----------------------+-----------------------+-----------------------+
| Example Name          | EVM's supported       |                       |
|                       |                       | Notes                 |
+=======================+=======================+=======================+
| **USB_DevMsc_mmcsd**  | AM335GP EVM,          | eMMC is used on AM572 |
|                       | BeagleBoneBlack,      | and BealgeBoneBlack   |
|                       | AM572 EVM,            | examples              |
|                       |                       | This example can be   |
|                       |                       | used to format eMMC,  |
|                       |                       | just like any other   |
|                       |                       | USB storage device    |
+-----------------------+-----------------------+-----------------------+
| **USB_DevMsc_mmcsd**  | AM572xIDK,            | SD card is used as    |
|                       | AM574IDK,             | storage media for     |
|                       | AM571IDK              | USB MSC application   |
|                       |                       | Insert a SD card into |
|                       |                       | the board while       |
|                       |                       | running the example.  |
+-----------------------+-----------------------+-----------------------+
| **USB_DevMsc**        | AM335GP, AM437xGP,    | OMAPL13 LCDK host and |
|                       | OMAP137EVM,           | device examples share |
|                       | OMAPL138LCDK,         | the same USB port.    |
|                       | AM57xIDK, AM572 EVM,  |                       |
|                       | K2G EVM, DRA7xx EVM,  |                       |
|                       | AM65x EVM/IDK         |                       |
|                       |                       |                       |
+-----------------------+-----------------------+-----------------------+
|  **USB_HostMsc**      | AM335GP, AM437xGP,    | OMAPL13 LCDK host and |
|                       | OMAP136EVM,           | device examples share |
|                       | OMAPL137LCDK,         | the same USB port.    |
|                       | AM57xIDK, K2G EVM,    | Need OTG cable for    |
|                       | DRA7xx EVM,           | EVM with OTG port to  |
|                       | AM65x EVM/IDK         | work in host mode.    |
|                       |                       |                       |
|                       |                       | USB3.0 host supported |
|                       |                       | on AM572IDK.          |
+-----------------------+-----------------------+-----------------------+
| **USB_DevAudio**      | AM335xGP,OMAPL137     | Refer to Hardware     |
|                       | EVM,OMAPL138 LCDK     | Setup and How to Run  |
|                       |                       | the Demo sections     |
|                       |                       | below                 |
+-----------------------+-----------------------+-----------------------+
| **USB_DevBulk**       | AM335xGP, AM437xGP,   | Verifies USB device   |
|                       | AM572xIDK, AM571xIDK, | operation in bulk mode|
|                       | AM574xIDK, K2GEVM,    | Host trasactions are  |
|                       | OMAPL137EVM,          | invoked using Python  |
|                       | OMAP138LCDK,          | scripts provided as   |
|                       | AM654x EVM/IDK        | part of the example.  |
|                       |                       |                       |
+-----------------------+-----------------------+-----------------------+



Test Application
^^^^^^^^^^^^^^^^

USB test applications are built using makefile. Some of the test application are
RTOS/BIOS apps, other are bare metal apps. They are replica of the USB examples but built by
makefile instead of CCS projects.

Refer to the `Processor SDK RTOS Getting Started Guide <index_overview.html#setup-environment>`__
for details  of how to setup the build environment. Once you have setup the build environment,
issue the following commands:

- cd <pdk>/packages/

- To build: make usb

- To clean: make usb_clean

- Test applications are then under (TI_PDK_INSTALL_DIR)/packages/ti/binary/

+-----------------------------------+-----------------------+-------+---------------------------------+
| Test App Name                     | EVM's supported       | Bare  |                                 |
|                                   |                       | metal | Notes                           |
+===================================+=======================+=======+=================================+
| **USB_Baremetal_DevMsc_TestApp**  |  AM65xx EVM/IDK       |  yes  | Equivalent to DevMsc example    |
+-----------------------------------+-----------------------+-------+---------------------------------+
| **USB_Baremetal_HostMsc_TestApp** |   AM654x EVM/IDK      |  yes  | Same function as HostMsc example|
+-----------------------------------+-----------------------+-------+---------------------------------+
| **USB_HostMsc_TestApp**           |   AM654x EVM/IDK      |  no   | Same as HostMsc example         |
+-----------------------------------+-----------------------+-------+---------------------------------+
| **USB_DevMsc_TestApp**            |   AM654x EVM/IDK      |  no   | Same as DevMsc example          |
+-----------------------------------+-----------------------+-------+---------------------------------+
| **USB_DevBulk_TestApp**           |   AM654x EVM/IDK      |  no   | Same as DevBulk example         |
+-----------------------------------+-----------------------+-------+---------------------------------+
|                                   |                       |       | Same as USB DevMsc example.     |
|                                   |                       |       |                                 |
| **usb_d_msc_<platform>**          | AM335xGP,AM437xEVM    |       | Build by going to               |
|                                   | OMAPL137 EVM          |  yes  | example/usb_dev/msc/            |
|                                   | OMAPL138 LCDK         |       | build/<platform>                |
|                                   |                       |       |                                 |
+-----------------------------------+-----------------------+-------+---------------------------------+
|                                   |                       |       |                                 |
|                                   |                       |       | Same as USB HostMsc example     |
|                                   |                       |       |                                 |
| **usb_h_msc_<platform>**          | AM335xGP,AM437xEVM    |       | Build by going to               |
|                                   | OMAPL137 EVM          |  yes  | example/usb_dev/msc/            |
|                                   | OMAPL138 LCDK         |       | build/<platform>                |
|                                   |                       |       |                                 |
+-----------------------------------+-----------------------+-------+---------------------------------+


Both examples and test applications can be loaded and run on their intended EVM via
  	-  CCS JTAG connector, or
  	-  Via SBL: the "app" file under CCS project's debug directory (<PDK_INSTALL_PATH/MyExampleProjects/<ExampleProjectDirectory>/Debug>) is SBL loadable file of the built project.
   	--  Project Memory layout must be considered and following SBL guideline so that examples can run safely via SBL. Please refer to `SBL Component <index_Foundational_Components.html#boot>`__   for more detail



Benchmark tool
--------------

USB host MSC
^^^^^^^^^^^^
    - To measure the USB host MSC throughput, a new command (bm) is added into the USB host mode example (or test application).
    - This command is to run with a good known fast USB thumb drive attached to the USB host port.
    - The throughput measurement result varies greatly depends on which USB device is plugged in and which filesystem is used
    - The USB drive needs to be formated as FAT32 (since the USB host example only supports FAT filesystem) and has at least 100MB free space. Fast blank USB thumb drive is recomended.
    - The command, when run, writes a 100MB file into the thumb drive and measures the time it takes to do so. It then reads back this 100MB file with time measurement to find the read throughput.
    - The write and read are done in block size of 100KB, 256KB, 1MB, and 5MB. It prints throughput measurements for each of these blocks.
    - This command is only supported in AM65xx at the moment.
    - Syntax:

::

            bm <test_file_name>


USB device MSC
^^^^^^^^^^^^^^
    - To measure USB device MSC throughtput a simple linux shell script usb_dev_msc_perf.sh is provided in PDK/packages/ti/drv/usb/example/usb_dev/msc/
    - This script assumes the USB Dev MSC drive (PDK-USBDEV) is already mounted on the Linux host PC (under /media/$USER/PDK-USBDEV) when it runs
    - It uses "dd" command to report the thoughput
    - Tested on Ubuntu 16.04. Different version of Linux might mount the MSC drive at different place. Please adjust the script accordingly.
    - The script writes a file to the PDK-USBDEV drive with a number of blocksize. By default it creates a 15MB test file by writing 150 blocks of 100K each (which would fit inside the 16MB RAM disk provided by the USB Dev MSC.)
    - User is free to change the block size and number of blocks for the test. However it doens't check if the end result file would fit the PDK-USBDEV drive or not.
    - Syntax:

::

         usb_dev_msc_perf.sh [<blocksize> <count>]



Hardware Setup
--------------

This section provides the specific HW setup required to run the USB
examples.

|

-  **USB Device Audio**

USB audio class demo requires additional setup for running playback and
record operations. Below sections provide the setup details for each
platform supported.

|

**AM335x GP EVM**

.. Image:: /images/Am335x_usb_ac_setup.jpg

**OMAPL137 EVM**

.. Image:: /images/Omapl137_usb_ac_setup.jpg
**OMAPL138 LCDK**

.. Image:: /images/Omapl138_usb_ac_setup.jpg

**How to Run the Demo**

-  Follow this link `Processor SDK RTOS Setup CCS <How_to_Guides.html#setup-ccs-for-evm-and-processor-sdk-rtos>`__
   to get target configuration setup correctly.
-  Use CCS to import the USB_DevAudio_<board>_<core>ExampleProject under
   pdk_<platform>_<version>/packages/MyExampleProjects.
-  Build the imported project. the OUT file will be at
   pdk_<platform>_<version>/packages/MyExampleProjects/USB_DevAudio_<board>_<core>ExampleProject/Debug.
-  Make the HW connections as shown in `Hardware
   Setup <index_device_drv.html#hardware-setup>`__ section
-  Launch the target configuration for the EVM from CCS 7.x.
-  Connect to ARM or DSP core as applicable.
-  Load the
   pdk_<platform>_<version>/packages/MyExampleProjects/USB_DevAudio_<board>_<core>ExampleProject/Debug/USB_DevAudio_<board>_armExampleProject.out.
-  Run the program (loaded previously) by pressing F8
-  The CCS ConsoleIO will display the following:

.. Image:: /images/CCS_console_output.png

-  Right click on the "Speaker Icon" on the USB Host (right side of the
   toolbar), then select "Playback devices"
-  Wait until the "Speakers USB Audio Device" shows up in the "Sound"
   dialog

.. Image:: /images/Sound.png

-  Select the "Speakers USB Audio Device" in the "Sound" dialog, then
   click the "Configure"
.. Image:: /images/Speaker_setup.png

-  Click the "Test" in "Speaker Setup", you should hear the testing tone
   in the headphone connected to the EVM

.. note::

   'board' can be evmAM335x, evmOMAPL137 or lcdkOMAPL138

   'core' can be arm or c674x

