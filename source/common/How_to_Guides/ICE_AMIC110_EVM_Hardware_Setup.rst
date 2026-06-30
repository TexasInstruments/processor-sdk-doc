
AMIC110 ICE EVM Hardware Setup
===============================

Description
---------------

The AMIC110 ICE is a high-performance, low-power platform that enables
users to evaluate and develop industrial communications applications for
the Sitara AMIC110 ARM Cortex-A8 processor SoC from Texas Instruments.™

EVM Layout and Key Components
------------------------------

.. Image:: /images/ICEAMIC110TopLayout.PNG
	:scale: 50%

.. Image:: /images/ICEAMIC110BottomLayout.PNG
	:scale: 50%

Quick Start Guide
--------------------

This quick start guide can be found in the `Hardware User's
Guide <http://www.ti.com/lit/spruie6a>`_.


1. Unbox the board and identify the various components
and connectors shown above.

2. To download a bootable image into the onboard SPI Flash, connect a 20-pin JTAG emulator to J1 on the ICE board. For example, the XDS110
or the XDS200 emulators may be used for this purpose and can be purchased from
the TI store: `XDS200 <https://store.ti.com/TMDSEMU200-U-XDS200-USB-Debug-Probe-P4281.aspx>`__ and `XDS110 <https://store.ti.com/TMDSEMU110-U-XDS110-JTAG-Debug-Probe-P51766.aspx>`__.

.. Image:: /images/ICEAMIC110JTAG.PNG
	:scale: 50%

3. Connect the pin header connector of the included TTL-232R-3V3 serial cable to J3 on the ICE board. Ensure that pin 1 of the serial cable (black wire, marked with a triangle) is connected to pin 1 of J3, which is indicated by a dot on the silk screen. Connect the
USB connector of the serial cable to a PC host port. The datasheet for this cable can found at http://www.ftdichip.com/Support/Documents/DataSheets/Cables/DS_TTL-232R_CABLES.pdf

.. Image:: /images/ICEAMIC110TTL.PNG
	:scale: 50%

4. Connect a CAT5 Ethernet cable from a PC running TwinCAT software to ECAT IN/PHY1 (J6) of the ICE board. If you have multiple ICE boards in a
chain, please connect another CAT5 Ethernet cable from ECAT OUT/PHY2 (J7) to PHY1 of the next ICE board. PHY2 of the last ICE board in the chain is left open.

.. Image:: /images/ICEAMIC110ETHERNET.PNG
	:scale: 50%

5. Connect the recommended power supply (CUI Inc. SMI18-5-V-P5, procurable at: http://www.digikey.com/product-detail/en/cui-inc/SMI18-5-V-P5/102-3571-ND/5415042) or equivalent (Output voltage/current: 5 Volts DC +/- 10% @ 1.2 Amps; Output connector: 2.1-mm ID, 5.5-mm OD barrel plug, center positive) power supply to J8 on the ICE board.
Apply power to the power supply to power up the ICE board. Do not hot plug the 5-V supply into the ICE board.

.. Image:: /images/ICEAMIC1105V.PNG
	:scale: 50%

Once the ICE board is powered on, the ON LED (D15) and LED4 (D19) will
turn on.

6. The AMIC110 ICE can now be connected to from the host machine via
UART. The serial port should be setup as shown below.

.. Image:: /images/Baudrate.jpg
	:scale: 50%

Boot Configuration
---------------------

The various boot configurations are discussed in the `Hardware User
Guide. <http://www.ti.com/lit/spruip3>`__

Connecting the AMIC110 ICE to Code Composer Studio
----------------------------------------------------

1. Download Code Composer Studio and the AMIC110 Sitara Device Support package as
described in the `Processor SDK RTOS Getting Started Guide <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/Overview.html#processor-sdk-rtos-getting-started-guide>`_.

2. Connect the AMIC110 ICE as described in the
Quick Start Guide.

3. Launch CCS and create a new target configuration file (File->New->Target Configuration File) as shown below. Select
the appropriate emulator and the ICE\_AMIC110 as the target as shown below.


.. Note:: If the ICE\_AMIC110 target is not listed, make sure the Sitara Device Support package v1.3.6 or greater is installed.

.. Image:: /images/ICEAMIC110TargetConfig.PNG
	:scale: 50%

4. Click Save to save the target configuration. Then press Test Connection to test the connection. If successful, a message should be
seen similar to the one below.

.. Image:: /images/ICEAMIC110Test.PNG
	:scale: 50%

5. Launch the target configuration and
connect to the ARM Cortex-A8.

The complete GEL log from the Cortex A8 is provided below.

::

    CortxA8: Output: ****  AMIC110_ICE & BoosterPack Initialization is in progress ......
    CortxA8: Output: ****  AMIC110 & Booster Pack ALL PLL Config for OPP == OPP100 is in progress ........
    CortxA8: Output: Input Clock Read from SYSBOOT[15:14]:  25MHz
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
    CortxA8: Output: ****  AMIC110 BoosterPack ALL ADPLL Config for 25 MHz OPP == OPP100 25MHz is Done .........
    CortxA8: Output: ****  AMIC110 DDR3 EMIF and PHY configuration is in progress...
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
    CortxA8: Output: ****  AMIC110_ICE Initialization is Done ******************

Running Board Diagnostics
---------------------------

The Processor SDK RTOS Diagnostic package is designed to be a set of
baremetal tests to run on a given board to provide data path continuity
testing on peripherals.

To run diagnostics on the AMIC110 ICE, follow the procedure given in the
`RTOS Software Developer
Guide <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index_board.html#diagnostics>`__
