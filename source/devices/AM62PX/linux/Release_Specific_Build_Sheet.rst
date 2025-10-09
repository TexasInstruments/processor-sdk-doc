.. _build_sheet:

====================
Software Build Sheet
====================

Build Sheet of supported features and modules for this |__SDK_FULL_NAME__| Release.
The following table lists the supported features and modules for the corresponding category,
along with the support status for Linux on A53, RTOS on MCU R5F, RTOS on WKUP R5F.

The support status is indicated by the following codes:

   - "Yes": The feature or module is supported.
   - "No": The feature or module is not supported.
   - "SDKx.y": The feature or module will be supported in a future version of the SDK.
   - "NA": The feature or module is not applicable in the hardware.
   - "ANY": The feature or module is a new update in this revision of the SDK.

.. csv-table:: Software Build Sheet
   :header: "Category", "Module", "SubModule", "Linux on A53", "RTOS on MCU R5F", "RTOS on WKUP R5F"
   :widths: 20, 20, 20, 20, 20, 20

   System Interconnect,Bandwidth regulator,,No,No,No
   ,CBASS auto-clock gating,,No,No,No
   Initialization,I2C Bootloader Operation,,No,No,No
   ,SPI Bootloader Operation,,No,No,No
   ,QSPI Bootloader Operation,NOR,Yes,NA,No
   ,,NAND,No,NA,No
   ,OSPI Bootloader Operation,NOR,Yes,NA,Yes
   ,,NAND (1-bit mode),No,NA,No
   ,,NAND (8-bit mode),No,NA,No
   ,GPMC Bootloader Operation,NOR,No,NA,No
   ,,NAND,No,NA,No
   ,Ethernet Bootloader Operation,,No,NA,No
   ,USB Bootloader Operation,Host,Yes,NA,No
   ,,Device,Yes,NA,No
   ,MMCSD Bootloader Operation,SD Card (no UHS),Yes,NA,Yes
   ,,eMMC,Yes,NA,Yes
   ,UART Bootloader Operation,,Yes,NA,Yes
   Device Configuration,Power Supply Modules,POK,No,No,Yes
   ,,POR,No,No,No
   ,,PRG,No,No,No
   ,,PGD,No,No,No
   ,,VTM,Yes,Yes,Yes
   Power Management,Deep Sleep Low Power Mode,,Yes,NA,NA
   ,Deep Sleep LPM Wakeup Events,RTC Timer,Yes,NA,NA
   ,,GT Timers,No,NA,NA
   ,,WKUP UART,Yes,NA,NA
   ,,I2C,No,NA,NA
   ,,MCU GPIO,Yes,NA,NA
   ,,I/O Daisy Chain,Yes,NA,NA
   ,,USB Connect/Disconnect,Yes,NA,NA
   ,,USB Remote Wakeup,Yes,NA,NA
   ,MCU-Only Low Power Mode,,Yes,NA,NA
   ,Standby Low Power Mode,,SDK11.1,NA,NA
   ,IO + DDR Low power mode,,Yes,NA,NA
   ,Partial I/O Low Power Mode,,Yes,NA,NA
   ,Boot-time OPP configurations,,Yes,No,No
   ,Runtime Power Management,,Yes,NA,NA
   ,DFS/CPUFreq,,Yes,NA,NA
   ,CPUIdle (A53 WFI),,Yes,NA,NA
   ,CPUIdle (DDR in Self-Refresh),,No,NA,NA
   Processors & Accelerators,Programmable Real-Time Unit and Industrial,General PRU Use,NA,NA,NA
   ,Communication Subsystem (PRUSS-M),,,,
   ,,Industrial Protocols,NA,NA,NA
   Interprocessor Communication,Mailbox,,Yes,Yes,Yes
   ,Spinlock,,Yes,No,No
   Memory Controllers,DDR Subsystem (DDRSS),DDR4,NA,No,No
   ,,LPDDR4,Yes,No,Yes
   ,,Inline ECC (1bit err),Yes,No,Yes
   ,,Inline ECC (mbit err),Yes,No,Yes
   ,Region-based Address Translation,,No,Yes,Yes
   Time Sync,Time Sync Module (CPTS),,Yes,No,No
   ,Timer Manager,,No,No,No
   ,Time Sync and Compare Events,,No,No,No
   Data Movement Architecture (DMA),Data Movement Subsystem (DMSS),,Yes,Yes,Yes
   ,Peripheral DMA (PDMA),,Yes,No,No
   ,RingAcc,,Yes,Yes,Yes
   ,BCDMA,,Yes,Yes,Yes
   ,Packet Streaming Interface Link,,Yes,No,No
   General Connectivity Peripherals (MAIN domain),Multichannel Audio Serial Port (McASP),Input,Yes,NA,Yes
   ,,Output,Yes,NA,Yes
   ,,HDMI Output,Yes,NA,NA
   ,General-Purpose Interface (GPIO),,Yes,Yes,Yes
   ,Inter-Integrated Circuit (I2C),Controller,Yes,Yes,Yes
   ,,Target,No,Yes,Yes
   ,Multichannel Serial Peripheral Interface (McSPI),Controller,Yes,Yes,Yes
   ,,Peripheral,No,Yes,Yes
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes,Yes,Yes
   ,,RS-485,Yes,No,No
   ,,IrDA,No,No,No
   General Connectivity Peripherals (MCU domain),General-Purpose Interface (GPIO),,Yes,Yes,Yes
   ,Inter-Integrated Circuit (I2C),Controller,Yes,Yes,Yes
   ,,Target,No,Yes,Yes
   ,Multichannel Serial Peripheral Interface (McSPI),Controller,Yes,Yes,Yes
   ,,Peripheral,No,Yes,Yes
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes,Yes,Yes
   ,,RS-485,Yes,No,No
   ,,IrDA,No,No,No
   "General Connectivity Peripherals
   (WKUP domain)",Inter-Integrated Circuit (I2C),Controller,Yes,Yes,Yes
   ,,Target,No,Yes,Yes
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes,No,Yes
   ,,RS-485,Yes,No,No
   ,,IrDA,No,No,No
   High-speed Serial Interfaces,Gigabit Ethernet Switch (CPSW3G),Switch,Yes,No,No
   ,,EndPoint,Yes,No,No
   ,,TSN,Yes,No,No
   ,,TSN - VLAN,Yes,No,No
   ,Universal Serial Bus Subsystem (USBSS),Host 3.1,NA,No,No
   ,,Device 3.1,NA,No,No
   ,,Host 2.0,Yes,No,No
   ,,Device 2.0,Yes,No,No
   Memory Interfaces,Flash Subsystem (FSS),,No,No,No
   ,Quad Serial Peripheral Interface (QSPI),NOR,Yes,No,No
   ,,NAND,NA,No,No
   ,Octal Serial Peripheral Interface (OSPI),NOR,Yes,No,Yes
   ,,NAND,Yes,No,No
   ,Expanded Serial Peripheral Interface (xSPI),,Yes,No,No
   ,General-Purpose Memory Controller (GPMC),FPGA,No,No,No
   ,,NAND,Yes,No,No
   ,,NOR,No,No,No
   ,,etc.,No,No,No
   ,Error Location Module (ELM),,Yes,No,No
   ,Multimedia Card Secure Digital (MMCSD) Interface,SD Card,Yes,No,Yes
   ,,eMMC,Yes,Yes,Yes
   ,,eMMC HS400 mode,Yes (SR1.2 only),Yes,Yes
   Industrial & Control Interfaces,Controller Area Network (MCAN) - MAIN domain,CAN,Yes,No,Yes
   ,,CAN FD,Yes,No,Yes
   ,Controller Area Network (MCAN) - MCU domain,CAN,Yes,Yes,No
   ,,CAN FD,Yes,Yes,No
   ,Enhanced Capture (ECAP) Module,Capture,Yes,No,No
   ,,PWM,Yes,Yes,No
   ,Enhanced Pulse Width Modulation (EPWM) Module,,Yes,Yes,No
   ,Enhanced Quadrature Encoder Pulse (EQEP) Module,,Yes,No,No
   Camera Subsystem,Camera Streaming Interface Receiver (CSI_RX_IF),,Yes,NA,NA
   ,MIPI D-PHY Receiver (DPHY_RX),,Yes,NA,NA
   ,Multiple Camera,,Yes,NA,NA
   Timer Modules,Global Timebase Cunter (GTC),,Yes,No,Yes
   ,Windowed Watchdog Timer (WWDT) - MAIN domain,,Yes,No,No
   ,Windowed Watchdog Timer (WWDT) - MCU domain,,NA,No,No
   ,Windowed Watchdog Timer (WWDT) - WKUP domain,,NA,No,No
   ,Real-Time Clock (RTC),,Yes,Yes,No
   ,Timers - MAIN domain,Timer,Yes,NA,NA
   ,,Capture,No,NA,NA
   ,,Compare,No,NA,NA
   ,,PWM,Yes,NA,NA
   ,Timers - MCU domain,Timer,No,Yes,NA
   ,,Capture,No,No,NA
   ,,Compare,No,No,NA
   ,,PWM,No,No,NA
   ,Timers - WKUP domain,Timer,Yes,NA,Yes
   ,,Capture,No,NA,No
   ,,Compare,No,NA,No
   ,,PWM,No,NA,No
   Internal Diagnostics Modules,Dual Clock Comparator (DCC),,No,Yes,No
   ,Error Signaling Module (ESM),,No,Yes,No
   ,Memory Cyclic Redundancy Check (MCRC) Controller,,No,Yes,No
   ,SDL Driver Porting Layer(SDL DPL),,No,Yes,No
   ,RTI(WWDG),,No,Yes,No
   ,Voltage and Thermal Management(VTM),,Yes,Yes,No
   ,Interconnect Isolation Gasket(STOG),,No,Yes,No
   ,Interconnect Isolation Gasket(MTOG),,No,Yes,No
   ,Power OK(POK),,No,Yes,No
   ,PBIST(Built In Self Test),,No,Yes,No
   ,ECC Aggregator,,No,Yes,No
   DISPLAY Subsystem,Open LVDS Display Interface Transmitter (OLDITX),,Yes,NA,Yes
   ,DISPLAY Parallel Interface (DPI),,Yes,NA,Yes
   ,DSI (display serial interface),,Yes,NA,No
   ,Triple Display,,Yes,NA,No
   Video Processing Unit,Cnm Wave521CL,,Yes,,
   Graphics Processing Unit,IMG BXS,,Yes,NA,No
   On-Die Temperature sensor,,,Yes,NA,NA
   On-Chip Debug,,,NA,NA,NA
   Crypto Accelerator (SA3UL),Advanced Encryption Standard (AES),AES-CBC,Yes,NA,NA
   ,,AES-ECB,Yes,NA,NA
   ,SHA/MD5 Crypto Hardware-Accelerated Module (SHA/MD5),SHA-256,Yes,NA,NA
   ,,SHA-512,Yes,NA,NA
   ,True Random Number Generator (TRNG),,SDK11.0,NA,NA
