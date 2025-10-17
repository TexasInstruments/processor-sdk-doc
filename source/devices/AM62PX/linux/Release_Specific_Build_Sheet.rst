.. _build_sheet:

====================
Software Build Sheet
====================

Build Sheet of supported features and modules for this |__SDK_FULL_NAME__| Release.
The following table lists the supported features and modules with the support status
for Linux on A53. Please refer to `RTOS Build Sheet <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62PX/11_01_01_08/exports/docs/build_sheet/am62p-sw-buildsheet.html>`__
for the supported features and modules on RTOS.

The support status is indicated by the following codes:

   - "Yes": The feature or module is supported.
   - "No": The feature or module is not supported.
   - "SDKx.y": The feature or module will be supported in a future version of the SDK.
   - "NA": The feature or module is not applicable in the hardware.
   - "ANY": The feature or module is a new update in this revision of the SDK.

.. csv-table:: Software Build Sheet
   :header: "Category", "Module", "SubModule", "Linux on A53"
   :widths: 20, 20, 20, 20

   System Interconnect,Bandwidth regulator,,No
   ,CBASS auto-clock gating,,No
   Initialization,I2C Bootloader Operation,,No
   ,SPI Bootloader Operation,,No
   ,QSPI Bootloader Operation,NOR,Yes
   ,,NAND,No
   ,OSPI Bootloader Operation,NOR,Yes
   ,,NAND (1-bit mode),No
   ,,NAND (8-bit mode),No
   ,GPMC Bootloader Operation,NOR,No
   ,,NAND,No
   ,Ethernet Bootloader Operation,,No
   ,USB Bootloader Operation,Host,Yes
   ,,Device,Yes
   ,MMCSD Bootloader Operation,SD Card (no UHS),Yes
   ,,eMMC,Yes
   ,UART Bootloader Operation,,Yes
   Device Configuration,Power Supply Modules,POK,No
   ,,POR,No
   ,,PRG,No
   ,,PGD,No
   ,,VTM,Yes
   Power Management,Deep Sleep Low Power Mode,,Yes
   ,Deep Sleep LPM Wakeup Events,RTC Timer,Yes
   ,,GT Timers,No
   ,,WKUP UART,Yes
   ,,I2C,No
   ,,MCU GPIO,Yes
   ,,I/O Daisy Chain,Yes
   ,,USB Connect/Disconnect,Yes
   ,,USB Remote Wakeup,Yes
   ,MCU-Only Low Power Mode,,Yes
   ,Standby Low Power Mode,,SDK11.1
   ,IO + DDR Low power mode,,Yes
   ,Partial I/O Low Power Mode,,Yes
   ,Boot-time OPP configurations,,Yes
   ,Runtime Power Management,,Yes
   ,DFS/CPUFreq,,Yes
   ,CPUIdle (A53 WFI),,Yes
   ,CPUIdle (DDR in Self-Refresh),,No
   Processors & Accelerators,Programmable Real-Time Unit and Industrial,General PRU Use,NA
   ,Communication Subsystem (PRUSS-M),,
   ,,Industrial Protocols,NA
   Interprocessor Communication,Mailbox,,Yes
   ,Spinlock,,Yes
   Memory Controllers,DDR Subsystem (DDRSS),DDR4,NA
   ,,LPDDR4,Yes
   ,,Inline ECC (1bit err),Yes
   ,,Inline ECC (mbit err),Yes
   ,Region-based Address Translation,,No
   Time Sync,Time Sync Module (CPTS),,Yes
   ,Timer Manager,,No
   ,Time Sync and Compare Events,,No
   Data Movement Architecture (DMA),Data Movement Subsystem (DMSS),,Yes
   ,Peripheral DMA (PDMA),,Yes
   ,RingAcc,,Yes
   ,BCDMA,,Yes
   ,Packet Streaming Interface Link,,Yes
   General Connectivity Peripherals (MAIN domain),Multichannel Audio Serial Port (McASP),Input,Yes
   ,,Output,Yes
   ,,HDMI Output,Yes
   ,General-Purpose Interface (GPIO),,Yes
   ,Inter-Integrated Circuit (I2C),Controller,Yes
   ,,Target,No
   ,Multichannel Serial Peripheral Interface (McSPI),Controller,Yes
   ,,Peripheral,No
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes
   ,,RS-485,Yes
   ,,IrDA,No
   General Connectivity Peripherals (MCU domain),General-Purpose Interface (GPIO),,Yes
   ,Inter-Integrated Circuit (I2C),Controller,Yes
   ,,Target,No
   ,Multichannel Serial Peripheral Interface (McSPI),Controller,Yes
   ,,Peripheral,No
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes
   ,,RS-485,Yes
   ,,IrDA,No
   "General Connectivity Peripherals
   (WKUP domain)",Inter-Integrated Circuit (I2C),Controller,Yes
   ,,Target,No
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes
   ,,RS-485,Yes
   ,,IrDA,No
   High-speed Serial Interfaces,Gigabit Ethernet Switch (CPSW3G),Switch,Yes
   ,,EndPoint,Yes
   ,,TSN,Yes
   ,,TSN - VLAN,Yes
   ,Universal Serial Bus Subsystem (USBSS),Host 3.1,NA
   ,,Device 3.1,NA
   ,,Host 2.0,Yes
   ,,Device 2.0,Yes
   Memory Interfaces,Flash Subsystem (FSS),,No
   ,Quad Serial Peripheral Interface (QSPI),NOR,Yes
   ,,NAND,NA
   ,Octal Serial Peripheral Interface (OSPI),NOR,Yes
   ,,NAND,Yes
   ,Expanded Serial Peripheral Interface (xSPI),,Yes
   ,General-Purpose Memory Controller (GPMC),FPGA,No
   ,,NAND,Yes
   ,,NOR,No
   ,,etc.,No
   ,Error Location Module (ELM),,Yes
   ,Multimedia Card Secure Digital (MMCSD) Interface,SD Card,Yes
   ,,eMMC,Yes
   ,,eMMC HS400 mode,Yes (SR1.2 only)
   Industrial & Control Interfaces,Controller Area Network (MCAN) - MAIN domain,CAN,Yes
   ,,CAN FD,Yes
   ,Controller Area Network (MCAN) - MCU domain,CAN,Yes
   ,,CAN FD,Yes
   ,Enhanced Capture (ECAP) Module,Capture,Yes
   ,,PWM,Yes
   ,Enhanced Pulse Width Modulation (EPWM) Module,,Yes
   ,Enhanced Quadrature Encoder Pulse (EQEP) Module,,Yes
   Camera Subsystem,Camera Streaming Interface Receiver (CSI_RX_IF),,Yes
   ,MIPI D-PHY Receiver (DPHY_RX),,Yes
   ,Multiple Camera,,Yes
   Timer Modules,Global Timebase Cunter (GTC),,Yes
   ,Windowed Watchdog Timer (WWDT) - MAIN domain,,Yes
   ,Windowed Watchdog Timer (WWDT) - MCU domain,,NA
   ,Windowed Watchdog Timer (WWDT) - WKUP domain,,NA
   ,Real-Time Clock (RTC),,Yes
   ,Timers - MAIN domain,Timer,Yes
   ,,Capture,No
   ,,Compare,No
   ,,PWM,Yes
   ,Timers - MCU domain,Timer,No
   ,,Capture,No
   ,,Compare,No
   ,,PWM,No
   ,Timers - WKUP domain,Timer,Yes
   ,,Capture,No
   ,,Compare,No
   ,,PWM,No
   Internal Diagnostics Modules,Dual Clock Comparator (DCC),,No
   ,Error Signaling Module (ESM),,No
   ,Memory Cyclic Redundancy Check (MCRC) Controller,,No
   ,SDL Driver Porting Layer(SDL DPL),,No
   ,RTI(WWDG),,No
   ,Voltage and Thermal Management(VTM),,Yes
   ,Interconnect Isolation Gasket(STOG),,No
   ,Interconnect Isolation Gasket(MTOG),,No
   ,Power OK(POK),,No
   ,PBIST(Built In Self Test),,No
   ,ECC Aggregator,,No
   DISPLAY Subsystem,Open LVDS Display Interface Transmitter (OLDITX),,Yes
   ,DISPLAY Parallel Interface (DPI),,Yes
   ,DSI (display serial interface),,Yes
   ,Triple Display,,Yes
   Video Processing Unit,Cnm Wave521CL,,Yes
   Graphics Processing Unit,IMG BXS,,Yes
   On-Die Temperature sensor,,,Yes
   On-Chip Debug,,,Yes
   Crypto Accelerator (SA3UL),Advanced Encryption Standard (AES),AES-CBC,Yes
   ,,AES-ECB,Yes
   ,SHA/MD5 Crypto Hardware-Accelerated Module (SHA/MD5),SHA-256,Yes
   ,,SHA-512,Yes
   ,True Random Number Generator (TRNG),,SDK11.0
