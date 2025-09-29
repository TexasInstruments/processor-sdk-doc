.. _build_sheet:

====================
Software Build Sheet
====================

Build Sheet of supported features and modules for this |__SDK_FULL_NAME__|
Release. The following table lists the supported features and modules for the
corresponding category, along with the support status for Linux on A53 and RTOS
on A53.

The support status is indicated by the following codes:

   - "Yes": The feature or module is supported.
   - "No": The feature or module is not supported.
   - "SDKx.y": The feature or module will be supported in a future version of the SDK.
   - "NA": The feature or module is not applicable in the hardware.
   - "ANY": The feature or module is a new update in this revision of the SDK.

.. csv-table:: Software Build Sheet
   :header: "Category", "Module", "SubModule", "Linux on A53", "RTOS on A53"
   :widths: 20, 20, 20, 20, 20

   Initialization,I2C Bootloader Operation,,No,No
   ,SPI Bootloader Operation,,No,No
   ,QSPI Bootloader Operation,NOR,Yes,No
   ,NAND,No,SDK11.2
   ,OSPI Bootloader Operation,NOR,Yes,SDK11.1
   ,NAND (1-bit mode),Yes,No
   ,NAND (8-bit mode),Yes,No
   ,GPMC Bootloader Operation,NOR,No,No
   ,NAND,No,No
   ,Ethernet Bootloader Operation,,NA,NA
   ,USB Bootloader Operation,Host,No,No
   ,Device,No,No
   ,MMCSD Bootloader Operation,SD Card (no UHS),Yes,SDK11.1
   ,eMMC,Yes,SDK11.1
   ,UART Bootloader Operation,,Yes,SDK11.1
   Device Configuration,,VTM,Yes,SDK11.1
   Power Management,Deep Sleep Low Power Mode,,Yes,SDK11.2
   ,Deep Sleep LPM Wakeup Events,RTC Timer,Yes,SDK11.2
   ,GT Timers,No,No
   ,WKUP UART,No,No
   ,I2C,No,No
   ,I/O Daisy Chain,Yes,No
   ,USB Connect/Disconnect,No,No
   ,USB Remote Wakeup,No,No
   ,Standby Low Power Mode,,SDK11.1,SDK11.2
   ,Partial I/O Low Power Mode,,SDK11.1,No
   ,Boot-time OPP configurations,,No,No
   ,Runtime Power Management,,SDK11.1,No
   ,DFS/CPUFreq,,No,No
   ,CPUIdle (A53 WFI),,No,No
   ,CPUIdle (DDR in Self-Refresh),,No,No
   Interprocessor Communication,Mailbox,,Yes,No
   Memory Controllers,DDR Subsystem (DDRSS),DDR4,No,No
   ,,LPDDR4,Yes,SDK11.1
   ,,Inline ECC (1bit err),Yes,SDK11.1
   ,,Inline ECC (mbit err),Yes,SDK11.1
   Time Sync,Time Sync Module (CPTS),,Yes,No
   ,Timer Manager,,No,No
   ,Time Sync and Compare Events,,No,No
   Data Movement Architecture (DMA),Data Movement Subsystem (DMSS),,Yes,March-End
   ,Peripheral DMA (PDMA),,Yes,March-End
   ,RingAcc,,Yes,March-End
   ,BCDMA,,Yes,March-End
   ,Packet Streaming Interface Link,,Yes,March-End
   General Connectivity Peripherals (MAIN domain),Multichannel Audio Serial Port (McASP),Input,Yes,SDK11.1
   ,,Output,Yes,SDK11.1
   ,,HDMI Output,Yes,No
   ,Analog to Digital Converter,ADC,Yes,March-End
   ,General-Purpose Interface (GPIO),,Yes,Yes
   ,Inter-Integrated Circuit (I2C),Controller,Yes,Yes
   ,,Target,No,No
   ,Multichannel Serial Peripheral Interface (McSPI),Controller,Yes,Yes
   ,,Peripheral,No,No
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes,Yes
   ,,RS-485,Yes,No
   ,,IrDA,No,No
   General Connectivity Peripherals (WKUP domain),General-Purpose Interface (GPIO),,Yes,Yes
   ,Inter-Integrated Circuit (I2C),Controller,Yes,Yes
   ,,Target,No,No
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes,Yes
   ,,RS-485,Yes,No
   ,,IrDA,No,No
   High-speed Serial Interfaces,Gigabit Ethernet Switch (CPSW3G),Switch,Yes,SDK11.1
   ,,EndPoint,Yes,SDK11.1
   ,,TSN,Yes,SDK11.1
   ,,TSN - VLAN,Yes,SDK11.1
   Universal Serial Bus Subsystem (USBSS),Host 3.1,NA,NA
   ,,Device 3.1,NA,NA
   ,,Host 2.0,Yes,SDK12.0
   ,,Device 2.0,Yes,SDK12.0
   Memory Interfaces,Flash Subsystem (FSS),,No,No
   ,Quad Serial Peripheral Interface (QSPI),NOR,Yes,No
   ,,NAND,NA,SDK11.2
   ,Octal Serial Peripheral Interface (OSPI),NOR,Yes,Yes
   ,,NAND,Yes,No
   ,Expanded Serial Peripheral Interface (xSPI),,Yes,No
   ,General-Purpose Memory Controller (GPMC),FPGA,No,SDK12.0
   ,,NAND,Yes,SDK11.2
   ,,NOR,No,No
   ,,PSRAM,No,SDK11.2
   ,Error Location Module (ELM),,No,No
   ,Multimedia Card Secure Digital (MMCSD) Interface,SD Card,Yes,Yes
   ,,eMMC,Yes,Yes
   Industrial & Control Interfaces,Controller Area Network (MCAN) - MAIN domain,CAN,Yes,Yes
   ,,CAN FD,Yes,Yes
   ,Enhanced Capture (ECAP) Module,Capture,Yes,Yes
   ,,PWM,Yes,Yes
   ,Enhanced Pulse Width Modulation (EPWM) Module,,Yes,Yes
   ,Enhanced Quadrature Encoder Pulse (EQEP) Module,,Yes,Yes
   Timer Modules,Global Timebase Counter (GTC),,Yes,Yes
   ,Windowed Watchdog Timer (WWDT) - MAIN domain,,Yes,SDK11.1
   ,Windowed Watchdog Timer (WWDT) - WKUP domain,,NA,NA
   ,Real-Time Clock (RTC),,Yes,SDK11.1
   ,Timers - MAIN domain,Timer,Yes,Yes
   ,,Capture,No,No
   ,,Compare,No,No
   ,,PWM,Yes,No
   ,Timers - WKUP domain,Timer,Yes,No
   ,,Capture,No,No
   ,,Compare,No,No
   ,,PWM,No,No
   CRC32,,,Yes,No
   RTI(WWDG),,,No,No
   Voltage and Thermal Management(VTM),,,No,No
   Display Subsystem,DISPLAY Parallel Interface (DPI),,Yes,No
   On-Die Temperature sensor,,,Yes,No
   On-Chip Debug,,,NA,NA
   Crypto Accelerator (DTHEv2),Advanced Encryption Standard (AES),AES-CBC,Yes,SDK11.1
   ,,AES-ECB,Yes,SDK11.1
   ,SHA/MD5 Crypto Hardware-Accelerated Module (SHA/MD5),SHA-256,Yes,SDK11.1
   ,,SHA-512,Yes,SDK11.1
   ,True Random Number Generator (TRNG),,No,No
   Board Specifics (AM62L EVM),cc3351 M.2,Wifi,Yes,No
   ,TPS65214,PMIC,SDK11.1,No
