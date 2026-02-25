With ICSS switch firmware, RSTP can be supported with L2 forwarding
offload on the ICSSs in  AM57x IDK platforms.

.. note::

   RSTP functionality over PRU Ethernet is neither tested nor supported
   on AM335x and AM437x.

Briefly, in this case, the PRU ethernet driver together with the
switch firmware are responsible for creating a forwarding database
(FDB) table. MAC address in a frame received on a physical port is
learned dynamically and a corresponding entry is created in the FDB
table. When frames with a learned MAC address as the destination
address is received, it will be cut-through forwarded to the port
indicated in the FDB entry directly without involving the host.

To set up a RSTP network with ICSS switch firmware, connect 3 AM571x-IDK
as follows:

.. Image:: /images/rstp_with_switch_firmware.jpg

Example: 3 node ring demonstrating RSTP with switch firmware

.. note::

 The ICSS switch firmware has multicast filtering enabled by default, hence it's important to ensure
 that STP multicast address 01:80:c2:00:00:00 is enabled in the ICSS switch firmware.
 The STP multicast address can be added manually to the bridge netdev once it's created,
 like: ``ip maddr add 01:80:c2:00:00:00 dev br0``, and PRU ethernet driver will ensure it's
 configured properly when PRU netdev added to the bridge.

|

.. note::

 Some rootfs systems, like systemd, may assign random, local MAC address to the bridge netdev by default.
 It's recommended to reassign bridge netdev MAC address to the MAC address of the one of the child interfaces.
 Like: ``ip link set dev br0 address $(cat /sys/class/net/<intf>/address)``

Boot up the IDKs as follows:

1. Boot IDKs into linux prompt.

2. Make sure the following lines appear in the boot log:

.. code-block:: bash

 [   30.617491] prueth pruss1_eth: TI PRU ethernet initialized: Dual EMAC mode
 [   31.207474] prueth pruss2_eth: TI PRU ethernet initialized: Dual EMAC mode

Note: timing is for reference only.

3. Run the following script rstp.sh on each IDK.

The script can be run with default (eth2, eth3, br0) or user parameters, like ``rstp.sh pru10 pru11``

.. code-block:: bash

 #!/bin/bash
 # rstp.sh

 set -x #echo on

 ETH1=${1:-eth2}
 ETH2=${2:-eth3}
 BR0=${4:-br0}

 mstpd
 sleep 1

 ip link set dev $ETH1 up
 sleep 1

 ip link set dev $ETH2 up
 sleep 1

 brctl addbr $BR0
 sleep 1

 # manually add STP MC address to enable it in PRU MC filter table
 ip maddr add 01:80:c2:00:00:00 dev $BR0

 ip link set dev $BR0 address $(cat /sys/class/net/$ETH1/address)

 brctl addif $BR0 $ETH1
 sleep 1

 brctl addif $BR0 $ETH2
 sleep 1

 brctl stp $BR0  on
 sleep 1

 mstpctl setforcevers $BR0 rstp
 sleep 1

 ip link set dev $BR0 up
 sleep 1

 mstpctl showbridge

|

The script

   a. starts mstpd daemon

   b. crates a bridge interface br0 on eth2 and eth3

   c. enables rstp on the bridge br0

   d. shows some information about the bridge

4. Issue command to show port information on each IDK:

.. code-block:: console

 $ mstpctl showport br0 eth2
 $ mstpctl showport br0 eth3

sample output:

.. code-block:: console

 eth2  8.001 forw 8.000.70:FF:76:1C:16:EF 8.000.70:FF:76:1C:16:EF 8.001 Desg

where

forw is the port state

Desg is the port role

Note 1:
In the test setup shown above , the port state and port role are shown in
(state, role), eg. (f,R) - port state is forwarding and port role is Root.

Note 2:
The (state, role) pairs may show on different DUTs but there must be
a discard state appears. This discard state is a result of the RSTP protocol
which breaks the cyclic connection into a tree (in this case, a serial
connection.

Note 3:
In step 3 as soon as the **both** interface are added to the Linux bridge, the
Ethernet device automatically change mode to SWITCH. When the interface is
brought up, driver loads SWITCH firmware and brings up the PRUs in switch
mode. Similarly when last interface is removed from the Linux bridge, the
driver change the Etherent type to Dual EMAC. Thus Dual EMAC firmware is
loaded and run at the PRUs when next time interface is brought up.

5. In step 4, make sure the cyclic connection is broken by a discard
   state in one of the ports of one of the DUTs.

   In setup in step 1, it is Dut2.eth2.

6. configure an IP address on br0 on any one DUT and another IP address
   of the same subnet on another DUT. E.g.

   on Dut1:
   $ ip addr add 192.168.1.1/24 dev br0

   on Dut3:
   $ ip addr add 192.168.1.2/24 dev br0

7. Make sure ping works fron Dut1 to Dut3.

8. Unplug any of the 3 cables and make sure the ping continues to work each time.


