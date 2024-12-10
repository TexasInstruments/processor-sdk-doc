.. _processor-sdk-rtos-release-notes:

*************
Release Notes
*************

Overview
========

The **Processor Software Development Kit (Processor-SDK)** provides the
core foundation and building blocks that facilitate application software
development on TI's embedded processors. This *Release Notes* focuses on
the Real-time operating system (RTOS).

|

Licensing
=========

Please refer to the software manifest, which outlines the licensing
status for all packages included in this release. The manifest can be
found on the SDK download page or in the installed directory as
indicated below.

|

Documentation
=============

-  :ref:`Getting Started Guide <Processor-SDK-RTOS-Getting-Started-Guide-label>`:
   Provides information on getting the software and running basic
   examples/demonstrations bundled in the SDK.
-  :ref:`Migration Guide <RTOS-SDK-Migration-Guide-label>` Provides
   migration information for applications built on top of the Processor
   SDK for RTOS.
-  :ref:`Software Developer Guide <Index-Processor-SDK-RTOS-label>`
   Provides information on features, functions, delivery package and,
   compile tools for the Processor SDK RTOS release. This also provides
   detailed information regarding software elements and software
   infrastructure to allow developers to start creating applications.
-  **Software Manifest**: Provides license information on software
   included in the SDK release. This document is in the release at
   ``/processor_sdk_rtos_<SOC>_<version>/docs`` and available to view
   from the software download page.
-  **EVM Quick Start Guide**: Provides information on hardware setup and
   running the demonstration application that is loaded on flash. This
   document is provided as part of the EVM kit.

|

Processor SDK v06.03.00
=======================

Released Apr 2020

.. rubric::  What's New
   :name: whats-new

.. rubric::  New Features
   :name: new-features

- Generic Updates
    - Sysbios update to 6.76.03.01
    - TI ARM CGT update to 18.12.5 LTS

- Descoped features
    - Sercos3 softmaster demo on AM335x

.. _release-notes-component-version:

.. rubric::  Component Version
   :name: component-version

The following software components and host tools are bundled with the
SDK installer. See the :ref:`Software Developer Guide <Index-Processor-SDK-RTOS-label>` for
more information on each item.

.. note::
   | This release has been tested with the following component and tool versions. It is recommended to use the versions listed here to avoid compatibility issues.

+-------------+------------+------+------+------+------+-------+------+------+------+------+------+---------+---------+
|  Component  |   Version  |AM335x|AM437x|AM57x |AM65x |K2H/K2K| K2E  | K2L  | K2G  |C665x |C667x |OMAP-L137|OMAP-L138|
+=============+============+======+======+======+======+=======+======+======+======+======+======+=========+=========+
| CG_XML      | 2.61.0     |   X  |  X   |  X   |  X   |   X   |  X   |  X   |  X   |  X   |  X   |    X    |    X    |
+-------------+------------+------+------+------+------+-------+------+------+------+------+------+---------+---------+
| CTOOLSLIB   | 2.2.0.0    |      |      |  X   |      |   X   |  X   |  X   |  X   |  X   |  X   |         |         |
+-------------+------------+------+------+------+------+-------+------+------+------+------+------+---------+---------+
|  DSPLIB     | 3.4.0.4    |      |      |  X   |      |   X   |  X   |  X   |  X   |  X   |  X   |    X    |    X    |
+-------------+------------+------+------+------+------+-------+------+------+------+------+------+---------+---------+
|  EDMA3 LLD  | 2.12.5.30  |   X  |  X   |  X   |      |       |  X   |  X   |  X   |  X   |  X   |    X    |    X    |
+-------------+------------+------+------+------+------+-------+------+------+------+------+------+---------+---------+
|  FC         | 3.40.2.7   |      |      |  X   |      |   X   |  X   |  X   |  X   |  X   |  X   |         |         |
+-------------+------------+------+------+------+------+-------+------+------+------+------+------+---------+---------+
|  FFTLIB     | 3.1.0.0    |      |      |      |      |       |      |      |      |      |  X   |         |         |
+-------------+------------+------+------+------+------+-------+------+------+------+------+------+---------+---------+
|  IMGLIB     | 3.1.1.0    |      |      |  X   |      |   X   |  X   |  X   |  X   |  X   |  X   |         |         |
+-------------+------------+------+------+------+------+-------+------+------+------+------+------+---------+---------+
|  IPC        | 3.50.4     |      |      |  X   |   X  |   X   |  X   |  X   |  X   |  X   |  X   |         |    X    |
+-------------+------------+------+------+------+------+-------+------+------+------+------+------+---------+---------+
|  LIBARCH    | 1.0.0.0    |      |      |      |      |   X   |      |      |      |      |  X   |         |         |
+-------------+------------+------+------+------+------+-------+------+------+------+------+------+---------+---------+
|  LINALG     | 1.2.0.0    |      |      |      |      |   X   |      |      |      |      |  X   |         |         |
+-------------+------------+------+------+------+------+-------+------+------+------+------+------+---------+---------+
|  MATHLIB    | 3.1.2.4    |      |      |  X   |      |   X   |  X   |  X   |  X   |  X   |  X   |    X    |    X    |
+-------------+------------+------+------+------+------+-------+------+------+------+------+------+---------+---------+
|  MPM        | 3.0.4.0    |      |      |      |      |   X   |  X   |  X   |  X   |      |      |         |         |
+-------------+------------+------+------+------+------+-------+------+------+------+------+------+---------+---------+
|  NDK        | 3.61.1     |   X  |  X   |  X   |   X  |   X   |  X   |  X   |  X   |  X   |  X   |    X    |    X    |
+-------------+------------+------+------+------+------+-------+------+------+------+------+------+---------+---------+
|  NS         | 2.60.1     |   X  |  X   |  X   |   X  |   X   |  X   |  X   |  X   |  X   |  X   |    X    |    X    |
+-------------+------------+------+------+------+------+-------+------+------+------+------+------+---------+---------+
|  OPENCL     | 1.2.0.2    |      |      |  X   |      |       |      |      |      |      |      |         |         |
+-------------+------------+------+------+------+------+-------+------+------+------+------+------+---------+---------+
|  OPENMP     | 2.6.3.0    |      |      |  X   |      |   X   |  X   |  X   |  X   |  X   |  X   |         |         |
+-------------+------------+------+------+------+------+-------+------+------+------+------+------+---------+---------+
|  PDK        |            |1.0.17|1.0.17|1.0.17| 1.0.7| 4.0.16|4.0.16|4.0.16|1.0.16|2.0.16|2.0.16|  1.0.11 |  1.0.11 |
+-------------+------------+------+------+------+------+-------+------+------+------+------+------+---------+---------+
|  SYS/BIOS   | 6.76.3.1   |   X  |  X   |  X   |   X  |   X   |  X   |  X   |  X   |  X   |  X   |    X    |    X    |
+-------------+------------+------+------+------+------+-------+------+------+------+------+------+---------+---------+
|  UIA        | 2.30.1.2   |      |      |  X   |   X  |   X   |  X   |  X   |  X   |  X   |  X   |    X    |    X    |
+-------------+------------+------+------+------+------+-------+------+------+------+------+------+---------+---------+
|  XDAIS      | 7.24.0.4   |      |      |  X   |      |   X   |  X   |  X   |  X   |  X   |  X   |    X    |    X    |
+-------------+------------+------+------+------+------+-------+------+------+------+------+------+---------+---------+
|  XDCTOOLS   | 3.55.02    |   X  |  X   |  X   |   X  |   X   |  X   |  X   |  X   |  X   |  X   |    X    |    X    |
+-------------+------------+------+------+------+------+-------+------+------+------+------+------+---------+---------+


The following compilers are bundled with the SDK installer:

+----------------+---------+------+------+------+------+-------+-----+--------+--------+-----+-----+---------+---------+
|    Compiler    | Version |AM335x|AM437x|AM57x |AM65x |K2H/K2K| K2E | K2L    |  K2G   |C665x|C667x|OMAP-L137|OMAP-L138|
+================+=========+======+======+======+======+=======+=====+========+========+=====+=====+=========+=========+
|GNU ARM Embedded|7-2018-q2|   A8 |  A9  |  A15 |      |  A15  | A15 | A15    |  A15   |     |     |         |         |
+----------------+---------+------+------+------+------+-------+-----+--------+--------+-----+-----+---------+---------+
|GNU Linaro GCC  | 7.2.1   |      |      |      | A53  |       |     |        |        |     |     |         |         |
+----------------+---------+------+------+------+------+-------+-----+--------+--------+-----+-----+---------+---------+
|TI ARM CGT      | 18.12.5 |      |      |  M4  |  R5  |       |     |A15(SBL)|        |     | ARM9|   ARM9  |         |
+----------------+---------+------+------+------+------+-------+-----+--------+--------+-----+-----+---------+---------+
|TI C6000 CGT    | 8.3.2   |      |      | C66x |      | C66x  |C66x | C66x   |  C66x  |C66x |C66x |   C674x |   C674x |
+----------------+---------+------+------+------+------+-------+-----+--------+--------+-----+-----+---------+---------+
|TI PRU CGT      | 2.3.2   | PRU  | PRU  | PRU  |  PRU |       |     |  PRU   |        |     |     |         |         |
+----------------+---------+------+------+------+------+-------+-----+--------+--------+-----+-----+---------+---------+

The SDK uses Code Composer Studio (CCS) as the integrated development
environment (IDE) for all devices and EVMs:

+-----------+----------+------+------+------+------+-------+-----+-----+-----+-----+-----+---------+---------+
| Component | Version  |AM335x|AM437x|AM57x |AM65x |K2H/K2K| K2E | K2L | K2G |C665x|C667x|OMAP-L137|OMAP-L138|
+===========+==========+======+======+======+======+=======+=====+=====+=====+=====+=====+=========+=========+
|   CCS     | 9.3.0    |   X  |  X   |  X   |  X   |   X   |  X  |  X  |  X  |  X  |  X  |    X    |    X    |
+-----------+----------+------+------+------+------+-------+-----+-----+-----+-----+-----+---------+---------+
|   EMU Pack|Sitara    |   X  |  X   |  X   |  X   |       |     |     |     |     |     |         |         |
|           |Device    |      |      |      |      |       |     |     |     |     |     |         |         |
|           |1.4.5     |      |      |      |      |       |     |     |     |     |     |         |         |
+-----------+----------+------+------+------+------+-------+-----+-----+-----+-----+-----+---------+---------+
|    TI     |8.3.0.0   |   X  |  X   |  X   |  X   |   X   |  X  |  X  |  X  |  X  |  X  |     X   |     X   |
| Emulators |          |      |      |      |      |       |     |     |     |     |     |         |         |
+-----------+----------+------+------+------+------+-------+-----+-----+-----+-----+-----+---------+---------+

If you need to install CCS, see the :ref:`CCS installation section <overview-code-composer-studio>`
in the *Getting Started Guide* for options to select for Processor-SDK.



Fixed Issues
============

.. csv-table::
   :header: "Record ID","Board/s", "Component/s", "Summary"
   :widths: 15, 20,20,30

	PRSDK-7627,"am654x-evm, am654x-hsevm, am654x-idk",PRUSS-Firmware,ICSSG: firmware - support changing of speed/duplex on the fly from DUT
	PRSDK-7722,am654x-idk,PDK,PN_Switch: EMAC LLD free_pkt_cb callback function returns invalid data
	PRSDK-5935,"am654x-evm, j721e-evm",UNIFLASH,Flashing speed for OSPI with Uniflash 5.0 is very poor (about 7KB/s)
	PRSDK-6109,"am654x-evm, am654x-hsevm, am654x-idk, j721e-evm",Boot,ROM load time of SBL increased on GP devices because SBL is not signed with ROM degeneratekey
	PRSDK-7907,am572x-evm,Chip Support,AM572x GP EVM eth0 is not working at 10Mbps
	PRSDK-8171,"am335x-evm, beagleboneblack",PDK,UART DMA Transmission and Receiving isn't working
	PRSDK-8343,am654x-idk,SCIClient,Sciclient_pmDeviceReset failing on SDK 6.3
	PRSDK-7120,"j721e-evm, k2g-evm",PDK,SPI master slave test fails in non-dma callback mode
	PRSDK-5966,"am654x-evm, am654x-hsevm, am654x-idk",Boot,PLL settings for Maxwell are not optimal
	PRSDK-5397,am574x-idk,Chip Support,"CSL ECC EMIF test hangs at ""OCMC FULL ECC Mode"" on ARM"
	PRSDK-7292,"am335x-evm, am335x-ice, amic110-ice, beagleboneblack",Control Drivers,AM335x SPI: No DMA support for McSPI slave mode examples
	PRSDK-7898,j721e-evm,"Board Support, PDK",PSDKRA release docs indicate Uniflash support exists for J721E
	PRSDK-8136,"am654x-evm, am654x-hsevm, am654x-idk",Chip Support,AM65xx: NAVSS bit field definitions missing from CSL
	PRSDK-7518,am572x-evm,Documentation,PRSDK docs contains incorrect info concerning AM572x GP EVM camera support
	PRSDK-8116,"am654x-evm, am654x-idk, j721e-evm",SCIClient,[SCICLIENT] Trail bytes logic overwrites response parameters
	PRSDK-7958,am572x-idk,Control Drivers,AM57xx: C66 repeated McSPI loopback transfer crashes
	PRSDK-8092,"am654x-evm, am654x-idk",Chip Support,AM65xx: A53_0 CSL ePWM example build incorrect & run-time failure
	PRSDK-7489,"am571x-idk, am572x-idk",OSAL,AM57xx: OSAL Timer on DSP requires Board_init() with UART_STDIO_INIT
	PRSDK-8020,"am654x-evm, am654x-idk",Documentation,AM65xx:R5F Incorrect documentation concerning RTOS template app
	PRSDK-8117,"am570x-evm, am571x-idk, am572x-evm, am572x-idk, am574x-idk",Chip Support,AM5728: CSL cache API always returns error
	PRSDK-3727,"c6748-evm, c6748-lcdk",PDK,C6748 is missing from SOC description list in pdkProjectCreate
	PRSDK-8114,c6657-evm,Networking,C6657 NIMU ping test failure for packet size greater than 1510 bytes

Known Issues
============

This section contains the list of known issues at the time of making the
release and any known workaround.

.. csv-table::
   :header: "Record ID","Board/s","Component/s","Summary","Workaround"
   :widths: 15,100,20,30,20

	PRSDK-769,Posix-SMP Demo DMIPS are wrong,Demonstrations,Multiple Platforms
	PRSDK-5642,USB_DevBulk_ExampleProject: Failed to load/run app,Board Support,am335x-evm,Use JTAG to load and run the example
	PRSDK-5186,"*Multiple platforms",Board Support,PDK Driver examples wrongly puts libgcc in to DDR invalidating IO delay configuration,"The user application could explicitly place the libgcc.a in to OCMC RAM along with BOARD_IO_DELAY_DATA/CODE sections so that there is no DDR access while calling IO Delay functions "
	PRSDK-6653,"Diagnostics tests(Haptics,Temperature,Accelerometer,ADC,Ambient light, button, mmcsd) hangs on evmAM335x/AM437x",Diagnostics,"am335x-evm, am437x-evm"
	PRSDK-2336,"am335x-evm, am437x-evm",Power,AM3 & AM4 PM Examples experience I2C bus lockup when communicating with PMIC,"The debug versions of the PM apps are still functional. To build them: From the top-level makefile in pdk.../packages folder run ""make BUILD_PROFILE=debug pm"" This will build the debug versions of the PM RTOS and measurement apps."
	PRSDK-6043,TI-RTOS Kernel Example does not work with Resource Explorer in CCS 9.x,CCS,Multiple Platforms
	PRSDK-8163,output from pinmux template file for AM335x causes ADP_Stopped exception in Board_init(),Board Support,am335x-ice,Existing pinmux files available in release will need to be updated
	PRSDK-8300,"Diag(MEM,LED,MMCSD) test failures on am335x-ice",Diagnostics,am335x-ice
	PRSDK-6184,BIOS 6.75 newlib-nano and header incompatibility with GCCv7.3.1 toolchain in SDK,System Integration,Multiple Platforms
	PRSDK-335,USB host MSC fails to re-enumerate,High-Speed Drivers,"am437x-evm, k2g-evm",Re-enumeration support for the case of device unplugged and plugged back currently fails for the example. Workaround is to avoid disconnecting drive while running example
	PRSDK-6161,ICSS_EMAC_BasicExample fails on AM437x IDK with errors in received acyclic pkt content,Networking,am437x-idk
	PRSDK-5936,IO-Link master example does not work with Balluff inductive coupler,PDK,am437x-idk
	PRSDK-4583,PRUSS-I2C-FW: Does not support 1Mhz mode. Incorrect STOP condition generated for HS mode,PRUSS-Firmware,am437x-idk
	PRSDK-5938,I2C Master Slave Example: SPI TX/RX FIFO trigger level test failure (UT1),PDK,"am437x-idk, am571x-idk, am572x-idk"
    PRSDK-2892,"am571x-idk, am572x-evm, am572x-idk",PDK,Incorrect A15 MMU configurations in default config file,"Set MMU attribute to not executable for device memory attrs0.noExecute = true; // Not executable"
	PRSDK-5087,ICSS_EMAC_BasicExample fails on AM57xx-IDK with Packet cyclic timestamp error,Networking,"am571x-idk, am572x-idk, am574x-idk"
	PRSDK-3876,CM_EMU_CLKSTCTRL=0x2 needed for reliable low power exit if EMU[1:0] pins are used as GPIOs,Boot,am572x-evm
	PRSDK-5987,UART Rx/TX trigger level test fails in SMP mode for AM572x EVM (DMA),Control Drivers,am572x-evm
	PRSDK-4667,Image Processing Demo lock up on AM572x GP EVM,"Demonstrations, Networking",am572x-evm,Issue seen using 1Gig router on ETH0. Replace with 100Mbps
	PRSDK-1975,timer_DiagExample_evmAM572x_arm7.out doesn't work on ARM1 core,Diagnostics,am572x-evm,Example can run on ARM Core 0
	PRSDK-6958,pm_rtos_testapp DSP/M4: shutdown test failed,Power,am572x-evm
	PRSDK-3656,PM: shutdown test failed on DSP core for am572x-evm,Power,am572x-evm
	PRSDK-8170,AM57xx: A15 QSPI flash block erase & DMA mode write issues,Control Drivers,am572x-idk,Use non-DMA (cpu based copy) instead of the DMA transfer
	PRSDK-5879,Board: Board library needs to cover entire DDR region connected to EMIF1,Board Support,am654x-evm
    PRSDK-7735,am65xx:Need to optimize time it takes to poll for packets from udma rings on R5,am654x-idk,"emac_poll_ctrl API is used to poll for rx packets, rx management responses and tx completion events. The parameters to this API are the port number, bitmap of receive packets, bitmap of management rings, and bitmap of tx completion rings to poll. The bitmaps are specified in the driver interface header file. In order to reduce the polling interval, it is recommended to call this API with only bitmap of rings that are required to be polled for an applications use call rather than polling for all the rings. Note that for release 6.3 applications and libraries for rR5F core are being compiled in thumb mode and initial testing indicates a ~20% reduction in cycle time versus release 6.1"
	PRSDK-6382,SBL: R5F: Core 1 boot is not working with unsigned binary with ipc images,Boot,am654x-evm
	PRSDK-4661,Maxwell: Board diagnostics LCD touchscreen test reports incorrect number of touch events,Diagnostics,"am654x-evm, am654x-hsevm, am654x-idk"
	PRSDK-7908,R5 Board Diagnostics Apploader crashes on AM65x (PG1 & 2),PDK,"am654x-evm, am654x-hsevm, am654x-idk",Board Diagnostics can be executed from A53
	PRSDK-7176,AM65x R5 diagnostic tests are hanging while running from diag framework,Board Support,"am654x-evm, am654x-idk"
	PRSDK-2951,Maxwell_M4_Diag: LCD Display Diagnostic Stress Test,"Board Support, Diagnostics","am654x-evm, am654x-idk"
	PRSDK-5074,McASP driver hangs with small buffer size,PDK,"am654x-evm, j721e-evm",Use packet size 32 samples or greater
	PRSDK-5626,OSPI Read using UDMA fails on AM65x HS devices.,"Boot, DMA",am654x-hsevm,Non-DMA mode could be used for the read operation
	PRSDK-5229,PCIe diagnostic test validates only one port on PCIe 2-lane card,Board Support,am654x-idk
	PRSDK-5989,USB Host MSC test hangs in SMP mode on AM65xx IDK board,Control Drivers,am654x-idk
	PRSDK-5751,AM65xx IDK PCIe diagnostic test failure,Diagnostics,am654x-idk
	PRSDK-5022,am65xx: Running emac unit test on R5 core from ddrless SBL at times does not complete execution,Networking,am654x-idk
	PRSDK-3114,K2G: RTOS ECC support broken on ARM core,Diagnostics,"k2g-evm, k2g-hsevm, k2g-ice"
	PRSDK-2989,MMCSD LLD fails on OMAPl137 with 1024 byte block size,High-Speed Drivers,omapl137-evm
	PRSDK-4043,OMAPL13x: USB Baremetal project binaries not built via top level make,High-Speed Drivers,"omapl137-evm, omapl138-lcdk"

.. _RN-Supported-Platforms-label:

Supported Platforms
===================

Devices
-------

The following table lists all supported devices for a given installer.

+----------------+------------+-------------------------------------------------------------------------------+
|   Installer    |Platform/SOC|                                 Supported Devices                             |
+================+======+=====+===============================================================================+
|                |`AM335x`_   | `AM3351`_, `AM3352`_, `AM3354`_, `AM3356`_, `AM3357`_, `AM3358`_, `AM3359`_   |
|`RTOS-AM335X`_  +------------+-------------------------------------------------------------------------------+
|                |`AMIC11x`_  | `AMIC110`_                                                                    |
+----------------+------------+-------------------------------------------------------------------------------+
|`RTOS-AM437X`_  |`AM437x`_   | `AM4376`_, `AM4377`_, `AM4378`_, `AM4379`_                                    |
+----------------+------------+-------------------------------------------------------------------------------+
|`RTOS-AM57X`_   |`AM57x`_    |`AM5706`_, `AM5708`_, `AM5716`_, `AM5718`_, `AM5726`_, `AM5728`_,              |
|                |            |`AM5746`_, `AM5748`_                                                           |
+----------------+------------+-------------------------------------------------------------------------------+
| `RTOS-AM65X`_  | `AM65x`_   |`AM6526`_, `AM6527`_, `AM6528`_, `AM6546`_, `AM6548`_, DRA80xM                 |
+----------------+------------+-------------------------------------------------------------------------------+
|`RTOS-C665X`_   |`C665x`_    | `C6652`_, `C6654`_, `C6655`_, `C6657`_                                        |
+----------------+------------+-------------------------------------------------------------------------------+
|`RTOS-C667X`_   |`C667x`_    | `C6671`_, `C6672`_, `C6674`_, `C6678`_                                        |
+----------------+------------+-------------------------------------------------------------------------------+
|`RTOS-K2E`_     |`K2E`_      | `66AK2E02`_, `66AK2E05`_, `AM5K2E02`_, `AM5K2E04`_                            |
+----------------+------------+-------------------------------------------------------------------------------+
|`RTOS-K2G`_     |`K2G`_      | `66AK2G02`_, `66AK2G12`_                                                      |
+----------------+------------+-------------------------------------------------------------------------------+
|                |`K2H`_      | `66AK2H06`_, `66AK2H12`_, `66AK2H14`_                                         |
| `RTOS-K2HK`_   +------------+-------------------------------------------------------------------------------+
|                |`K2K`_      | `TCI6638K2K`_                                                                 |
+----------------+------------+-------------------------------------------------------------------------------+
|`RTOS-K2L`_     |`K2L`_      | `66AK2L06`_                                                                   |
+----------------+------------+-------------------------------------------------------------------------------+
|`RTOS-OMAPL137`_|`OMAP-L1x`_ | `OMAP-L137`_, `C6743`_, `C6745`_, `C6747`_                                    |
+----------------+------------+-------------------------------------------------------------------------------+
|`RTOS-OMAPL138`_|`OMAP-L1x`_ | `OMAP-L138`_, `C6742`_, `C6746`_, `C6748`_                                    |
+----------------+------------+-------------------------------------------------------------------------------+


.. _RTOS-AM335X: http://software-dl.ti.com/processor-sdk-rtos/esd/AM335X/latest/index_FDS.html
.. _AM335x: http://www.ti.com/am335x
.. _AM3351: http://www.ti.com/product/am3351
.. _AM3352: http://www.ti.com/product/am3352
.. _AM3354: http://www.ti.com/product/am3354
.. _AM3356: http://www.ti.com/product/am3356
.. _AM3357: http://www.ti.com/product/am3357
.. _AM3358: http://www.ti.com/product/am3358
.. _AM3359: http://www.ti.com/product/am3359

.. _AMIC11x: http://www.ti.com/lsds/ti/processors/sitara/industrial-ethernet/amic11x/amic11x-overview.page>`__
.. _AMIC110: http://www.ti.com/product/amic110

.. _RTOS-AM437X: http://software-dl.ti.com/processor-sdk-rtos/esd/AM437X/latest/index_FDS.html
.. _AM437x: http://www.ti.com/am437x
.. _AM4376: http://www.ti.com/product/am4376
.. _AM4377: http://www.ti.com/product/am4377
.. _AM4378: http://www.ti.com/product/am4378
.. _AM4379: http://www.ti.com/product/am4379

.. _RTOS-AM57X: http://software-dl.ti.com/processor-sdk-rtos/esd/AM57X/latest/index_FDS.html
.. _AM57x: http://www.ti.com/am57x
.. _AM5706: http://www.ti.com/product/am5706
.. _AM5708: http://www.ti.com/product/am5708
.. _AM5716: http://www.ti.com/product/am5716
.. _AM5718: http://www.ti.com/product/am5718
.. _AM5726: http://www.ti.com/product/am5726
.. _AM5728: http://www.ti.com/product/am5728
.. _AM5746: http://www.ti.com/product/am5746
.. _AM5748: http://www.ti.com/product/am5748

.. _RTOS-AM65X: http://software-dl.ti.com/processor-sdk-rtos/esd/AM65X/latest/index_FDS.html
.. _AM65x: http://www.ti.com/am65x
.. _AM6526: http://www.ti.com/product/am6526
.. _AM6527: http://www.ti.com/product/am6527
.. _AM6528: http://www.ti.com/product/am6528
.. _AM6546: http://www.ti.com/product/am6546
.. _AM6548: http://www.ti.com/product/am6548

.. _RTOS-C665X: http://software-dl.ti.com/processor-sdk-rtos/esd/C665x/latest/index_FDS.html
.. _C665x: http://www.ti.com/lsds/ti/processors/dsp/c6000_dsp/c66x/overview.page
.. _C6652: http://www.ti.com/product/tms320c6652
.. _C6654: http://www.ti.com/product/tms320c6654
.. _C6655: http://www.ti.com/product/tms320c6655
.. _C6657: http://www.ti.com/product/tms320c6657

.. _RTOS-C667X: http://software-dl.ti.com/processor-sdk-rtos/esd/C667x/latest/index_FDS.html
.. _C667x: http://www.ti.com/lsds/ti/processors/dsp/c6000_dsp/c66x/overview.page
.. _C6671: http://www.ti.com/product/tms320c6671
.. _C6672: http://www.ti.com/product/tms320c6672
.. _C6674: http://www.ti.com/product/tms320c6674
.. _C6678: http://www.ti.com/product/tms320c6678

.. _RTOS-K2E: http://software-dl.ti.com/processor-sdk-rtos/esd/K2E/latest/index_FDS.html
.. _K2E: http://www.ti.com/lsds/ti/processors/dsp/c6000_dsp-arm/66ak2x/overview.page
.. _66AK2E02: http://www.ti.com/product/66ak2e02
.. _66AK2E05: http://www.ti.com/product/66ak2e05
.. _AM5K2E02: http://www.ti.com/product/am5k2e02
.. _AM5K2E04: http://www.ti.com/product/am5k2e04

.. _RTOS-K2G: http://software-dl.ti.com/processor-sdk-rtos/esd/K2G/latest/index_FDS.html
.. _K2G: http://www.ti.com/processors/dsp/c6000-dsp-arm/66ak2x/overview.html
.. _66AK2G02: http://www.ti.com/product/66ak2g02
.. _66AK2G12: http://www.ti.com/product/66ak2g12

.. _RTOS-K2HK: http://software-dl.ti.com/processor-sdk-rtos/esd/K2HK/latest/index_FDS.html
.. _K2H: http://www.ti.com/lsds/ti/processors/dsp/c6000_dsp-arm/66ak2x/overview.page
.. _66AK2H06: http://www.ti.com/product/66ak2h06
.. _66AK2H12: http://www.ti.com/product/66ak2h12
.. _66AK2H14: http://www.ti.com/product/66ak2h14

.. _K2K: http://www.ti.com/lsds/ti/processors/dsp/c6000_dsp-arm/66ak2x/overview.page
.. _TCI6638K2K: http://www.ti.com/product/tci6638k2k

.. _RTOS-K2L: http://software-dl.ti.com/processor-sdk-rtos/esd/K2L/latest/index_FDS.html
.. _K2L: http://www.ti.com/lsds/ti/processors/dsp/c6000_dsp-arm/66ak2x/overview.page
.. _66AK2L06: http://www.ti.com/product/66ak2l06

.. _RTOS-OMAPL137: http://www.ti.com/tool/processor-sdk-omapl137
.. _OMAP-L1x: http://www.ti.com/lsds/ti/processors/dsp/c6000_dsp-arm/omap-l1x/overview.page
.. _OMAP-L137: http://www.ti.com/product/OMAP-L137
.. _C6743: http://www.ti.com/product/tms320c6743
.. _C6745: http://www.ti.com/product/tms320c6745
.. _C6747: http://www.ti.com/product/tms320c6747

.. _RTOS-OMAPL138: http://www.ti.com/tool/processor-sdk-omapl138
.. _OMAP-L1x: http://www.ti.com/lsds/ti/processors/dsp/c6000_dsp-arm/omap-l1x/overview.page
.. _OMAP-L138: http://www.ti.com/product/OMAP-L138
.. _C6742: http://www.ti.com/product/tms320c6742
.. _C6746: http://www.ti.com/product/tms320c6746
.. _C6748: http://www.ti.com/product/tms320c6748

Evaluation Modules
------------------

See :ref:`Processor SDK Supported Platforms <RTOS-SDK-Supported-Platforms>`
page for a list of supported EVMs per platform and links to more
information.

Demonstrations
--------------

See :ref:`Examples and Demonstrations <index-examples-demos>`
page for a list of demonstrations per platform and EVM.

Drivers
-------

The following tables show RTOS driver availability per platform and EVM.
A shaded box implies that the feature is not applicable for that
platform/EVM.

**Sitara devices**

+------------------+--------------------------------+---------------+-----------+-----------+-----------+----------+
|     Feature      |    Platform/SOC                |  AM335x EVM   |AM437x EVM | AM57x EVM | AM65x EVM |J721E EVM |
+==================+=======+======+=====+=====+=====+===+===+===+===+===+===+===+=====+=====+=====+=====+==========+
|                  |AM335x |AM437x|AM57x|AM65x|J721E|GP |ICE|SK |BBB|GP |IDK|SK | GP  | IDK | GP  | IDK |  GP      |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| CSL              |   X   |   X  |  X  |  X  |  X  | X | X | X | X | X | X | X |  X  |  X  |  X  |  X  |  X       |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| EMAC             |   X   |   X  |  X  |  X  |  X  | X | X | X | X | X | X | X |  X  |  X  |  X  |  X  |  X       |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| EDMA3            |   X   |   X  |  X  |     |     | X |   |   |   | X |   |   |  X  |     |     |     |          |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| GPIO             |   X   |   X  |  X  |  X  |  X  |   | X |   | X | X |   | X |  X  |  X  |  X  |  X  |  X       |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| GPMC             |   X   |   X  |     |     |     |   | X |   |   | X |   |   |     |     |     |     |          |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| I2C              |   X   |   X  |  X  |  X  |  X  | X | X | X | X | X | X | X |  X  |  X  |  X  |  X  |  X       |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| PRUSS-I2C f/w    |   X   |   X  |  X  |     |     |   | X |   |   |   | X |   |     |  X  |     |     |          |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| PRUSS-eSPI f/w   |   X   |   X  |     |     |     |   |   |   |   |   |   |   |     |     |     |     |          |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| ICSS-EMAC        |   X   |   X  |  X  |  X  |     |   | X |   |   |   | X |   |     |  X  |     |     |          |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| McASP            |   X   |   X  |  X  |  X  |  X  | X |   |   |   | X |   |   |  X  |     |  X  |  X  |  X       |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| McSPI            |   X   |   X  |  X  |  X  |  X  |   | X |   |   |   | X |   |     |  X  |   X |  X  |  X       |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| MMC-SD           |   X   |   X  |  X  |  X  |  X  | X | X | X | X | X | X | X |  X  |  X  |  X  |  X  |  X       |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| PCIe             |       |      |  X  |  X  |     |   |   |   |   |   |   |   |     |  X  |  X  |     |          |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| PM               |   X   |      |  X  |  X  |  X  | X |   |   |   |   |   |   |  X  |     |  X  |  X  |  X       |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| PRUSS            |   X   |   X  |  X  |  X  |  X  |   | X |   |   |   | X |   |     |  X  |  X  |  X  |  X       |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| QSPI             |       |   X  |  X  |  X  |  X  |   |   |   |   |   | X | X |     |  X  |     |     |  X       |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| OSPI             |       |      |     |  X  |  X  |   |   |   |   |   |   |   |     |     |  X  |  X  |  X       |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| UART             |   X   |   X  |  X  |  X  |  X  | X | X | X | X | X | X | X |  X  |  X  |  X  |  X  |  X       |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| USB              |   X   |   X  |  X  |  X  |  X  | X |   |   |   | X |   |   |  X  |  X  |  X  |   X |  X       |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| USB Device Audio |   X   |      |     |     |     | X |   |   |   |   |   |   |     |     |     |     |          |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| USB Device Bulk  |   X   |   X  |  X  |  X  |  X  | X |   |   |   | X |   |   |  X  |  X  |  X  |   X |  X       |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| VPS              |       |      |  X  |     |     |   |   |   |   |   |   |   |  X  |  X  |     |     |          |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| UDMA             |       |      |     |  X  |  X  |   |   |   |   |   |   |   |     |     |  X  |  X  |  X       |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| SCICLIENT        |       |      |     |  X  |  X  |   |   |   |   |   |   |   |     |     |  X  |  X  |  X       |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| SA               |       |      |     |  X  |  X  |   |   |   |   |   |   |   |     |     |  X  |  X  |  X       |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| CAL              |       |      |     |  X  |  X  |   |   |   |   |   |   |   |     |     |  X  |  X  |  X       |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| DSS              |       |      |     |  X  |  X  |   |   |   |   |   |   |   |     |     |  X  |  X  |  X       |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+
| FVID2            |       |      |     |  X  |  X  |   |   |   |   |   |   |   |     |     |  X  |  X  |  X       |
+------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+----------+

**DSP devices - K2x, C66x**

+------------------+-------------------------------+-----------------------+-----------+
|     Feature      |         Platform/SOC          |        K2 EVM         | C66x EVM  |
+==================+=======+===+===+===+=====+=====+===+===+===+===+=======+=====+=====+
|                  |K2H/K2K|K2E|K2L|K2G|C665x|C667x|K2H|K2E|K2L|K2G|K2G-ICE|C665x|C667x|
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| CSL              |   X   | X | X | X |  X  |  X  | X | X | X | X |   X   |  X  |  X  |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| AIF2             |   X   |   |   |   |     |     | X |   |   |   |       |     |     |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| BCP              |   X   |   | X |   |     |     | X |   | X |   |       |     |     |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| CPPI             |   X   | X | X | X |  X  |  X  | X | X | X | X |   X   |  X  |  X  |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| DFE              |       |   | X |   |     |     |   |   | X |   |       |     |     |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| EDMA3            |   X   | X | X | X |  X  |  X  | X | X | X | X |   X   |  X  |  X  |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| EMAC             |       |   |   | X |  X  |     |   |   |   | X |   X   |  X  |     |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| FFTC             |   X   |   | X |   |     |     | X |   | X |   |       |     |     |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| GPIO             |   X   | X | X | X |  X  |  X  | X | X | X | X |   X   |  X  |  X  |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| HYPLNK           |   X   | X |   |   |  X  |  X  | X | X |   |   |       |  X  |  X  |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| ICSS-EMAC        |       |   |   | X |     |     |   |   |   |   |   X   |     |     |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| I2C              |   X   | X | X | X |  X  |  X  | X | X | X | X |   X   |  X  |  X  |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| IQN2             |       |   | X |   |     |     |   |   | X |   |       |     |     |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| McASP            |       |   |   | X |     |     |   |   |   | X |       |     |     |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| McBSP            |       |   |   | X |  X  |     |   |   |   | X |       |  X  |     |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| MMAP             |   X   | X |   |   |     |     | X | X |   |   |       |     |     |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| MMC-SD           |       |   |   | X |     |     |   |   |   | X |   X   |     |     |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| NWAL             |   X   | X | X |   |     |  X  | X | X | X |   |       |     |  X  |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| PA               |   X   | X | X |   |     |  X  | X | X | X |   |       |     |  X  |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| PCIe             |   X   | X | X | X |  X  |  X  | X | X | X | X |       |  X  |  X  |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| QMSS             |   X   | X | X | X |  X  |  X  | X | X | X | X |   X   |  X  |  X  |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| RM               |   X   | X | X | X |  X  |  X  | X | X | X | X |   X   |  X  |  X  |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| SA               |   X   | X | X | X |     |  X  | X | X | X | X |       |     |  X  |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| SPI              |   X   | X | X | X |  X  |  X  | X | X | X | X |   X   |  X  |  X  |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| SRIO             |   X   |   |   |   |  X  |  X  | X |   |   |   |       |  X  |  X  |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| TCP3D            |   X   |   | X |   |  X  |     | X |   | X |   |       |  X  |     |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| TSIP             |       | X |   |   |     |  X  |   | X |   |   |       |     |  X  |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| UART             |   X   | X | X | X |  X  |  X  | X | X | X | X |   X   |  X  |  X  |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| USB              |       |   |   | X |     |     |   |   |   | X |       |     |     |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| USB Device Audio |       |   |   |   |     |     |   |   |   |   |       |     |     |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| USB Device Bulk  |       |   |   | X |     |     |   |   |   | X |       |     |     |
+------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+


**DSP devices - OMAP-L13x, C674x**

+----------------+-------------------+-------------+----------------+
|    Feature     |   Platform/SOC    |OMAP-L137 EVM| OMAP-L138 EVM  |
+================+=========+=========+=============+=======+========+
|                |OMAP-L137|OMAP-L138| L137/6747 SK|LCDK138|LCDK6748|
+----------------+---------+---------+-------------+-------+--------+
|CSL             |    X    |    X    |      X      |   X   |   X    |
+----------------+---------+---------+-------------+-------+--------+
|EDMA3           |    X    |    X    |      X      |   X   |   X    |
+----------------+---------+---------+-------------+-------+--------+
|EMAC            |    X    |    X    |      X      |   X   |   X    |
+----------------+---------+---------+-------------+-------+--------+
|GPIO            |    X    |    X    |      X      |   X   |   X    |
+----------------+---------+---------+-------------+-------+--------+
|I2C             |    X    |    X    |      X      |   X   |   X    |
+----------------+---------+---------+-------------+-------+--------+
|McASP           |    X    |    X    |      X      |   X   |   X    |
+----------------+---------+---------+-------------+-------+--------+
|MMC-SD          |    X    |    X    |      X      |   X   |   X    |
+----------------+---------+---------+-------------+-------+--------+
|SPI             |    X    |    X    |      X      |   X   |   X    |
+----------------+---------+---------+-------------+-------+--------+
|UART            |    X    |    X    |      X      |   X   |   X    |
+----------------+---------+---------+-------------+-------+--------+
|USB             |    X    |    X    |      X      |   X   |   X    |
+----------------+---------+---------+-------------+-------+--------+
|USB Device Audio|    X    |    X    |      X      |   X   |   X    |
+----------------+---------+---------+-------------+-------+--------+
|USB Device Bulk |    X    |    X    |      X      |   X   |   X    |
+----------------+---------+---------+-------------+-------+--------+

**Unsupported Features**

- In general driver support is available across all cores within an SOC
  with following exceptions

+----------------+-------------------+
|    Feature     | Not supported     |
+================+=========+=========+
|                |SOC      |CPU/Core |
+----------------+---------+---------+
|McASP           |  AM57x  |    M4   |
+----------------+---------+---------+
|USB             |  AM57x  |    C66x |
+----------------+---------+---------+
|USB             |  AM57x  |    M4   |
+----------------+---------+---------+
|USB             |  K2G    |    C66x |
+----------------+---------+---------+
|McBSP           |  K2G    |    A15  |
+----------------+---------+---------+
|McBSP           |OMAP-L13x|    ARM9 |
+----------------+---------+---------+
|All Drivers     | K2E/L/K |    A15  |
+----------------+---------+---------+

Other Features
--------------

The following table shows other feature availability per platform and
EVM:

**Sitara devices**

+----------------------------+--------------------------------+---------------+-----------+-----------+-----------+ -----------+
|          Feature           |    Platform/SOC                |   AM335x EVM  |AM437x EVM | AM57x EVM | AM65x EVM |  J721E EVM |
+============================+=======+======+=====+=====+=====+===+===+===+===+===+===+===+=====+=====+=====+=====+============+
|                            |AM335x |AM437x|AM57x|AM65x|J721E|GP |ICE|SK |BBB|GP |IDK|SK | GP  | IDK | GP  | IDK |  GP        |
+----------------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+ -----------+
| Board Support              |   X   |  X   |  X  |  X  |  X  | X | X | X | X | X | X | X |  X  |  X  |  X  |  X  |   X        |
+----------------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+ -----------+
| Boot (SBL)                 |   X   |  X   |  X  |  X  |  X  | X | X | X | X | X | X | X |  X  |  X  |  X  |  X  |   X        |
+----------------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+ -----------+
| Diagnostics                |   X   |  X   |  X  |  X  |  X  | X |   |   |   | X |   |   |  X  |  X  |  X  |  X  |   X        |
+----------------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+ -----------+
| FATFS                      |   X   |  X   |  X  |  X  |  X  | X | X |   |   | X | X |   |  X  |  X  |  X  |  X  |   X        |
+----------------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+ -----------+
| NDK-NIMU(CPSW)             |   X   |  X   |  X  |  X  |  X  | X | X | X | X | X | X | X |  X  |  X  |  X  |  X  |   X        |
+----------------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+ -----------+
| NDK-NIMU(ICSS)             |   X   |  X   |  X  |  X  |  X  |   | X |   |   |   | X |   |     |  X  |  X  |  X  |   X        |
+----------------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+ -----------+
|CC-LINK IE Field Basic(CPSW)|   X   |  X   |  X  |     |     | X | X | X | X | X | X | X |  X  |  X  |     |     |            |
+----------------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+ -----------+
|CC-Link IE Field Basic(ICSS)|   X   |  X   |  X  |     |     |   | X |   |   |   | X |   |     |  X  |     |     |            |
+----------------------------+-------+------+-----+-----+-----+---+---+---+---+---+---+---+-----+-----+-----+-----+ -----------+

**DSP devices - K2x, C66x**

+----------------------------+-------------------------------+-----------------------+-----------+
|          Feature           |         Platform/SOC          |        K2 EVM         | C66x EVM  |
+============================+=======+===+===+===+=====+=====+===+===+===+===+=======+=====+=====+
|                            |K2H/K2K|K2E|K2L|K2G|C665x|C667x|K2H|K2E|K2L|K2G|K2G-ICE|C665x|C667x|
+----------------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| Board Support              |   X   | X | X | X |  X  |  X  | X | X | X | X |   X   |  X  |  X  |
+----------------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| Boot (IBL/SBL)             |   X   | X | X | X |  X  |  X  | X | X | X | X |   X   |  X  |  X  |
+----------------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| Diagnostics                |       |   |   | X |     |     |   |   |   | X |   X   |     |     |
+----------------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| FATFS                      |       |   |   | X |     |     |   |   |   | X |   X   |     |     |
+----------------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| Fault Management           |   X   | X | X |   |     |     | X | X | X |   |       |     |     |
+----------------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| IPC Transport (QMSS)       |   X   | X | X |   |  X  |  X  | X | X | X |   |       |  X  |  X  |
+----------------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| IPC Transport (SRIO)       |   X   |   |   |   |  X  |  X  | X |   |   |   |       |  X  |  X  |
+----------------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| MAD-UTIL                   |       |   |   |   |  X  |  X  |   |   |   |   |       |  X  |  X  |
+----------------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| Network (CPSW)             |   X   | X | X | X |  X  |  X  | X | X | X | X |   X   |  X  |  X  |
+----------------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| Network (ICSS)             |       |   |   | X |     |     |   |   |   | X |       |     |     |
+----------------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
|CC-Link IE Field Basic(ICSS)|       |   |   | X |     |     |   |   |   | X |       |     |     |
+----------------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
|Platform Library (obsolete) |   X   | X | X |   |  X  |  X  | X | X | X |   |       |  X  |  X  |
+----------------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| PKTLIB                     |   X   | X | X |   |     |  X  | X | X | X |   |       |     |  X  |
+----------------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| POST                       |   X   | X | X |   |  X  |  X  | X | X | X |   |       |  X  |  X  |
+----------------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| SERDES Diagnostics         |   X   | X | X |   |     |     | X | X | X |   |       |     |     |
+----------------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+
| Trace Framework            |   X   | X | X |   |     |     | X | X | X |   |       |     |     |
+----------------------------+-------+---+---+---+-----+-----+---+---+---+---+-------+-----+-----+


**DSP devices - OMAP-L13x, C674x**

+--------------+-------------------+-------------+----------------+
|   Feature    |   Platform/SOC    |OMAP-L137 EVM| OMAP-L138 EVM  |
+==============+=========+=========+=============+=======+========+
|              |OMAP-L137|OMAP-L138| 137/6747 SK |LCDK138|LCDK6748|
+--------------+---------+---------+-------------+-------+--------+
|Board Support |    X    |    X    |      X      |   X   |   X    |
+--------------+---------+---------+-------------+-------+--------+
|Boot (SBL)    |    X    |    X    |      X      |   X   |   X    |
+--------------+---------+---------+-------------+-------+--------+
|Diagnostics   |    X    |         |      X      |       |        |
+--------------+---------+---------+-------------+-------+--------+
|FATFS         |    X    |    X    |      X      |   X   |   X    |
+--------------+---------+---------+-------------+-------+--------+
|Network (CPSW)|    X    |    X    |      X      |   X   |   X    |
+--------------+---------+---------+-------------+-------+--------+

Installation and Usage
======================

The :ref:`Getting Started Guide <Processor-SDK-RTOS-Getting-Started-Guide-label>` provides
instructions on how to setup up your development environment, install
the SDK and start your development.

To uninstall the SDK, remove the individual component directories from
the installed path. This is safe to do even in Windows since these
components do not modify the Windows registry.

|

Technical Support and Product Updates
=====================================

For further information or to report any problems, contact:
-  `TI E2E Processor Support <https://e2e.ti.com/support/processors/>`__ for all supported platforms


|

Archived
========
-  `Processor-SDK RTOS
   6.1.0 <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/06_01_00_08/rtos/Release_Specific.html#processor-sdk-rtos-release-notes>`__
-  `Processor-SDK RTOS
   6.0.0 <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/06_00_00_07/rtos/Release_Specific.html#processor-sdk-rtos-release-notes>`__
-  `Processor-SDK RTOS
   5.3.0 <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/05_03_00_07/rtos/Release_Specific.html#processor-sdk-rtos-release-notes>`__
-  `Processor-SDK RTOS
   5.2.0 <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/05_02_00_10/rtos/Release_Specific.html#processor-sdk-rtos-release-notes>`__
-  `Processor-SDK RTOS
   5.1.0 <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/05_01_00_11/rtos/Release_Specific.html#processor-sdk-rtos-release-notes>`__
-  `Processor-SDK RTOS
   5.0.0 <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/05_00_00_15/rtos/Release_Specific.html#processor-sdk-rtos-release-notes>`__
-  `Processor-SDK RTOS
   5.0.0 AM65x EA Release <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/05_00_00_09/rtos/Release_Specific.html#processor-sdk-rtos-release-notes>`__
-  `Processor-SDK RTOS
   4.3.0 <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/04_03_00_05/rtos/Release_Specific.html#processor-sdk-rtos-release-notes>`__

**Note:** Release Notes prior to 4.3 are not archived. Please see the
:ref:`Migration Guide <RTOS-SDK-Migration-Guide-label>` for information on
migration from these releases.

