.. _build_sheet:

====================
Software Build Sheet
====================

Build Sheet of supported features and modules for this |__SDK_FULL_NAME__| Release.
The following table lists the supported features and modules for the corresponding category,
along with the support status for Linux on A53, RTOS on MCU R5F, RTOS on WKUP R5, RTOS on A53, RTOS on C7X.

The support status is indicated by the following codes:

   - "Yes": The feature or module is supported.
   - "No": The feature or module is not supported.
   - "SDKx.y": The feature or module will be supported in a future version of the SDK.
   - "NA": The feature or module is not applicable in the hardware.
   - "ANY": The feature or module is a new update in this revision of the SDK.

.. csv-table:: Software Build Sheet
   :header: "Category", "Module", "SubModule", "RTOS on MCU R5F", "RTOS on WKUP R5", "RTOS on A53", "RTOS on C7X"
   :widths: 20, 20, 20, 20, 20, 20, 20

   System Interconnect,Bandwidth regulator,,No,No,No,No
   ,CBASS auto-clock gating,,No,No,No,No
   Initialization,I2C Bootloader Operation,,No,No,No,No
   ,SPI Bootloader Operation,,No,No,No,No
   ,QSPI Bootloader Operation,NOR,NA,No,NA,NA
   ,,NAND,NA,No,NA,NA
   ,OSPI Bootloader Operation,NOR,NA,Yes,NA,NA
   ,,NAND (1-bit mode),NA,No,NA,NA
   ,,NAND (8-bit mode),NA,No,NA,NA
   ,GPMC Bootloader Operation,NOR,NA,No,NA,NA
   ,,NAND,NA,No,NA,NA
   ,Ethernet Bootloader Operation,,NA,No,NA,NA
   ,USB Bootloader Operation,Host,NA,No,NA,NA
   ,,Device,NA,No,NA,NA
   ,MMCSD Bootloader Operation,SD Card (no UHS),NA,Yes,NA,NA
   ,,eMMC,NA,Yes,NA,NA
   ,UART Bootloader Operation,,NA,Yes,NA,NA
   Device Configuration,Power Supply Modules,POK,No,No,No,No
   ,,POR,No,No,No,No
   ,,PRG,No,No,No,No
   ,,PGD,No,No,No,No
   ,,VTM,Yes,No,No,No
   Power MaNAgement,Deep Sleep Low Power Mode  ,,NA,No,No,No
   ,Deep Sleep LPM Wakeup Events,RTC Timer,NA,No,No,No
   ,,GT Timers,NA,No,No,No
   ,,WKUP UART,NA,No,No,No
   ,,I2C,NA,No,No,No
   ,,MCU GPIO,NA,No,No,No
   ,,I/O Daisy Chain,NA,No,No,No
   ,,USB Connect/Disconnect,NA,No,No,No
   ,,USB Remote Wakeup,NA,No,No,No
   ,MCU-Only Low Power Mode,,NA,No,No,No
   ,Standby Low Power Mode,,NA,No,No,No
   ,Partial I/O Low Power Mode,,NA,No,No,No
   ,IO + DDR low power mode,,NA,No,No,No
   ,Boot-time OPP configurations,,No,No,No,No
   ,Runtime Power MaNAgement,,NA,No,No,No
   ,DFS/CPUFreq,,NA,No,No,No
   ,CPUIdle (A53 WFI),,NA,No,No,No
   ,CPUIdle (DDR in Self-Refresh),,NA,No,No,No
   Interprocessor Communication,Mailbox,,Yes,Yes,Yes,Yes
   ,Spinlock,,No,No,No,No
   Memory Controllers,DDR Subsystem (DDRSS),DDR4,No,No,No,No
   ,,LPDDR4,No,Yes,No,No
   ,,Inline ECC (1bit err),No,Yes,No,No
   ,,Inline ECC (mbit err),No,No,No,No
   ,Region-based Address Translation,,Yes,Yes,NA,NA
   Time Sync,Time Sync Module (CPTS),,No,No,No,No
   ,Timer MaNAger,,No,No,No,No
   ,Time Sync and Compare Events,,No,No,No,No
   Data Movement Architecture (DMA),Data Movement Subsystem (DMSS),,Yes,Yes,Yes,Yes
   ,Peripheral DMA (PDMA),,No,No,No,No
   ,RingAcc,,No,No,No,No
   ,BCDMA,,Yes,Yes,Yes,Yes
   ,DRU,,NA,NA,NA,Yes
   ,Packet Streaming Interface Link,,No,No,No,No
   General Connectivity Peripherals (MAIN domain),Multichannel Audio Serial Port (McASP),Input,NA,No,Yes,Yes
   ,,Output,NA,No,Yes,Yes
   ,,HDMI Output,NA,No,No,No
   ,General-Purpose Interface (GPIO),,Yes,Yes,Yes,Yes
   ,Inter-Integrated Circuit (I2C),Controller,Yes,Yes,Yes,Yes
   ,,Target,Yes,Yes,Yes,Yes
   ,Multichannel Serial Peripheral Interface (McSPI),Controller,Yes,No,Yes,No
   ,,Peripheral,Yes,No,Yes,No
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes,Yes,Yes,Yes
   ,,RS-485,NA,No,No,No
   ,,IrDA,NA,No,No,No
   General Connectivity Peripherals (MCU domain),General-Purpose Interface (GPIO),,Yes,Yes,Yes,No
   ,Inter-Integrated Circuit (I2C),Controller,Yes,Yes,Yes,Yes
   ,,Target,No,No,No,No
   ,Multichannel Serial Peripheral Interface (McSPI),Controller,Yes,No,No,No
   ,,Peripheral,No,No,No,No
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes,Yes,Yes,Yes
   ,,RS-485,No,No,No,No
   ,,IrDA,No,No,No,No
   General Connectivity Peripherals (WKUP domain),Inter-Integrated Circuit (I2C),Controller,Yes,Yes,Yes,No
   ,,Target,NA,No,No,No
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,NA,Yes,No,No
   ,,RS-485,NA,No,No,No
   ,,IrDA,NA,No,No,No
   High-speed Serial Interfaces,Gigabit Ethernet Switch (CPSW3G),Switch,No,No,No,No
   ,,EndPoint,No,No,No,No
   ,,TSN,No,No,No,No
   ,,TSN - VLAN,No,No,No,No
   ,Universal Serial Bus Subsystem (USBSS),Host 3.1,No,No,No,No
   ,,Device 3.1,No,No,No,No
   ,,Host 2.0,No,No,No,No
   ,,Device 2.0,No,No,No,No
   Memory Interfaces,Flash Subsystem (FSS),,No,No,No,No
   ,Quad Serial Peripheral Interface (QSPI),NOR,No,No,No,No
   ,,NAND,No,No,No,No
   ,Octal Serial Peripheral Interface (OSPI),NOR,Yes,Yes,Yes,No
   ,,NAND,No,No,No,No
   ,Expanded Serial Peripheral Interface (xSPI),,No,No,No,No
   ,General-Purpose Memory Controller (GPMC),FPGA,No,No,No,No
   ,,NAND,No,No,No,No
   ,,NOR,No,No,No,No
   ,,etc.,No,No,No,No
   ,Error Location Module (ELM),,No,No,No,No
   ,Multimedia Card Secure Digital (MMCSD) Interface,SD Card,No,Yes,Yes,No
   ,,eMMC,No,Yes,Yes,No
   Industrial & Control Interfaces,Controller Area Network (MCAN) - MAIN domain,CAN,No,No,Yes,No
   ,,CAN FD,No,No,Yes,No
   ,Controller Area Network (MCAN) - MCU domain,CAN,Yes,No,No,No
   ,,CAN FD,Yes,No,No,No
   ,Enhanced Capture (ECAP) Module,Capture,No,No,No,No
   ,,PWM,No,No,Yes,Yes
   ,Enhanced Pulse Width Modulation (EPWM) Module,,No,No,Yes,Yes
   ,Enhanced Quadrature Encoder Pulse (EQEP) Module,,No,No,Yes,No
   Camera Subsystem,Camera Streaming Interface Receiver (CSI_RX_IF),,NA,No,No,No
   ,MIPI D-PHY Receiver (DPHY_RX),,NA,No,No,No
   ,Multiple Camera,,NA,No,No,No
   ,OV2312 RGB + IR sensor,,NA,No,No,No
   ,iMX219 sensor,,NA,No,No,No
   Timer Modules,Global Timebase Cunter (GTC),,No,No,No,No
   ,Windowed Watchdog Timer (WWDT) - MAIN domain,,No,No,Yes,No
   ,Windowed Watchdog Timer (WWDT) - MCU domain,,No,No,No,No
   ,Windowed Watchdog Timer (WWDT) - WKUP domain,,No,No,No,No
   ,Real-Time Clock (RTC),,No,Yes,No,No
   ,Timers - MAIN domain,Timer,NA,No,Yes,Yes
   ,,Capture,NA,No,No,No
   ,,Compare,NA,No,No,No
   ,,PWM,NA,No,No,No
   ,Timers - MCU domain,Timer,Yes,No,No,No
   ,,Capture,No,No,No,No
   ,,Compare,No,No,No,No
   ,,PWM,No,No,No,No
   ,Timers - WKUP domain,Timer,NA,Yes,No,No
   ,,Capture,NA,No,No,No
   ,,Compare,NA,No,No,No
   ,,PWM,NA,No,No,No
   Internal Diagnostics Modules,Dual Clock Comparator (DCC),,Yes,No,No,No
   ,Error Signalling Module (ESM),,Yes,No,No,No
   ,Memory Cyclic Redundancy Check (MCRC) Controller,,Yes,No,No,No
   ,SDL Driver Porting Layer(SDL DPL),,Yes,No,No,No
   ,RTI(WWDG),,Yes,No,No,No
   ,Voltage and Thermal Management(VTM),,Yes,No,No,No
   ,Interconnect Isolation Gasket(STOG),,Yes,No,No,No
   ,Interconnect Isolation Gasket(MTOG),,Yes,No,No,No
   ,Power OK(POK),,Yes,No,No,No
   ,PBIST(Built In Self Test),,Yes,No,No,No
   ,ECC Aggregator,,Yes,No,No,No
   DISPLAY Subsystem,Open LVDS Display Interface Transmitter (OLDITX),,NA,No,No,No
   ,DISPLAY Parallel Interface (DPI),,NA,No,No,No
   ,Dual Display,,NA,NA,NA,NA
   Video Processing Unit,,,NA,No,No,No
   Image Encoder,JPEG Encoder E5010,,,,,
   On-Die Temperature sensor,,,NA,No,No,No
   On-Chip Debug,,,NA,NA,NA,NA
   Crypto Accelerator (SA3UL),Advanced Encryption Standard (AES),AES-CBC,NA,No,Yes,No
   ,,AES-ECB,NA,No,Yes,No
   ,SHA/MD5 Crypto Hardware-Accelerated Module (SHA/MD5),SHA-256,NA,No,Yes,No
   ,,SHA-512,NA,No,Yes,No
   ,True Random Number Generator (TRNG),,NA,No,Yes,No
   ISP (Image SigNAl Processing),Hardware accelerated ISP for RGB and IR,,NA,No,No,No
   Deep Learning,Hardware accelerated deep learning,,NA,No,No,No
