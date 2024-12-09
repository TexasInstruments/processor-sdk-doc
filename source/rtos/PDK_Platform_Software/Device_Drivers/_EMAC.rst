.. http://http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_EMAC

Introduction
-------------

EMAC driver provides a well defined API layer which allows
applications to use the EMAC peripheral to control the flow of packet
data from the processor to the PHY and the MDIO module to control PHY
configuration and status monitoring. EMAC driver is a common driver for
supporting all 1 Gigabit Network interfaces including CPSW and ICSSG
for applicable SOC's.

Driver Configuration
---------------------

Board Specific Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All the board specific configurations eg:enabling and pin-mux of
RGMII/MDIO pins should be performed before calling any driver APIs. By
default Board_Init() API supports all initialization sequence for TI
supported EVMs.Refer `Processor SDK RTOS Board
Support <index_board.html#board-support>`__ for additional
details.

Once the board specific configuration is complete driver API emac_open()
can be called to initialize driver

.. rubric:: **EMAC Configuration Structure**
   :name: EMAC-configuration-structure

The emac_soc.c file binds driver with hardware attributes on the board
through EMAC_Cfg structure. This structure must be provided to EMAC
driver. It must be initialized before the emac_open() function is
called.

For details about individual fields of this structure, see the Doxygen
help by opening
PDK_INSTALL_DIR\\packages\\ti\\drv\\emac\\docs\\doxygen\\html\\index.html.

APIs
-----

API reference for application:

::

    #include <ti/drv/emac/emac_drv.h>

.. rubric:: API Call Flow
   :name: api-call-flow

The below sequence indicates the calling sequence of EMAC driver
APIs for a use case of an EMAC example which implements a single
Ethernet MAC port. This example call flow is illustrated using port
number 0.

.. code-block:: c

    port_num = 0;

    Board_initCfg cfg = BOARD_INIT_UART_STDIO | BOARD_INIT_PINMUX_CONFIG | BOARD_INIT_MODULE_CLOCK  | BOARD_INIT_ETH_PHY;

    Board_init(boardCfg);

    /* Update emac_cfg with SOC specific config required by the driver */
    /* Do a socGet, update emac_cfg as required and followed by socSet */
    EMAC_socGetInitCfg(port_num, &emac_cfg);
    ...
    EMAC_socSetInitCfg(port_num, &emac_cfg);
    ...
    /* For UDMA based DMA interface, init the UDMA driver */
    retVal = Udma_init(&gUdmaDrvObj, &initPrms);
    ....
    /* Populate open_cfg structure with application specific configuration */
    retVal = emac_open(port_num, &open_cfg)
    ....
    /* Provide RX filter configuration (currently
       only applicable for C6657 & OMAPL13x SOCs */
    retVal = emac_config(port_num, &cfg_info);
    ....
    /* For SOCs with CPSW ports, query driver for CPSW statistics */
    retVal = emac_get_statistics(port_num, &stats);
    ....
    /* For SOCs with ICSSG ports, query driver for ICSSG hardware statistics */
    retVal = emac_get_statistics_icssg(port_num, &stats, clear);

At this point EMAC driver is ready to send and receive packets.

.. code-block:: c

    /* Provide a context to poll the driver for received packets, showing RTOS use case */
    Task_create(app_test_task_poll_pkt, &taskParams, NULL);
    /* Sample implementation of task context */
    app_test_task_pol_pkt(UArg arg0, UArg arg1)
    {
        while (1)
        {
            /* AM65xx supports optional mode of direct polling of RX queue for packets which can be
	       configured at time of emac_open.  This mode of operation does not use
	       interrupts. Note that default mode is via use of interrupts*/
            emac_poll_pkt(port_num);
        }
    }

    /* Provide a context to poll the driver for link status, showing RTOS use case */
    Task_create(app_test_task_poll_link, &taskParams, NULL);
    /* Sample implementation of task context */
    app_test_task_pol_link(UArg arg0, UArg arg1)
    {
        EMAC_LINK_INFO_T linkInfo;
        do
        {
            emac_poll(port_num, &linkInfo);
            Osal_delay(1000);
            UART_printf("Link for port %d is DOWN\n", port_num);
        } while(linkInfo.link_status == EMAC_LINKSTATUS_NOLINK);

	UART_printf("Link for port %d is UP\n", port_num);
    }

    /* Close port and release all resources allocated at time of emac_open */
    retVal = emac_close(port_num);

|


Interposer Card Support
------------------------
Interposer card is an ethernet wiring adapter to let 2 ICSSG subsystems drive 2 ethernet ports with DUAL MAC or SWITCH firmware.
So that each direction (TX/RX) can be handled by one pair of PRU cores.
The interposer card permits the power of two ICSSG instances to be used on a two port switch or dual EMAC as opposed to the two-port, single ICSSG configuration.
The following diagrams show the PRU-ICSSG RGMII TX/RX mapping to the physical ports for Maxwell and then for Maxwell with interposer card configured.
Interposer card functionality can be verified by running the icssg-emac DIAG test( Refer `Processor SDK RTOS Board
Support <index_board.html#board-support>`__ for additional details ) or the emac LLD test
application (Emac_Icssg_TestApp described below).
Note that prior to running these tests on Maxwell with interposer card, please hook up an ethernet cable between PHY0 and PHY1.


.. rubric:: Interposer Layout
   :name: Interposer Layout

.. Image:: /images/Interposer.png

Example and Test Applications
------------------------------

+------------------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| Name                         | Description           | Expected Results      | SOC Suppported        | Build Type            |
+==============================+=======================+=======================+=======================+=======================+
| EMAC_BasicExample            | EMAC Loopback test    | Unit Test will        |    AM335x,            |  CCS project          |
|                              | at CPSW switch        | print "All tests      |    AM437x,            |                       |
|                              | interface.            | have passed" via      |    AM572x,            |                       |
|                              | Reference example     | UART console.         |    AM571x,            |                       |
|                              | for developers        |                       |    AM574x,            |                       |
|                              |                       |                       |    K2G                |                       |
|                              | Example demonstrates  |                       |                       |                       |
|                              | loopback capability   |                       |                       |                       |
|                              | by sending dummy      |                       |                       |                       |
|                              | broadcast packet to   |                       |                       |                       |
|                              | CPSW switch. Unit     |                       |                       |                       |
|                              | test registers        |                       |                       |                       |
|                              | receive packet        |                       |                       |                       |
|                              | callback routine with |                       |                       |                       |
|                              | LLD to be called for  |                       |                       |                       |
|                              | RX packet. Call back  |                       |                       |                       |
|                              | routine will extract  |                       |                       |                       |
|                              | packet received,      |                       |                       |                       |
|                              | perform simple memory |                       |                       |                       |
|                              | comparison against    |                       |                       |                       |
|                              | packet sent for       |                       |                       |                       |
|                              | integrity check. Unit |                       |                       |                       |
|                              | test will iterate     |                       |                       |                       |
|                              | over configured       |                       |                       |                       |
|                              | packet count for      |                       |                       |                       |
|                              | packet transmission   |                       |                       |                       |
|                              | and reception check.  |                       |                       |                       |
+------------------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| EMAC_SMP_BasicExample        | EMAC Loopback test    | Unit Test will        |     AM572x-EVM        |  CCS project          |
|                              | at CPSW switch        | print "All tests      |                       |                       |
|                              | interface with SMP    | have passed" via      |                       |                       |
|                              | enabled.              | UART console.         |                       |                       |
|                              | (A15 core only)       |                       |                       |                       |
|                              |                       |                       |                       |                       |
|                              |                       |                       |                       |                       |
+------------------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| EMACLoopback_testProj        | EMAC Loopback test    | Unit Test will        |  C6657,               | CCS project           |
| ect                          | at CPSW switch        | print "Loopback       |  DRA7xx,              |                       |
|                              | interface.            | Test completed        |  OMAPL137,            |                       |
|                              | Reference example     | successfully on       |  OMAPL138             |                       |
|                              | for developers        | core 0" via CCS       |                       |                       |
|                              |                       | console for C6657     |                       |                       |
|                              | Example demonstrates  | and on UART serial    |                       |                       |
|                              | loopback capability   | console for           |                       |                       |
|                              | by sending dummy      | OMAPL13x.             |                       |                       |
|                              | broadcast packet to   |                       |                       |                       |
|                              | CPSW switch. Unit     |                       |                       |                       |
|                              | test registers        |                       |                       |                       |
|                              | receive packet        |                       |                       |                       |
|                              | callback routine with |                       |                       |                       |
|                              | LLD to be called for  |                       |                       |                       |
|                              | RX packet. Call back  |                       |                       |                       |
|                              | routine will extract  |                       |                       |                       |
|                              | packet received,      |                       |                       |                       |
|                              | perform simple memory |                       |                       |                       |
|                              | comparison against    |                       |                       |                       |
|                              | packet sent for       |                       |                       |                       |
|                              | integrity check. Unit |                       |                       |                       |
|                              | test will iterate     |                       |                       |                       |
|                              | over configured       |                       |                       |                       |
|                              | packet count for      |                       |                       |                       |
|                              | packet transmission   |                       |                       |                       |
|                              | and reception check.  |                       |                       |                       |
|                              |                       |                       |                       |                       |
|                              | This example needs to |                       |                       |                       |
|                              | be run on the         |                       |                       |                       |
|                              | OMAPL137 and OMAPL138 |                       |                       |                       |
|                              | platforms using       |                       |                       |                       |
|                              | external loopback     |                       |                       |                       |
|                              | cable. OMAPL137 EVM   |                       |                       |                       |
|                              | is having two         |                       |                       |                       |
|                              | Ethernet ports.       |                       |                       |                       |
|                              | Connect the loopback  |                       |                       |                       |
|                              | cable to the port 1   |                       |                       |                       |
|                              | (ENET-P1) while       |                       |                       |                       |
|                              | running the loopback  |                       |                       |                       |
|                              | example.              |                       |                       |                       |
+------------------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| EMAC_PktInspectionExa        | This demonstrates how | Pass criteria:        |  DRA7xx               | CCS project           |
| mple                         | to write an           |                       |                       |                       |
|                              | application to filter | -  The total packet   |                       |                       |
|                              | Ethernet packets      |    sent for each      |                       |                       |
|                              | based on IP address   |    stream is shown at |                       |                       |
|                              |                       |    the bottom of the  |                       |                       |
|                              |                       |                       |                       |                       |
|                              | Prerequisites:        |    packETH widow. The |                       |                       |
|                              |                       |    packet stream      |                       |                       |
|                              | -  Install the        |    statistics must    |                       |                       |
|                              |    packETH utility (v |    match the packet   |                       |                       |
|                              |    1.8.1) on a Linux  |    statistics printed |                       |                       |
|                              |    PC. The packETH    |    by the DUT via     |                       |                       |
|                              |    tool is available  |    serial port        |                       |                       |
|                              |    for Windows as     | -  The packet         |                       |                       |
|                              |    well, but not all  |    inspection utility |                       |                       |
|                              |    features are       |    periodically       |                       |                       |
|                              |    supported          |    prints the EMAC    |                       |                       |
|                              | -  Download the test  |    statistics, which  |                       |                       |
|                              |    PCAP `files`_      |    include DMA        |                       |                       |
|                              |                       |    overruns,          |                       |                       |
|                              |                       |    underruns and      |                       |                       |
|                              |    and update the     |    other error. No    |                       |                       |
|                              |    source and dest    |    errors should be   |                       |                       |
|                              |    MAC address of the |    seen during the    |                       |                       |
|                              |    PC and EVM to be   |    transfer.          |                       |                       |
|                              |    used in the test.  |                       |                       |                       |
|                              |    The tcprewrite     | Fail criteria:        |                       |                       |
|                              |    utility can be     |                       |                       |                       |
|                              |    used to set the    | -  Packet count       |                       |                       |
|                              |    new MAC addresses  |    mismatch between   |                       |                       |
|                              |    (i.e. tcprewrite   |    packETH utility    |                       |                       |
|                              |    --enet-smac=<PC-MA |    and counters from  |                       |                       |
|                              | C-address>            |    the IPU1           |                       |                       |
|                              |    --enet-dmac=<EVM-M |    application        |                       |                       |
|                              | AC-address>           | -  Any EMAC errors    |                       |                       |
|                              |    -i ./ip1_test.pcap |    reported by the    |                       |                       |
|                              |    -o                 |    IPU1 application   |                       |                       |
|                              |    ./ip1_test.pcap)   |                       |                       |                       |
|                              |                       |                       |                       |                       |
|                              | Steps:                |                       |                       |                       |
|                              |                       |                       |                       |                       |
|                              | -  Launch the packETH |                       |                       |                       |
|                              |    utility on the     |                       |                       |                       |
|                              |    Linux PC with root |                       |                       |                       |
|                              |    permissions        |                       |                       |                       |
|                              | -  Go to the "Gen-S"  |                       |                       |                       |
|                              |    tab of the packETH |                       |                       |                       |
|                              |    utility and select |                       |                       |                       |
|                              |    the PCAP files to  |                       |                       |                       |
|                              |    be used            |                       |                       |                       |
|                              | -  Set the transfer   |                       |                       |                       |
|                              |    rate for each PCAP |                       |                       |                       |
|                              |    file (i.e. 200     |                       |                       |                       |
|                              |    Mbit/s and 150     |                       |                       |                       |
|                              |    Mbit/s)            |                       |                       |                       |
|                              | -  Set the total      |                       |                       |                       |
|                              |    packets to         |                       |                       |                       |
|                              |    transfer to 500000 |                       |                       |                       |
|                              | -  Load and run the   |                       |                       |                       |
|                              |    EMAC packet        |                       |                       |                       |
|                              |    inspection         |                       |                       |                       |
|                              |    application to the |                       |                       |                       |
|                              |    IPU1 core          |                       |                       |                       |
|                              | -  Hit the "Send"     |                       |                       |                       |
|                              |    button on the      |                       |                       |                       |
|                              |    packETH utility to |                       |                       |                       |
|                              |    start streaming    |                       |                       |                       |
|                              | -  The packet         |                       |                       |                       |
|                              |    streaming should   |                       |                       |                       |
|                              |    last for few       |                       |                       |                       |
|                              |    seconds            |                       |                       |                       |
+------------------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| Emac_Cpsw_TestApp            | EMAC Loopback test    | Unit Test will        | AM65xx,               | makefile              |
|                              | at CPSW switch        | print "All tests      | J721E                 |                       |
|                              | interface.            | have passed" via      |                       |                       |
|                              | Reference application | UART console.         |                       |                       |
|                              | for developers        |                       |                       |                       |
|                              |                       |                       |                       |                       |
|                              | TestApp demonstrates  |                       |                       |                       |
|                              | loopback capability   |                       |                       |                       |
|                              | by sending packets to |                       |                       |                       |
|                              | CPSW switch. Unit     |                       |                       |                       |
|                              | test registers        |                       |                       |                       |
|                              | receive packet        |                       |                       |                       |
|                              | callback routine with |                       |                       |                       |
|                              | LLD to be called for  |                       |                       |                       |
|                              | RX packet. Call back  |                       |                       |                       |
|                              | routine will extract  |                       |                       |                       |
|                              | packet received,      |                       |                       |                       |
|                              | perform simple memory |                       |                       |                       |
|                              | comparison against    |                       |                       |                       |
|                              | packet sent for       |                       |                       |                       |
|                              | integrity check. Unit |                       |                       |                       |
|                              | test will iterate     |                       |                       |                       |
|                              | over configured       |                       |                       |                       |
|                              | packet count for      |                       |                       |                       |
|                              | packet transmission   |                       |                       |                       |
|                              | and reception check.  |                       |                       |                       |
+------------------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| Emac_Cpsw_SMP_TestApp        | EMAC Loopback test    | Unit Test will        | AM65xx                | makefile              |
|                              | at CPSW switch        | print "All tests      |                       |                       |
|                              | interface with SMP    | have passed" via      |                       |                       |
|                              | enabled               | UART console.         |                       |                       |
|                              | (A53 core only)       |                       |                       |                       |
|                              |                       |                       |                       |                       |
+------------------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| Emac_Icssg_TestApp           | EMAC port 2 port test | Unit Test will        | AM65xx                | makefile              |
|                              | between ICSSG ports.  | print "All tests      |                       |                       |
|                              | Reference application | have passed" via      |                       |                       |
|                              | for developers        | UART console          |                       |                       |
|                              |                       |                       |                       |                       |
|                              | Prior to running this |                       |                       |                       |
|                              | test, please connect  |                       |                       |                       |
|                              | the ICSSG ports as    |                       |                       |                       |
|                              | follows with          |                       |                       |                       |
|                              | ethernet cables:      |                       |                       |                       |
|                              |                       |                       |                       |                       |
|                              | PHY0 to PHY1          |                       |                       |                       |
|                              |                       |                       |                       |                       |
|                              | PHY2 to PHY3          |                       |                       |                       |
|                              |                       |                       |                       |                       |
|                              | PHY4 to PHY5          |                       |                       |                       |
|                              |                       |                       |                       |                       |
|                              | Test app demonstrates |                       |                       |                       |
|                              | packet TX/RX between  |                       |                       |                       |
|                              | 2 ICSSG ports. All 6  |                       |                       |                       |
|                              | ICSSG ports will be   |                       |                       |                       |
|                              | tested for am65xx-idk.|                       |                       |                       |
|                              | PRU2 ports will be    |                       |                       |                       |
|                              | tested for am65xx-evm.|                       |                       |                       |
|                              | Unit test registers   |                       |                       |                       |
|                              | receive packet        |                       |                       |                       |
|                              | callback routine with |                       |                       |                       |
|                              | LLD to be called for  |                       |                       |                       |
|                              | RX packet. Call back  |                       |                       |                       |
|                              | routine will extract  |                       |                       |                       |
|                              | packet received,      |                       |                       |                       |
|                              | perform simple memory |                       |                       |                       |
|                              | comparison against    |                       |                       |                       |
|                              | packet sent for       |                       |                       |                       |
|                              | integrity check. Unit |                       |                       |                       |
|                              | test will iterate     |                       |                       |                       |
|                              | over configured       |                       |                       |                       |
|                              | packet count for      |                       |                       |                       |
|                              | packet transmission   |                       |                       |                       |
|                              | and reception check.  |                       |                       |                       |
+------------------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| Emac_Icssg_Switch_TestApp    | Switch port 2 port    | Unit Test will        | AM65xx                | makefile              |
|                              | test between ICSSG    | print "All tests      |                       |                       |
|                              | ports.                |                       |                       |                       |
|                              | Reference application | have passed" via      |                       |                       |
|                              | for developers        | UART console          |                       |                       |
|                              |                       |                       |                       |                       |
|                              | Prior to running this |                       |                       |                       |
|                              | test, please connect  |                       |                       |                       |
|                              | the ICSSG ports as    |                       |                       |                       |
|                              | follows with          |                       |                       |                       |
|                              | ethernet cables:      |                       |                       |                       |
|                              |                       |                       |                       |                       |
|                              | PHY0 to PHY1          |                       |                       |                       |
|                              |                       |                       |                       |                       |
|                              | Test app demonstrates |                       |                       |                       |
|                              | packet TX/RX between  |                       |                       |                       |
|                              | 2 ICSSG Switch ports. |                       |                       |                       |
|                              | Unit test registers   |                       |                       |                       |
|                              | receive packet        |                       |                       |                       |
|                              | callback routine with |                       |                       |                       |
|                              | LLD to be called for  |                       |                       |                       |
|                              | RX packet. Call back  |                       |                       |                       |
|                              | routine will extract  |                       |                       |                       |
|                              | packet received,      |                       |                       |                       |
|                              | perform simple memory |                       |                       |                       |
|                              | comparison against    |                       |                       |                       |
|                              | packet sent for       |                       |                       |                       |
|                              | integrity check. Unit |                       |                       |                       |
|                              | test will iterate     |                       |                       |                       |
|                              | over configured       |                       |                       |                       |
|                              | packet count for      |                       |                       |                       |
|                              | packet transmission   |                       |                       |                       |
|                              | and reception check.  |                       |                       |                       |
+------------------------------+-----------------------+-----------------------+-----------------------+-----------------------+


Support for Benchmark Testing
------------------------------

+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| Name                  | Description           | Expected Results      | SOC Suppported        | Build Type            |
+=======================+=======================+=======================+=======================+=======================+
| Emac_Icssg_TestApp    | Test application with | Test applicaiton      |  am65xx               | make                  |
|                       | modifications can     | will print "polling   |                       |                       |
|                       | used for performance  | rx packets on port 4" |                       |                       |
|                       | benchmarking          | via the UART console  |                       |                       |
|                       |                       |                       |                       |                       |
|                       |                       | Every 60 seconds,     |                       |                       |
|                       | In order to run the   | a sub-set of hardware |                       |                       |
|                       | test application in   | statistics will be    |                       |                       |
|                       | benchamrk mode you    | displayed via UART    |                       |                       |
|                       | need to update        | console               |                       |                       |
|                       | ti/drv/emac/test/     |                       |                       |                       |
|                       | EmacLoopbackTest/     |                       |                       |                       |
|                       | test_loc.h to enable  |                       |                       |                       |
|                       | EMAC_BENCHMARK macro  |                       |                       |                       |
|                       |                       |                       |                       |                       |
|                       |                       |                       |                       |                       |
|                       | Connect external      |                       |                       |                       |
|                       | packet generator to   |                       |                       |                       |
|			| PHY4.                 |                       |                       |                       |
|                       |                       |                       |                       |                       |
|                       | The unit test will    |                       |                       |                       |
|                       | poll the RX packet    |                       |                       |                       |
|                       | channel/ring for the  |                       |                       |                       |
|                       | port being testing and|                       |                       |                       |
|                       | will loop the packet  |                       |                       |                       |
|                       | back to the external  |                       |                       |                       |
|                       | traffic generator with|                       |                       |                       |
|                       | "no touch" to the     |                       |                       |                       |
|                       | packet                |                       |                       |                       |
|                       |			|                       |                       |                       |
+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| Emac_Cpsw_TestApp     | Test application with | Test application      |  am65xx               | make                  |
|                       | modifications can     | will print "polling   |                       |                       |
|                       | used for performance  | rx packets on port 6" |                       |                       |
|                       | benchmarking          | via the UART console  |                       |                       |
|                       |                       |                       |                       |                       |
|                       |                       | Every 60 seconds,     |                       |                       |
|                       | In order to run the   | a sub-set of hardware |                       |                       |
|                       | test application in   | statistics will be    |                       |                       |
|                       | benchamrk mode you    | displayed via UART    |                       |                       |
|                       | need to update        | console               |                       |                       |
|                       | ti/drv/emac/test/     |                       |                       |                       |
|                       | EmacLoopbackTest/     |                       |                       |                       |
|                       | test_loc.h to enable  |                       |                       |                       |
|                       | EMAC_BENCHMARK macro  |                       |                       |                       |
|                       |                       |                       |                       |                       |
|                       | To benchmark ICSSG    |                       |                       |                       |
|                       | connect external      |                       |                       |                       |
|                       | packet generator to   |                       |                       |                       |
|			| PHY4.                 |                       |                       |                       |
|                       |                       |                       |                       |                       |
|                       | To benchmark CPSW     |                       |                       |                       |
|                       | connect external      |                       |                       |                       |
|                       | packet generator to   |                       |                       |                       |
|                       | CPSW port             |                       |                       |                       |
|                       |                       |                       |                       |                       |
|                       | The unit test will    |                       |                       |                       |
|                       | poll the RX packet    |                       |                       |                       |
|                       | channel/ring for the  |                       |                       |                       |
|                       | port being testing and|                       |                       |                       |
|                       | will loop the packet  |                       |                       |                       |
|                       | back to the external  |                       |                       |                       |
|                       | traffic generator with|                       |                       |                       |
|                       | "no touch" to the     |                       |                       |                       |
|                       | packet                |                       |                       |                       |
|                       |			|                       |                       |                       |
+-----------------------+-----------------------+-----------------------+-----------------------+-----------------------+


Building EMAC Test applications via makefiles
----------------------------------------------

-  EMAC Test applications and dependent libraries are built from the top level emac
   makefile
-  Refer to the `Processor SDK RTOS Getting Started Guide <index_overview.html#setup-environment>`__  for details
   of how to setup the build environment. Once you have setup the build environment, issue the following commands:

    -  cd <pdk>/packages/
    -  To build: make emac
    -  To clean: make emac_clean

- Similarly, to build at the module level, issue the following commands for rebuilding :

    - cd <pdk>/packages/ti/drv/emac
    - To build: make all
    - To clean: make clean


Running EMAC Examples and Test applications
--------------------------------------------

.. rubric::  *Description*
   :name: description

EMAC Test applications demonstrates the key features of the driver.

|

.. rubric::  **Running the EMAC Test applications**
   :name: running-the-emac-Test applications

**Via CCS connection**:

-  Load the System firmware as specified in SCICLIENT documentation for AM65xx SOC
-  Load the generated executable file in CCS
-  Run the application.
-  The application print will be displayed on the CCS and UART console. The UART console used depends on the core in which the application is run.


**Via Secondary Bootloader (SBL)**:

EMAC Test applications can also be run via SBL. To run via SBL, please following the instructions as specified in the following link:
`SBL User Guide <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index_Foundational_Components.html#am655x-compiling-apps-for-sbl>`__

.. _files: :download:`</images/Pcap.zip>`

Additional References
----------------------

+-----------------------------------+-----------------------------------------+
|           **Document**            |           **Location**                  |
+-----------------------------------+-----------------------------------------+
| API Reference Manual              | $(TI_PDK_INSTALL_DIR)\\packages\\ti     |
|                                   | \\drv\\emac\\docs\\doxygen\\html\\index |
|                                   | .html                                   |
+-----------------------------------+-----------------------------------------+
| Release Notes                     | $(TI_PDK_INSTALL_DIR)\\packages\\ti     |
|                                   | \\drv\\emac\\docs\\ReleaseNotes_EMAC_   |
|                                   | LLD.pdf                                 |
+-----------------------------------+-----------------------------------------+
| Software Design                   | $(TI_PDK_INSTALL_DIR)\\packages\\ti     |
|                                   | \\drv\\emac\\docs\\EMAC_LLD_SD.pdf      |
+-----------------------------------+-----------------------------------------+

