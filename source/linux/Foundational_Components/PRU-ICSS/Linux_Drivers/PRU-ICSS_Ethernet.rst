.. _pru_icss_ethernet:

##################
PRU_ICSSM Ethernet
##################

.. contents::
   :local:
   :depth: 3

************
Introduction
************

As of version 11.0 of the Linux Processor SDK, the evaluation modules
listed below support additional 100 Mbps Ethernet ports through the
PRU-ICSS while running Linux as your host operating system.

This page **DOES NOT** cover any of the industrial protocols that are
supported by the PRU-ICSS while running other host operating systems
(bare metal, StarterWare, TI RTOS, third party, etc).

.. note::

   Starting with the SDK 11.1 release, the Linux driver is not compatible with earlier versions
   of the PRU Ethernet firmware from previous SDK releases. The Linux driver provided
   with this release should be used with the PRU firmware from this release.
   Similarly, the PRU Ethernet firmware from this release is not compatible with earlier versions
   of Linux drivers from before the SDK 11.1 release.

******************
Features supported
******************

- Rx and Tx over PRU Ethernet ports in Dual EMAC mode
- Full duplex with 100 Mbps link speed
- VLAN filtering
- Enhanced multicast filtering
- Promiscuous mode
- Storm prevention
- Interrupt coalescing
- Linux PTP (ptp4l) Ordinary clock
- ethtool support for link status and statistics

********************
Driver Configuration
********************

The TI Processor SDK has ICSSM driver enabled by default on supported platforms.
In case of custom builds, please ensure following configs are enabled.

.. code-block:: text

   CONFIG_TI_PRUSS
   CONFIG_REMOTEPROC
   CONFIG_PRU_REMOTEPROC
   CONFIG_TI_PRUSS_INTC
   CONFIG_TI_DAVINCI_MDIO
   CONFIG_TI_ICSS_IEP
   CONFIG_TI_PRUETH_ECAP

.. rubric:: **Module Build**

Module build for the ICSSM driver is supported. To do this, use option 'm' for above configs, where applicable.

********************
Device tree bindings
********************

The DT bindings description can be found at:

| `Documentation/devicetree/bindings/net/ti,icssm-prueth.yaml <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/Documentation/devicetree/bindings/net/ti,icssm-prueth.yaml?h=ti-linux-6.12.y>`__
| `Documentation/devicetree/bindings/net/ti,davinci-mdio.yaml <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/Documentation/devicetree/bindings/net/ti,davinci-mdio.yaml?h=ti-linux-6.12.y>`__
|

************
How It Works
************

Texas Instruments provides all of the necessary software and firmware in
the Linux Processor SDK to enable the PRU-ICSS Ethernet ports. The PRU
firmware binaries can be found in the :file:`/lib/firmware/ti-pruss/` folder
in the filesystem. A Linux kernel networking driver is provided that can
be found at
:file:`<%LINUX\_PROC\_SDK\_X\_X\_X\_X%>/board-support/linux-x.y.z..../drivers/net/ethernet/ti/icssm/**`.

As the boards boot, the prussN\_eth device tree node causes the
ti-prueth driver to be probed. This probe function does several things
to prepare the PRU-ICSS Ethernet ports:

-  Configures the mux mode of the PRU pins for MII mode
-  Requests ownership of the PRUSS memory regions from the pruss driver
-  Allocates a pool of memory in OCMC SRAM for the Ethernet buffers to
   be passed from the PRU to Linux
-  Initializes a netdev device
-  Registers the network device with Linux

At this point the Linux driver is ready for the new Ethernet interface
to be started. Once the user issues the interface up command (``ifconfig
eth2 up`` for example), the **emac\_ndo\_open** function is called in the
ti-prueth driver which uses the remoteproc interface to boot the PRU
cores with the firmware provided in the :file:`/lib/firmware/ti-pruss/`
folder of the EVM filesystem. The PRUs running this firmware, coupled
with the ti-prueth Linux driver, allows up to 2 additional 100 Mbps
Ethernet interfaces to be exposed to the user.

Block Diagram
=============

This is a high level block diagram to show how everything fits
together. For more information see the schematics for the boards as
well as the Linux driver source code.

.. Image:: /images/Pru_eth_block_diagram_3_0_0_4.PNG

.. ifconfig:: CONFIG_part_variant in ('AM335X')

   -  On the AM3359 ICE there are only two Ethernet ports on the board

      -  In order to use the PRU-ICSS with these ports (instead of the
         CPSW) you need to correctly configure both of the jumpers that
         are located right next to the RJ45 jacks

         -  Jumpers J18 and J19 both need to be set to MII to use
            PRU-ICSS on the ports, you need to reboot the device for
            jumper changes to take effect
         -  If you set both of these jumpers to RMII then the CPSW will
            drive the ports, not the PRU-ICSS
         -  It is not supported to set the two jumpers to different
            values. Both need to be MII (PRU-ICSS) or both need to be
            RMII (CPSW).

.. ifconfig:: CONFIG_part_variant in ('AM437X')

   -  On the AM437x IDK the silkscreen says **PRUETH0** and **PRUETH1**
      for the supported PRU ports

.. ifconfig:: CONFIG_part_variant in ('AM57X')

   -  On the AM571x IDK the silkscreen says **PRU1 ETH0**, **PRU1
      ETH1**, **PRU2 ETH0**, and **PRU2 ETH1** for the supported PRU
      ports

      .. note::

         On the AM571x IDK board, the pins used for PRU1 ETH0 and PRU1 ETH1
         are shared with pins used for the optional LCD touchscreen. U-Boot
         uses jumper **J51** to determine if the LCD touchscreen should be
         enabled or not. If **J51** is closed (jumper is present across the
         two pins), then U-Boot will load a device tree that enables the
         LCD touchscreen and disables PRUSS1 Ethernet ports. This means
         that only **PRU2 ETH0** and **PRU2 ETH1** will be supported if
         jumper **J51** is closed. If **J51** is open (jumper is not
         present across the two pins), then U-Boot will load a device tree
         that enables all four PRUSS Ethernet ports, two from PRUSS1 and
         two from PRUSS2. In this mode, the LCD touchscreen is disabled.

   -  On the AM572x IDK the silkscreen says **PRU2 ETH0** and **PRU2
      ETH1** for the supported PRU ports

******************
Network Topologies
******************

The following network topologies are possible with the PRU-ICSS Ethernet
ports.

Single Port Mode
================

In this mode only one of the PRU-ICSS Ethernet ports are used. This is
the simplest mode and works as you would expect it to.

.. Image:: /images/Pru_eth_block_single_port_3_0_0_4.PNG

Dual MAC mode
=============

One use case made possible with two ports on the same device is to allow
your device to act as a gateway between two different subnets. In this
use case you just need to bring up both ports and then plug them into
the two subnets as shown below.

.. note::

   It is not a normal use case to plug both PRU-ICSS Ethernet ports into
   the same switch (same subnet) out-of-the-box. While it may appear to
   work at first, it will lead to unexpected behavior including (but not
   limited to) packets entering/exiting the device on the opposite port
   that you would expect due to ARP broadcasts and other topics that are
   outside the scope of this document.

.. Image:: /images/Pru_eth_block_gateway_3_0_0_4.PNG

**********
User guide
**********

Bringing Up interface
=====================

The network interface can be configured automatically depending on root file system or configured manually. Manual configuration:

.. code-block:: console

   ip addr add 192.168.1.1/24 dev eth2
   ip link set dev eth2 up

   < or >

   ifconfig eth2 <ip> netmask <mask> up

Get information (ethtool)
=========================

Get driver information
----------------------

The interface can be identified by using ``ethtool -i DEVNAME`` command.
It also provides some information about supported features.

.. code-block:: console

   ~# ethtool -i eth2
   driver: prueth
   version:
   firmware-version:
   expansion-rom-version:
   bus-info: pruss2-eth
   supports-statistics: yes
   supports-test: no
   supports-eeprom-access: no
   supports-register-dump: yes
   supports-priv-flags: no


Display standard information about device/link
----------------------------------------------

Run ``ethtool DEVNAME`` command without parameters.

.. code-block:: console

   ~# ethtool eth2
   Settings for eth2:
         Supported ports: [ TP    MII ]
         Supported link modes:   100baseT/Full
         Supported pause frame use: No
         Supports auto-negotiation: Yes
         Supported FEC modes: Not reported
         Advertised link modes:  100baseT/Full
         Advertised pause frame use: No
         Advertised auto-negotiation: Yes
         Advertised FEC modes: Not reported
         Link partner advertised link modes:  10baseT/Half 10baseT/Full
                                                100baseT/Half 100baseT/Full
         Link partner advertised pause frame use: Symmetric
         Link partner advertised auto-negotiation: Yes
         Link partner advertised FEC modes: Not reported
         Speed: 100Mb/s
         Duplex: Full
         Auto-negotiation: on
         Port: MII
         PHYAD: 0
         Transceiver: external
         Link detected: yes

Display time stamping capabilities
----------------------------------

The interface time stamping capabilities can be retrieved by using  ``ethtool -T DEVNAME`` command.

.. code-block:: console

   ~# ethtool -T eth2
   Time stamping parameters for eth2:
   Capabilities:
         hardware-transmit
         hardware-receive
         software-receive
         software-system-clock
         hardware-raw-clock
   PTP Hardware Clock: 1
   Hardware Transmit Timestamp Modes:
         off
         on
   Hardware Receive Filter Modes:
         none
         ptpv2-event

Show adapter statistics
-----------------------

The interface statistics are divided into several parts. Different statistics can be retrieved using the commands as mentioned below.

Standard netdev statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^

You can retrieve standard netdev statistics such as RX / TX bytes / packet counts by using the command ``ip -s -s link show dev DEVNAME``.
For more details, see `Standard interface statistics <https://docs.kernel.org/networking/statistics.html#standard-interface-statistics>`__.

.. code-block:: console

   ~# ip -s -s link show dev eth2
   6: eth2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
      link/ether 70:ff:76:1d:5c:64 brd ff:ff:ff:ff:ff:ff
      RX:  bytes packets errors dropped  missed   mcast
            2554      19      0       0       0       0
      RX errors:  length    crc   frame    fifo overrun
                        0      0       0       0       0
      TX:  bytes packets errors dropped carrier collsns
            22493     208      0      18       0       0
      TX errors: aborted   fifo  window heartbt transns
                        0      0       0       0       3

Protocol-specific statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can retrieve protocol specific statistics such as packet counts for different octet sizes by using the command ``ethtool -S DEVNAME --groups rmon``. For more details refer `Protocol specific statistics <https://docs.kernel.org/networking/statistics.html#protocol-specific-statistics>`__

.. code-block:: console

   ~# ethtool -S eth2 --groups rmon
   Standard stats for eth2:
   rmon-etherStatsUndersizePkts: 0
   rmon-etherStatsOversizePkts: 0
   rx-rmon-etherStatsPkts64Octets: 11
   rx-rmon-etherStatsPkts65to127Octets: 145
   rx-rmon-etherStatsPkts128to255Octets: 48
   rx-rmon-etherStatsPkts256to511Octets: 7
   rx-rmon-etherStatsPkts512to1023Octets: 0
   tx-rmon-etherStatsPkts64Octets: 12
   tx-rmon-etherStatsPkts65to127Octets: 2
   tx-rmon-etherStatsPkts128to255Octets: 1
   tx-rmon-etherStatsPkts256to511Octets: 5
   tx-rmon-etherStatsPkts512to1023Octets: 0

Driver-defined statistics
^^^^^^^^^^^^^^^^^^^^^^^^^

Driver-defined ethtool statistics can be retrieved by using ``ethtool -S DEVNAME`` command.
It displays statistic for the ethernet port.

.. code-block:: console

   ~# ethtool -S eth2
   NIC statistics:
      tx_bcast: 5
      tx_mcast: 85
      tx_ucast: 123
      rx_bcast: 4
      rx_mcast: 1
      rx_ucast: 15
      rx_misalignment_frames: 0
      stormprev_counter_bc: 0
      stormprev_counter_mc: 0
      stormprev_counter_uc: 0
      mac_rxerror: 0
      sfd_error: 0
      mac_txerror: 0
      rx_oversized_frames: 0
      rx_undersized_frames: 0
      dropped_packets: 0
      tx_hwq_overflow: 0
      tx_hwq_underflow: 0


VLAN Config
===========

VLAN can be added/deleted using ``ip`` utility.

*VLAN Add*

.. code-block:: console

   ip link add link eth2 name eth2.5 type vlan id 5

*VLAN del*

.. code-block:: console

   ip link del eth2.5

*VLAN IP assigning*

IP address can be assigned to the VLAN interface either via udhcpc
when a VLAN aware dhcp server is present or via static ip assigning
using ``ip`` or ``ifconfig``.

Once VLAN is added, it will create a new entry in Ethernet interfaces
like eth2.5, below is an example how it check the vlan interface

.. code-block:: console

   ip addr add 10.0.0.5/24 dev eth2.5

   < or >

   ifconfig eth2.5 10.0.0.5
   ....

   ~# ifconfig eth2.5
   eth2.5: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
         inet 10.0.0.5  netmask 255.255.255.0  broadcast 0.0.0.0
         inet6 fe80::887a:20ff:fedd:b4e1  prefixlen 64  scopeid 0x20<link>
         ether 8a:7a:20:dd:b4:e1  txqueuelen 1000  (Ethernet)
         RX packets 0  bytes 0 (0.0 B)
         RX errors 0  dropped 0  overruns 0  frame 0
         TX packets 26  bytes 4904 (4.7 KiB)
         TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

*VLAN Packet Send/Receive*

To Send or receive packets with the VLAN tag, bind the socket to the
proper Ethernet interface shown above and can send/receive via that
socket-fd.

|

Interrupt pacing
================

The Interrupt pacing (IRQ coalescing) based on hrtimers is supported for RX path
and can be enabled by ethtool commands:

.. code-block:: console

   ethtool -C ethX rx-usecs N # Enable RX coalescing

The Interrupt pacing (IRQ coalescing) configuration can be retrieved by commands:

.. code-block:: console

   ethtool -c ethX # Show RX coalescing

Multicast Add/Delete
====================

Multicast MAC address can be added/deleted using *ip maddr* commands or Linux
socket ioctl SIOCADDMULTI/SIOCDELMULTI.

*Show muliticast address*

.. code-block:: console

   ~# ip maddr show eth2
      6:      eth2
      link  01:80:c2:00:00:0e users 2 static
      link  01:80:c2:00:00:03 users 2 static
      link  01:80:c2:00:00:00 users 2 static
      link  01:00:5e:00:00:01
      link  01:00:5e:00:00:fb
      link  33:33:00:00:00:01
      link  33:33:ff:1d:5c:64
      link  33:33:00:00:00:fb
      inet6 ff02::fb
      inet6 ff02::1:ff1d:5c64
      inet6 ff02::1 users 2
      inet6 ff01::1

*Add muliticast address*

.. code-block:: console

   ~# ip maddr add 01:00:5e:00:00:05 dev eth2
   ~# ip maddr show dev eth2
      6:      eth2
      link  01:80:c2:00:00:0e users 2 static
      link  01:80:c2:00:00:03 users 2 static
      link  01:80:c2:00:00:00 users 2 static
      link  01:00:5e:00:00:01
      link  01:00:5e:00:00:fb
      link  33:33:00:00:00:01
      link  33:33:ff:1d:5c:64
      link  33:33:00:00:00:fb
      link  01:00:5e:00:00:05 static
      inet6 ff02::fb
      inet6 ff02::1:ff1d:5c64
      inet6 ff02::1 users 2
      inet6 ff01::1


*Delete muliticast address*

.. code-block:: console

    # ip maddr del 01:00:5e:00:00:05 dev eth2

.. rubric:: **Multicast + VLAN**

Multicast MAC address can be added/deleted using *ip maddr* commands for vlan interfaces.

*Show multicast address for vlan interface*

.. code-block:: console

   ~# ip maddr show eth1.5

*Add multicast address for vlan interface*

.. code-block:: console

   ~# ip maddr add 01:00:5e:00:00:05 dev eth1.5

*Delete multicast address for vlan interface*

.. code-block:: console

   ~# ip maddr del 01:00:5e:00:00:05 dev eth1.5

|

Promiscous Mode
===============
By default promiscous mode is disabled. It can be enabled by using
the below command.

Please note running a tool like tcpdump will itself enable promiscous
mode.

.. code-block:: console

   ip link set eth0 promisc on

Configure interface (ethtool)
=============================

``ethtool -s|--change DEVNAME`` command can be used for configuring interface generic options.
The main purpose of this command is to configure physical link settings (PHY) like speed, duplex, auto-negotiation.

The PRU Ethernet driver forwards the following commands to the PHY driver:

.. code-block:: console

   # ethtool -s <dev>
   [ speed %d ]
   [ duplex half|full ]
   [ autoneg on|off ]
   [ wol p|u|m|b|a|g|s|d... ]
   [ sopass %x:%x:%x:%x:%x:%x ]

.. ifconfig:: CONFIG_part_variant in ('AM335X')

   .. note::

      Half Duplex is only supported for `pruss_emac0` interface. Configuring `pruss_emac1` in half duplex
      is not functional. This is a known issue that is being tracked separately.

Below is an example of forcing link speed to 100M/10M and duplexity to full:

.. code-block:: console

   # ethtool -s eth0 duplex half speed 100
   [  169.620032] prueth pruss-eth eth0: Link is Down
   [  171.727166] prueth pruss-eth eth0: Link is Up - 100Mbps/Half - flow control off

   # ethtool -s eth0 duplex half speed 10
   [  266.901225] prueth pruss-eth eth0: Link is Down
   [  269.018796] prueth pruss-eth eth0: Link is Up - 10Mbps/Half - flow control off

PTP Ordinary Clock
==================

The PRU Ethernet & IEP drivers implement the Linux PTP hardware clock subsystem APIs.
See `PTP hardware clock infrastructure for Linux <https://www.kernel.org/doc/html/latest/driver-api/ptp.html?highlight=ptp#ptp-hardware-clock-infrastructure-for-linux>`__ for
more details.

The PTP Ordinary Clock (OC) implementation is provided by the linuxptp application.

.. code-block:: console

   ptp4l -f oc.cfg

oc.cfg is a ptp4l configuration file.

Example oc.cfg for OC,

.. code-block:: text

   [global]
   tx_timestamp_timeout 10
   logMinPdelayReqInterval -3
   logSyncInterval -3
   twoStepFlag 1
   summary_interval 0
   [eth2]
   delay_mechanism P2P
   network_transport L2

where **eth2** is the intended PRU-ICSSM Ethernet port over which the OC
functionality is provided.

See `The Linux PTP Project <https://linuxptp.sourceforge.net#>`__ for
more details about linuxptp in general and `ptp4l(8) - Linux man
page <https://man.cx/ptp4l>`__ about ptp4l configurations in particular.

Here is a sample screen display of ptp4l for PRU-ICSS Ethernet port as
PTP/OC in slave mode:

.. code-block:: console

   # ptp4l -f oc.cfg -s -m
   ptp4l[6753.465]: selected /dev/ptp1 as PTP clock
   ptp4l[6753.520]: port 1 (eth2): INITIALIZING to LISTENING on INIT_COMPLETE
   ptp4l[6753.520]: port 0 (/var/run/ptp4l): INITIALIZING to LISTENING on INIT_COMPLETE
   ptp4l[6753.521]: port 0 (/var/run/ptp4lro): INITIALIZING to LISTENING on INIT_COMPLETE
   ptp4l[6757.507]: port 1 (eth2): new foreign master 70ff76.fffe.1f3c10-1
   ptp4l[6761.457]: selected local clock 70ff76.fffe.1d5c64 as best master
   ptp4l[6761.509]: selected best master clock 70ff76.fffe.1f3c10
   ptp4l[6761.509]: port 1 (eth2): LISTENING to UNCALIBRATED on RS_SLAVE
   ptp4l[6761.885]: port 1 (eth2): UNCALIBRATED to SLAVE on MASTER_CLOCK_SELECTED
   ptp4l[6762.511]: rms 634337579602795 max 1268675159205708 freq  -2928 +/- 1269 delay   927 +/-   4
   ptp4l[6763.512]: rms  210 max  317 freq  -2488 +/- 289 delay   933 +/-   1
   ptp4l[6764.513]: rms  350 max  375 freq  -1844 +/-  93 delay   931 +/-   1
   ptp4l[6765.514]: rms  218 max  294 freq  -1728 +/-  21 delay   925 +/-   2
   ptp4l[6766.515]: rms   72 max  119 freq  -1794 +/-  32 delay   923 +/-   0
   ptp4l[6767.516]: rms   10 max   24 freq  -1866 +/-  13 delay   926 +/-   1
   ptp4l[6768.517]: rms   27 max   37 freq  -1912 +/-  10 delay   925 +/-   1
   ptp4l[6769.518]: rms   16 max   23 freq  -1911 +/-  15 delay   927 +/-   1
   ptp4l[6770.519]: rms   12 max   20 freq  -1912 +/-  15 delay   928 +/-   1
   ptp4l[6771.520]: rms    8 max   17 freq  -1907 +/-  11 delay   932 +/-   1
   ptp4l[6772.521]: rms   16 max   28 freq  -1890 +/-  19 delay   929 +/-   2
   ptp4l[6773.522]: rms   13 max   19 freq  -1891 +/-  18 delay   926 +/-   0
   ptp4l[6774.523]: rms   14 max   24 freq  -1900 +/-  18 delay   928 +/-   1
   ptp4l[6775.525]: rms   11 max   21 freq  -1893 +/-  15 delay   924 +/-   2
   ptp4l[6776.526]: rms   15 max   22 freq  -1898 +/-  21 delay   931 +/-   2
   ptp4l[6777.527]: rms   14 max   19 freq  -1888 +/-  18 delay   930 +/-   1
   ptp4l[6778.528]: rms   11 max   19 freq  -1887 +/-  14 delay   929 +/-   3
   ptp4l[6779.529]: rms   17 max   25 freq  -1895 +/-  23 delay   925 +/-   1
   ptp4l[6780.530]: rms   12 max   20 freq  -1894 +/-  16 delay   926 +/-   2
   ptp4l[6781.531]: rms   11 max   20 freq  -1887 +/-  14 delay   928 +/-   2
   ptp4l[6782.532]: rms   13 max   19 freq  -1892 +/-  17 delay   929 +/-   1
   ptp4l[6783.533]: rms   15 max   29 freq  -1866 +/-  11 delay   924 +/-   2
   ptp4l[6784.534]: rms   11 max   15 freq  -1877 +/-  16 delay   925 +/-   1

   ...

|

************************
Two Port Ethernet Switch
************************

PRU_ICSSM can operate as VLAN aware Switch mode with two external physical ports
and one internal host port. By default, interfaces come up in Dual independent
EMAC mode and can be changed to operate in Switch mode at runtime.
Note that changing from Dual EMAC to Switch mode needs loading of
different firmwares to various PRU cores and thus have to follow
specific sequence as shown in below sections:

Enabling Switch mode
====================

Example assuming ETH2 and ETH3 as ICSSM interfaces:

.. code-block:: console

   ip link set dev eth2 down
   ip link set dev eth3 down
   ip link add name br0 type bridge
   ip link set dev eth2 master br0
   ip link set dev eth3 master br0
   ip link set dev br0 up
   bridge vlan add dev br0 vid 1 pvid untagged self
   ip link set dev eth2 up
   ip link set dev eth3 up

Going back to Dual EMAC mode
----------------------------

.. code-block:: console

   ip link set dev eth2 down
   ip link set dev eth3 down
   ip link set dev br0 down
   ip link set dev eth1 nomaster
   ip link set dev eth2 nomaster
   ip link del name br0 type bridge
   ip link set dev eth2 up
   ip link set dev eth3 up

Forwarding Data Bases (FDBs)
============================

Forwarding entries for MAC addresses are automatically added on the
appropriate switch port upon detection as default operation as an
unmanaged bridge. For managed bridge operation manually add FDB entries
as required.

Manually adding FDBs

.. code-block:: console

   bridge fdb add aa:bb:cc:dd:ee:fe dev eth2 master

Multicast Data Bases (MDBs)
===========================

Multicast entries are automatically added on the appropriate switch port
upon detection as default operation as an unmanaged bridge. For managed
bridge operation manually add MDB entries as required.

Manually adding MDBs

.. code-block:: console

   bridge mdb add dev br0 port eth2 grp 239.1.1.1 permanent

Multicast flooding
------------------

CPU port mcast_flooding is always on

Turning flooding on/off on switch ports

.. code-block:: console

   bridge link set dev eth2 mcast_flood on/off

--------------

.. rubric:: Frequently Asked Questions
   :name: frequently-asked-questions

.. rubric:: Are the HSR or PRP protocols supported?
   :name: are-the-hsr-or-prp-protocols-supported

Yes! The HSR and PRP protocols are currently supported on the AM572x IDK
board. To learn more about the HSR and PRP PRU firmware implementation
click `here <../../../Industrial_Protocols_HSR_PRP.html>`__. To learn more about
running the protocols/firmwares while using the Linux Processor SDK
click `here <../../../Industrial_Protocols_HSR_PRP.html#linux-software>`__.

HSR stands for High Availability Seamless Redundancy. This is a protocol
used to support redundant networks needed for industrial applications
such as factory automation, substation automation etc. The standard is
defined in IEC 62439-3 clause 5.

PRP stands for Parallel Redundancy Protocol which is another redundancy
protocol defined by IEC 62439-3 clause 4.

.. rubric:: I am using the AM571x IDK, why do I only see 4 Ethernet
   interfaces instead of 6?
   :name: i-am-using-the-am571x-idk-why-do-i-only-see-4-ethernet-interfaces-instead-of-6

Due to pin sharing between the optional LCD and the PRUSS1 Ethernet
pins, the AM571x IDK supports two different configurations: 4-port
Ethernet + LCD or 6-port Ethernet with no LCD. Jumper **J51** controls
which configuration is selected. If **J51** is closed then the 4-port +
LCD configuration is selected and if **J51** is open then the 6-port
Ethernet configuration is selected and the LCD is disabled.

.. rubric:: What if I want the PRU-ICSS to run a custom firmware (not
   Ethernet) on one of these industrial boards?
   :name: what-if-i-want-the-pru-icss-to-run-a-custom-firmware-not-ethernet-on-one-of-these-industrial-boards

The pru\_rproc driver uses the of\_machine\_is\_compatible() function to
check if the device that it is running on is compatible with one of the
boards above. If it is compatible, then the pru\_rproc driver loads the
Texas Instruments provided PRU-ICSS Ethernet firmwares. If you would
like to run your own PRU firmwares on one of the IDKs or the ICE board
then you will need to modify the device tree file to remove the IDK or
ICE compatibility declaration:

-  AM3359 ICE board

   -  Remove the **"ti,am3359-icev2"** compatible declaration at the top
      of the **arch/arm/boot/dts/am335x-icev2.dts** file

-  AM437x IDK board

   -  Remove the **"ti,am437x-idk-evm"** compatible declaration at the
      top of the **arch/arm/boot/dts/am437x-idk-evm.dts** file

-  AM572x IDK board

   -  Remove the **"ti,am5718-idk"** compatible declaration at the top
      of the **arch/arm/boot/dts/am571x-idk.dts** file

-  AM572x IDK board

   -  Remove the **"ti,am5728-idk"** compatible declaration at the top
      of the **arch/arm/boot/dts/am572x-idk.dts** file

Once these compatibility declarations are removed you will need to
rebuild your .dtb file and place it wherever it needs to be when you
reboot your board (filesystem, nfs directory, tftp directory, etc.)

Keep in mind that the PRU pin muxing on these boards is configured to
bring the MII pins out of the device. Changing the pin muxing to
accommodate your custom PRU firmware will be left as an exercise for the
user.

.. rubric:: What is the expected PRU-ICSS Ethernet throughput? How can I
   test the throughput on my setup?
   :name: what-is-the-expected-pru-icss-ethernet-throughput-how-can-i-test-the-throughput-on-my-setup

The maximum bandwidth of the PRU-ICSS Ethernet ports is 100 Mbps. The
observed throughput that I have achieved consistently is around 94 Mbps
using TCP or UDP and testing with iperf. Here are the commands needed to
test for yourself (this assumes you've followed the steps on this page
to get your PRU-ICSS interface up and running already):

-  Make sure that your board and your Linux development machine can
   'see' each other on the network (I connect both to the same switch
   and allow them to use DHCP to acquire IP addresses on the same
   network)
-  Use **ip/ifconfig** on both your Linux development machine and your
   board and note down each IP address

   -  For the purposes of this example I will use 192.168.0.105 as the
      Linux host IP and 192.168.1.110 as the board's IP

-  Testing TCP transmit throughput

   -  Start an iperf server on your Linux development machine (**sudo
      apt-get install iperf** if you don't already have iperf installed)

      -  **iperf -s**

   -  Run the iperf client from your board to connect to the iperf
      server you just started

      -  **iperf -c 192.168.0.105**

   -  You should see your board connect to the server and a few seconds
      later both the server and the client will output the Bandwidth
      achieved

      -  For me this is output is around 94 Mbits/sec

   -  Quit the iperf server that is running on your Linux development
      machine

      -  **Ctrl + c**

-  Testing TCP receive throughput

   -  Use the same procedure as provided for testing TCP transmit
      throughput except swap the commands on the two devices (**iperf
      -s** from the board and **iperf -c 192.168.1.110** from the Linux
      development machine)

-  Testing UDP transmit throughput

   -  Start a UDP iperf server on your Linux development machine

      -  **iperf -s -u**

   -  Run a UDP iperf client from your board and specify the bandwidth
      you'd like to achieve

      -  **iperf -c 192.168.0.105 -u -b 100M**

   -  Once again my results are around 94 Mbit/sec
   -  Quit the iperf server that is running on your Linux development
      machine

      -  **Ctrl + c**

-  Testing UDP receive throughput

   -  Use the same procedure as provided for testing UDP transmit
      throughput except swap the commands on the two devices (**iperf -s
      -u** from the board and **iperf -c 192.168.0.110 -u -b 100M** from
      the Linux development machine)

.. rubric:: Is flow control supported in the PRU-ICSS Ethernet ports?
   :name: is-flow-control-supported-in-the-pru-icss-ethernet-ports

Flow control is not currently supported in this version of the
PRU-ICSS Ethernet firware that is provided by Texas Instruments.

.. rubric:: Are multicast and VLAN filtering as well as storm prevention
   supported in the PRU-ICSS Ethernet ports?
   :name: are-multicast-and-VLAN-filtering-as-well-as-storm-prevention-supported-in-the-pru-icss-ethernet-ports

Yes, the Dual EMAC firmware supports per port multicast and VLAN filtering, as well
as network storm prevention. These features also exist in the HSR/PRP firmware
and are detailed for both HSR/PRP and Dual EMAC here:
`HSR/PRP Linux Software <Industrial_Protocols_HSR_PRP.html#linux_software>`__

.. rubric:: How do I check the link status and hardware statistics of my
   PRU-ICSS Ethernet ports?
   :name: how-do-i-check-the-link-status-and-hardware-statistics-of-my-pru-icss-ethernet-ports

You can use the **ethtool** utility:

-  **ethtool eth2** (for link status)
-  **ethtool -S eth2** (for hardware statistics)

.. rubric:: How to tune the system to optimize RX performance to minimize packet loss in -rt kernel?

Linux driver uses NAPI for RX processing which relies on ksoftirqd kernel thread to
schedule and poll for incoming packets. To minimize packet loss we need to increase
the priority of ksoftirqd like so.

* Throughput example:

::

    DUT: am571x-idk eth2
    root@am57xx-evm:~# chrt -f -p 40 $(pgrep ksoftirqd/?)
    root@am57xx-evm:~# iperf3 -s

    [ ID] Interval Transfer Bitrate Jitter Lost/Total Datagrams
    [ 5] 0.00-3599.99 sec 37.7 GBytes 90.0 Mbits/sec 0.166 ms 0/27513582 (0%) receiver


    Traffic generator: PC
    :~$ iperf3 -c 192.168.3.102 -u -b 90M -l 1472 -t 3600

    - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval Transfer Bitrate Jitter Lost/Total Datagrams
    [ 5] 0.00-3600.00 sec 37.7 GBytes 90.0 Mbits/sec 0.000 ms 0/27513582 (0%) sender
    [ 5] 0.00-3599.99 sec 37.7 GBytes 90.0 Mbits/sec 0.166 ms 0/27513582 (0%) receiver

* Packets per second example:

You can download the sample udp-packet.pcap but make sure you update the MAC addresses and IP addresses to match your setup.

:download:`udp-packet.pcap </files/udp-packet.pcap>`

::

    DUT: AM571x-idk eth2
    root@am57xx-evm:~# chrt -f -p 40  $(pgrep ksoftirqd/?)


    PC:
    sudo packETHcli -m 2 -t 300 -d 26 -i enx503eaa3bcbd5 -f udp-packet.pcap

    Results:

    PC:
    Sent 11337831 packets on enx503eaa3bcbd5; 148 bytes packet length; 38161 packets/s; 45.182 Mbit/s data rate; 52.509 Mbit/s link utilization
    ------------------------------------------------
    Sent 11375671 packets on enx503eaa3bcbd5 in 300.000031 second(s).
    ------------------------------------------------

    DUT:
    root@am57xx-evm:~# ip -s link show dev eth2
    <or>
    root@am57xx-evm:~# ifconfig eth2
    eth2      Link encap:Ethernet  HWaddr 70:FF:76:1C:0A:D1
              inet addr:192.168.3.102  Bcast:192.168.3.255  Mask:255.255.255.0
              inet6 addr: fe80::72ff:76ff:fe1c:ad1/64 Scope:Link
              UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
              RX packets:11375690 errors:0 dropped:0 overruns:0 frame:0
              TX packets:364 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000
              RX bytes:1683600596 (1.5 GiB)  TX bytes:61115 (59.6 KiB)

Currently driver doesn't use Tx IRQ as it is found that small frame througput
performance is better when Tx IRQ is not used. However for MTU frames,
performance is seen better with Tx IRQ used. If a specific application
predominantly uses MTU frame, user may enable Tx IRQ in the driver by adding
Tx Interrupt property in the DTS. For details refer to
Documentation/devicetree/bindings/net/ti-prueth.txt

.. rubric:: Is full-duplex and half-duplex PHY operation supported?

The firmware and ICSS subsystem supports both full-duplex and half-duplex PHYs.
However some TI boards do not have COL and CS lines of the PHY connected to the
SoC for half-duplex support. On such boards, half-duplex support is disabled
by passing the 'ti,no-half-duplex" flag to the PRU Ethernet device tree node.
