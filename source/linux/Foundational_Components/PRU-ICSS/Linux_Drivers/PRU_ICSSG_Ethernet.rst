.. _pru_icssg_ethernet:

******************
PRU_ICSSG Ethernet
******************

.. contents:: :local:
    :depth: 3

Introduction
############

Driver is developed complying to Linux Driver model and implements netdev and NAPI APIs along with other basic driver functions. Driver supports multiple instances of ICSSG each of which has two slices. Each slice consists of a pair of Programmable Real-Time Units (PRUs), Auxillary Programmable Real-time Units (RTUs) and TX Programmable Real-Time Units (TX_PRUS). So each ICSSG instance supports two Ethernet interfaces i.e. one per slice.

One of the key difference in the driver implementation compared to PRU-ICSS driver is the use of UDMA driver interface and ring accelerator driver available on Keystone III SoC to send/receive frames between ARM Host processor and PRU_ICSSG. This allows for efficient moving of data and is more efficient than the shared memory transport used in PRU-ICSS.

Supported platforms
###################

+-----------+-------------------------------+
| SoC       | Number of external ports      |
+===========+===============================+
| AM65X     | 3 x ICSSG, 6 Ports max        |
+-----------+-------------------------------+
| AM64X     | 2 x ICSSG, 4 Ports max        |
+-----------+-------------------------------+

.. ifconfig:: CONFIG_part_variant in ('AM65X')

  .. include:: AM65X_PRU_ICSSG_boards.rst

Features supported
##################

- 1G/100M/10M Full-Duplex Ethernet ports
- 100M/10M Half-Duplex Ethernet ports
- RGMII mode with TX delay (configured in DTS). RX delay is not supported and
  has to be provided by PHY.
- MII mode
- Multiple TX queues (upto 4), single RX queue.
- PTP Ordinary clock
- PPS Out
- Promiscuous mode
- Different MII modes for Real-Time Ethernet ports (MII_G_RT1 and MII_G_RT2) on different PRU_ICSSG instances. For example, MII on a PRU_ICSSG1 port, and RGMII on a PRU_ICSSG2 port, is supported.
- IRQ Coalescing also known as interrupt pacing.
- Multi-cast HW filtering
- XDP Native Mode and XDP Generic Mode
- Cut Through forwarding
- PHY Interrupt mode for ICSSG2
- Multicast filtering support for VLAN interfaces

.. rubric:: **Features not supported**

- VLAN HW filtering
- All-multi mode is always enabled
- Different MII modes for Real-Time Ethernet ports (MII_G_RT1 and MII_G_RT2) on a single PRU_ICSSG instance. For example, MII_G_RT1=MII and MII_G_RT2=RGMII.
- XDP with Zero-copy mode

Driver Configuration
####################

The TI Processor SDK has ICSSG driver enabled by default on supported platforms.
In case of custom builds, please ensure following configs are enabled.

.. code-block:: text

    CONFIG_TI_PRUSS
    CONFIG_REMOTEPROC
    CONFIG_PRU_REMOTEPROC
    CONFIG_TI_PRUSS_INTC
    CONFIG_TI_DAVINCI_MDIO
    CONFIG_TI_ICSS_IEP
    CONFIG_TI_ICSSG_PRUETH

.. rubric:: **Module Build**

Module build for the ICSSG driver is supported. To do this, use option 'm' for above configs, where applicable.

Device tree bindings
####################

The DT bindings description can be found at:

| `Documentation/devicetree/bindings/net/ti,icssg-prueth.yaml <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/Documentation/devicetree/bindings/net/ti,icssg-prueth.yaml?h=ti-linux-6.6.y>`__
| `Documentation/devicetree/bindings/net/ti,davinci-mdio.yaml <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/Documentation/devicetree/bindings/net/ti,davinci-mdio.yaml?h=ti-linux-6.6.y>`__
|

User guide
##########

Bringing Up interface
*********************

The network interface can be configured automatically depending on root file system or configured manually. Manual configuration:

.. code-block:: console

    ip addr add 192.168.1.1/24 dev eth1
    ip link set dev eth1 up

    < or >

    ifconfig eth1 <ip> netmask <mask> up

Get information (ethtool)
*************************

Get driver information
^^^^^^^^^^^^^^^^^^^^^^

The interface can be identified by using ``ethtool -i|--driver DEVNAME`` command.
It also provides some information about supported features.

.. code-block:: console

   ~# ethtool -i eth1
   driver: icssg-prueth
   version:
   firmware-version:
   expansion-rom-version:
   bus-info: pruss2_eth
   supports-statistics: yes
   supports-test: no
   supports-eeprom-access: no
   supports-register-dump: no
   supports-priv-flags: no

Display standard information about device/link
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run ``ethtool DEVNAME`` command without parameters.

.. code-block:: console

   ~# ethtool eth1
   Settings for eth1:
      Supported ports: [ TP MII ]
      Supported link modes:   100baseT/Full
                              1000baseT/Full
      Supported pause frame use: No
      Supports auto-negotiation: Yes
      Supported FEC modes: Not reported
      Advertised link modes:  100baseT/Full
                              1000baseT/Full
      Advertised pause frame use: No
      Advertised auto-negotiation: Yes
      Advertised FEC modes: Not reported
      Link partner advertised link modes:  10baseT/Half 10baseT/Full
                                           100baseT/Half 100baseT/Full
                                           1000baseT/Full
      Link partner advertised pause frame use: Symmetric Receive-only
      Link partner advertised auto-negotiation: Yes
      Link partner advertised FEC modes: Not reported
      Speed: 1000Mb/s
      Duplex: Full
      Port: MII
      PHYAD: 0
      Transceiver: internal
      Auto-negotiation: on
      Current message level: 0x00007fff (32767)
                              drv probe link timer ifdown ifup rx_err tx_err tx_queued intr tx_done rx_status pktdata hw wol
      Link detected: yes

Display time stamping capabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The interface time stamping capabilities can be retrieved by using  ``ethtool -T|--show-time-stamping DEVNAME`` command.

.. code-block:: console

   ethtool -T eth2
   Time stamping parameters for eth2:
   Capabilities:
        hardware-transmit     (SOF_TIMESTAMPING_TX_HARDWARE)
        software-transmit     (SOF_TIMESTAMPING_TX_SOFTWARE)
        hardware-receive      (SOF_TIMESTAMPING_RX_HARDWARE)
        software-receive      (SOF_TIMESTAMPING_RX_SOFTWARE)
        software-system-clock (SOF_TIMESTAMPING_SOFTWARE)
        hardware-raw-clock    (SOF_TIMESTAMPING_RAW_HARDWARE)
   PTP Hardware Clock: 2
   Hardware Transmit Timestamp Modes:
        off                   (HWTSTAMP_TX_OFF)
        on                    (HWTSTAMP_TX_ON)
   Hardware Receive Filter Modes:
        none                  (HWTSTAMP_FILTER_NONE)
        all                   (HWTSTAMP_FILTER_ALL)

Show permanent hardware address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The interface permanent hardware address can be retrieved by using ``ethtool -P|--show-permaddr DEVNAME`` command.

.. code-block:: console

   ~# ethtool -P eth1
   Permanent address: 70:ff:76:1d:5c:64

Query Channels information
^^^^^^^^^^^^^^^^^^^^^^^^^^

The interface DMA Channels information can be retrieved by using ``ethtool-l|--show-channels DEVNAME`` command.

.. code-block:: console

   # ethtool -l eth1
   Channel parameters for eth1:
   Pre-set maximums:
   RX:             1
   TX:             4
   Other:          0
   Combined:       0
   Current hardware settings:
   RX:             1
   TX:             1
   Other:          0
   Combined:       0

Show adapter statistics
^^^^^^^^^^^^^^^^^^^^^^^

The interface statistics are divided into several parts. Different statistics can be retrieved using the commands as mentioned below.

Standard netdev statistics
""""""""""""""""""""""""""

You can retrieve standard netdev statistics such as RX / TX bytes / packet counts by using the command ``ip -s -s link show dev DEVNAME``.
For more details, see `Standard interface statistics <https://docs.kernel.org/networking/statistics.html#standard-interface-statistics>`__.

.. code-block:: console

   ~# ip -s -s link show dev eth1
   10: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
      link/ether 70:ff:76:1d:ea:f9 brd ff:ff:ff:ff:ff:ff
      RX:  bytes packets errors dropped  missed   mcast
            2958      18      0       0       0       8
      RX errors:  length    crc   frame    fifo overrun
                       0      0       0       0       0
      TX:  bytes packets errors dropped carrier collsns
           13138     138      0       0       0       0
      TX errors: aborted   fifo  window heartbt transns
                       0      0       0       0       2

Protocol-specific statistics
""""""""""""""""""""""""""""

You can retrieve protocol specific statistics such as packet counts for different octet sizes by using the command ``ethtool -S DEVNAME --groups rmon``. For more details refer `Protocol specific statistics <https://docs.kernel.org/networking/statistics.html#protocol-specific-statistics>`__

.. code-block:: console

   ~# ethtool -S eth1 --groups rmon
   Standard stats for eth1:
   rmon-etherStatsUndersizePkts: 0
   rx-rmon-etherStatsPkts64Octets: 3
   rx-rmon-etherStatsPkts65to128Octets: 1
   rx-rmon-etherStatsPkts129to256Octets: 4
   rx-rmon-etherStatsPkts257to512Octets: 2
   rx-rmon-etherStatsPkts513to2000Octets: 0
   tx-rmon-etherStatsPkts64Octets: 0
   tx-rmon-etherStatsPkts65to128Octets: 53
   tx-rmon-etherStatsPkts129to256Octets: 18
   tx-rmon-etherStatsPkts257to512Octets: 2
   tx-rmon-etherStatsPkts513to2000Octets: 0

Driver-defined statistics
"""""""""""""""""""""""""

Driver-defined ethtool statistics can be retrieved by using ``ethtool -S | --statistics DEVNAME`` command.
It displays statistic for the ethernet port.

.. code-block:: console

   ~# ethtool -S eth1
   NIC statistics:
       rx_broadcast_frames: 0
       rx_mii_error_frames: 0
       rx_odd_nibble_frames: 0
       rx_max_size_error_frames: 0
       rx_min_size_error_frames: 0
       rx_class0_hits: 16
       rx_class1_hits: 0
       rx_class2_hits: 0
       rx_class3_hits: 0
       rx_class4_hits: 0
       rx_class5_hits: 0
       rx_class6_hits: 0
       rx_class7_hits: 0
       rx_class8_hits: 16
       rx_class9_hits: 16
       rx_class10_hits: 0
       rx_class11_hits: 0
       rx_class12_hits: 0
       rx_class13_hits: 0
       rx_class14_hits: 0
       rx_class15_hits: 0
       rx_smd_frags: 0
       rx_tx_total_bytes: 14348
       tx_broadcast_frames: 2
       tx_multicast_frames: 35
       tx_odd_nibble_frames: 0
       tx_underflow_errors: 0
       tx_max_size_error_frames: 0
       tx_min_size_error_frames: 0

IET FPE statistics
""""""""""""""""""

ICSSG supports Intersperse Express Traffic (IET, defined in P802.3br/D2.0 spec which later is included in IEEE 802.3 2018) Frame preemption (FPE) feature. The statistics related to IET can be obtained by using ``ethtool --include-statistics --show-mm DEVNAME``

.. code-block:: console

   ~# ethtool --include-statistics --show-mm eth1
   MAC Merge layer state for eth1:
   pMAC enabled: on
   TX enabled: off
   TX active: off
   TX minimum fragment size: 0
   RX minimum fragment size: 124
   Verify enabled: off
   Verify time: 0
   Max verify time: 128
   Verification status: UNKNOWN
   Statistics:
    MACMergeFrameAssErrorCount: 0
    MACMergeFrameSmdErrorCount: 0
    MACMergeFrameAssOkCount: 0
    MACMergeFragCountRx: 0
    MACMergeFragCountTx: 0

Show EEE settings
^^^^^^^^^^^^^^^^^

The interface EEE settings can be retrieved by using ``ethtool --show-eee DEVNAME`` command.

.. code-block:: console

   ethtool --show-eee eth1
   EEE Settings for eth1:
      EEE status: disabled
      Tx LPI: disabled
      Supported EEE link modes:  100baseT/Full
                  1000baseT/Full
      Advertised EEE link modes:  Not reported
      Link partner advertised EEE link modes:  100baseT/Full
                      1000baseT/Full


VLAN Config
***********

VLAN can be added/deleted using ``ip`` or ``vconfig`` utility.


*VLAN Add*

.. code-block:: console

    ip link add link eth1 name eth1.5 type vlan id 5

    < or >

    vconfig add eth1 5

*VLAN del*

.. code-block:: console

    ip link del eth1.5

    < or >

    vconfig rem eth1 5

*VLAN IP assigning*

IP address can be assigned to the VLAN interface either via udhcpc
when a VLAN aware dhcp server is present or via static ip assigning
using ``ip`` or ``ifconfig``.

Once VLAN is added, it will create a new entry in Ethernet interfaces
like eth1.5, below is an example how it check the vlan interface

.. code-block:: console

    ip addr add 10.0.0.5/24 dev eth1.5

    < or >

    ifconfig eth1.5 10.0.0.5
    ....

    ~# ifconfig eth1.5
    eth1.5    Link encap:Ethernet  HWaddr 70:FF:76:1D:5C:64
              inet addr:10.0.0.5  Bcast:10.255.255.255  Mask:255.0.0.0
              inet6 addr: fe80::72ff:76ff:fe1d:5c64/64 Scope:Link
              UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
              RX packets:0 errors:0 dropped:0 overruns:0 frame:0
              TX packets:45 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000
              RX bytes:0 (0.0 B)  TX bytes:7590 (7.4 KiB)

*VLAN Packet Send/Receive*

To Send or receive packets with the VLAN tag, bind the socket to the
proper Ethernet interface shown above and can send/receive via that
socket-fd.

|

Interrupt pacing
****************

The Interrupt pacing (IRQ coalescing) based on hrtimers for RX / TX data path separately can be enabled by ethtool commands (min value is 20us):

.. code-block:: console

  ethtool -C ethX rx-usecs N # Enable RX coalescing
  ethtool -C ethX tx-usecs N # Enable TX coalescing for TX0 by default.
  ethtool -Q ethX queue_mask 1 --coalesce tx-usecs 100 # Enable coalescing for TX0
  ethtool -Q ethX queue_mask 2 --coalesce tx-usecs 100 # Enable coalescing for TX1
  ethtool -Q ethX queue_mask 3 --coalesce tx-usecs 100 --coalesce tx-usecs 100 # Enable coalescing for both TX0 and TX1

The Interrupt pacing (IRQ coalescing) configuration can be retrieved by commands:

.. code-block:: console

  ethtool -c ethX # Show RX coalescing and TX coalescing for TX0
  ethtool -Q ethX queue_mask 1 --show-coalesce # Show coalescing configuration for TX0
  ethtool -Q ethX queue_mask 2 --show-coalesce # Show coalescing configuration for TX1
  ethtool -Q ethX queue_mask 3 --show-coalesce # Show coalescing configuration for both TX0 and TX1


|

Multicast Add/Delete
********************

Multicast MAC address can be added/deleted using *ip maddr* commands or Linux
socket ioctl SIOCADDMULTI/SIOCDELMULTI.

*Show muliticast address*

.. code-block:: console

	~# ip maddr show eth1
	3:      eth1
		link  33:33:00:00:00:01 users 2
		link  01:00:5e:00:00:01 users 2
		link  01:00:5e:00:00:fb users 2
		link  33:33:ff:1d:5c:64 users 2
		link  01:00:5e:00:00:fc users 2
		link  33:33:00:01:00:03 users 2
		link  33:33:00:00:00:fb users 2
		link  01:80:c2:00:00:21 users 2
		inet  224.0.0.252
		inet  224.0.0.251
		inet  224.0.0.1
		inet6 ff02::fb
		inet6 ff02::1:3
		inet6 ff02::1:ff1d:5c64
		inet6 ff02::1
		inet6 ff01::1


*Add muliticast address*

.. code-block:: console

	~# ip maddr add 01:00:5e:00:00:05 dev eth1
	~# ip maddr show dev eth1
	3:      eth1
		link  33:33:00:00:00:01 users 2
		link  01:00:5e:00:00:01 users 2
		link  01:00:5e:00:00:fb users 2
		link  33:33:ff:1d:5c:64 users 2
		link  01:00:5e:00:00:fc users 2
		link  33:33:00:01:00:03 users 2
		link  33:33:00:00:00:fb users 2
		link  01:80:c2:00:00:21 users 2
		link  01:00:5e:00:00:05 static
		inet  224.0.0.252
		inet  224.0.0.251
		inet  224.0.0.1
		inet6 ff02::fb
		inet6 ff02::1:3
		inet6 ff02::1:ff1d:5c64
		inet6 ff02::1
		inet6 ff01::1

*Delete muliticast address*

.. code-block:: console

    # ip maddr del 01:00:5e:00:00:05 dev eth1

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
***************
By default promiscous mode is disabled. It can be enabled by using
the below command.

Please note running a tool like tcpdump will itself enable promiscous
mode.

.. code-block:: console

     ip link set eth0 promisc on

Configure interface (ethtool)
*****************************

Change generic options
^^^^^^^^^^^^^^^^^^^^^^

The interface generic options can be configured by using ``ethtool -s|--change DEVNAME`` command.
The main purpose of this command is to configure physical link settings (PHY) like speed, duplex, auto-negotiation.

Below commands will be redirected to the phy driver:

.. code-block:: console

       # ethtool -s <dev>
       [ speed %d ]
       [ duplex half|full ]
       [ autoneg on|off ]
       [ wol p|u|m|b|a|g|s|d... ]
       [ sopass %x:%x:%x:%x:%x:%x ]

.. note::

    ICSSG Ethernet driver does not perform any kind of WOL specific actions or
    configurations.

Below is an example of forcing link speed to 100M and duplexity to full:

.. code-block:: console

	# ethtool -s eth1 duplex full speed 100
	[   74.768324] icssg-prueth pruss2_eth eth1: Link is Down
	[   78.592924] icssg-prueth pruss2_eth eth1: Link is Up - 100Mbps/Full - flow control off


Restart N-WAY (PHY) negotiation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The interface PHY auto-negotiation can be restarted by using ``ethtool -r|--negotiate DEVNAME`` command.

.. code-block:: console

	# ethtool -r eth1
	[  273.151655] icssg-prueth pruss2_eth eth1: Link is Down
	[  276.225423] icssg-prueth pruss2_eth eth1: Link is Up - 1Gbps/Full - flow control off

Set Channels parameters
^^^^^^^^^^^^^^^^^^^^^^^

The interface DMA channels parameters can be set by using ``ethtool -L\|--set-channels DEVNAME`` command.
It allows to control number of TX channels driver is allowed to work with at DMA level. The maximum number of TX channels is 4.
Supported options ``[ tx N ]``:

.. code-block:: console

      # ethtool -L eth1 tx 4

|

PTP Ordinary Clock
******************

The PRU Ethernet & IEP drivers implement the Linux PTP hardware clock subsystem APIs, the PRU-ICSS PTP clock can therefore be adjusted by
using those standard APIs. See `PTP hardware clock infrastructure for
Linux <https://www.kernel.org/doc/html/latest/driver-api/ptp.html?highlight=ptp#ptp-hardware-clock-infrastructure-for-linux>`__ for
more details.

The IEP0 is used by PRU Ethernet driver and Firmware PTP hardware clock and shared between PRU Ethernet ports.
The IEP1 is used for Firmware purposes.

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
    [eth1]
    delay_mechanism P2P
    network_transport L2

where **eth1** is the intended PRU-ICSSG Ethernet port over which the OC
functionality is provided.

See `The Linux PTP Project <https://linuxptp.sourceforge.net#>`__ for
more details about linuxptp in general and `ptp4l(8) - Linux man
page <https://man.cx/ptp4l>`__ about ptp4l configurations in particular.

Here is a sample screen display of ptp4l for PRU-ICSS Ethernet port as
PTP/OC in slave mode:

.. code-block:: console

	# ptp4l -f oc.cfg -s -m
	ptp4l[1255.613]: selected /dev/ptp2 as PTP clock
	ptp4l[1255.664]: port 1: INITIALIZING to LISTENING on INITIALIZE
	ptp4l[1255.665]: port 0: INITIALIZING to LISTENING on INITIALIZE
	ptp4l[1255.665]: port 1: link up
	ptp4l[1263.081]: selected best master clock 70ff76.fffe.1d5c64
	ptp4l[1269.343]: selected best master clock 70ff76.fffe.1d5c64
	ptp4l[1271.367]: port 1: new foreign master d494a1.fffe.8c36e9-1
	ptp4l[1275.368]: selected best master clock d494a1.fffe.8c36e9
	ptp4l[1275.368]: port 1: LISTENING to UNCALIBRATED on RS_SLAVE
	ptp4l[1275.754]: port 1: UNCALIBRATED to SLAVE on MASTER_CLOCK_SELECTED
	ptp4l[1276.381]: rms 789386424832367360 max 1578772849664738816 freq -60377 +/- 22862 delay   229 +/-   6
	ptp4l[1277.385]: rms  473 max  729 freq -67059 +/- 642 delay   251 +/-   4
	ptp4l[1278.389]: rms  792 max  830 freq -65620 +/- 211 delay   253 +/-   0
	ptp4l[1279.393]: rms  504 max  667 freq -65335 +/-  17 delay   255 +/-   1
	ptp4l[1280.397]: rms  166 max  271 freq -65484 +/-  59 delay   251 +/-   2
	ptp4l[1281.401]: rms   26 max   42 freq -65649 +/-  34 delay   249 +/-   1
	ptp4l[1282.405]: rms   43 max   50 freq -65727 +/-  10 delay   253 +/-   3
	ptp4l[1283.409]: rms   26 max   39 freq -65739 +/-   6 delay   256 +/-   1
	ptp4l[1284.412]: rms    5 max    7 freq -65725 +/-   3 delay   253 +/-   1
	ptp4l[1285.416]: rms    5 max    7 freq -65717 +/-   6 delay   252 +/-   1
	ptp4l[1286.420]: rms   11 max   14 freq -65698 +/-   6 delay   252 +/-   1
	ptp4l[1287.424]: rms    8 max   12 freq -65693 +/-   5 delay   254 +/-   1
	ptp4l[1288.427]: rms    7 max   12 freq -65687 +/-   4 delay   251 +/-   2
	ptp4l[1289.430]: rms    4 max    8 freq -65686 +/-   3 delay   249 +/-   1
	ptp4l[1290.434]: rms    5 max    8 freq -65693 +/-   7 delay   249 +/-   1
	ptp4l[1291.438]: rms    4 max    9 freq -65696 +/-   5 delay   251 +/-   1
	ptp4l[1292.441]: rms    7 max    9 freq -65682 +/-   5 delay   253 +/-   0
	ptp4l[1293.445]: rms   11 max   14 freq -65667 +/-   4 delay   252 +/-   0
	ptp4l[1294.448]: rms    8 max   14 freq -65662 +/-   5 delay   254 +/-   1
	ptp4l[1295.452]: rms    6 max    8 freq -65659 +/-   5 delay   254 +/-   2
	ptp4l[1296.456]: rms    3 max    7 freq -65657 +/-   2 delay   251 +/-   0
	ptp4l[1297.459]: rms    4 max    5 freq -65661 +/-   6 delay   256 +/-   2
	...

|

PPS Pulse Per Second support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. ifconfig:: CONFIG_part_variant in ('AM65X')

  PPS hardware pin is available only on the IDK application card i.e. ICSSG0 port 0 and ICSSG1 port 1.
  They are available at LEDs LD2 and LD5 respectively.

.. ifconfig:: CONFIG_part_variant in ('AM64X')

  To enable PPS on AM64x, the hardware pin PRG0_IEP0_EDC_SYNC_OUT0 needs to be enabled.

PPS can be tested using `testptp.c <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/tools/testing/selftests/ptp/testptp.c>`__ tool.

To find out the PTP device number i.e. PTP Hardware Clock, use ``ethtool -T DEVNAME``

.. note:: For PPS to work, the firmware needs to be running so the ICSSG network interface must be brought up.

To turn on PPS,

.. code-block:: console

       # ip link set dev eth1 up
       # ./testptp -d /dev/ptp2 -P 1
       pps for system time request okay

.. ifconfig:: CONFIG_part_variant in ('AM65X')

  You should be able to see either LD2 or LD5 blink at 1 second interval on AM654x-IDK.

.. ifconfig:: CONFIG_part_variant in ('AM64X')

  This will generate PPS signal with 1 pulse per second which can be probed at J18 SYNC_OUT0 header on the EVM and capture using oscilloscope.

To turn off PPS,

.. code-block:: console

       # ./testptp -d /dev/ptp2 -P 0
       pps for system time request okay


XDP
###

The PRU_ICSSG Ethernet driver supports Native XDP as well as Generic XDP. XDP with Zero-copy mode is not supported yet.
For detailed setup and how to test XDP please refer to :ref:`pru_icssg_xdp`.


Tips
####

.. _eth-phy-bundings:

Ethernet PHYs/MDIO bindings
***************************

The PRU_ICSSG Ethernet driver follows standard Linux DT bindings for MDIO bus, Ethernet controlers and PHYs which can be found at:

| `ethernet-controller.yaml <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/Documentation/devicetree/bindings/net/ethernet-controller.yaml?h=ti-linux-6.12.y>`__
| `mdio.yaml <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/Documentation/devicetree/bindings/net/mdio.yaml?h=ti-linux-6.12.y>`__
| `ethernet-phy.yaml <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/Documentation/devicetree/bindings/net/ethernet-phy.yaml?h=ti-linux-6.12.y>`__
|

The existing TI Ethernet PHYs DT bindings:

| `ti,dp83822.yaml <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/Documentation/devicetree/bindings/net/ti,dp83822.yaml?h=ti-linux-6.12.y>`__
| `ti,dp83867.yaml <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/Documentation/devicetree/bindings/net/ti,dp83867.yaml?h=ti-linux-6.12.y>`__
| `ti,dp83869.yaml <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/Documentation/devicetree/bindings/net/ti,dp83869.yaml?h=ti-linux-6.12.y>`__
|

.. _fixed-link:

Fixed link
**********

The Linux PRU_ICSSG Ethernet driver provides support for 'fixed-link' MAC-MAC connection support
which can be defined following standard :ref:`Ethernet Controller Generic Binding<eth-phy-bundings>` for each "ethernet-miiX' ICSSG port.

.. note::

    Fixed link is use-case specific and got limited testing, so should be considered experimental.


Example

.. code-block:: dts

   icssg2_emac1: ethernet-mii1 {
      phy-mode = "rgmii-rxid";
      syscon-rgmii-delay = <&scm_conf 0x4124>;
      local-mac-address = [00 00 00 00 00 00];

      fixed-link {
         speed = <1000>;
         full-duplex;
      };
   };

**RGMII Fixed link**

In case of RGMII MAC-MAC the 'phy-mode' DT property should be specifying properly for RGMII RX/TX delay configuration,
taking into account ICSSG HW capability to provide only TX delay (which for some SoCs is not recommended to be disabled).
Consult with SoC documentation (Data sheet, User guide) for supported RGMII RX/TX delay configurations.

100M/10M Half-Duplex
********************

The 10/100 half duplex (HD) support depends on HW capability to route PHY output pin (COL) to ICSSG GPI1O pin (PRGx_PRU0/1_GPI10) as input.
To indicate that HW supports HD the DT "ti,half-duplex-capable" property shell be added to the corresponding ICSSG "ethernet-mii0" port node.

For example:

.. code-block:: dts

  icssg0_eth: icssg0-eth {
  ...

     icssg0_emac1: ethernet-mii1 {
     ...

            ti,half-duplex-capable;
     };
  }

  &main_pmx0 {
  ...

     icssg0_rgmii_pins_default: icssg0-rgmii-pins-default {
           pinctrl-single,pins = <
           ...
                  AM65X_IOPAD(0x026c, PIN_INPUT, 1) /* (AA28) PRG0_PRU1_GPO10.PRG0_PRU1_GPI10 - col */
           >;
     };
  };

MII Support
********************

.. ifconfig:: CONFIG_part_variant in ('AM65X')

    On AM654x-evm the DP83867HM are strapped to RGMII configuration by default. To use MII mode for ICSSG interfaces  pinmux `settings <https://dev.ti.com/sysconfig/#/config/?args=--device%20AM65xx_SR2.0_beta%20--part%20Default%20--package%20ACD%20--theme%20light>`_ for MII mode needs to be added to the device tree.

.. ifconfig:: CONFIG_part_variant in ('AM64X')

  .. rubric:: AM64 GP EVM

  On AM64x-evm the DP83869HM are strapped to RGMII configuration by default. To use MII interface the
  k3-am642-evm-icssg1-dualemac-mii.dtbo overlay file has to be applied using the following command in uboot.

    .. code-block:: console

      setenv bootcmd 'run findfdt; run envboot; run init_${boot}; run get_kern_${boot}; run get_fdt_${boot};
      setenv name_overlays ti/k3-am642-evm-icssg1-dualemac-mii.dtbo; run get_overlay_${boot}; run run_kern'

   .. rubric:: **Limitations**

   - In order to implement single EMAC mode with RGMII port, disable the unused port in the devicetree, which is the default configuration.

   - In order to implement single EMAC mode with an MII port, both MIIx ports must be enabled in the devicetree. The driver requires both the MII ports to be enabled, even if one of the ports is unused (No Ethernet PHY wired).
     Use fixed-link for the unused port. Refer :ref:`Add fixed link support for a given ICSSG port<fixed-link>` for more details.


CPSW / PRU Ethernet Selection
#############################

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   Driver supports two Ethernet port modes, "Single EMAC" and "Dual EMAC" based on how many ports will be operated for a given ICSSG instance, for both MII and RGMII mode.

   - Single EMAC: 1 Ethernet port on a single PRU_ICSSG instance
   - Dual EMAC: 2 Ethernet ports on a single PRU_ICSSG instance

   On AM64x EVM (`TMDS64EVM <https://www.ti.com/tool/TMDS64EVM>`__ & `TMDS64GPEVM <https://www.ti.com/tool/TMDS64GPEVM>`__), one Ethernet port is connected to CPSW, one Ethernet port is connected to PRU Ethernet, and one Ethernet port can be muxed to either CPSW or PRU Ethernet depending on the device tree settings.
   The Ethernet port is muxed to CPSW by default in the AM64x EVM device tree :file:`k3-am642-evm.dts`, disabling this port for ICSSG (Single EMAC).

   To use **RGMII** interface in **Dual EMAC** mode the :file:`k3-am642-evm-icssg1-dualemac.dtbo` overlay file has to be applied using the following command in u-boot.

    .. code-block:: console

      setenv bootcmd 'run findfdt; run envboot;run init_${boot}; run get_kern_${boot}; run get_fdt_${boot};setenv name_overlays ti/k3-am642-evm-icssg1-dualemac.dtbo; run get_overlay_${boot}; run run_kern'

   To use **MII** interface in **Dual EMAC** mode the :file:`k3-am642-evm-icssg1-dualemac-mii.dtbo` overlay file has to be applied using the following command in u-boot.

    .. code-block:: console

      setenv bootcmd 'run findfdt; run envboot;run init_${boot}; run get_kern_${boot}; run get_fdt_${boot};setenv name_overlays ti/k3-am642-evm-icssg1-dualemac-mii.dtbo; run get_overlay_${boot}; run run_kern'

.. ifconfig:: CONFIG_part_variant in ('AM65X')

  This feature is not supported.

Time Senstive Network (TSN) Offload Support
###########################################

.. ifconfig:: CONFIG_part_variant in ('AM65X','AM64X')

  ICSSG Ethernet supports offloading of features such as Enhancements for Scheduled Traffic
  (EST) and Intersperse Express Traffic (IET) Frame Preemption offload
  similar to CPSW.

  For EST setup refer to :ref:`kernel_driver_cpsw2g_est` and IET configuration refer to :ref:`kernel_driver_cpsw2g_iet`.

  For the interface ethX, IET related statistics can be retrieved by using ``ethtool -S ethX | grep iet`` command.


SRAM Requirement
################

The ICSSG Ethernet driver supports multiple instances of ICSSG each of which has two slices. Each ICSSG instance supports two Ethernet interfaces i.e. one per slice.

SRAM Required for each ICSSG instance (per two ports) is as below.

.. ifconfig:: CONFIG_part_variant in ('AM65X')

  +------------------+--------------------------+-----------------------------------+
  | SoC              | Mode                     | SRAM Required per ICSSG instance  |
  +==================+==========================+===================================+
  | AM65X SR 2.0     | Emac Mode                |             192 KB                |
  +------------------+--------------------------+-----------------------------------+
  | AM65X SR 2.0     | Emac Mode + Switch Mode  |             256 KB                |
  +------------------+----------------------+---+-----------------------------------+

.. ifconfig:: CONFIG_part_variant in ('AM64X')

  +-----------+--------------------------+-----------------------------------+
  | SoC       | Mode                     | SRAM Required per ICSSG Instance  |
  +===========+==========================+===================================+
  | AM64X     | Emac Mode                |             192 KB                |
  +-----------+--------------------------+-----------------------------------+

For each ICSSG instance, the SRAM required needs to be contiguous.
PRUETH only uses the required amount of SRAM from the SRAM/MSMC pool. If PRUETH doesn't get the required amount of SRAM, the prueth_probe() API will return with -ENOMEM error.

Firmware name handling
######################

Starting from Processor SDK v11.01, the ICSSG PRUETH driver reads firmware names from the device tree instead of using hard-coded values. This change improves flexibility and maintainability, especially when supporting different SoCs or firmware versions.

**How driver reads firmware names:**

- Specify the firmware names for each core (PRU, RTU, TX_PRU) and for each slice (MAC port) using the device tree property `firmware-name`.
- The device tree specifies only the EMAC (Ethernet MAC) firmware names.
- The driver reads these names at probe time and stores them internally.

- For other supported modes (SWITCH, HSR and PRP), the driver generates the firmware names dynamically by replacing the string in the EMAC firmware name:

   - The driver replaces `"eth"` with `"sw"` for SWITCH mode.
   - The driver replaces `"eth"` with `"hsr"` for HSR mode.
   - The driver replaces `"eth"` with `"prp"` for PRP mode.


**Device tree example:**

.. ifconfig:: CONFIG_part_variant in ('AM65X')

  .. code-block:: dts

      icssg2_eth: icssg2-eth@... {
         ...
         firmware-name =
               "ti-pruss/am65x-sr2-pru0-prueth-fw.elf",
               "ti-pruss/am65x-sr2-rtu0-prueth-fw.elf",
               "ti-pruss/am65x-sr2-txpru0-prueth-fw.elf",
               "ti-pruss/am65x-sr2-pru1-prueth-fw.elf",
               "ti-pruss/am65x-sr2-rtu1-prueth-fw.elf",
               "ti-pruss/am65x-sr2-txpru1-prueth-fw.elf";
         ...
      };

.. ifconfig:: CONFIG_part_variant in ('AM64X')

  .. code-block:: dts

      icssg1_eth: icssg1-eth@... {
         ...
         firmware-name =
               "ti-pruss/am64x-sr2-pru0-prueth-fw.elf",
               "ti-pruss/am64x-sr2-rtu0-prueth-fw.elf",
               "ti-pruss/am64x-sr2-txpru0-prueth-fw.elf",
               "ti-pruss/am64x-sr2-pru1-prueth-fw.elf",
               "ti-pruss/am64x-sr2-rtu1-prueth-fw.elf",
               "ti-pruss/am64x-sr2-txpru1-prueth-fw.elf";
         ...
      };

.. note::

   - This approach is compatible with earlier versions as the existing device
     trees already provide the ``firmware-name`` property.
   - To use a different firmware version, simply update the
     ``firmware-name`` property in your device tree.
   - The driver will automatically handle the correct firmware names for all
     supported modes.

For more details, refer to the upstream commit:
https://patch.msgid.link/20250613064547.44394-1-danishanwar@ti.com
