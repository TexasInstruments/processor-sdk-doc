.. _build_sheet:

====================
Software Build Sheet
====================

Build Sheet of supported features and modules for this |__SDK_FULL_NAME__|
Release. The following table lists the supported features and modules with the support status
for Linux on A53. Please refer to `RTOS Build Sheet <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62LX/11_00_00_23/exports/docs/build_sheet/am62l-sw-buildsheet.html>`__
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

   Initialization,I2C Bootloader Operation,,No
   ,SPI Bootloader Operation,,No
   ,QSPI Bootloader Operation,NOR,Yes
   ,,NAND,No
   ,OSPI Bootloader Operation,NOR,Yes
   ,,NAND (1-bit mode),Yes
   ,,NAND (8-bit mode),Yes
   ,GPMC Bootloader Operation,NOR,No
   ,,NAND,No
   ,Ethernet Bootloader Operation,,NA
   ,USB Bootloader Operation,Host,No
   ,,Device,Yes
   ,MMC Bootloader Operation,SD Card,Yes
   ,,SD Card (UHS),Yes
   ,,eMMC,Yes
   ,,eMMC (UHS),Yes
   ,UART Bootloader Operation,,Yes
   Device Configuration,VTM,,Yes
   Power Management,Deep Sleep Low Power Mode,,Yes
   ,Deep Sleep LPM Wakeup Events,RTC Timer,Yes
   ,,GT Timers,No
   ,,I/O Daisy Chain,Yes
   ,,I2C,No
   ,,RTC,Yes
   ,,USB Connect/Disconnect,No
   ,,USB Remote Wakeup,Yes
   ,,WKUP UART,No
   ,Standby Low Power Mode,,Yes
   ,RTC Only,,SDK12.0
   ,RTC + DDR,,Yes
   ,Boot-time OPP configurations,,No
   ,Runtime Power Management,,Yes
   ,DFS/CPUFreq,,No
   ,CPUIdle (A53 WFI),,No
   ,CPUIdle (DDR in Self-Refresh),,No
   Interprocessor Communication,Mailbox,,Yes
   Memory Controllers,DDR Subsystem (DDRSS),DDR4,Yes
   ,,LPDDR4,Yes
   ,,Inline ECC (1bit err),No
   ,,Inline ECC (mbit err),No
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
   ,Analog to Digital Converter,ADC,Yes
   ,General-Purpose Interface (GPIO),,Yes
   ,Inter-Integrated Circuit (I2C),Controller,Yes
   ,,Target,No
   ,Multichannel Serial Peripheral Interface (McSPI),Controller,Yes
   ,,Peripheral,No
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes
   ,,RS-485,Yes
   ,,IrDA,No
   General Connectivity Peripherals (WKUP domain),General-Purpose Interface (GPIO),,Yes
   ,Inter-Integrated Circuit (I2C),Controller,Yes
   ,,Target,No
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes
   ,,RS-485,Yes
   ,,IrDA,No
   High-speed Serial Interfaces,Gigabit Ethernet Switch (CPSW3G),Switch,Yes
   ,,EndPoint,Yes
   ,,TSN,Yes
   ,,TSN - VLAN,Yes
   Universal Serial Bus Subsystem (USBSS),SuperSpeed+ (3.1),Host,NA
   ,,Device,NA
   ,High-Speed (2.0),Host,Yes
   ,,Device,Yes
   Memory Interfaces,Flash Subsystem (FSS),,No
   ,Quad Serial Peripheral Interface (QSPI),NOR,Yes
   ,,NAND,NA
   ,Octal Serial Peripheral Interface (OSPI),NOR,Yes
   ,,NAND,Yes
   ,Expanded Serial Peripheral Interface (xSPI),,Yes
   ,General-Purpose Memory Controller (GPMC),FPGA,No
   ,,NAND,Yes
   ,,NOR,No
   ,,PSRAM,No
   ,Error Location Module (ELM),,Yes
   ,Multimedia Card Secure Digital (MMCSD) Interface,SD Card,Yes
   ,,eMMC,Yes
   Industrial & Control Interfaces,Controller Area Network (MCAN) - MAIN domain,CAN,Yes
   ,,CAN FD,Yes
   ,Enhanced Capture (ECAP) Module,Capture,Yes
   ,,PWM,Yes
   ,Enhanced Pulse Width Modulation (EPWM) Module,,Yes
   ,Enhanced Quadrature Encoder Pulse (EQEP) Module,,Yes
   Timer Modules,Global Timebase Counter (GTC),,Yes
   ,Windowed Watchdog Timer (WWDT) - MAIN domain,,Yes
   ,Windowed Watchdog Timer (WWDT) - WKUP domain,,NA
   ,Real-Time Clock (RTC),,Yes
   ,Timers - MAIN domain,Timer,Yes
   ,,Capture,No
   ,,Compare,No
   ,,PWM,Yes
   ,Timers - WKUP domain,Timer,Yes
   ,,Capture,No
   ,,Compare,No
   ,,PWM,No
   CRC32,,,Yes
   RTI(WWDG),,,No
   Voltage and Thermal Management(VTM),,,Yes
   Display Subsystem,DISPLAY Parallel Interface (DPI),,Yes
   On-Die Temperature sensor,,,Yes
   On-Chip Debug,,,Yes
   Crypto Accelerator (DTHEv2),Advanced Encryption Standard (AES),AES-CBC,Yes
   ,,AES-ECB,Yes
   ,SHA/MD5 Crypto Hardware-Accelerated Module (SHA/MD5),SHA-256,Yes
   ,,SHA-512,Yes
   ,True Random Number Generator (TRNG),,Yes
   Board Specifics (AM62L EVM),WI-FI,CC3351 (connected via M.2),Yes
   ,PMIC,TPS65214,Yes
