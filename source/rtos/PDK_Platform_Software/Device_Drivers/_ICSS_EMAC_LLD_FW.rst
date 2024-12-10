Introduction
-------------

The ICSS_EMAC (industrial communications subsystem Ethernet Media Access
Controller) driver provide APIs to transmit and receive packets with a
firmware based Ethernet switch that has been implemented on TI’s
PRU-ICSS (Programmable Real-Time Unit Subsystem and Industrial
Communication SubSystem) 32-bit RISC cores.

|

.. rubric::  Software Architecture
   :name: software-architecture

The ICSS EMAC low level driver can be partitioned into the following:

-  Driver software running on the host processor, provides a well
   defined set of APIs to configure the driver, send packets to the
   firmware and receive packet from the firmware.
-  Firmware which implements a 2 port ethernet switch supporting 802.1d
   @100 Mbps. This runs on the TI-PRU-ICSS cores.

|

.. rubric::  Driver Features
   :name: driver-features

ICSS_EMAC LLD implements following:

-  Rx - Copying packet received from firmware and providing it to TCP/IP
   stack
-  Tx - Providing packet from TCP/IP stack to firmware
-  Learning/Forwarding Data Base
-  Storm Prevention implementation
-  Host Statistics implementation
-  TCP/IP stack related initialization
-  Configuring IP address
-  ARM interrupt management


For details of the driver, please refer to
  `[1] <http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_ICSS-EMAC-Design>`__

|

User Interface
----------------

Driver Configuration
^^^^^^^^^^^^^^^^^^^^^

| **Board Specific Configuration**
| All the board specific configurations eg: enabling clock and pin-mux
  for GPIO/MDIP/IEP pins should be performed before calling any driver
  APIs. By default Board_Init() API supports all initialization sequence
  for TI supported EVMs. In addition it initializes UART instance for
  Console/STDIO.Refer `Processor SDK RTOS Board
  Support <index_board.html#board-support>`__ for
  additional details.Once board specific configuration is complete
  driver APIS can be invoked.

|
| **ICSS_EMAC Configuration Structure**
| The icss_emacSoc.c file contains the declaration of the hardware
  attributes corresponding to the ICSS_EMAC subsystem. Hardware
  attributes includes base address of various sub-subsystems required by
  the the ICSS_EMAC LLD. This configuration is required and needs to be
  passed in as part of the ICSS_EMAC Handle when calling the
  icss_emacInit API. For details about individual fields of this
  structure, see the Doxygen help by opening
  PDK_INSTALL_DIR\\packages\\ti\\drv\\icss_emac\\docs\\doxygen\\html\\index.html.

|

APIs
^^^^^

API reference for application:

::

    #include <ti/drv/icss_emac/icss_emacDrv.h>

.. rubric:: API Call Flow
   :name: api-call-flow

The below sequence indicates the calling sequence of ICSS_EMAC driver
APIs for a use case of an EMAC example which implements single Ethernet
MAC using PRU-ICSS Instance 2, ETH0. For additional details refer
example inside package

::

    ...
    Board_init(cfg);

    /* Perform MDIO init */
    ICSS_EMAC_testMdioInit(CSL_MPU_PRUSS2_U_MII_MDIO_REGS);

::

    /* Create handle for PRUICSS instance*/
    ICSS_EMAC_testPruIcssHandle2= PRUICSS_create(pruss_config,2);

    /* Setup crossbar configuration to receive PRU-ICSS interrupts and map them to A15 (illustration for PRU2ETH0) */
    CSL_xbarDspIrqConfigure(..);  /* Link ISR */
    CSL_xbarDspIrqConfigure(..);  /* RX PKT ISR */
    CSL_xbarDspIrqConfigure(..);  /* TX PKT ISR */

::

    /*Initialize driver */
    ...
    ICSS_EmacInit(..);

    /* Register callbacks for RX/TX, Link Interrupts, these are called in context of ISR */
    ICSS_EmacRegisterPort0ISRCallback(..);
    ICSS_EmacRegisterHwIntRx(..);
    ICSS_EmacRegisterHwIntTx(..);

::

    /* Enable interrupts for RX/TX/Link*/
    ICSS_EMAC_testInterruptInit(ICSS_EMAC_testHandle2);

::

    /* Enable Link Interrupt in MDIO sub-system */
    ICSS_EMAC_testMdioEnableLinkInterrupt(..);

::

    /* At this point, ICSS_EMAC LLD APIs can be called */
    </syntaxhighlight>

.. rubric::  Firmware
   :name: firmware

TI PRU-ICSS cores (Programmable Real-Time Unit Industrial Communication
Subsystem) is firmware programmable and can take on various
personalities. Examples include an SORTE, ethernet Switch, Industrial
protocol switch. Please refer to `ICSS-EMAC Firmwares <index_pru_icss_fw.html#pru-icss-firmware>`__ for
further explanation.

|

Application
------------

Examples
^^^^^^^^^

Refer “ICSS_EMAC_<Basic/Switch>Example_<SOC>_<CPU>Testproject” for
additional reference. Refer Release Note for ICSS_EMAC supported on
different EVMs.


+-----------------+-----------------+-----------------+-----------------+
|| Name           || Description    || EVM            || Expected       |
|                 |                 | Configuration   | Results         |
+=================+=================+=================+=================+
| ICSS_EMAC_Basic | EMAC Loopback   | 10/100 Mb/s     | Unit Test will  |
| Example         | test at         | loopback cable  | print ^All      |
|                 | PRU-ICSS        |                 | tests have      |
|                 | EMAC PHY.       |                 | passed^ via     |
|                 |                 |                 | UART console.   |
|                 | | Example       |                 |                 |
|                 |   demonstrates  |                 |                 |
|                 |   loopback      |                 |                 |
|                 |   capability by |                 |                 |
|                 |   sending dummy |                 |                 |
|                 |   broadcast     |                 |                 |
|                 |   packet to     |                 |                 |
|                 |   PRU-ICSS      |                 |                 |
|                 |   instance 2,   |                 |                 |
|                 |   ethernet port |                 |                 |
|                 |   0 (PRU ETH0). |                 |                 |
|                 |   Unit test     |                 |                 |
|                 |   registers     |                 |                 |
|                 |   receive       |                 |                 |
|                 |   packet        |                 |                 |
|                 |   callback      |                 |                 |
|                 |   routine with  |                 |                 |
|                 |   LLD to be     |                 |                 |
|                 |   called for RX |                 |                 |
|                 |   packet. Call  |                 |                 |
|                 |   back routine  |                 |                 |
|                 |   will extract  |                 |                 |
|                 |   packet        |                 |                 |
|                 |   received,     |                 |                 |
|                 |   perform       |                 |                 |
|                 |   simple memory |                 |                 |
|                 |   comparison    |                 |                 |
|                 |   against       |                 |                 |
|                 |   packet sent   |                 |                 |
|                 |   for integrity |                 |                 |
|                 |   check. Unit   |                 |                 |
|                 |   test will     |                 |                 |
|                 |   iterate 10    |                 |                 |
|                 |   times for     |                 |                 |
|                 |   packet        |                 |                 |
|                 |   transmission  |                 |                 |
|                 |   and reception |                 |                 |
|                 |   check.        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| ICSS_EMAC_Switc | Switch Loopback | 100 Mb/s        | Unit Test will  |
| hExample        | test at         | loopback cable  | print ^All      |
|                 | PRU-ICSS        |                 | tests have      |
|                 | EMAC PHY.       |                 | passed^ via     |
|                 |                 |                 | UART console.   |
|                 | | Example       |                 |                 |
|                 |   demonstrates  |                 |                 |
|                 |   switch        |                 |                 |
|                 |   learning      |                 |                 |
|                 |   loopback      |                 |                 |
|                 |   capability by |                 |                 |
|                 |   sending dummy |                 |                 |
|                 |   broadcast     |                 |                 |
|                 |   packet to     |                 |                 |
|                 |   PRU-ICSS      |                 |                 |
|                 |   instance,     |                 |                 |
|                 |   ethernet      |                 |                 |
|                 |   port. Unit    |                 |                 |
|                 |   test          |                 |                 |
|                 |   registers     |                 |                 |
|                 |   receive       |                 |                 |
|                 |   packet        |                 |                 |
|                 |   callback      |                 |                 |
|                 |   routine with  |                 |                 |
|                 |   LLD to be     |                 |                 |
|                 |   called for RX |                 |                 |
|                 |   packet. Call  |                 |                 |
|                 |   back routine  |                 |                 |
|                 |   will extract  |                 |                 |
|                 |   packet        |                 |                 |
|                 |   received,     |                 |                 |
|                 |   perform       |                 |                 |
|                 |   simple memory |                 |                 |
|                 |   comparison    |                 |                 |
|                 |   against       |                 |                 |
|                 |   packet sent   |                 |                 |
|                 |   for integrity |                 |                 |
|                 |   check. As     |                 |                 |
|                 |   with switch   |                 |                 |
|                 |   for every 1   |                 |                 |
|                 |   transmitted   |                 |                 |
|                 |   packet,       |                 |                 |
|                 |   firmware will |                 |                 |
|                 |   respond back  |                 |                 |
|                 |   with 2        |                 |                 |
|                 |   recieved      |                 |                 |
|                 |   packets. Unit |                 |                 |
|                 |   test will     |                 |                 |
|                 |   iterate 10    |                 |                 |
|                 |   times for     |                 |                 |
|                 |   packet        |                 |                 |
|                 |   transmission  |                 |                 |
|                 |   and reception |                 |                 |
|                 |   check.        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

|

Debug Guide
------------

For debugging ICSS EMAC examples or LLD. Please refer to `ICSS-EMAC
Debug Guide <http://processors.wiki.ti.com/index.php/ICSS_EMAC_LLD_debug_guide>`__.

Additional References
----------------------

+-----------------------------------+------------------------------------------+
| **Document**                      | **Location**                             |
+-----------------------------------+------------------------------------------+
| API Reference Manual              | $(TI_PDK_INSTALL_DIR)\\packages\\ti      |
|                                   | \\drv\\icss_emac\\docs\\doxygen\\html\\  |
|                                   | index.html                               |
+-----------------------------------+------------------------------------------+
| Release Notes                     | $(TI_PDK_INSTALL_DIR)\\packages\\ti      |
|                                   | \\drv\\icss_emac\\docs\\ReleaseNotes_    |
|                                   | ICSS_EMAC_LLD.pdf                        |
+-----------------------------------+------------------------------------------+
| ICSS-EMAC LLD Details             | `[2] <http://processors.wiki.ti.c        |
|                                   | om/index.php/ICSS-EMAC>`__               |
+-----------------------------------+------------------------------------------+

|

