.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_PCIe

Overview
--------

PCIe module supports dual operation mode: End Point (EP or Type0) or
Root Complex (RC or Type1). This driver focuses on EP mode but it also
provides access to some basic RC configuration/functionality. For RC
this is the lowest level; additional software is needed to perform
generic enumeration of third party devices.

The PCIe subsystem has two address spaces. The first (Address Space 0)
is dedicated for local application registers, local configuration
accesses and remote configuration accesses. The second (Address Space 1)
is dedicated for data transfer. This PCIe driver focuses on
configuration of the interface and sending/receiving interrupts via
Address Space 0. Data is transferred outside the scope of the LLD using
CPU or EDMA through the data area.

There are three revisions of the pcie hardware. The first, v0, in KeyStone
devices (C66x, K2x). The second, v1, is in AM57xx devices. The third,
v2, is in AM65xx devices.  The LLD
abstacts the configuration of standards-based PCIe registers (Type 0,
Type 1 and Capabilities registers) so same user code can be used on both
device types. However, there are different interfaces for the registers
not based on PCIe standards (port logic and ti-conf which generally
covers interrupts and address translation). That portion of user code
needs to differ between C66x/K2x, AM57xx, and AM65xx devices.

The example includes configuration of one SoC as EP and a second as RC.
It then performs a simple CPU-based memory transfer (EDMA can be used
via the same addresses used by the CPU), and interrupt generation (from
EP) and reception (to RC). It also shows differences in user code
required to support both C66x/K2x, AM57xx and AM65xx devices.

.. rubric:: Differences in Operation between C66x/K2x and AM57xx devices
   :name: differences-in-operation-between-c66xk2x-and-am57xx-devices

C66x/K2x, AM57xx, and AM65xx are functionally identical, except that interrupts
are handled by example and lld only on AM57xx.  Also older devices only support
gen 1/2, while AM65xx supports gen 3.

.. rubric:: Modes of Operation
   :name: modes-of-operation

The LLD is intended to bring up the PCIe peripheral, open memory
mappings, and send/receive interrupts.

.. rubric:: Root Complex (RC)
   :name: root-complex-rc

The PCIe peripheral can be used as a root complex. One or more other
endpoints can be connected (more than one requires a PCIe switch on the
board). The LLD configures the peripheral in RC mode. It doesn't attempt
to emulate the full enumeration capability of a Linux driver. Instead
the user will need to supply code specific to each endpoint they intend
to support.

.. rubric:: Endpoint (EP)
   :name: endpoint-ep

The PCIe peripheral can be used as an endpoint. This is the more
intended usecase for the LLD. Once the link is initialized, the LLD can
provide data addresses and send interrupts to the RC.

.. rubric:: Interrupts
   :name: interrupts

The example for AM57XX provides code to send interrupts from an
endpoint, and the LLD/example together contain code to receive/demux the
interrupts (both MSI and Legacy) on an RC.

User Interface
--------------

Driver Configuration
^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Board-specific configuration
   :name: board-specific-configuration

PCIe's board specific configuration is in the example in
PDK_INSTALL_DIR/packages/ti/drv/pcie/example/sample/am57x/src/pcie_sample_board.c.
Calling sequence is in example and repeated below.

.. rubric:: PCIe configuration structure
   :name: pcie-configuration-structure

The pcie_soc.c binds the driver to the hardware on the board. It is
passed into the driver via the call to Pcie_init().

API Call Flow
^^^^^^^^^^^^^

The API call flow is covered in pcie_sample.c.

The overall components are:

#. Initialize the driver
#. Initialize the SERDES and Power the peripheral (see example code for
   order for each device)
#. Configure RC or EP symmetrically to talk to another similar device
#. Perform data IO and interrupt.

Application
------------

Examples
^^^^^^^^

+-----------------+-----------------+-----------------+-----------------+
| Name            | Description     | EVM             | Expected        |
|                 |                 | Configuration   | Results         |
+=================+=================+=================+=================+
| PCIE_idkAM57[1\ | 2-device PCIe   | **IMPORTANT:**  | **AM572x/AM574x |
| 24]x*ExamplePr\ | connection      | Cable must be   | or AM571x       |
| oject           |                 | `MODIFIED`_     | EVM** : One     |
|                 |                 | in order to     | board is        |
|                 |                 | avoid damaging  | EP/other is RC; |
|                 |                 | the clock       | link is         |
|                 |                 | drivers in the  | established and |
|                 |                 | SoC!            | data/interrupts |
|                 |                 |                 | exchanged. All  |
|                 |                 |                 | printed output  |
|                 |                 | Connect two     | goes to the     |
|                 |                 | like AM57xx     | serial console. |
|                 |                 | IDK EVMs J22    |                 |
|                 |                 | `MODIFIED`_     |                 |
|                 |                 | male-male       |                 |
|                 |                 | crossover       |                 |
|                 |                 | PCIe x1 or x4   |                 |
|                 |                 | cable and       |                 |
|                 |                 | optional        |                 |
|                 |                 | straight-through|                 |
|                 |                 | extender. For   |                 |
|                 |                 | AM572x/AM574x   |                 |
|                 |                 | we used a       |                 |
|                 |                 | one-lane        |                 |
|                 |                 | cross cable;    |                 |
|                 |                 | for AM571x we   |                 |
|                 |                 | used a 4-lane   |                 |
|                 |                 | cross cable.    |                 |
|                 |                 | | Projects      |                 |
|                 |                 | available for   |                 |
|                 |                 | C66, A15, and   |                 |
|                 |                 | M4.             |                 |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| PCIE_sample_Ex\ | 2-device PCIe   | **IMPORTANT:**  | **AM65xx IDK**  |
| ampleProject    | connection      | Cable must be   | One board is EP/|
|                 |                 | `MODIFIED`_     | other           |
| (for AM65xx IDK)|                 | in order to     | is              |
|                 |                 | avoid damaging  | RC;             |
|                 |                 | the clock       | link is         |
|                 |                 | drivers in the  | established and |
|                 |                 | SoC!            | data            |
|                 |                 |                 | exchanged. All  |
|                 |                 |                 | printed output  |
|                 |                 | Connect two     | goes to the     |
|                 |                 | like AM65xx     | serial console. |
|                 |                 | IDK EVMs PCIe   |                 |
|                 |                 | using a         |                 |
|                 |                 | `MODIFIED`_     |                 |
|                 |                 | male-male       |                 |
|                 |                 | crossover       |                 |
|                 |                 | PCIe x1 or x4   |                 |
|                 |                 | cable and       |                 |
|                 |                 | optional        |                 |
|                 |                 | straight-through|                 |
|                 |                 | extender.       |                 |
|                 |                 |                 |                 |
|                 |                 | We used a       |                 |
|                 |                 | one-lane        |                 |
|                 |                 | cross cable.    |                 |
|                 |                 |                 |                 |
|                 |                 | Executables     |                 |
|                 |                 | for A53 (mpu)   |                 |
|                 |                 | and R5 (mcu)    |                 |
|                 |                 | available.      |                 |
|                 |                 |                 |                 |
|                 |                 | Note: this is   |                 |
|                 |                 | NOT a CCS       |                 |
|                 |                 | project.  It    |                 |
|                 |                 | is built from   |                 |
|                 |                 | running         |                 |
|                 |                 | ``make pcie``   |                 |
|                 |                 | from $(TI_PDK\  |                 |
|                 |                 | _INSTALL_DIR)/\ |                 |
|                 |                 | packages.       |                 |
|                 |                 | Result is in    |                 |
|                 |                 | ti/binary.      |                 |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| PCIE_evmK2G*Ex\ | 2-device PCIe   | **IMPORTANT:**  | **K2G EVM** :   |
| ampleProject    | connection      | Cable must be   | One board is    |
|                 |                 | `MODIFIED`_     | EP/other is RC; |
|                 |                 | in order to     | link is         |
|                 |                 | avoid damaging  | established and |
|                 |                 | the clock       | data is         |
|                 |                 | drivers in the  | exchanged. All  |
|                 |                 | SoC!            | printed output  |
|                 |                 |                 | goes to serial  |
|                 |                 |                 | console.        |
|                 |                 |                 |                 |
|                 |                 | Connect two     |                 |
|                 |                 | K2G  EVMs J5    |                 |
|                 |                 | using a         |                 |
|                 |                 | `MODIFIED`_     |                 |
|                 |                 | male-male       |                 |
|                 |                 | crossover       |                 |
|                 |                 | PCIe x1 cable   |                 |
|                 |                 | and optional    |                 |
|                 |                 | straight-through|                 |
|                 |                 | extender. We    |                 |
|                 |                 | used a          |                 |
|                 |                 | one-lane        |                 |
|                 |                 | cross cable.    |                 |
|                 |                 | Ensure that     |                 |
|                 |                 | jumper J15 is   |                 |
|                 |                 | positioned to   |                 |
|                 |                 | the left hand   |                 |
|                 |                 | two pins as     |                 |
|                 |                 | viewed with     |                 |
|                 |                 | "J15"           |                 |
|                 |                 | silkscreen      |                 |
|                 |                 | right side up   |                 |
|                 |                 | (pin 0 isn't    |                 |
|                 |                 | clearly         |                 |
|                 |                 | marked). In     |                 |
|                 |                 | the right       |                 |
|                 |                 | hand            |                 |
|                 |                 | position, the   |                 |
|                 |                 | PCIe PLL will   |                 |
|                 |                 | NOT get         |                 |
|                 |                 | clock.          |                 |
|                 |                 | Projects        |                 |
|                 |                 | available for   |                 |
|                 |                 | C66 and A15.    |                 |
+-----------------+-----------------+-----------------+-----------------+
| PCIE_idkAM571x\ | Packet Exchange | **IMPORTANT:**  | **AM571X        |
| _*armEdmaPktEx\ | over PCIe       | Cable must be   | >=REV1.3A       |
| ampleProject    | Benchmark       | `MODIFIED`_     | IDK** : One     |
| *(Available     |                 | in order to     | board is        |
| starting in     |                 | avoid damaging  | EP/other is RC; |
| Processor-SDK   |                 | the clock       | link is         |
| 3.1)*           |                 | drivers in the  | established and |
|                 |                 | SoC!            | data is         |
|                 |                 |                 | exchanged.      |
|                 |                 |                 | Produces same   |
|                 |                 |                 | output as       |
|                 |                 |                 | standard        |
|                 |                 |                 | ExampleProject, |
|                 |                 | Connect two     | except EP also  |
|                 |                 | like            | prints packet   |
|                 |                 | >=REV1.3A       | exchange        |
|                 |                 | AM571x  IDK     | benchmark       |
|                 |                 | EVMs J22        | results.        |
|                 |                 | using a         |                 |
|                 |                 | `MODIFIED`_     |                 |
|                 |                 | male-male       |                 |
|                 |                 | crossover       |                 |
|                 |                 | PCIe x4 cable   |                 |
|                 |                 | and optional    |                 |
|                 |                 | straight-through|                 |
|                 |                 | extender. We    |                 |
|                 |                 | used a 4-lane   |                 |
|                 |                 | cross cable.    |                 |
|                 |                 | Projects        |                 |
|                 |                 | available for   |                 |
|                 |                 | A15 only.       |                 |
|                 |                 | >=REV1.3A EVM   |                 |
|                 |                 | required (for   |                 |
|                 |                 | x4 PCIe         |                 |
|                 |                 | connectors).    |                 |
+-----------------+-----------------+-----------------+-----------------+
| Remaining       | 2-device PCIe   | Connect two     | **6678, 6657,   |
| PCIE_*ExampleP\ | connection      | like C66x/K2x   | K2E, K2H,       |
| roject          |                 | (except K2G,    | K2L** : One     |
|                 |                 | see previous    | board is        |
|                 |                 | row) EVMs using | EP/other is RC; |
|                 |                 | an AMC breakout | link is         |
|                 |                 | card. For K2L,  | established and |
|                 |                 | it is necessary | data exchanged. |
|                 |                 | to configure    | For A15         |
|                 |                 | the mux via the | projects, all   |
|                 |                 | BMC console     | printed output  |
|                 |                 | with            | goes to serial  |
|                 |                 | "interface_muxs | console. For    |
|                 |                 | el              | C66 projects,   |
|                 |                 | pcie" command.  | all printed     |
|                 |                 | Projects        | output goes to  |
|                 |                 | available for   | CCS console.    |
|                 |                 | A15 and/or C66  |                 |
|                 |                 | as present in   |                 |
|                 |                 | each device.    |                 |
+-----------------+-----------------+-----------------+-----------------+
| PCIE_Qos_Examp\ | 2-device PCIe   | **IMPORTANT:**  | **AM65xx IDK**  |
| leProject       | connection      | Cable must be   | One board is EP/|
|                 |                 | `MODIFIED`_     | other           |
| (for AM65xx IDK)|                 | in order to     | is              |
|                 |                 | avoid damaging  | RC;             |
|                 |                 | the clock       | link is         |
|                 |                 | drivers in the  | established and |
|                 |                 | SoC!            | data            |
|                 |                 |                 | exchanged with  |
|                 |                 |                 | TC0/TC1/TC2(DDR)|
|                 |                 | Connect two     | /TC3(MSMC).     |
|                 |                 | like AM65xx     | Then PCIE CPU   |
|                 |                 | IDK EVMs PCIe   | read latency    |
|                 |                 | using a         | with TC3 is     |
|                 |                 | `MODIFIED`_     | measured with   |
|                 |                 | male-male       | background PCIE |
|                 |                 | crossover       | read traffic    |
|                 |                 | PCIe x1 or x4   | over TC0 using  |
|                 |                 | cable and       | DMA.            |
|                 |                 | optional        | All printed     |
|                 |                 | straight-through| output goes to  |
|                 |                 | extender.       | serial console. |
|                 |                 |                 |                 |
|                 |                 | We used a       |                 |
|                 |                 | one-lane        |                 |
|                 |                 | cross cable.    |                 |
|                 |                 |                 |                 |
|                 |                 | Executables     |                 |
|                 |                 | for A53 (mpu)   |                 |
|                 |                 | and R5 (mcu)    |                 |
|                 |                 | available.      |                 |
|                 |                 |                 |                 |
|                 |                 | Note: this is   |                 |
|                 |                 | NOT a CCS       |                 |
|                 |                 | project.  It    |                 |
|                 |                 | is built from   |                 |
|                 |                 | running         |                 |
|                 |                 | ``make pcie``   |                 |
|                 |                 | from $(TI_PDK\  |                 |
|                 |                 | _INSTALL_DIR)/\ |                 |
|                 |                 | packages.       |                 |
|                 |                 | Result is in    |                 |
|                 |                 | ti/binary.      |                 |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

.. _MODIFIED: http://processors.wiki.ti.com/index.php/PCIe_CableMod

.. rubric:: Quick setup of xds100 for two EVMs
   :name: quick-setup-of-xds100-for-two-evms

#. create new target configuration using XDS100v2 and AM572x (or AM571x)
   from the basic tab.
#. Select Advanced tab.
#. Highlight the XDS100v2, and click the "new" button and add second
   XDS100v2.
#. Highlight the newly added XDS100v2, click the "add" button and select
   a second Am572x.
#. open command prompt, and run ti\ccs_base\common\uscif\xds100serial to
   get your serial numbers
#. Highlight first XDS100v2, select "Debug Probe Selection" to "Select
   by Serial number" and enter one of the 2 serial numbers
#. Repeat second XDS100v2, setting to to the second serial number.

General instructions for configuring multiple EVMs with any emulator
type are available in
`Debugging with Multiple Debug Probes <http://software-dl.ti.com/ccs/esd/documents/sdto_ccs_multi-probe-debug.html>`__

.. rubric:: Detailed instructions to run example
   :name: detailed-instructions-to-run-example

Ensure 2 Like EVMs are connected with a x1 PCIe male/male cross cable
(for AM5XX) or a breakout card (for C667x, C665x, K2x)

Build project(s) appropriate for your EVM. Projects for A15 and C66 are
provided based on core types available on each device.

Load via jtag either the ARM or DSP projects (but don't mix and match)
onto the first arm or dsp core of each the 2 EVMs. Same .out file
supports both RC and EP. Use an "expressions" window to set PcieModeGbl
to PCIE_RC_MODE on one EVM (it makes that EVM RC). Leave the second EVM
alone (pcie_EP_MODE). Run the loaded cores. See table above to determine
whether output is expected on serial console or CCS console.

.. rubric:: Sample example output
   :name: sample-example-output

Note that output will vary slightly based on device type. The following
is from A57XX. The output from the RC and EP are interleaved since this
is run from a 2*XDS1000 double config as described in `Quick setup of
xds100 for two EVMs <#quick-setup-of-xds100-for-two-evms>`__

::

    **********************************************
    *             PCIe Test Start                *
    *                RC mode                     *
    **********************************************

    Version #: 0x02020003; string PCIE LLD Revision: 02.02.00.03:Dec 24 2015:17:38:37

    PCIe Power Up.
    PLL configured.
    Successfully configured Inbound Translation!
    Successfully configured Outbound Translation!
    Starting link training...
    **********************************************
    *             PCIe Test Start                *
    *                EP mode                     *
    **********************************************

    Version #: 0x02020003; string PCIE LLD Revision: 02.02.00.03:Dec 24 2015:17:38:37

    PCIe Power Up.
    PLL configured.
    Successfully configured Inbound Translation!
    Successfully configured Outbound Translation!
    Starting link training...
    Link is up.
    Link is up.
    End Point received data.
    End Point sent data to Root Complex, completing the loopback.
    EP sending interrupts to RC
    Root Complex received data.
    RC waiting for 10 of each of 2 types of interrupts
    RC got all 20 interrupts
    Test passed.
    End of Test.

|

Debug FAQ
---------

**If example fails to get link up**

   #. Confirm that male/male cross cable or breakout board is correctly
      connected.
   #. If running from ARM cores, confirm that immediately after
      reset/reload that both devices have PcieModeGbl=PCIE_EP_MODE. If
      the PCIE_RC_MODE seems to survive reset/reload, it seems to mean
      watch window failed to refresh. Click the "Refresh" button for the
      watch window and it should flip back to EP, where you can reset it
      to RC. Simply running will cause both sides to run as EP, which
      leads to test failure.
   #. Confirm that one side of the example has PcieModeGbl=PCIE_RC_MODE
      and the other is PCIE_EP_MODE.

      .. note:: When changing to RC you must click somewhere outside
         the expression value to make the modification for RC to "take
         effect". Simply pressing F8 after modifying the value will run
         without actually modifying the variable! The modification will
         be done when the ARM or DSP is stopped, **so everything looks
         right, except that the log will show "PCIe test start EP mode"
         twice** instead of "PCIe test start EP mode" once and "PCIe
         test start RC mode" once.

**How to debug common PCIe issues**

Please refer to `PCI Express (PCIe)
FAQ <http://www.ti.com/lit/an/sprac59a/sprac59a.pdf>`__ for Keystone devices.


Additional References
---------------------

Additional documentation can be found in:

+-----------------------------------+---------------------------------------------+
| **Document**                      | **Location**                                |
+-----------------------------------+---------------------------------------------+
| Hardware Peripheral Users Guide   | -  C66x/K2x: `User                          |
|                                   |    Guide <http://www.ti.com/lit/sprugs6>`__ |
|                                   |                                             |
|                                   | -  AM57XX: TRM Chapter 24.9                 |
|                                   |    titled "PCIe Controller"                 |
|                                   |                                             |
|                                   | -  AM65XX: TRM Chapter 12.2.2               |
|                                   |    titled "Peripheral Component Controller  |
|                                   |    Interconnect Express (PCIe)              |
|                                   |    Subsystem"                               |
|                                   |                                             |
+-----------------------------------+---------------------------------------------+
| API Reference Manual              | $(TI_PDK_INSTALL_DIR)/packages/ti           |
|                                   | /drv/pcie/docs/doxygen/html/index           |
|                                   | .html                                       |
+-----------------------------------+---------------------------------------------+
| Release Notes                     | $(TI_PDK_INSTALL_DIR)/packages/ti           |
|                                   | /drv/pcie/docs/ReleaseNotes_PCIE_LLD.pdf    |
+-----------------------------------+---------------------------------------------+

|
