.. _build_sheet:

====================
Software Build Sheet
====================

Build Sheet of supported features and modules for this |__SDK_FULL_NAME__| Release.
The following table lists the supported features and modules with the support status
for Linux on A53. Please refer to `RTOS Build Sheet <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62DX/11_01_00_16/exports/docs/build_sheet/am62d-sw-buildsheet.html>`__
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
   ,QSPI Bootloader Operation,NOR,No
   ,,NAND,No
   ,OSPI Bootloader Operation,NOR,No
   ,,NAND (1-bit mode),No
   ,,NAND (8-bit mode),No
   ,GPMC Bootloader Operation,NOR,No
   ,,NAND,No
   ,Ethernet Bootloader Operation,,No
   ,USB Bootloader Operation,Host,No
   ,,Device,Yes
   ,MMCSD Bootloader Operation,SD Card (no UHS),Yes
   ,,eMMC,Yes
   ,UART Bootloader Operation,,Yes
   Device Configuration,Power Supply Modules,POK,No
   ,,POR,No
   ,,PRG,No
   ,,PGD,No
   ,,VTM,Yes
   Power Management,Deep Sleep Low Power Mode  ,,No
   ,Deep Sleep LPM Wakeup Events,RTC Timer,No
   ,,GT Timers,No
   ,,WKUP UART,No
   ,,I2C,No
   ,,MCU GPIO,No
   ,,I/O Daisy Chain,No
   ,,USB Connect/Disconnect,No
   ,,USB Remote Wakeup,No
   ,MCU-Only Low Power Mode,,No
   ,Standby Low Power Mode,,No
   ,Partial I/O Low Power Mode,,No
   ,IO + DDR low power mode,,No
   ,Boot-time OPP configurations,,No
   ,Runtime Power Management,,No
   ,DFS/CPUFreq,,No
   ,CPUIdle (A53 WFI),,No
   ,CPUIdle (DDR in Self-Refresh),,No
   Interprocessor Communication,Mailbox,,Yes
   ,Spinlock,,No
   Memory Controllers,DDR Subsystem (DDRSS),DDR4,Yes
   ,,LPDDR4,Yes
   ,,Inline ECC (1bit err),No
   ,,Inline ECC (mbit err),No
   ,Region-based Address Translation,,No
   Time Sync,Time Sync Module (CPTS),,No
   ,Timer MaNAger,,No
   ,Time Sync and Compare Events,,No
   Data Movement Architecture (DMA),Data Movement Subsystem (DMSS),,No
   ,Peripheral DMA (PDMA),,Yes
   ,RingAcc,,Yes
   ,BCDMA,,Yes
   ,DRU,,NA
   ,Packet Streaming Interface Link,,Yes
   General Connectivity Peripherals (MAIN domain),Multichannel Audio Serial Port (McASP),Input,No
   ,,Output,Yes
   ,,HDMI Output,NA
   ,General-Purpose Interface (GPIO),,Yes
   ,Inter-Integrated Circuit (I2C),Controller,Yes
   ,,Target,No
   ,Multichannel Serial Peripheral Interface (McSPI),Controller,No
   ,,Peripheral,No
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes
   ,,RS-485,No
   ,,IrDA,No
   General Connectivity Peripherals (MCU domain),General-Purpose Interface (GPIO),,No
   ,Inter-Integrated Circuit (I2C),Controller,No
   ,,Target,No
   ,Multichannel Serial Peripheral Interface (McSPI),Controller,No
   ,,Peripheral,No
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes
   ,,RS-485,No
   ,,IrDA,No
   General Connectivity Peripherals (WKUP domain),Inter-Integrated Circuit (I2C),Controller,No
   ,,Target,No
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes
   ,,RS-485,No
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
   ,Quad Serial Peripheral Interface (QSPI),NOR,No
   ,,NAND,No
   ,Octal Serial Peripheral Interface (OSPI),NOR,No
   ,,NAND,No
   ,Expanded Serial Peripheral Interface (xSPI),,No
   ,General-Purpose Memory Controller (GPMC),FPGA,No
   ,,NAND,No
   ,,NOR,No
   ,,etc.,No
   ,Error Location Module (ELM),,No
   ,Multimedia Card Secure Digital (MMCSD) Interface,SD Card,Yes
   ,,eMMC,Yes
   Industrial & Control Interfaces,Controller Area Network (MCAN) - MAIN domain,CAN,No
   ,,CAN FD,No
   ,Controller Area Network (MCAN) - MCU domain,CAN,No
   ,,CAN FD,No
   ,Enhanced Capture (ECAP) Module,Capture,No
   ,,PWM,No
   ,Enhanced Pulse Width Modulation (EPWM) Module,,No
   ,Enhanced Quadrature Encoder Pulse (EQEP) Module,,No
   Camera Subsystem,Camera Streaming Interface Receiver (CSI_RX_IF),,NA
   ,MIPI D-PHY Receiver (DPHY_RX),,NA
   ,Multiple Camera,,NA
   ,OV2312 RGB + IR sensor,,NA
   ,iMX219 sensor,,NA
   Timer Modules,Global Timebase Cunter (GTC),,Yes
   ,Windowed Watchdog Timer (WWDT) - MAIN domain,,Yes
   ,Windowed Watchdog Timer (WWDT) - MCU domain,,NA
   ,Windowed Watchdog Timer (WWDT) - WKUP domain,,NA
   ,Real-Time Clock (RTC),,No
   ,Timers - MAIN domain,Timer,No
   ,,Capture,No
   ,,Compare,No
   ,,PWM,Yes
   ,Timers - MCU domain,Timer,No
   ,,Capture,No
   ,,Compare,No
   ,,PWM,No
   ,Timers - WKUP domain,Timer,No
   ,,Capture,No
   ,,Compare,No
   ,,PWM,No
   Internal Diagnostics Modules,Dual Clock Comparator (DCC),,No
   ,Error Signalling Module (ESM),,No
   ,Memory Cyclic Redundancy Check (MCRC) Controller,,No
   ,SDL Driver Porting Layer(SDL DPL),,No
   ,RTI(WWDG),,No
   ,Voltage and Thermal Management(VTM),,No
   ,Interconnect Isolation Gasket(STOG),,No
   ,Interconnect Isolation Gasket(MTOG),,No
   ,Power OK(POK),,No
   ,PBIST(Built In Self Test),,No
   ,ECC Aggregator,,No
   DISPLAY Subsystem,Open LVDS Display Interface Transmitter (OLDITX),,No
   ,DISPLAY Parallel Interface (DPI),,NA
   ,Dual Display,,NA
   Video Processing Unit,,,NA
   Image Encoder,JPEG Encoder E5010,,NA
   On-Die Temperature sensor,,,Yes
   On-Chip Debug,,,Yes
   Crypto Accelerator (SA3UL),Advanced Encryption Standard (AES),AES-CBC,Yes
   ,,AES-ECB,Yes
   ,SHA/MD5 Crypto Hardware-Accelerated Module (SHA/MD5),SHA-256,Yes
   ,,SHA-512,Yes
   ,True Random Number Generator (TRNG),,No
   ISP (Image SigNAl Processing),Hardware accelerated ISP for RGB and IR,,NA
   Deep Learning,Hardware accelerated deep learning,,NA
   Board Specific (AM62D EVM),Audio Codec,DAC,Yes
   ,,ADC,No
