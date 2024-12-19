
.. _Benchmark-Demo-User-Guide-label:

Benchmark Demo - User Guide
===========================

Overview
--------

The default application loaded on the AM64x is the Benchmark Demo. It's
purpose is to showcase the capabilities of the four R5F cores as well as
the A53 core right out of the box. One of the four R5F benchmarks will run
on one of the 4 R5F cores. There are 4 running options available for each
benchmark. Users can switch using the drop-down to test the AM64x and view
it's performance.

All of the necessary equipment requirement and instructions are provided here.

Hardware Prerequisites
----------------------

-  TI AM64x EVM

-  PC (Windows or Linux)

-  Ethernet cables

-  Ethernet switch or ethernet router with DHCP service

-  SD card (minimum 2GB)

Get Started
-----------

1.  Follow the instructions in section
    :ref:`am64x-create-sd-card-with-default-images` to create an SD card with
    the prebuilt WIC image.

2.  Insert the SD card into the AM64x EVM

3.  Set the AM64x EVM Boot mode to "Boot from SD card"

    - SW2(1:8) on, on, off, off, off, off, on, off
    - SW3(1:8) off, on, off, off, off, off, off, off

.. Image:: /images/boot_pins_sd_mode_oob.png

4.  Connect an ethernet cable from your ethernet switch or router to the
    AM64x EVM

5.  Connect your PC to the same ethernet switch or router

6.  Connect the UART (J26 via USB cable) to the PC's USB port.

7. Open the the main UART0 port using the TeraTerm or other UART emulator
    program. Set the port to 115200bps, 8 bit, no parity, 1 stop bit, no flow control

8. Power on the AM64x

9. After the Linux boot completes, login as "root", then type in "ifconfig" in
    Linux prompt to find out the IP address for the AM64x EVM

.. Image:: /images/OOB_Linux_ifconfig.png

10. On the PC, open a Internet Browser and enter in the
    following: \ http://IP_ADDRESS_OF_AM64x_EVM:8081, for example, http://192.168.86.198:8081

11. The following web page will pop up:

.. Image:: /images/OOB_GUI_root.png

12. Click on the "Benchmark Demo": 

.. Image:: /images/OOB_GUI_stats.png

13. With the current release, the R5F app for each R5F core are fixed. User can only
    change the "Options" for each core, then click "LOAD" to refresh the statistics 

+-------------+------------------+----------------------+-----------------------------------------------------------+
| **R5 Core** | **App Name**     |   Default Option     | **Description**                                           |
+=============+==================+======================+===========================================================+
| 0_0         | ADC and PWM Loop |      8Khz            | ADC/PWM benchmark for R5 5 ADC sample read & 1 PWM write  |
|             |                  |                      | This is not enabled in current release.                   |
+-------------+------------------+----------------------+-----------------------------------------------------------+
| 0_1         | CFFT             |      1Khz & 128pt    | CMSIS CFFT benchmark for R5                               |
+-------------+------------------+----------------------+-----------------------------------------------------------+
| 1_0         | FIR Filtering    |      1Khz            | CMSIS FIR filtering benchmark for R5 320pt & 29-tap       |
+-------------+------------------+----------------------+-----------------------------------------------------------+
| 1_1         | FOC Loop         |      16Khz           | CMSIS FOC benchmark for R5                                |
+-------------+------------------+----------------------+-----------------------------------------------------------+

Software Architecture
---------------------

.. Image:: /images/OOB_SW_arch.png

Building Blocks
---------------

-  **User Interface:** The GUI was built by using `GUI Composer <https://dev.ti.com/gc/v2/>`__. The
   Benchmark Demo is the second page where inputs and outputs can be
   accessed.

-  **Web Server:** The benchmark data is sent between the GUI and the
   AM64x via HTTP communication. New data are pulled from the AM64x and
   sent to the GUI every second, while data sending from the GUI to the
   AM64x is transmitted every time "Load" is clicked. The data are
   transmitted and received in JSON format.

-  **R5 and A53 Applications:**

   -  All the R5F applicatins are built in MCU+ SDK. Please refer
      MCU+ SDK for more details.

   -  Linux application code handles the IPC RPMsg\_char and the JSON
      file update for A53 

   -  Web server code is built on Node JS

Demo Internals
--------------

Programming Paradigm
~~~~~~~~~~~~~~~~~~~~

-  The user interface of the demo is built from GUI Composer and runs on
   a PC's browser

-  The web server is built on Node JS, transmits and receives data in
   JSON format, and runs on the Linux A53 core

-  The linux app is written in C and runs on the Linux A53 core

-  Each of the CMSIS applications run on any given baremetal R5F core

   -  Applications are chosen using the Imperative Programming Paradigm
      (Procedural Programming Paradigm)

Node JS
~~~~~~~

When the AM64x boots, an initialization script executes the web server
code by calling the Node JS code. Several node packages are used to edit
the JSON file, create the demo instance, and serve up the files to the
client.

HTTP
~~~~

All data communication is handled via HTTP. Benchmark data from the
AM64x is requested by the GUI every second, whereas the option selection
data is pushed from the GUI to the AM64x when the "Load" button is clicked.
The HTTP requests are handled with jQuery, and the body of each HTTP request
is a JSON string containing the input/output benchmark data.

JSON
~~~~

A JSON file has been used to exchange structured information between the
web server and the A53 Linux application (a user space application
program). It will read the user input such as the input application and
parameters used to run on the desired R5F core. On the other hand, the
A53 Linux application will also get the benchmark data from the R5 cores
and then update the JSON file accordingly. The updated JSON file
will then be displayed on the GUI every second.     

Build Baremetal Demos and Update SD card
----------------------------------------

1. Install MCU+ SDK `[Use Link] <https://software-dl.ti.com/mcu-plus-sdk/esd/AM64X/10_01_00_32/exports/docs/api_guide_am64x/SDK_DOWNLOAD_PAGE.html>`__.
   Refer MCU+ SDK benchmark demo user guide
   `[Use Link] <https://software-dl.ti.com/mcu-plus-sdk/esd/AM64X/10_01_00_32/exports/docs/api_guide_am64x/EXAMPLE_MOTORCONTROL_BENCHMARKDEMO.html>`__
   on how to build demos.
   Generated binaries will be in  <MCU+ SDK>/examples/motor_control/benchmark_demo/am64x-evm/system_nortos

2. Once the R5F binaries are available, copy them to Linux file system in folder /lib/firmware/mcusdk-benchmark_demo/.
   The copy step can only be done using a Linux machine since the Linux filesystem on the
   SD card cannot be seen on a Windows machine. Once copied, make sure the soft links are pointing to the correct binaries.

Directory Structure
-------------------

The source code can be found at `[this link] <https://git.ti.com/cgit/processor-sdk/sitara-apps/>`__.

+------+--------------------------------------------------+----------------------------------------------------------------------------------------+
|      | **Directory Name**                               | **Description**                                                                        |
+======+==================================================+========================================================================================+
| 1    | apps/benchmark\_demo/webserver\_app/app          | GUI code and component files                                                           |
+------+--------------------------------------------------+----------------------------------------------------------------------------------------+
| 2    | apps/benchmark\_demo/webserver\_app/linux\_app   | Linux application code handles the IPC RPMsg\_char and the JSON file update for A53    |
+------+--------------------------------------------------+----------------------------------------------------------------------------------------+
| 3    | apps/benchmark\_demo/webserver\_app/webserver    | Web server and node files                                                              |
+------+--------------------------------------------------+----------------------------------------------------------------------------------------+
