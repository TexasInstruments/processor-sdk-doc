.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_HYPLNK

Overview
--------

Introduction
^^^^^^^^^^^^

Hyperlink is a point-to-point peripheral. Each device has equal
capability to operate on the address space of the other device. This
also means that there is no complex enumeration in order to get started.

.. rubric:: Modes of Operation
   :name: modes-of-operation

The LLD is intended to bring up the Hyperlink peripheral and open memory
mappings.

.. rubric:: Interrupts
   :name: interrupts

There is an interrupt generation example (in
PDK_INSTALL_DIR/packages/ti/drv/hyplnk/example/cicInterruptExample)
which maps and pokes the other device's CIC (Chip/SOC level interrupt
controller) to generate interrupts for data transfers.

The PDK_INSTALL_DIR/packages/ti/drv/hyplnk/example/common/hyplnkIsr.c
monitors local interrupts to detect fatal errors. It can also be used
for IO interrupts, but there is only one output event that has to be
demuxed. Thus for multicore orthogonality, the cicInterruptExample is
often better example (because each destination core can have completely
independent interrupts).

User Interface
--------------

Driver Configuration
^^^^^^^^^^^^^^^^^^^^^

The driver itself is entirely configured via API at runtime. However,
the examples are configured using compiler flags that are in
hyplnkPlatCfg.h and hyplnkLLDCfg.h.

.. rubric:: Hyperlink configuration structure
   :name: hyperlink-configuration-structure

The hyplnk_device.c binds the driver to the hardware on the board. It is
passed into the driver via the call to Hyplnk_init().

APIs
^^^^^

.. rubric:: API Call Flow
   :name: api-call-flow

The API call flow is covered in
example\memoryMappedExample\src\hyplnkExample.

They key parts are:

#. Initialize the LLD via Hyplnk_init().
#. Configure PLL, PSC and memories via hyplnkExampleSysSetup() which is
   all example code
#. Install ISR(s)
#. Enable the peripheral using sequence in hyplnkExamplePeriphSetup()
#. Open memory maps using hyplnkExampleAddrMap() as a guide
#. Exchange data with memcpy or EDMA using mapped address (returned from
   hyplnkExampleAddrMap).

|

Application
------------

Examples
^^^^^^^^

Hyperlink/hyplnk is supported only on Keystone devices. It is available
on 6678, 6657, K2H, K2K, K2E. All examples can be used in either
loopback (on any EVM without any special cables or breakout cards) or
with two boards. For 6678 or 6657, the required cable is
`HL5CABLE <https://store.ti.com/HL5CABLE-Hyperlink-Cable-P2888.aspx>`__.
For K2H/K2K/K2E, the breakout card is
`RTM-BOCRT <http://www.ti.com/devnet/docs/catalog/endequipmentproductfolder.tsp?actionPerformed=productFolder&productId=17440>`__,
and the cable is also required. Below is a picture showing how a K2H EVM
is connected to a 6678 EVM via breakout card and cable.


.. Image:: /images/K2-k1-hyplnk.jpg

+-----------------+-----------------+-----------------+-----------------+
| Name            | Description     | EVM             | Expected        |
|                 |                 | Configuration   | Results         |
+=================+=================+=================+=================+
| memoryMappedExa | Memory mapped   | Loopback runs   | Link is         |
| mple            | data exchange   | without any     | established and |
|                 | with loopback   | extra hardware. | data is         |
|                 | or 2 devices    | See below for   | exchanged.      |
|                 |                 | details on      |                 |
|                 |                 | configuring     |                 |
|                 |                 | board-to-board. |                 |
+-----------------+-----------------+-----------------+-----------------+
| cicInterruptExa | CIC-based       | Loopback runs   | Interrupts are  |
| mple            | interrupt       | without any     | sent between    |
|                 | exchange.       | extra hardware. | ARM Linux       |
|                 |                 | See below for   | Userspace and   |
|                 |                 | details on      | DSPs.           |
|                 |                 | configuring     |                 |
|                 |                 | board-to-board. |                 |
+-----------------+-----------------+-----------------+-----------------+

.. rubric:: Setup of multiple EVMs with one instance of CCS
   :name: setup-of-multiple-evms-with-one-instance-of-ccs

This is only needed for 2 board use cases. See
`Multi-Emulator_Debug_with_CCS <http://processors.wiki.ti.com/index.php/Multi-Emulator_Debug_with_CCS>`__
for general configuration of multiple EVMs/emulators within one instance
of CCS.

.. rubric:: Detailed instructions to run memoryMappedExample
   :name: detailed-instructions-to-run-memorymappedexample

If running with one board, enable loopback via uncommenting
hyplnk_EXAMPLE_LOOPBACK in
PDK_INSTALL_DIR/packages/ti/drv/hyplnk/example/common/hyplnkLLDCfg.h.

Compile the project for the specific device/evm in use.

For loopback: Load the example with hyplnk_EXAMPLE_LOOPBACK definined
onto one board and run. The results should be as below.

For 2 board: Make sure the both boards configuration match each other by
checking
PDK_INSTALL_DIR/packages/ti/drv/hyplnk/example/common/hyplnkLLDCfg.h:

::

    hyplnk_EXAMPLE_PORT --> which port to use for K2H/K2K/K2E
    hyplnk_EXAMPLE_ALLOW_x_LANES --> 0, 1 or 4 lanes
    hyplnk_EXAMPLE_SERRATE_xxpxxx --> serdes rate setup

Load the same example on both boards. It is fulling symmetric. No
special configuration is needed to distinguish side A and side B. Each
side should generate output similar to below.

.. rubric:: Detailed instructions to run cicInterruptExample
   :name: detailed-instructions-to-run-cicinterruptexample

This only works on devices with A15 running Linux (K2H, K2K, K2E). See
PDK_INSTALL_DIR/packages/ti/drv/hyplnk/example/cicInterruptExample/Readme.txt
for instructions.

.. rubric:: Sample example output
   :name: sample-example-output

This came from k2h device running in loopback.

::

    Version #: 0x02010005; string HYPLNK LLD Revision: 02.01.00.05:Dec 24 2015:17:48:28
    About to do system setup (PLL, PSC, and DDR)
    Power domain is already enabled.  You probably re-ran without device reset (which is OK)
    Constructed SERDES configs: PLL=0x00000228; RX=0x0046c495; TX=0x000ccf95
    system setup worked
    About to set up HyperLink Peripheral
    ============================Hyperlink Testing Port 0
    ========================================== begin registers before initialization ===========
    Revision register contents:
      Raw    = 0x4e902101
    Status register contents:
      Raw        = 0x00003004
    Link status register contents:
      Raw       = 0x00000000
    Control register contents:
      Raw             = 0x00000000
    Control register contents:
      Raw        = 0x00000000
    ============== end registers before initialization ===========
    Hyperlink Serdes Common Init Complete
    Hyperlink Serdes Lane 0 Init Complete
    Hyperlink Serdes Lane 1 Init Complete
    Hyperlink Serdes Lane 2 Init Complete
    Hyperlink Serdes Lane 3 Init Complete
    ============== begin registers after initialization ===========
    Status register contents:
      Raw        = 0x04402005
    Link status register contents:
      Raw       = 0xfdf0bdf0
    Control register contents:
      Raw             = 0x00006206
    ============== end registers after initialization ===========
    Waiting 5 seconds to check link stability
    Precursors 1
    Postcursors: 19
    Link seems stable
    About to try to read remote registers
    ============== begin REMOTE registers after initialization ===========
    Status register contents:
      Raw        = 0x0440080f
    Link status register contents:
      Raw       = 0xfdf0bdf0
    Control register contents:
      Raw             = 0x00006202
    ============== end REMOTE registers after initialization ===========
    Peripheral setup worked
    About to read/write once
    Single write test passed
    About to pass 65536 tokens; iteration = 0
    === this is not an optimized example ===
    Link Speed is 4 * 3.125 Gbps
    Passed 65536 tokens round trip (read+write through hyplnk) in 16829 Mcycles
    Approximately 256799 cycles per round-trip
    === this is not an optimized example ===
    Checking statistics
    About to pass 65536 tokens; iteration = 1
    === this is not an optimized example ===
    Link Speed is 4 * 3.125 Gbps
    Passed 65536 tokens round trip (read+write through hyplnk) in 16829 Mcycles
    Approximately 256799 cycles per round-trip
    === this is not an optimized example ===
    Checking statistics
    About to pass 65536 tokens; iteration = 2
    .
    .
    .

Debug FAQ
---------

#. If it seems to not work, check for lError and rError in the status
   register (hyplnkStatusReg_s). If these appear, it means double ecc
   error occurred and the link is non functional. This is fatal error.
   Next look at hyplnkECCErrorReg_s for single (corrected) bit errors.
   After startup these should increment slowly (order of minutes, hours,
   days, not seconds or less). If they are incrementing quickly (several
   times per minute or second), then it means the SERDES coefficients
   should be calibrated by following the Keystone SERDES UG. See
   references section.
#. Note that if the link goes down (uncorrectable ECC error) it is
   possible for the entire interconnect to lock up. If this occurs, it
   will not be possible to access any memory even through the JTAG
   interface (CCS will return errors instead of reading memory, and
   often disconnect the target). Thus the primary cause of this lockup
   should be avoided by carefully following the shutdown/reset
   requirement in section 2.9 of the Hyperlink UG (which is to invoke
   serial stop, and wait for it to take effect before resetting either
   endpoint).
#. Another workaround for ECC single errors is to lower link rate and/or
   reduce to 1 lane. This can be done by adjusting the commented defines
   in
   PDK_INSTALL_DIR/packages/ti/drv/hyplnk/example/common/hyplnkLLDCfg.h.

Additional References
---------------------

Additional documentation can be found in:

+-----------------------------------+-----------------------------------------+
| **Document**                      | **Location**                            |
+-----------------------------------+-----------------------------------------+
| Hardware Peripheral Hyperlink     | `User                                   |
| Users Guide                       | Guide <http://www.ti.com/lit/spru       |
|                                   | gw8>`__                                 |
+-----------------------------------+-----------------------------------------+
| Serdes Users Guide                | `User                                   |
|                                   | Guide <http://www.ti.com/lit/spru       |
|                                   | ho3>`__                                 |
+-----------------------------------+-----------------------------------------+
| CIC Peripheral Users Guide        | `CIC User                               |
|                                   | Guide <http://www.ti.com/lit/spru       |
|                                   | gw4>`__                                 |
+-----------------------------------+-----------------------------------------+
| API Reference Manual              | $(TI_PDK_INSTALL_DIR)\\packages\\ti     |
|                                   | \\drv\\hyplnk\\docs\\doxygen\\html\\ind |
|                                   | ex.html                                 |
+-----------------------------------+-----------------------------------------+
| Release Notes                     | $(TI_PDK_INSTALL_DIR)\\packages\\ti     |
|                                   | \\drv\\hyplnk\\docs\\ReleaseNotes_HYP   |
|                                   | LNK_LLD.pdf                             |
+-----------------------------------+-----------------------------------------+

|

