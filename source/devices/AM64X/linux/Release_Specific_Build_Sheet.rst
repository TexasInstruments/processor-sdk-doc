.. _build_sheet:

====================
Software Build Sheet
====================

Build Sheet of supported features and modules for this |__SDK_FULL_NAME__| Release.
The following table lists the supported features and modules with the support status
for Linux on A53. Please refer to `RTOS Build Sheet <https://software-dl.ti.com/mcu-plus-sdk/esd/AM64X/11_01_00_17/exports/docs/build_sheet/am64x-sw-buildsheet.html>`__
for the supported features and modules on RTOS.

The support status is indicated by the following codes:

   - "Yes": The feature or module is supported.
   - "No": The feature or module is not supported.
   - "SDKx.y": The feature or module will be supported in a future version of the SDK.
   - "N/A": The feature or module is not applicable in the hardware.
   - "ANY": The feature or module is a new update in this revision of the SDK.

.. csv-table:: Software Build Sheet
   :header: "Category", "Module", "SubModule", "Linux on A53"
   :widths: 20, 20, 20, 20

   Memory Map,MAIN Domain Memory Map,,Yes
   ,MCU Domain Memory Map,,Yes
   ,Processors View Memory Map,,Yes
   ,Region-based Address Translation,,No
   System Interconnect,,,Yes
   Initialization,I2C Bootloader Operation,,No
   ,SPI Bootloader Operation,,No
   ,QSPI Bootloader Operation,,Yes
   ,OSPI Bootloader Operation,,Yes
   ,PCIe Bootloader Operation,,No
   ,GPMC Bootloader Operation,NOR,No
   ,,NAND,Yes
   ,Ethernet Bootloader Operation,,Yes
   ,USB Bootloader Operation,Host,Yes
   ,,Device,Yes
   ,MMCSD Bootloader Operation,SD Card (4 bit),Yes
   ,,SD Card (8 bit),No
   ,,eMMC,Yes
   ,UART Bootloader Operation,,Yes
   Device Configuration,Power,,Yes
   ,Reset,,Yes
   ,Clocking,,Yes
   Processors and Accelerators,Dual-R5F MCU Subsystem,,Yes
   ,Dual-A53 MPU Subsystem,,Yes
   ,Cortex-M4F Subsystem,,No
   ,Programmable Real-Time Unit and Industrial Communication Subsystem - Gigabit,General PRU Use,Yes
   ,,EtherCAT Device,No
   ,,Profinet RT Device,No
   ,,Profinet IRT Device,No
   ,,EtherNet/IP adapter,No
   ,,Ethernet Endpoint (EMAC),Yes
   ,,Ethernet Switch,Yes
   ,,Ethernet HSR,Yes
   ,,IO Link Primary,No
   ,,"HDSL, EnDat 2.2",No
   Interprocessor Communication (IPC),Mailbox,,Yes
   ,Spinlock,,Yes
   Memory Controllers,DDR Subsystem (DDRSS),DDR4,Yes
   ,,LPDDR4,Yes
   ,,Inline ECC,Yes
   ,Region-based Address Translation (RAT) Module,,No
   Interrupts,MCU Domain Interrupt Maps,,Yes
   ,MAIN Domain Interrupt Maps,,Yes
   Time Sync,Time Sync Module (CPTS),,Yes
   ,Timer Manager,,No
   ,Time Sync and Compare Events,,Yes
   Data Movement Architecture (DMA),Data Movement Subsystem (DMSS),,Yes
   ,Peripheral DMA (PDMA),,Yes
   ,RingAcc,,Yes
   ,Secure Proxy,,Yes
   ,Interrup Aggregator,,Yes
   ,Packet Streaming Interface Link,,Yes
   General Connectivity Peripherals,Analog-to-Digital Converter (ADC),,Yes
   ,General-Purpose Interface (GPIO),,Yes
   ,Inter-Integrated Circuit (I2C) Interface,Controller,Yes
   ,,Target,No
   ,Multichannel Serial Peripheral Interface (MCSPI),Controller,Yes
   ,,Peripheral,No
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes
   ,,RS-485,Yes
   ,,IrDA,No
   High-speed Serial Interfaces,Gigabit Ethernet Switch (CPSW0),Switch,Yes
   ,,EndPoint,Yes
   ,Peripheral Component Interconnect Express (PCIe) Subsystem,Root Complex,Yes
   ,,EndPoint,Yes
   ,Universal Serial Bus Subsystem (USBSS),Host 3.0,N/A
   ,,Device 3.0,N/A
   ,,Host 2.0,Yes
   ,,Device 2.0,Yes
   ,Serializer/Deserializer (SerDes),,Yes
   Memory Interfaces,Flash Subsystem (FSS) ,,No
   ,Octal Serial Peripheral Interface (OSPI),,Yes
   ,General-Purpose Memory Controller (GPMC),FPGA,No
   ,,NAND,Yes
   ,,NOR,No
   ,,etc.,No
   ,Error Location Module (ELM),,Yes
   ,Multimedia Card Secure Digital (MMCSD) Interface,4-bit,Yes
   ,,8-bit,Yes
   Industrial and Control Interfaces,Enhanced Capture (ECAP) Module,Capture,No
   ,,PWM,Yes
   ,Enhanced Pulse Width Modulation (EPWM) Module,,Yes
   ,Enhanced Quadrature Encoder Pulse (EQEP) Module,,Yes
   ,Controller Area Network (MCAN),Classic CAN,Yes
   ,,Classic CAN FD,Yes
   ,FSI,Receiver,No
   ,,Transmitter,No
   Timer Modules,Global Timebase Counter (GTC),,Yes
   ,Windowed Watchdog Timer (WWDT),,Yes
   ,Timers,Timer,Yes
   ,,Capture,No
   ,,Compare,No
   ,,PWM,No
   Internal Diagnostics Modules,Dual Clock Comparator (DCC),,No
   ,Error Signaling Module (ESM),,No
   ,RTI(WWDG) ,,No
   ,Voltage and Thermal Management(VTM) ,,No
   ,Interconnect Isolation Gasket(STOG) ,,No
   ,Interconnect Isolation Gasket(MTOG) ,,No
   ,Power OK(POK) ,,No
   ,PBIST(Built In Self Test) ,,No
   ,LBIST(Built In Self Test) ,,No
   ,Memory Cyclic Redundancy Check (MCRC) Controller,,No
   ,ECC AggrB70:B117egator,,No
   On-Chip Debug,,,Yes
