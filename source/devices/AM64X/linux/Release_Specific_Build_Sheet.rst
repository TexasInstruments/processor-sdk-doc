.. _build_sheet:

====================
Software Build Sheet
====================

Build Sheet of supported features and modules for this |__SDK_FULL_NAME__| Release.
The following table lists the supported features and modules for the corresponding category,
along with the support status for Linux on A53, RTOS on R5F, RTOS on M4, RTOS on A53.

The support status is indicated by the following codes:

   - "Yes": The feature or module is supported.
   - "No": The feature or module is not supported.
   - "SDKx.y": The feature or module will be supported in a future version of the SDK.
   - "N/A": The feature or module is not applicable in the hardware.
   - "ANY": The feature or module is a new update in this revision of the SDK.

.. csv-table:: Software Build Sheet
   :header: "Category", "Module", "SubModule", "Linux on A53", "RTOS on R5F", "RTOS on M4", "RTOS on A53"
   :widths: 20, 20, 20, 20, 20, 20, 20

   Memory Map,MAIN Domain Memory Map,,Yes,Yes,Yes,No
   ,MCU Domain Memory Map,,Yes,Yes,Yes,No
   ,Processors View Memory Map,,Yes,N/A,N/A,No
   ,Region-based Address Translation,,No,Yes,Yes,No
   System Interconnect,,,Yes,N/A,N/A,N/A
   Initialization,I2C Bootloader Operation,,No,N/A,N/A,N/A
   ,SPI Bootloader Operation,,No,N/A,N/A,N/A
   ,QSPI Bootloader Operation,,Yes,Yes,N/A,N/A
   ,OSPI Bootloader Operation,,Yes,Yes,N/A,N/A
   ,PCIe Bootloader Operation,,No,N/A,N/A,N/A
   ,GPMC Bootloader Operation,NOR,No,No,N/A,N/A
   ,,NAND,Yes,No,N/A,N/A
   ,Ethernet Bootloader Operation,,Yes,No,N/A,N/A
   ,USB Bootloader Operation,Host,Yes,No,N/A,N/A
   ,,Device,Yes,No,N/A,N/A
   ,MMCSD Bootloader Operation,SD Card (4 bit),Yes,Yes,N/A,N/A
   ,,SD Card (8 bit),No,No,N/A,N/A
   ,,eMMC,Yes,Yes,N/A,N/A
   ,UART Bootloader Operation,,Yes,Yes,N/A,N/A
   Device Configuration,Power,,Yes,Yes,Yes,No
   ,Reset,,Yes,Yes,Yes,Yes
   ,Clocking,,Yes,Yes,Yes,Yes
   Processors and Accelerators,Dual-R5F MCU Subsystem,,Yes,Yes,N/A,N/A
   ,Dual-A53 MPU Subsystem,,Yes,N/A,N/A,Yes
   ,Cortex-M4F Subsystem,,No,N/A,Yes,N/A
   ,Programmable Real-Time Unit and Industrial Communication Subsystem - Gigabit,General PRU Use,Yes,Yes,No,No
   ,,EtherCAT Device,No,Yes,No,No
   ,,Profinet RT Device,No,Yes,No,No
   ,,Profinet IRT Device,No,Yes,No,No
   ,,EtherNet/IP adapter,No,Yes,No,No
   ,,Ethernet Endpoint (EMAC),Yes,Yes,No,No
   ,,Ethernet Switch,Yes,No,No,No
   ,,Ethernet HSR,Yes,No,No,No
   ,,IO Link Primary,No,Yes,No,No
   ,,"HDSL, EnDat 2.2",No,Yes,No,No
   Interprocessor Communication (IPC),Mailbox,,Yes,Yes,Yes,Yes
   ,Spinlock,,Yes,Yes,Yes,Yes
   Memory Controllers,DDR Subsystem (DDRSS),DDR4,Yes,Yes,N/A,N/A
   ,,LPDDR4,Yes,No,N/A,N/A
   ,,Inline ECC,Yes,Yes,N/A,N/A
   ,Region-based Address Translation (RAT) Module,,No,Yes,Yes,No
   Interrupts,MCU Domain Interrupt Maps,,Yes,Yes,Yes,Yes
   ,MAIN Domain Interrupt Maps,,Yes,Yes,N/A,Yes
   Time Sync,Time Sync Module (CPTS),,Yes,Yes,No,No
   ,Timer Manager,,No,No,No,No
   ,Time Sync and Compare Events,,Yes,No,No,No
   Data Movement Architecture (DMA),Data Movement Subsystem (DMSS),,Yes,Yes,N/A,Yes
   ,Peripheral DMA (PDMA),,Yes,Yes,N/A,No
   ,RingAcc,,Yes,Yes,N/A,No
   ,Secure Proxy,,Yes,Yes,N/A,No
   ,Interrup Aggregator,,Yes,Yes,N/A,No
   ,Packet Streaming Interface Link,,Yes,Yes,N/A,No
   General Connectivity Peripherals,Analog-to-Digital Converter (ADC),,Yes,Yes,No,Yes
   ,General-Purpose Interface (GPIO),,Yes,Yes,Yes,Yes
   ,Inter-Integrated Circuit (I2C) Interface,Controller,Yes,Yes,Yes,Yes
   ,,Target,No,Yes,Yes,Yes
   ,Multichannel Serial Peripheral Interface (MCSPI),Controller,Yes,Yes,Yes,Yes
   ,,Peripheral,No,Yes,Yes,Yes
   ,Universal Asynchronous Receiver/Transmitter (UART),UART,Yes,Yes,Yes,Yes
   ,,RS-485,Yes,No,No,No
   ,,IrDA,No,No,No,No
   High-speed Serial Interfaces,Gigabit Ethernet Switch (CPSW0),Switch,Yes,Yes,N/A,No
   ,,EndPoint,Yes,Yes,N/A,No
   ,Peripheral Component Interconnect Express (PCIe) Subsystem,Root Complex,Yes,Yes,N/A,No
   ,,EndPoint,Yes,Yes,N/A,No
   ,Universal Serial Bus Subsystem (USBSS),Host 3.0,N/A,No,N/A,No
   ,,Device 3.0,N/A,No,N/A,No
   ,,Host 2.0,Yes,No,N/A,No
   ,,Device 2.0,Yes,Yes,N/A,No
   ,Serializer/Deserializer (SerDes),,Yes,Yes,N/A,No
   Memory Interfaces,Flash Subsystem (FSS) ,,No,No,N/A,No
   ,Octal Serial Peripheral Interface (OSPI),,Yes,Yes,N/A,Yes
   ,General-Purpose Memory Controller (GPMC),FPGA,No,No,N/A,No
   ,,NAND,Yes,No,N/A,No
   ,,NOR,No,No,N/A,No
   ,,etc.,No,No,N/A,No
   ,Error Location Module (ELM),,Yes,No,N/A,No
   ,Multimedia Card Secure Digital (MMCSD) Interface,4-bit,Yes,Yes,N/A,Yes
   ,,8-bit,Yes,Yes,N/A,Yes
   Industrial and Control Interfaces,Enhanced Capture (ECAP) Module,Capture,No,Yes,N/A,Yes
   ,,PWM,Yes,No,N/A,Yes
   ,Enhanced Pulse Width Modulation (EPWM) Module,,Yes,Yes,N/A,Yes
   ,Enhanced Quadrature Encoder Pulse (EQEP) Module,,Yes,Yes,N/A,Yes
   ,Controller Area Network (MCAN),Classic CAN,Yes,Yes,N/A,Yes
   ,,Classic CAN FD,Yes,Yes,N/A,Yes
   ,FSI,Receiver,No,Yes,N/A,No
   ,,Transmitter,No,Yes,N/A,No
   Timer Modules,Global Timebase Counter (GTC),,Yes,Yes,Yes,Yes
   ,Windowed Watchdog Timer (WWDT),,Yes,Yes,No,Yes
   ,Timers,Timer,Yes,Yes,Yes,Yes
   ,,Capture,No,No,No,No
   ,,Compare,No,No,No,No
   ,,PWM,No,No,No,No
   Internal Diagnostics Modules,Dual Clock Comparator (DCC),,No,Yes,Yes,No
   ,Error Signaling Module (ESM),,No,Yes,Yes,No
   ,RTI(WWDG)	,,No,Yes,Yes,No
   ,Voltage and Thermal Management(VTM)	,,No,Yes,Yes,No
   ,Interconnect Isolation Gasket(STOG)	,,No,Yes,Yes,No
   ,Interconnect Isolation Gasket(MTOG)	,,No,No,Yes,No
   ,Power OK(POK)	,,No,Yes,Yes,No
   ,PBIST(Built In Self Test)	,,No,Yes,Yes,No
   ,LBIST(Built In Self Test)	,,No,No,Yes,No
   ,Memory Cyclic Redundancy Check (MCRC) Controller,,No,Yes,Yes,No
   ,ECC AggrB70:B117egator,,No,Yes,Yes,No
    On-Chip Debug,,,Yes,Yes,Yes,No
