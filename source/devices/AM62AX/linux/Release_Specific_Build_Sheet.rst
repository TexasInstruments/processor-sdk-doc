.. _build_sheet:

====================
Software Build Sheet
====================

Build Sheet of supported features and modules for this |__SDK_FULL_NAME__| Release.
The following table lists the supported features and modules for the corresponding category,
along with the support status for Linux on A53, RTOS on MCU R5F, RTOS on WKUP R5F and RTOS on C7X.

The support status is indicated by the following codes:

   - "Yes": The feature or module is supported.
   - "No": The feature or module is not supported.
   - "SDKx.y": The feature or module will be supported in a future version of the SDK.
   - "NA": The feature or module is not applicable in the hardware.
   - "ANY": The feature or module is a new update in this revision of the SDK.

.. csv-table:: Software Build Sheet
   :header: "Category", "Module", "SubModule", "Linux on A53", "RTOS on MCU R5F", "RTOS on WKUP R5F", "RTOS on C7X"
   :widths: 20, 20, 20, 20, 20, 20, 20

   System Interconnect,Bandwidth regulator,,No,No,No,No
   ,CBASS auto-clock gating,,No,No,No,No
   Initialization,I2C Bootloader Operation,,No,No,No,No
   ,SPI Bootloader Operation,,No,No,No,No
   ,QSPI Bootloader Operation,NOR,No,NA,No,NA
   ,,NAND,No,NA,No,NA
   ,OSPI Bootloader Operation,NOR,Yes,NA,Yes,NA
   ,,NAND (1-bit mode),Yes,NA,Yes,NA
   ,,NAND (8-bit mode),Yes,NA,Yes,NA
   ,GPMC Bootloader Operation,NOR,No,NA,No,NA
   ,,NAND,Yes,NA,No,NA
   ,Ethernet Bootloader Operation,,Yes,NA,No,NA
   ,USB Bootloader Operation,Host,No,NA,No,NA
   ,,Device,Yes,NA,No,NA
   ,MMCSD Bootloader Operation,SD Card (no UHS),Yes,NA,Yes,NA
   ,,eMMC,Yes,NA,Yes,NA
   ,UART Bootloader Operation,,Yes,NA,Yes,NA
   Device Configuration,Power Supply Modules,POK,No,No,No,No
   ,,POR,No,No,No,No
   ,,PRG,No,No,No,No
   ,,PGD,No,No,No,No
   ,,VTM,Yes,Yes,No,No
   Power MaNAgement,Deep Sleep Low Power Mode  ,,Yes,NA,No,No
   ,Deep Sleep LPM Wakeup Events,RTC Timer,Yes,NA,No,No
   ,,GT Timers,No,NA,No,No
   ,,WKUP UART,Yes,NA,No,No
   ,,I2C,No,NA,No,No
   ,,MCU GPIO,Yes,NA,No,No
   ,,I/O Daisy Chain,Yes,NA,No,No
   ,,USB Connect/Disconnect,Yes,NA,No,No
   ,,USB Remote Wakeup,Yes,NA,No,No
   ,MCU-Only Low Power Mode,,Yes,NA,No,No
   ,Standby Low Power Mode,,SDK11.1,NA,No,No
   ,Partial I/O Low Power Mode,,Yes,NA,No,No
   ,IO + DDR low power mode,,Yes,NA,No,No
   ,Boot-time OPP configurations,,Yes,No,No,No
   ,Runtime Power MaNAgement,,Yes,NA,No,No
   ,DFS/CPUFreq,,Yes,NA,No,No
   ,CPUIdle (A53 WFI),,Yes,NA,No,No
   ,CPUIdle (DDR in Self-Refresh),,No,NA,No,No
   Interprocessor Communication,Mailbox,,Yes,Yes,Yes,Yes
   ,Spinlock,,Yes,No,No,No
   Memory Controllers,DDR Subsystem (DDRSS),DDR4,Yes,No,No,No
   ,,LPDDR4,Yes,No,Yes,No
   ,,Inline ECC (1bit err),Yes,No,Yes,No
   ,,Inline ECC (mbit err),No,No,No,No
   ,Region-based Address Translation,,No,Yes,Yes,NA
   Time Sync,Time Sync Module (CPTS),,Yes,No,No,No
   ,Timer MaNAger,,No,No,No,No
   ,Time Sync and Compare Events,,No,No,No,No
   Data Movement Architecture (DMA),Data Movement Subsystem (DMSS),,Yes,Yes,Yes,Yes
   ,Peripheral DMA (PDMA),,Yes,No,No,No
   ,RingAcc,,Yes,No,No,No
   ,BCDMA,,Yes,Yes,Yes,Yes
   ,Packet Streaming Interface Link,,Yes,No,No,No
   General Connectivity Peripherals,Multichannel Audio Serial Port (McASP),Input,Yes,NA,Yes,Yes
   (MAIN domain),,Output,Yes,NA,Yes,Yes
   ,,HDMI Output,Yes,NA,No,No
   ,General-Purpose Interface (GPIO),,Yes,Yes,Yes,Yes
   ,Inter-Integrated Circuit (I2C),Controller,Yes,Yes,Yes,Yes
   ,,Target,No,Yes,Yes,Yes
   ,Multichannel Serial Peripheral Interface (McSPI),Controller,Yes,Yes,No,No
   ,,Peripheral,No,Yes,No,No
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes,Yes,Yes,Yes
   ,,RS-485,Yes,NA,No,No
   ,,IrDA,No,NA,No,No
   General Connectivity Peripherals,General-Purpose Interface (GPIO),,Yes,Yes,Yes,No
   (MCU domain),Inter-Integrated Circuit (I2C),Controller,Yes,Yes,Yes,Yes
   ,,Target,No,No,No,No
   ,Multichannel Serial Peripheral Interface (McSPI),Controller,Yes,Yes,No,No
   ,,Peripheral,No,No,No,No
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes,Yes,Yes,Yes
   ,,RS-485,Yes,No,No,No
   ,,IrDA,No,No,No,No
   General Connectivity Peripherals,Inter-Integrated Circuit (I2C),Controller,Yes,Yes,Yes,No
   (WKUP domain),,Target,No,NA,No,No
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes,NA,Yes,No
   ,,RS-485,Yes,NA,No,No
   ,,IrDA,No,NA,No,No
   High-speed Serial Interfaces,Gigabit Ethernet Switch (CPSW3G),Switch,Yes,No,No,No
   ,,EndPoint,Yes,No,No,No
   ,,TSN,Yes,No,No,No
   ,,TSN - VLAN,Yes,No,No,No
   ,Universal Serial Bus Subsystem (USBSS),Host 3.1,NA,NA,No,No
   ,,Device 3.1,NA,NA,No,No
   ,,Host 2.0,Yes,NA,No,No
   ,,Device 2.0,Yes,NA,No,No
   Memory Interfaces,Flash Subsystem (FSS),,No,NA,No,No
   ,Quad Serial Peripheral Interface (QSPI),NOR,No,NA,No,No
   ,,NAND,NA,NA,No,No
   ,Octal Serial Peripheral Interface (OSPI),NOR,Yes,NA,No,No
   ,,NAND,Yes,Yes,Yes,No
   ,Expanded Serial Peripheral Interface (xSPI),,Yes,NA,No,No
   ,General-Purpose Memory Controller (GPMC),FPGA,NA,NA,No,No
   ,,NAND,Yes,NA,No,No
   ,,NOR,No,NA,No,No
   ,,etc.,No,NA,No,No
   ,Error Location Module (ELM),,Yes,NA,No,No
   ,Multimedia Card Secure Digital (MMCSD) Interface,SD Card,Yes,NA,Yes,No
   ,,eMMC,Yes,NA,Yes,No
   Industrial & Control Interfaces,Controller Area Network (MCAN) - MAIN domain,CAN,Yes,NA,No,No
   ,,CAN FD,Yes,NA,No,No
   ,Controller Area Network (MCAN) - MCU domain,CAN,No,Yes,No,No
   ,,CAN FD,No,Yes,No,No
   ,Enhanced Capture (ECAP) Module,Capture,Yes,No,No,No
   ,,PWM,Yes,No,Yes,Yes
   ,Enhanced Pulse Width Modulation (EPWM) Module,,Yes,No,Yes,Yes
   ,Enhanced Quadrature Encoder Pulse (EQEP) Module,,No,No,No,No
   Camera Subsystem,Camera Streaming Interface Receiver (CSI_RX_IF),,Yes,NA,No,No
   ,MIPI D-PHY Receiver (DPHY_RX),,Yes,NA,No,No
   ,Multiple Camera,,Yes,NA,No,No
   ,OV2312 RGB + IR sensor,,Yes,NA,No,No
   ,iMX219 sensor,,Yes,NA,No,No
   Timer Modules,Global Timebase Cunter (GTC),,Yes,No,Yes,No
   ,Windowed Watchdog Timer (WWDT) - MAIN domain,,Yes,No,No,No
   ,Windowed Watchdog Timer (WWDT) - MCU domain,,NA,No,No,No
   ,Windowed Watchdog Timer (WWDT) - WKUP domain,,NA,No,No,No
   ,Real-Time Clock (RTC),,Yes,No,No,No
   ,Timers - MAIN domain,Timer,Yes,NA,No,Yes
   ,,Capture,No,NA,No,No
   ,,Compare,No,NA,No,No
   ,,PWM,Yes,NA,No,No
   ,Timers - MCU domain,Timer,No,Yes,No,No
   ,,Capture,No,No,No,No
   ,,Compare,No,No,No,No
   ,,PWM,No,No,No,No
   ,Timers - WKUP domain,Timer,Yes,NA,Yes,No
   ,,Capture,No,NA,No,No
   ,,Compare,No,NA,No,No
   ,,PWM,No,NA,No,No
   Internal Diagnostics Modules,Dual Clock Comparator (DCC),,No,Yes,No,No
   ,Error Signalling Module (ESM),,No,Yes,No,No
   ,Memory Cyclic Redundancy Check (MCRC) Controller,,Yes,Yes,No,No
   ,SDL Driver Porting Layer(SDL DPL),,No,Yes,No,No
   ,RTI(WWDG),,No,Yes,No,No
   ,Voltage and Thermal Management(VTM),,No,Yes,No,No
   ,Interconnect Isolation Gasket(STOG),,No,Yes,No,No
   ,Interconnect Isolation Gasket(MTOG),,No,Yes,No,No
   ,Power OK(POK),,No,Yes,No,No
   ,PBIST(Built In Self Test),,No,Yes,No,No
   ,ECC Aggregator,,No,Yes,No,No
   DISPLAY Subsystem,Open LVDS Display Interface Transmitter (OLDITX),,NA,NA,No,No
   ,DISPLAY Parallel Interface (DPI),,Yes,NA,No,No
   ,Dual Display,,NA,NA,NA,NA
   Video Processing Unit,,,Yes,NA,No,No
   Image Encoder,JPEG Encoder E5010,,Yes,,,
   On-Die Temperature sensor,,,Yes,NA,No,No
   On-Chip Debug,,,NA,NA,NA,NA
   Crypto Accelerator (SA3UL),Advanced Encryption Standard (AES),AES-CBC,Yes,NA,No,No
   ,,AES-ECB,Yes,NA,No,No
   ,SHA/MD5 Crypto Hardware-Accelerated Module (SHA/MD5),SHA-256,Yes,NA,No,No
   ,,SHA-512,Yes,NA,No,No
   ,True Random Number Generator (TRNG),,Yes,NA,No,No
   ISP (Image SigNAl Processing),Hardware accelerated ISP for RGB and IR,,Yes,NA,No,No
   Deep Learning,Hardware accelerated deep learning,,Yes,NA,No,No
