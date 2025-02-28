
OMAP-L138/C6748 LCDK Hardware Setup
====================================

Overview
---------------

The OMAP-L138/C6748 low-cost development kit (LCDK) enables fast and easy software and hardware development of everyday applications that require real-time signal processing
and control functional, including industrial control, medical diagnostics and communications.

Hardware
^^^^^^^^
Information on the LCDK hardware, including DIP switches, LEDs, and user bottons, can be found in the LCDK User's Guide at the following link.

`OMAP-L138/C6748 Low-Cost Development Kit User's Guide <http://www.ti.com/lit/ug/spruil2/spruil2.pdf>`__

Powering the LCDK
^^^^^^^^^^^^^^^^^^
The board can be powered with 5V input through the J1 barrel connector.

UART Connection
^^^^^^^^^^^^^^^^^
Connect a mini-USB cable between UART port (J3) of the EVM and the host PC. Open a serial console (e.g. Tera Term) on the host PC and configure the serial port as follows.

 - Baud rate - 115200
 - Data length - 8 bit
 - Parity - None
 - Stop bits - 1
 - Flow control - None

Linux Quick Start Guide
------------------------

The quick start guide for booting Linux on the Arm core can be found at the following link.

`OMAP-L138 DSP+ARM9™ Development Kit (LCDK) Quick Start Guide <http://www.ti.com/lit/ml/sprw268a/sprw268a.pdf>`__

Connecting the LCDK to Code Composer Studio
--------------------------------------------

The following section describes how to connect to the LCDK and load code via CCS for application development and debug.

Hardware Setup
^^^^^^^^^^^^^^^

- Set the SW1 DIP switches to UART boot mode
- Connect an external emulator to the J6 header.
- Power on the LCDK using the J1 barrel connector.

Software Setup
^^^^^^^^^^^^^^^^^^^^^^

- Code Composer Studio IDE - `Download <http://www.ti.com/tool/CCSTUDIO>`__

.. Note:: CCS versions 9.0 and later are 64-bit applications. Due to this, 32-bit emulators like the Spectrum Digital XDS510USB emulator are not supported with CCS versions 9.0 and later.

- Processor SDK RTOS for OMAP-L138/C6748 - `Download <http://www.ti.com/tool/PROCESSOR-SDK-OMAPL138>`__

.. Note:: Please check the `Processor SDK Release Notes <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index_release_specific.html#release-notes>`__ for the recommended CCS version.

- Setup the software environment as described in the "Download and install software" section of the `Processor SDK RTOS Getting Started Guide <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index_overview.html#download-and-install-software>`__

- Build an example. Below are some suggested examples to get started with.

	- `No OS (Bare Metal) Example <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index_examples_demos.html#id53>`__

	- `TI-RTOS Kernel Example <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index_examples_demos.html#dsp-c674x>`__

	- `GPIO LED Blink Example <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index_device_drv.html#id22>`__

Creating a Target Configuration File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- In CCS, navigate to View -> Target Configurations.

- In the Target Configurations window, right-click and select "New Target Configuration."

- For Connection, select your external emulator.

- For Board or Device, select LCDKC6748 or LCDKOMAPL138 as shown in the following image, and click Save.

.. Image:: /images/lcdk_targetConfig.png

|

- Navigate to the Advanced tab and ensure the GEL file is loaded for the ARM9_0 core (OMAP-L138) or C674X_0 core (C6748).

**OMAP-L138 LCDK GEL File:**

.. Image:: /images/lcdk_omapl138_gel.png
	:scale: 100%

**C6748 LCDK GEL File:**

.. Image:: /images/lcdk_c6748_gel.png
	:scale: 100%


Connecting to Target and Loading/Running Program
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Connecting to Target**

- In CCS, navigate to the Target Configurations window.

- Right-click on the newly created target configuration and select "Launch Selected Configuration."

- Right-click on the ARM9_0 core for OMAP-L138 or C674X_0 core for C6748, and click "Connect Target."


The following GEL outputs should appear in the CCS Console view.

**OMAP-L138 LCDK:**

::

	ARM9_0: Output: 	Target Connected.
	ARM9_0: Output: 	---------------------------------------------
	ARM9_0: Output: 	Memory Map Cleared.
	ARM9_0: Output: 	---------------------------------------------
	ARM9_0: Output: 	Memory Map Setup Complete.
	ARM9_0: Output: 	---------------------------------------------
	ARM9_0: Output: 	PSC Enable Complete.
	ARM9_0: Output: 	---------------------------------------------
	ARM9_0: Output: 	PLL0 init done for Core:300MHz, EMIFA:25MHz
	ARM9_0: Output: 	DDR initialization is in progress....
	ARM9_0: Output: 	PLL1 init done for DDR:150MHz
	ARM9_0: Output: 	Using DDR2 settings
	ARM9_0: Output: 	DDR2 init for 150 MHz is done
	ARM9_0: Output: 	---------------------------------------------
	ARM9_0: Output: 	DSP Wake Complete.
	ARM9_0: Output: 	---------------------------------------------

**C6748 LCDK:**

::

	C674X_0: Output: 	Target Connected.
	C674X_0: Output: 	---------------------------------------------
	C674X_0: Output: 	Memory Map Cleared.
	C674X_0: Output: 	---------------------------------------------
	C674X_0: Output: 	Memory Map Setup Complete.
	C674X_0: Output: 	---------------------------------------------
	C674X_0: Output: 	PSC Enable Complete.
	C674X_0: Output: 	---------------------------------------------
	C674X_0: Output: 	PLL0 init done for Core:300MHz, EMIFA:25MHz
	C674X_0: Output: 	DDR initialization is in progress....
	C674X_0: Output: 	PLL1 init done for DDR:150MHz
	C674X_0: Output: 	Using DDR2 settings
	C674X_0: Output: 	DDR2 init for 150 MHz is done
	C674X_0: Output: 	---------------------------------------------

|

**Loading Program**

- Select the desired core (ARM9_0 or C674X_0).
- Go to “Run -> Load -> Load Program.”
- Click “Browse” to choose a prebuilt .out or click “Browse project..” to choose a .out from an open project.
- Select the desired .out and click OK.

**Running Program**

- Go to “Run -> Resume”
