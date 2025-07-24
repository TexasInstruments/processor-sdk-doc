.. _cpsw3g:

######
CPSW3g
######

.. contents:: :local:
   :depth: 3

************
Introduction
************

The TI |__PART_FAMILY_DEVICE_NAMES__| family of devices have multi port
Gigabit Ethernet Switch subsystem. SoCs may have more than 2 external
port with selectable RGMII and RMII interfaces and an internal
Communications Port Programming Interface (CPPI) port (Host port 0).
Host Port 0 CPPI Packet Streaming Interface interface supports 8 TX
channels and one RX channel DMA channel.

Multi port Gigabit Ethernet Switch subsystem support both independent
MAC mode of operation supporting multiple independent Ethernet
interfaces with complete isolation (no packet switching between external
ports), or can be configured in Switch mode with IEEE 802.1Q HW bridge
in managed or learning mode between each of the individual MAC ports.

The driver follows the standard Linux network interface architecture and
supports the following features:

#. Mulitple indpendent MAC mode
#. Switch mode as per IEEE 802.1Q
#. Cut Through forwarding in Switch mode
#. 10/100/1000 Mbps mode of operation.
#. Auto negotiation.
#. Linux NAPI support
#. VLAN filtering
#. Ethertool
#. CPTS/PTP as per 802.1AS-2011 (TSN)
#. EST/TAS offload as per 802.1Q-2018 (TSN)
#. IET/preemption offload as per 802.1Q-2018 (TSN)
#. Forwarding and Queuing Enhancements for Time-Sensitive Streams (FQTSS) as per 802.1Q-2018 previously referred to as CBS or 802.1Qav


.. note::

   Default mode of operation is multiple indpendent MAC ports.

Supported platforms
===================

+-----------+-------------------------------+
| SoC       | Number of external ports      |
+===========+===============================+
| AM62PX    | 2 external ports (CPSW3g)     |
+-----------+-------------------------------+
| AM62LX    | 2 external ports (CPSW3g)     |
+-----------+-------------------------------+
| AM62AX    | 2 external ports (CPSW3g)     |
+-----------+-------------------------------+
| AM62X     | 2 external ports (CPSW3g)     |
+-----------+-------------------------------+
| AM64X     | 2 external ports (CPSW3g)     |
+-----------+-------------------------------+


.. ifconfig:: CONFIG_part_variant in ('AM62AX')

    .. note::
      | The second CPSW MAC port of the CPSW3g instance on AM62A requires an Add-On card.
      | Additionally, the device-tree overlay:
      |  **k3-am62a7-sk-ethernet-dc01.dtbo**
      | has to be applied at U-Boot stage using the command:
      |  **setenv name_overlays ti/k3-am62a7-sk-ethernet-dc01.dtbo**
      | to enable functionality of the second CPSW port in Linux.

********************
Driver Configuration
********************

Default SDK build will have these configurations enabled. In case of
custom builds, please ensure following configs are enabled.

.. code-block:: kconfig

   CONFIG_TI_DAVINCI_MDIO
   CONFIG_TI_K3_AM65_CPSW_NUSS
   CONFIG_TI_K3_AM65_CPSW_SWITCHDEV
   CONFIG_TI_K3_AM65_CPTS
   CONFIG_TI_AM65_CPSW_TAS
   CONFIG_PHY_TI_GMII_SEL

For further details regarding the above configs, refer:

#. ``drivers/net/ethernet/ti/Kconfig``
#. ``drivers/phy/ti/Kconfig``

.. rubric:: **Module Build**
   :name: k3-module-build

Module build for the cpsw driver is supported. To do this, use option 'm' for above configs, where applicable.

********************
Device tree bindings
********************

The DT bindings description can be found at:

|   `Documentation/devicetree/bindings/net/ti,k3-am654-cpsw-nuss.yaml <https://git.ti.com/ti-linux-kernel/ti-linux-kernel/blobs/ti-linux-6.6.y/Documentation/devicetree/bindings/net/ti,k3-am654-cpsw-nuss.yaml>`__

|   `Documentation/devicetree/bindings/net/ti,k3-am654-cpts.yaml <https://git.ti.com/ti-linux-kernel/ti-linux-kernel/blobs/ti-linux-6.6.y/Documentation/devicetree/bindings/net/ti,k3-am654-cpts.yaml>`__
|

**************
Multi MAC mode
**************

.. note::

   This section documents Independent MAC mode of operation with
   CPSW3g.

.. include:: _K3-CPSW-common.rst
   :parser: rst

***************
Promiscous Mode
***************

By default promiscous mode is disabled. It can be enabled by using
the below command.

Please note running a tool like tcpdump will itself enable promiscous
mode.

.. code-block:: console

   ip link set eth0 promisc on

***********************
Set MacAddress manually
***********************

While the default MacAddress of the port is obtained from EEPROM, it's
possible to change the MacAddress manually from shell.

.. code-block:: console

   ip link set dev <eth0> address <macaddress>

**********************
Multi port Switch mode
**********************

.. note::

   This section documents the Switch mode features available with
   CPSW3g

The Switch mode can be enabled by configuring devlink driver parameter
"switch_mode" to 1/true

.. code-block:: console

   devlink dev param set platform/8000000.ethernet \
   name switch_mode value true cmode runtime

Above setting can be done regardless of the state of Port's netdev
devices - UP/DOWN, but Port's netdev devices have to be in UP state
before joining the bridge. This is to avoid overwriting of bridge
configuration as CPSW switch driver completely reloads its configuration
when first port changes its state to UP.

When all the interfaces have joined the bridge - CPSW switch driver will
enable marking packets with offload_fwd_mark flag.

All configuration is implemented via switchdev API.

Bridge setup
============

.. code-block:: console

   devlink dev param set platform/8000000.ethernet \
   name switch_mode value true cmode runtime

   ip link add name br0 type bridge
   ip link set dev br0 type bridge ageing_time 1000
   ip link set dev eth0 up
   ip link set dev eth1 up
   ip link set dev eth0 master br0
   ip link set dev eth1 master br0

   [*] bridge vlan add dev br0 vid 1 self
   [*] bridge vlan add dev br0 vid 1 pvid untagged self
   [*] if vlan_filtering=1, where default_pvid=1

   Note: Steps [*] are mandatory.


Turn On/Off Spanning Tree Protocol (STP)
========================================

.. code-block:: console

   ip link set dev br0 type bridge stp_state 1/0

VLAN configuration
==================

.. code-block:: console

   bridge vlan add dev br0 vid 1 self # <---- add VLAN as a Bridge Entry
   bridge vlan add dev br0 vid 1 pvid untagged self # <---- add cpu port to VLAN 1

This step is mandatory for bridge/default_pvid.

Adding extra VLANs
==================

1. untagged

   .. code-block:: console

      bridge vlan add dev eth0 vid 100 pvid untagged master
      bridge vlan add dev sw0p2 vid 100 pvid untagged master
      bridge vlan add dev br0 vid 100 self # <---- add VLAN as a Bridge Entry
      bridge vlan add dev br0 vid 100 pvid untagged self # <---- Add cpu port to VLAN100

2. tagged

   .. code-block:: console

      bridge vlan add dev eth0 vid 100 master
      bridge vlan add dev sw0p2 vid 100 master
      bridge vlan add dev br0 vid 100 self # <---- add VLAN as a Bridge Entry
      bridge vlan add dev br0 vid 100 pvid tagged self # <---- Add cpu port to VLAN100

Forwarding Data Bases (FDBs)
============================

Forwarding entries for MAC addresses are automatically added on the
appropriate switch port upon detection as default operation as an
unmanaged bridge. For managed bridge operation manually add FDB entries
as required.

Manually adding FDBs

.. code-block:: console

   bridge fdb add aa:bb:cc:dd:ee:ff dev eth0 master vlan 100
   bridge fdb add aa:bb:cc:dd:ee:fe dev sw0p2 master # <---- Add on all VLANs

.. note::

   For untagged traffic, the PVID is 1 by default. Therefore to add FDB entry
   for untagged traffic, the commands mentioned above have to use "vid 1"
   at the respective places.

Multicast Data Bases (MDBs)
===========================

Multicast entries are automatically added on the appropriate switch port
upon detection as default operation as an unmanaged bridge. For managed
bridge operation manually add MDB entries as required.

Manually adding MDBs

.. code-block:: console

   bridge mdb add dev br0 port eth0 grp 239.1.1.1 permanent vid 100
   bridge mdb add dev br0 port eth0 grp 239.1.1.1 permanent # <---- Add on all VLANs

.. note::

   For untagged traffic, the PVID is 1 by default. Therefore to add MDB entry
   for untagged traffic, the commands mentioned above have to use "vid 1"
   at the respective places.

Multicast flooding
==================

CPU port mcast_flooding is always on

Turning flooding on/off on switch ports::

   bridge link set dev eth0 mcast_flood on/off

Enabling Cut Through Forwarding (CTF)
=====================================

.. caution::

   The Cut Through configuration interface could be changed significantly in the
   future depending on Linux Kernel mainline development.

Cut Through feature allows forwarding packet from one external port to
another without being stored in Port FIFOs thus reducing overall latency
for packet forwarding.

**Limitations:**

* Feature is only available in switch mode.
* Cut Through forwarding is only supported between external ports and no
  support for Cut Through to host port currently.
* Cut-Thru is not supported with 10/100 half-duplex.
* Cut-Thru is not supported with any form of flow control.
* If Intersperced Express Traffic (IET) is enabled, then Cut Through can
  only be enabled on an express priority queue and not on preemptible
  queues.

.. note::

   Currently per port priority mask is set via debugfs entries. This may change
   in future.

Here is the commands to setup cut-through for priority 0 traffic:

.. code-block:: console

   ip link set dev eth0 down
   ip link set dev eth1 down

   devlink dev param set platform/8000000.ethernet name switch_mode value true cmode runtime

   echo 1 > /sys/kernel/debug/8000000.ethernet/Port1/cut_thru_rx_pri_mask
   echo 1 > /sys/kernel/debug/8000000.ethernet/Port1/cut_thru_tx_pri_mask
   echo 1 > /sys/kernel/debug/8000000.ethernet/Port2/cut_thru_rx_pri_mask
   echo 1 > /sys/kernel/debug/8000000.ethernet/Port2/cut_thru_tx_pri_mask

   ethtool --set-priv-flags eth0 cut-thru on
   ethtool --set-priv-flags eth1 cut-thru on

   ip link add name br0 type bridge
   ip link set dev br0 type bridge ageing_time 1000

   ip link set dev eth0 up
   sleep 1
   ip link set dev eth1 up
   sleep 1

   ip link set dev eth0 master br0
   ip link set dev eth1 master br0
   ip link set dev br0 type bridge stp_state 1
   ip link set dev br0 up

   ip addr add 10.0.0.1/8 dev br0

   bridge vlan add dev br0 vid 1 self
   bridge vlan add dev br0 vid 1 pvid untagged self

The value being written to cut_thru_rx_pri_mask and cut_thru_tx_pri_mask
represents the priorties queues for which cut through feature needs to
be enabled. Can be configured only when all external ports are down.

With above settings, generate a iperf3 traffic from client on Port1 to
client on Port 2 and observe the ethtool statistics to see cut through
taking effect

.. code-block:: console

   root@evm:~# ethtool -S eth1 | grep col
      tx_collision_frames: 1796093
      tx_single_coll_frames: 0
      tx_mult_coll_frames: 3
      tx_excessive_collisions: 0
      tx_late_collisions: 0
   root@evm:~# ethtool -S eth0 | grep col
      tx_collision_frames: 3
      tx_single_coll_frames: 0
      tx_mult_coll_frames: 2002396
      tx_excessive_collisions: 52
      tx_late_collisions: 23

   tx_collision_frames:      Enet_Pn_TxCut Enet Port n Cut Thru with and without delay (full-duplex)
   tx_single_coll_frames:    Enet_pn_TxCut_SAF Enet Port n Tx Store and Forward (full-duplex)
   tx_mult_coll_frames:      Enet_Pn_RxCut_NoDelay Enet Port n Rx Cut Thru with no delay (full-duplex)
   tx_excessive_collisions:  Enet_Pn_RxCut_Delay Enet Port n Rx Cut Thru with delay (full-duplex)
   tx_late_collisions:       Enet_Pn_RxCut_SAF Enet Port n Rx Store and Forward (full-duplex)

Transmit Traffic Control and Rate Limiting
==========================================

The main difference between one port and multi port devices is that TX CPPI channels
are shared between all network devices while External Ports FIFO are per port.
The MQPRIO Qdisk can be used to assign different TX CPPI channels to different ports
and this way improve over all TX performance.

* The configured External Ports Fifos rate should must not be oversubscribed.
  If some Ext. port and Host port both send to the same priority then Ext. Ports
  Fifos rate for this priority has to be set as sum of Ext. and Host port rates
  plus some margin.

.. rubric:: Example Host port ingress with separate TX CPPI channel per port, no
   QoS

* switch mode: on | off
* Port 1 assigned TX CPPI channel 0
* Port 2 assigned TX CPPI channel 1
* TX CPPI channels processing mode: Round Robin

.. code-block:: console

   ip link set dev eth0 down
   ip link set dev eth1 down
   ethtool -L eth0 tx 2
   ethtool --set-priv-flags eth1 p0-rx-ptype-rrobin on
   ip link set dev eth0 up
   ip link set dev eth1 up
   tc qdisc add dev eth0 handle 100: parent root mqprio num_tc 1 map 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 queues 1@0 hw 1 mode channel
   tc qdisc add dev eth1 handle 100: parent root mqprio num_tc 1 map 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 queues 1@1 hw 1 mode channel

If TX CPPI channels processing mode is Round Robin (p0-rx-ptype-rrobin off) then Rate Limiting should for selected TX CPPI channels.

.. code-block:: console

   echo 800 > /sys/class/net/eth0/queues/tx-0/tx_maxrate
   echo 800 > /sys/class/net/eth0/queues/tx-1/tx_maxrate

.. rubric:: Example Host port ingress with separate TX CPPI channel per port and
   Rate Limiting

Linux Host send bulk and rate limited traffic to both ports.
No traffic switching between P1 and P2.

.. code-block:: text

   to Host1│  CPSW3g Host bridge │ to Host2
           │     /    \          │
           │   P1     P2         │
           │   |       |         │
           │  Host1   Host2      │
           ▼                     ▼

* switch mode: on
* tc filters are used to assign pri for iperf3 traffic using port as filter value
* VLAN tagged traffic vid=100

**eth0: Ports 1**

* pri7 traffic routed to TX CPPI channel 7, rate limit 100Mbit
* pri6 traffic routed to TX CPPI channel 6, rate limit 200Mbit
* pri0-5 traffic routed to TX CPPI channel 0
* pri7 traffic mapped to TC2, External Ports FIFO2, cir=100Mbit
* pri6 traffic mapped to TC1, External Ports FIFO1, cir=200Mbit
* pri0-5 traffic mapped to TC0, External Ports FIFO0

**eth1: Ports 2**

* pri7 traffic routed to TX CPPI channel 5, rate limit 100Mbit
* pri6 traffic routed to TX CPPI channel 4, rate limit 200Mbit
* pri0-5 traffic routed to TX CPPI channel 0
* pri7 traffic mapped to TC2, External Ports FIFO2, cir=100Mbit
* pri6 traffic mapped to TC1, External Ports FIFO1, cir=200Mbit
* pri0-5 traffic mapped to TC1, External Ports FIFO0

.. code-block:: console

   ip link set dev eth0 down
   ip link set dev eth1 down
   ethtool -L eth0 tx 8
   ethtool --set-priv-flags eth1 p0-rx-ptype-rrobin off
   ip link add name br0 type bridge
   ip link set dev eth0 up
   ip link set dev eth1 up
   ip link set dev eth0 master br0
   ip link set dev eth1 master br0
   ip link set dev br0 up

   #configure bridge...
   #configure bridge vlan
   ip link add link br0 name br0.100 type vlan id 100
   ip link set br0.100 type vlan egress 0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7
   bridge vlan add dev eth0 vid 100 master
   bridge vlan add dev eth1 vid 100 master
   bridge vlan add dev br0 vid 100 self

   # set IP to br0.100 192.168.100.1

   echo 100 > /sys/class/net/eth0/queues/tx-7/tx_maxrate
   echo 200 > /sys/class/net/eth0/queues/tx-6/tx_maxrate
   echo 100 > /sys/class/net/eth0/queues/tx-5/tx_maxrate
   echo 200 > /sys/class/net/eth0/queues/tx-4/tx_maxrate

   tc qdisc add dev br0.100 clsact
   tc filter add dev br0.100 egress protocol ip prio 1 u32 match ip dport 5001 0xffff action skbedit priority 7
   tc filter add dev br0.100 egress protocol ip prio 1 u32 match ip dport 5002 0xffff action skbedit priority 6

   #eth0
   tc qdisc add dev eth0 parent root handle 100: mqprio num_tc 3 \
   map 0 0 0 0 0 0 1 2 0 0 0 0 0 0 0 0 \
   queues 1@0 1@6 1@7 hw 1 mode channel \
   shaper bw_rlimit min_rate 0 200mbit 100mbit

   #eth1
   tc qdisc add dev eth1 parent root handle 100: mqprio num_tc 3 \
   map 0 0 0 0 0 0 1 2 0 0 0 0 0 0 0 0 \
   queues 1@0 1@4 1@5 hw 1 mode channel \
   shaper bw_rlimit min_rate 0 200mbit 100mbit

   iperf3 -c 192.168.100.3 -t10 -p5001 -Tpri71 & \
   iperf3 -c 192.168.100.3 -t10 -p5002 -Tpri61 & \
   iperf3 -c 192.168.100.3 -t10 -p5003 -Tpri01 & \
   iperf3 -c 192.168.100.2 -t10 -p5001 -Tpri72 & \
   iperf3 -c 192.168.100.2 -t10 -p5002 -Tpri62



.. rubric:: Example Bridging with TX CPPI channel and External Ports FIFO
   shapers

Linux Host send bulk and rate limited traffic to Host 2 (Port 2) pri3 200Mbit and
Host 1 sends rate limited traffic to Host 2 (Port 2) pri3 200Mbit.

.. code-block:: text

   CPSW3g Host bridge │ to Host2
      /    \          │ 200Mbit
    P1     P2         │
    |       |         │
   Host1   Host2      │
                      ▼

   ──────────────►
   to Host2
   200Mbit

* switch mode: on
* tc filters are used to assign pri for iperf3 traffic using port as filter value
* VLAN tagged traffic vid=100
* assume pri3 is class A and pri 2 is class B (not used)

**eth0: Ports 1**

* pri0-7 traffic routed to TX CPPI channel 0, no HW offload

**eth1: Ports 2**

* pri3 traffic routed to TX CPPI channel 7, rate limit 200Mbit
* pri2 traffic routed to TX CPPI channel 6, rate limit 100Mbit
* pri0,1,4-7 traffic routed to TX CPPI channel 0
* pri3 traffic mapped to TC2, External Ports FIFO2, cir=200Mbit
* pri2 traffic mapped to TC1, External Ports FIFO1, cir=100Mbit
* pri0,1,4-7 traffic mapped to TC0, External Ports FIFO0

**CPSW3g Host bridge configuration**

.. code-block:: console

   ip link set dev eth0 down
   ip link set dev eth1 down
   ethtool -L eth0 tx 8
   ethtool --set-priv-flags eth1 p0-rx-ptype-rrobin off
   ip link add name br0 type bridge
   ip link set dev eth0 up
   ip link set dev eth1 up
   ip link set dev eth0 master br0
   ip link set dev eth1 master br0
   ip link set dev br0 up

   #configure bridge...
   #configure bridge vlan
   ip link add link br0 name br0.100 type vlan id 100
   ip link set br0.100 type vlan egress 0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7
   bridge vlan add dev eth0 vid 100 master
   bridge vlan add dev eth1 vid 100 master
   bridge vlan add dev br0 vid 100 self

   # set IP to br0.100 192.168.100.1

   echo 200 > /sys/class/net/eth0/queues/tx-7/tx_maxrate
   echo 100 > /sys/class/net/eth0/queues/tx-6/tx_maxrate

   tc qdisc add dev br0.100 clsact
   tc filter add dev br0.100 egress protocol ip prio 1 u32 match ip dport 5002 0xffff action skbedit priority 3

   #eth0
   tc qdisc add dev eth0 handle 100: parent root mqprio num_tc 1 \
   map 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 queues 1@0 hw 0

   #eth1
   tc qdisc add dev eth1 parent root handle 100: mqprio num_tc 3 \
   map 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0 0 \
   queues 1@0 1@6 1@7 hw 1 mode channel \
   shaper bw_rlimit min_rate 0 100mbit 410mbit

   iperf3 -c 192.168.100.2 -t10 -p5002 -Tpri22 -t30 & \
   iperf3 -c 192.168.100.2 -t10 -p5003 -Tpri02 -t30 &

**Host 1 configuration**

.. code-block:: console

   ip link add link eth0 name eth0.100 type vlan id 100
   ip link set eth0.100 type vlan egress 0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7

   # set IP to br0.100 192.168.100.3

   tc qdisc add dev eth0.100 clsact
   tc filter add dev eth0.100 egress protocol ip prio 1 u32 match ip dport 5001 0xffff action skbedit priority 3

   #Real QoS configuration depends Host 2 functionality

   iperf3 -c 192.168.100.2 -t10 -p5001 -Tpri3 -t30
   # - or -
   iperf3 -c 192.168.100.2 -t10 -p5001 -Tpri3 -t30 -u -b210M

**Host 2 configuration**

.. code-block:: console

   ip link add link eth0 name eth0.100 type vlan id 100
   ip link set eth0.100 type vlan egress 0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7

   # set IP to br0.100 192.168.100.3

   iperf3 -s -p 5001&
   iperf3 -s -p 5002&
   iperf3 -s -p 5003&
