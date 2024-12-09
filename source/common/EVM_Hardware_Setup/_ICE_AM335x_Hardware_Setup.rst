
AM335x ICE EVM Hardware Setup
=============================

Description
------------

The low-cost ICE EVM can be used for evaluation and development of
industrial communication type applications. It has been equipped with a
TI AM3359 processor and a defined set of features to allow the user to
experience specifically industrial communication solutions using serial
or Ethernet based interfaces. It is not intended as a generic
development platform as some of the features and interfaces supplied by
the AM335x are not accessible from the ICE board. Using standard
interfaces, the ICE board may interface to other processors or systems
and act as a communication gateway in this case. In addition it can
directly operate as a standard remote I/O system or simple sensor
connected to an industrial communication network. The embedded emulation
logic allows emulation and debug using standard development tools such
as TI’s Code Composer Studio by just using the supplied USB cable.

EVM Layout and Key Components
------------------------------

.. Image:: /images/ICE_V2_marked.png
	:scale: 50%

Quick Start Guide
--------------------

This section details how to quickly setup the AM3359 ICE.

1. Unbox the board and identify the various components and connectors
shown above.

2. Connect the power cable to the power jack on the board and plug it
into an AC power source.

.. Image:: /images/ICE335924V.png
	:scale: 50%

Once powered on, the POWER ON LED (D16) and Industrial Output LEDs
(D6-D10, D12, D14, and D15) will turn on.


.. Note:: When powering the AM335x ICE, always use the supplied power supply (CUI/V-Infinity Part Number EMSA240075) or equivalent model having output voltage of +24VDC and output current max 0.75 Amps and that complies with applicable regional safety standards such as (by example) UL, CSA, VDE, CCC, PSE, etc.

3. Connect the microUSB cable to the USB JTAG/Console port on the ICE board and connect to the USB on the host. Connect an Ethernet cable to
ETH0 if network connectivity is required.

.. Image:: /images/ICE3359USB.png
	:scale: 50%

.. Note:: The serial port will not show up on the host PC until the board is powered on.

4. Users can now connect to UART and the on-board XDS100v2 emulator from
the host machine. For UART port connections, set the serial terminal
software baud rate to 115200 to view the log messages. Connecting to the
target using the on-board emulator is discussed in the section below.


.. Image:: /images/Serial_connect.jpg
	:scale: 50%

.. Image:: /images/Baudrate.jpg
	:scale: 50%

Boot Configuration
--------------------

The various boot configurations are discussed in the `Hardware User
Guide. <http://www.ti.com/lit/spruip3>`__

|

Connecting the AM3359 ICE to Code Composer Studio
------------------------------------------------------

1. Download Code Composer Studio and the AM335x Sitara Device Support
package as described in the `Processor SDK RTOS Getting Started
Guide. <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index_overview.html#code-composer-studio>`__

2. Connect the AM3359 ICE as described above in the
Quick Start Guide.

3. Launch CCS and create a new target configuration file
(File->New->Target Configuration File) as shown below. Select the Texas
Instruments XDS100v2 USB Debug Probe and the ICE\_AM3359 as shown below.


.. Note:: If the ICE\_AM3359 target is not listed, make sure the latest Sitara Device Support package is installed by going to Help->Check for Updates.

.. Image:: /images/ICE3359TargetConfig.png
	:scale: 50%

4. Click Save to save the target configuration. Then press Test
Connection to test the connection. If successful, a message should be
seen similar to the one below.

.. Image:: /images/ICE3359Test.png
	:scale: 50%

5. Launch the target configuration and connect
to the ARM Cortex-A8.

The complete GEL log from the Cortex A8 is provided below.

::

    CortxA8: Output: ****  AM3359_ICE Initialization is in progress ..........
    CortxA8: Output: ****  AM335x ALL PLL Config for OPP == OPP100 is in progress .........
    CortxA8: Output: Input Clock Read from SYSBOOT[15:14]:  24MHz
    CortxA8: Output: ****  Going to Bypass...
    CortxA8: Output: ****  Bypassed, changing values...
    CortxA8: Output: ****  Locking ARM PLL
    CortxA8: Output: ****  Core Bypassed
    CortxA8: Output: ****  Now locking Core...
    CortxA8: Output: ****  Core locked
    CortxA8: Output: ****  DDR DPLL Bypassed
    CortxA8: Output: ****  DDR DPLL Locked
    CortxA8: Output: ****  PER DPLL Bypassed
    CortxA8: Output: ****  PER DPLL Locked
    CortxA8: Output: ****  DISP PLL Config is in progress ..........
    CortxA8: Output: ****  DISP PLL Config is DONE ..........
    CortxA8: Output: ****  AM335x ALL ADPLL Config for OPP == OPP100 is Done .........
    CortxA8: Output: ****  AM335x DDR3 EMIF and PHY configuration is in progress...
    CortxA8: Output: EMIF PRCM is in progress .......
    CortxA8: Output: EMIF PRCM Done
    CortxA8: Output: DDR PHY Configuration in progress
    CortxA8: Output: Waiting for VTP Ready .......
    CortxA8: Output: VTP is Ready!
    CortxA8: Output: DDR PHY CMD0 Register configuration is in progress .......
    CortxA8: Output: DDR PHY CMD1 Register configuration is in progress .......
    CortxA8: Output: DDR PHY CMD2 Register configuration is in progress .......
    CortxA8: Output: DDR PHY DATA0 Register configuration is in progress .......
    CortxA8: Output: DDR PHY DATA1 Register configuration is in progress .......
    CortxA8: Output: Setting IO control registers.......
    CortxA8: Output: EMIF Timing register configuration is in progress .......
    CortxA8: Output: EMIF Timing register configuration is done .......
    CortxA8: Output: PHY is READY!!
    CortxA8: Output: DDR PHY Configuration done
    CortxA8: GEL Output: Turning on EDMA...
    CortxA8: GEL Output: EDMA is turned on...
    CortxA8: Output: ****  AM3359_ICE Initialization is Done ******************

|

Running Board Diagnostics
-----------------------------

The Processor SDK RTOS Diagnostic package is designed to be a set of
baremetal tests to run on a given board to provide data path continuity
testing on peripherals.

To run diagnostics on the AM335x ICE, follow the procedure given in the
`RTOS Software Developer
Guide <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index_board.html#running-the-diagnostic-examples>`__
