.. _build_sheet:

====================
Software Build Sheet
====================

Build Sheet of supported features and modules for this |__SDK_FULL_NAME__| Release.
The following table lists the supported features and modules for the corresponding category,
along with the support status for Linux on A53, RTOS on MCU R5F, RTOS on WKUP R5, RTOS on C7X.

The support status is indicated by the following codes:

   - "Yes": The feature or module is supported.
   - "No": The feature or module is not supported.
   - "SDKx.y": The feature or module will be supported in a future version of the SDK.
   - "NA": The feature or module is not applicable in the hardware.
   - "ANY": The feature or module is a new update in this revision of the SDK.

.. csv-table:: Software Build Sheet
   :header: "Category", "Module", "SubModule", "Linux on A53", "RTOS on MCU R5F", "RTOS on WKUP R5", "RTOS on C7X"
   :widths: 20, 20, 20, 20, 20, 20, 20

   System Interconnect,Bandwidth regulator,,No,No,No,No
   ,CBASS auto-clock gating,,No,No,No,No
   Initialization,I2C Bootloader Operation,,No,No,No,No
   ,SPI Bootloader Operation,,No,No,No,No
   ,QSPI Bootloader Operation,NOR,No,NA,No,NA
   ,,NAND,No,NA,No,NA
   ,OSPI Bootloader Operation,NOR,No,NA,Yes,NA
   ,,NAND (1-bit mode),No,NA,No,NA
   ,,NAND (8-bit mode),No,NA,No,NA
   ,GPMC Bootloader Operation,NOR,No,NA,No,NA
   ,,NAND,No,NA,No,NA
   ,Ethernet Bootloader Operation,,No,NA,No,NA
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
   Power Management,Deep Sleep Low Power Mode  ,,No,NA,No,No
   ,Deep Sleep LPM Wakeup Events,RTC Timer,No,NA,No,No
   ,,GT Timers,No,NA,No,No
   ,,WKUP UART,No,NA,No,No
   ,,I2C,No,NA,No,No
   ,,MCU GPIO,No,NA,No,No
   ,,I/O Daisy Chain,No,NA,No,No
   ,,USB Connect/Disconnect,No,NA,No,No
   ,,USB Remote Wakeup,No,NA,No,No
   ,MCU-Only Low Power Mode,,No,NA,No,No
   ,Standby Low Power Mode,,No,NA,No,No
   ,Partial I/O Low Power Mode,,No,NA,No,No
   ,IO + DDR low power mode,,No,NA,No,No
   ,Boot-time OPP configurations,,No,No,No,No
   ,Runtime Power Management,,No,NA,No,No
   ,DFS/CPUFreq,,No,NA,No,No
   ,CPUIdle (A53 WFI),,No,NA,No,No
   ,CPUIdle (DDR in Self-Refresh),,No,NA,No,No
   Interprocessor Communication,Mailbox,,Yes,Yes,Yes,Yes
   ,Spinlock,,No,No,No,No
   Memory Controllers,DDR Subsystem (DDRSS),DDR4,Yes,No,No,No
   ,,LPDDR4,Yes,No,Yes,No
   ,,Inline ECC (1bit err),No,No,Yes,No
   ,,Inline ECC (mbit err),No,No,No,No
   ,Region-based Address Translation,,No,Yes,Yes,NA
   Time Sync,Time Sync Module (CPTS),,No,No,No,No
   ,Timer MaNAger,,No,No,No,No
   ,Time Sync and Compare Events,,No,No,No,No
   Data Movement Architecture (DMA),Data Movement Subsystem (DMSS),,No,Yes,Yes,Yes
   ,Peripheral DMA (PDMA),,Yes,No,No,No
   ,RingAcc,,Yes,No,No,No
   ,BCDMA,,Yes,Yes,Yes,Yes
   ,DRU,,NA,NA,NA,Yes
   ,Packet Streaming Interface Link,,Yes,No,No,No
   General Connectivity Peripherals (MAIN domain),Multichannel Audio Serial Port (McASP),Input,No,NA,No,Yes
   ,,Output,Yes,NA,No,Yes
   ,,HDMI Output,NA,NA,No,No
   ,General-Purpose Interface (GPIO),,Yes,Yes,Yes,Yes
   ,Inter-Integrated Circuit (I2C),Controller,Yes,Yes,Yes,Yes
   ,,Target,No,Yes,Yes,Yes
   ,Multichannel Serial Peripheral Interface (McSPI),Controller,No,Yes,No,No
   ,,Peripheral,No,Yes,No,No
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes,Yes,Yes,Yes
   ,,RS-485,No,NA,No,No
   ,,IrDA,No,NA,No,No
   General Connectivity Peripherals (MCU domain),General-Purpose Interface (GPIO),,No,Yes,Yes,No
   ,Inter-Integrated Circuit (I2C),Controller,No,Yes,Yes,Yes
   ,,Target,No,No,No,No
   ,Multichannel Serial Peripheral Interface (McSPI),Controller,No,Yes,No,No
   ,,Peripheral,No,No,No,No
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes,Yes,Yes,Yes
   ,,RS-485,No,No,No,No
   ,,IrDA,No,No,No,No
   General Connectivity Peripherals (WKUP domain),Inter-Integrated Circuit (I2C),Controller,No,Yes,Yes,No
   ,,Target,No,NA,No,No
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes,NA,Yes,No
   ,,RS-485,No,NA,No,No
   ,,IrDA,No,NA,No,No
   High-speed Serial Interfaces,Gigabit Ethernet Switch (CPSW3G),Switch,Yes,No,No,No
   ,,EndPoint,Yes,No,No,No
   ,,TSN,Yes,No,No,No
   ,,TSN - VLAN,Yes,No,No,No
   ,Universal Serial Bus Subsystem (USBSS),Host 3.1,NA,No,No,No
   ,,Device 3.1,NA,No,No,No
   ,,Host 2.0,Yes,No,No,No
   ,,Device 2.0,Yes,No,No,No
   Memory Interfaces,Flash Subsystem (FSS),,No,No,No,No
   ,Quad Serial Peripheral Interface (QSPI),NOR,No,No,No,No
   ,,NAND,No,No,No,No
   ,Octal Serial Peripheral Interface (OSPI),NOR,No,Yes,Yes,No
   ,,NAND,No,No,No,No
   ,Expanded Serial Peripheral Interface (xSPI),,No,No,No,No
   ,General-Purpose Memory Controller (GPMC),FPGA,No,No,No,No
   ,,NAND,No,No,No,No
   ,,NOR,No,No,No,No
   ,,etc.,No,No,No,No
   ,Error Location Module (ELM),,No,No,No,No
   ,Multimedia Card Secure Digital (MMCSD) Interface,SD Card,Yes,No,Yes,No
   ,,eMMC,Yes,No,Yes,No
   Industrial & Control Interfaces,Controller Area Network (MCAN) - MAIN domain,CAN,No,No,No,No
   ,,CAN FD,No,No,No,No
   ,Controller Area Network (MCAN) - MCU domain,CAN,No,Yes,No,No
   ,,CAN FD,No,Yes,No,No
   ,Enhanced Capture (ECAP) Module,Capture,No,No,No,No
   ,,PWM,No,No,No,Yes
   ,Enhanced Pulse Width Modulation (EPWM) Module,,No,No,No,Yes
   ,Enhanced Quadrature Encoder Pulse (EQEP) Module,,No,No,No,No
   Camera Subsystem,Camera Streaming Interface Receiver (CSI_RX_IF),,NA,NA,No,No
   ,MIPI D-PHY Receiver (DPHY_RX),,NA,NA,No,No
   ,Multiple Camera,,NA,NA,No,No
   ,OV2312 RGB + IR sensor,,NA,NA,No,No
   ,iMX219 sensor,,NA,NA,No,No
   Timer Modules,Global Timebase Cunter (GTC),,Yes,No,No,No
   ,Windowed Watchdog Timer (WWDT) - MAIN domain,,Yes,No,No,No
   ,Windowed Watchdog Timer (WWDT) - MCU domain,,NA,No,No,No
   ,Windowed Watchdog Timer (WWDT) - WKUP domain,,NA,No,No,No
   ,Real-Time Clock (RTC),,No,No,No,No
   ,Timers - MAIN domain,Timer,No,NA,Yes,Yes
   ,,Capture,No,NA,No,No
   ,,Compare,No,NA,No,No
   ,,PWM,Yes,NA,No,No
   ,Timers - MCU domain,Timer,No,Yes,No,No
   ,,Capture,No,No,No,No
   ,,Compare,No,No,No,No
   ,,PWM,No,No,No,No
   ,Timers - WKUP domain,Timer,No,NA,Yes,No
   ,,Capture,No,NA,No,No
   ,,Compare,No,NA,No,No
   ,,PWM,No,NA,No,No
   Internal Diagnostics Modules,Dual Clock Comparator (DCC),,No,Yes,No,No
   ,Error Signalling Module (ESM),,No,Yes,No,No
   ,Memory Cyclic Redundancy Check (MCRC) Controller,,No,Yes,No,No
   ,SDL Driver Porting Layer(SDL DPL),,No,Yes,No,No
   ,RTI(WWDG),,No,Yes,No,No
   ,Voltage and Thermal Management(VTM),,No,Yes,No,No
   ,Interconnect Isolation Gasket(STOG),,No,Yes,No,No
   ,Interconnect Isolation Gasket(MTOG),,No,Yes,No,No
   ,Power OK(POK),,No,Yes,No,No
   ,PBIST(Built In Self Test),,No,Yes,No,No
   ,ECC Aggregator,,No,Yes,No,No
   DISPLAY Subsystem,Open LVDS Display Interface Transmitter (OLDITX),,No,NA,No,No
   ,DISPLAY Parallel Interface (DPI),,NA,NA,No,No
   ,Dual Display,,NA,NA,NA,NA
   Video Processing Unit,,,NA,NA,No,No
   Image Encoder,JPEG Encoder E5010,,NA,,,
   On-Die Temperature sensor,,,Yes,NA,No,No
   On-Chip Debug,,,NA,NA,NA,NA
   Crypto Accelerator (SA3UL),Advanced Encryption Standard (AES),AES-CBC,Yes,NA,No,No
   ,,AES-ECB,Yes,NA,No,No
   ,SHA/MD5 Crypto Hardware-Accelerated Module (SHA/MD5),SHA-256,Yes,NA,No,No
   ,,SHA-512,Yes,NA,No,No
   ,True Random Number Generator (TRNG),,No,NA,No,No
   ISP (Image SigNAl Processing),Hardware accelerated ISP for RGB and IR,,NA,NA,No,No
   Deep Learning,Hardware accelerated deep learning,,NA,NA,No,No
   Board Specific (AM62D EVM),Audio Codec,DAC,Yes,NA,No,No
   ,,ADC,No,NA,No,No
