.. _build_sheet:

====================
Software Build Sheet
====================

Build Sheet of supported features and modules for this |__SDK_FULL_NAME__| Release.
The following table lists the supported features and modules for the corresponding category,
along with the support status for Linux on A53, RTOS on MCU M4, RTOS on WKUP R5F, and RTOS on A53.

The support status is indicated by the following codes:

   - "Yes": The feature or module is supported.
   - "No": The feature or module is not supported.
   - "SDKx.y": The feature or module will be supported in a future version of the SDK.
   - "NA": The feature or module is not applicable in the hardware.
   - "ANY": The feature or module is a new update in this revision of the SDK.

.. csv-table:: Software Build Sheet
   :header: "Category", "Module", "SubModule", "Linux on A53", "RTOS on MCU M4", "RTOS on WKUP R5F", "RTOS on A53"
   :widths: 20, 20, 20, 20, 20, 20, 20

   System Interconnect,Bandwidth regulator,,No,No,No,No
   ,CBASS auto-clock gating,,No,No,No,No
   Initialization,I2C Bootloader Operation,,No,No,No,No
   ,SPI Bootloader Operation,,No,No,No,No
   ,QSPI Bootloader Operation,NOR,Yes,NA,No,NA
   ,,NAND,No,NA,No,NA
   ,OSPI Bootloader Operation,NOR,Yes,NA,Yes,NA
   ,,NAND (1-bit mode),Yes,NA,No,NA
   ,,NAND (8-bit mode),Yes,NA,Yes,NA
   ,GPMC Bootloader Operation,NOR,No,NA,No,NA
   ,,NAND,Yes,NA,Yes,NA
   ,Ethernet Bootloader Operation,,Yes,NA,No,NA
   ,USB Bootloader Operation,Host,No,NA,No,NA
   ,,Device,Yes,NA,No,NA
   ,MMCSD Bootloader Operation,SD Card (no UHS),Yes,NA,No,NA
   ,,eMMC,Yes,NA,Yes,NA
   ,UART Bootloader Operation,,Yes,NA,Yes,NA
   Device Configuration,Power Supply Modules,POK,No,No,Yes,No
   ,,POR,No,No,No,No
   ,,PRG,No,No,No,No
   ,,PGD,No,No,No,No
   ,,VTM,Yes,Yes,Yes,No
   Power Management,Deep Sleep Low Power Mode,,Yes,NA,NA,No
   ,Deep Sleep LPM Wakeup Events,RTC Timer,Yes,NA,NA,No
   ,,GT Timers,No,NA,NA,No
   ,,WKUP UART,Yes,NA,NA,No
   ,,I2C,No,NA,NA,No
   ,,MCU GPIO,Yes,NA,NA,No
   ,,I/O Daisy Chain,Yes,NA,NA,No
   ,,USB Connect/Disconnect,Yes,NA,NA,No
   ,,USB Remote Wakeup,Yes,NA,NA,No
   ,MCU-Only Low Power Mode,,Yes,NA,NA,No
   ,Standby Low Power Mode,,SDK11.1,NA,NA,No
   ,Partial I/O Low Power Mode,,Yes,NA,NA,No
   ,Boot-time OPP configurations,,Yes,No,No,No
   ,Runtime Power Management,,Yes,NA,NA,No
   ,DFS/CPUFreq,,Yes,NA,NA,No
   ,CPUIdle (A53 WFI),,Yes,NA,NA,No
   ,CPUIdle (DDR in Self-Refresh),,No,NA,NA,No
   Processors & Accelerators,Programmable Real-Time Unit and Industrial,General PRU Use,Yes,NA,NA,No
   ,Communication Subsystem (PRUSS-M),,,,,
   ,,Industrial Protocols,NA,NA,NA,NA
   Interprocessor Communication,Mailbox,,Yes,Yes,Yes,Yes
   ,Spinlock,,Yes,No,No,Yes
   Memory Controllers,DDR Subsystem (DDRSS),DDR4,Yes,No,Yes,No
   ,,LPDDR4,Yes,No,Yes,No
   ,,Inline ECC (1bit err),Yes,No,Yes,No
   ,,Inline ECC (mbit err),Yes,No,Yes,No
   ,Region-based Address Translation,,No,Yes,Yes,No
   Time Sync,Time Sync Module (CPTS),,Yes,No,No,No
   ,Timer Manager,,No,No,No,No
   ,Time Sync and Compare Events,,No,No,No,No
   Data Movement Architecture (DMA),Data Movement Subsystem (DMSS),,Yes,No,Yes,Yes
   ,Peripheral DMA (PDMA),,Yes,No,Yes,Yes
   ,RingAcc,,Yes,No,Yes,Yes
   ,BCDMA,,Yes,No,Yes,Yes
   ,Packet Streaming Interface Link,,Yes,No,No,No
   General Connectivity Peripherals,Multichannel Audio Serial Port (McASP),Input,Yes,NA,NA,Yes
   (MAIN domain),,Output,Yes,NA,NA,Yes
   ,,HDMI Output,Yes,NA,NA,No
   ,General-Purpose Interface (GPIO),,Yes,Yes,Yes,Yes
   ,Inter-Integrated Circuit (I2C),Controller,Yes,Yes,Yes,Yes
   ,,Target,No,Yes,Yes,Yes
   ,Multichannel Serial Peripheral Interface (McSPI),Controller,Yes,Yes,Yes,Yes
   ,,Peripheral,No,NA,NA,No
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes,Yes,Yes,Yes
   ,,RS-485,Yes,NA,NA,No
   ,,IrDA,No,NA,NA,No
   General Connectivity Peripherals,General-Purpose Interface (GPIO),,Yes,Yes,Yes,Yes
   (MCU domain),Inter-Integrated Circuit (I2C),Controller,Yes,Yes,Yes,Yes
   ,,Target,No,No,No,No
   ,Multichannel Serial Peripheral Interface (McSPI),Controller,Yes,Yes,Yes,Yes
   ,,Peripheral,No,Yes,Yes,Yes
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes,Yes,Yes,Yes
   ,,RS-485,Yes,No,No,No
   ,,IrDA,No,No,No,No
   General Connectivity Peripherals,Inter-Integrated Circuit (I2C),Controller,Yes,Yes,Yes,Yes
   (WKUP domain),,Target,No,Yes,Yes,Yes
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes,NA,Yes,Yes
   ,,RS-485,Yes,NA,NA,No
   ,,IrDA,No,NA,NA,No
   High-speed Serial Interfaces,Gigabit Ethernet Switch (CPSW3G),Switch,Yes,No,No,No
   ,,EndPoint,Yes,No,No,No
   ,,TSN,Yes,No,No,No
   ,,TSN - VLAN,Yes,No,No,No
   ,Universal Serial Bus Subsystem (USBSS),Host 3.1,NA,NA,No,No
   ,,Device 3.1,NA,NA,No,No
   ,,Host 2.0,Yes,NA,No,No
   ,,Device 2.0,Yes,NA,No,No
   Memory Interfaces,Flash Subsystem (FSS),,No,NA,No,No
   ,Quad Serial Peripheral Interface (QSPI),NOR,Yes,NA,No,No
   ,,NAND,NA,NA,No,No
   ,Octal Serial Peripheral Interface (OSPI),NOR,Yes,NA,Yes,Yes
   ,,NAND,Yes,NA,Yes,Yes
   ,Expanded Serial Peripheral Interface (xSPI),,Yes,NA,No,No
   ,General-Purpose Memory Controller (GPMC),FPGA,No,NA,No,No
   ,,NAND,Yes,NA,Yes,Yes
   ,,NOR,No,NA,No,No
   ,,etc.,No,NA,No,No
   ,Error Location Module (ELM),,Yes,NA,No,No
   ,Multimedia Card Secure Digital (MMCSD) Interface,SD Card,Yes,NA,Yes,Yes
   ,,eMMC,Yes,NA,Yes,Yes
   Industrial & Control Interfaces,Controller Area Network (MCAN) - MAIN domain,CAN,Yes,NA,Yes,Yes
   ,,CAN FD,Yes,NA,Yes,Yes
   ,Controller Area Network (MCAN) - MCU domain,CAN,Yes,Yes,No,Yes
   ,,CAN FD,Yes,Yes,No,Yes
   ,Enhanced Capture (ECAP) Module,Capture,Yes,No,No,Yes
   ,,PWM,Yes,No,No,Yes
   ,Enhanced Pulse Width Modulation (EPWM) Module,,Yes,Yes,No,Yes
   ,Enhanced Quadrature Encoder Pulse (EQEP) Module,,Yes,No,No,Yes
   Camera Subsystem,Camera Streaming Interface Receiver (CSI_RX_IF),,Yes,NA,No,No
   ,MIPI D-PHY Receiver (DPHY_RX),,Yes,NA,No,No
   ,Multiple Camera,,Yes,NA,No,No
   Timer Modules,Global Timebase Counter (GTC),,Yes,No,Yes,Yes
   ,Windowed Watchdog Timer (WWDT) - MAIN domain,,Yes,No,No,Yes
   ,Windowed Watchdog Timer (WWDT) - MCU domain,,NA,No,No,NA
   ,Windowed Watchdog Timer (WWDT) - WKUP domain,,NA,No,No,NA
   ,Real-Time Clock (RTC),,Yes,No,No,Yes
   ,Timers - MAIN domain,Timer,Yes,NA,NA,Yes
   ,,Capture,No,NA,NA,No
   ,,Compare,No,NA,NA,No
   ,,PWM,Yes,NA,NA,No
   ,Timers - MCU domain,Timer,No,Yes,NA,No
   ,,Capture,No,No,NA,No
   ,,Compare,No,No,NA,No
   ,,PWM,No,No,NA,No
   ,Timers - WKUP domain,Timer,Yes,NA,Yes,No
   ,,Capture,No,NA,No,No
   ,,Compare,No,NA,No,No
   ,,PWM,No,NA,No,No
   Internal Diagnostic Modules,Dual Clock Comparator (DCC),,No,Yes,Yes,No
   ,Error Signaling Module (ESM),,No,Yes,Yes,No
   ,SDL Driver Porting Layer(SDL DPL),,No,Yes,Yes,No
   ,Memory Cyclic Redundancy Check (MCRC) Controller,,Yes,Yes,Yes,No
   ,RTI(WWDG),,No,Yes,Yes,No
   ,Voltage and Thermal Management(VTM),,No,Yes,Yes,No
   ,Interconnect Isolation Gasket(STOG),,No,Yes,Yes,No
   ,Interconnect Isolation Gasket(MTOG),,No,Yes,No,No
   ,Power OK(POK),,No,Yes,Yes,No
   ,PBIST(Built In Self Test),,No,Yes,Yes,No
   ,ECC Aggregator,,No,Yes,Yes,No
   DISPLAY Subsystem,Open LVDS Display Interface Transmitter (OLDITX),,Yes,No,No,No
   ,DISPLAY Parallel Interface (DPI),,Yes,No,No,No
   ,Dual Display,,Yes,No,No,No
   Graphics Processing Unit,,,Yes,NA,NA,No
   On-Die Temperature sensor,,,Yes,NA,NA,No
   On-Chip Debug,,,NA,NA,NA,NA
   Crypto Accelerator (SA3UL),Advanced Encryption Standard (AES),AES-CBC,Yes,NA,NA,No
   ,,AES-ECB,Yes,NA,NA,No
   ,SHA/MD5 Crypto Hardware-Accelerated Module (SHA/MD5),SHA-256,Yes,NA,NA,No
   ,,SHA-512,Yes,NA,NA,No
   ,True Random Number Generator (TRNG),,Yes,NA,NA,No
