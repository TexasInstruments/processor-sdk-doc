===================
HSR PRP Non-Offload
===================

.. rubric:: **Introduction**

High-availability Seamless Redundancy (HSR) and Parellel Redundancy
Protocol (PRP) are protocols supporting redundant network connections defined
by IEC 62439-3. Both operate by using two ethernet ports together, and
duplicating every frame to be sent over both ports, so if one connection
fails, the transmission succeeds. Frames are tagged with a sequence number,
so the receiving node can identify and discard duplicates. HSR/PRP provides
an advantage over other protocols that handle link failure (e.g. STP/RSTP)
because there is no downtime or packet loss on link failure. This is
required in some industrial networking situations.

The major difference between HSR and PRP is that HSR networks are configured
as a ring, then frames are sent both directions around the ring by all nodes.
PRP networks can take any configuration, and all connections are simply
physically duplicated. Additionally, PRP nodes can interoperate with standard
ethernet networks, while HSR cannot. (See more details below and full details
in IEC 62439-3)

.. rubric:: **Linux HSR PRP Support**

Linux supports HSR/PRP protocol to be run over two EMAC ports where Linux
takes care of duplicating the packets sent over the two ethernet ports and
discarding the received duplicate packet. This is the non-offload HSR/PRP
mechanism.

.. rubric:: *Getting Started*

To try out HSR/PRP (assuming two supported platforms are set up already,
and the ethernet ports are eth1/eth2):

1) Connect the Ethernet ports between devices, eth1 to eth1 and eth2 to eth2.
(This acts as a 2 node ring for HSR, or a 2 node point-to-point for PRP)

2) The below script automates the steps to create a HSR/PRP interface using
ethernet interfaces and IP address for HSR/PRP provided as arguments

.. code-block:: bash

   #!/bin/sh

   if [ "$#" != "4" ]
   then
         echo "$0 <hsr|prp> <intf1> <intf2> <ip addr>"
         exit
   fi

   if [ "$1" != "hsr" ] && [ "$1" != "prp" ]
   then
         echo "$0 <hsr|prp>"
         exit
   fi

   if [ "$1" == "hsr" ]
   then
         if=hsr0
   else
         if=prp0
   fi

   ifa=$2
   ifb=$3

   ip=$4
   mac=`ifconfig $ifa | grep ether | cut -d " " -f 10`

   echo "ip=$ip"
   echo "if=$if"
   echo "mac=$mac"
   echo "slave-a=$ifa"
   echo "slave-b=$ifb"
   if [ "$1" == "hsr" ]
   then
         ip link delete prp0  2> /dev/null
   else
         ip link delete hsr0  2> /dev/null
   fi

   ip link set $ifa down
   ip link set $ifb down
   sleep 1

   ip link set dev $ifa address $mac
   ip link set dev $ifb address $mac

   if [ "$1" == "hsr" ]
   then
         ip link add name $if type hsr slave1 $ifa slave2 $ifb supervision 45 version 1
   else
         ip link add name $if type hsr slave1 $ifa slave2 $ifb supervision 45 proto 1
   fi
   sleep 3

   ip addr add $ip/24 dev $if
   ip link set $if up

   ip link set $ifa up
   ip link set $ifb up
   sleep 1

To create HSR interface with IP address 192.168.2.20 using eth1 and eth2, run
the script by passing the arguments as below

.. code-block:: console

   sh ./<script_filename.sh> hsr eth1 eth2 192.168.2.20

To create a PRP interface with IP address 192.168.2.20 using eth1 and eth2, run
the script by passing the arguments as below

.. code-block:: console

   sh ./<script_filename.sh> prp eth1 eth2 192.168.2.20

Please make sure that the IP address on both the platforms are unique

With the above configuration, if a ping is run between the two platforms on the
HSR/PRP interface, the ping will continue even if one of the connections is removed.

.. rubric:: *VLAN*

.. code-block:: console

   ifconfig hsr0 0.0.0.0
   ip link add link hsr0 name hsr0.2 type vlan id 2
   ip link add link hsr0 name hsr0.3 type vlan id 3

   ip addr add 192.168.2.3 dev hsr0.2
   ip addr add 192.168.3.3 dev hsr0.3

With the above configuration, tracing using tcpdump -i <hsr0> -xxx on the remote
side will show VLAN header with id information.

.. rubric:: *VLAN Filtering*

.. code-block:: console

   ip link add link hsr0 name hsr0.4 type vlan id 4

Suppose on the remote side a new VLAN ID '4' is created and attempt to ping
a system with only VLAN ID '2' and '3', the packet will be filtered and dropped.

.. rubric:: *Multicast Filtering*

All multi-cast addresses not registered will be filtered out.

.. rubric:: Multicast Add/Delete

Multicast MAC address can be added/deleted using ip maddr commands or Linux socket ioctl SIOCADDMULTI/SIOCDELMULTI.


.. rubric:: Show muliticast address

.. code-block:: console

   # ip maddr show dev <dev>
   2:      hsr0
   link  01:00:5e:00:00:01
   link  01:80:c2:00:00:00
   link  01:80:c2:00:00:03
   link  01:80:c2:00:00:0e
   link  01:00:5e:00:00:fc
   inet  224.0.0.252
   inet  224.0.0.1

.. rubric:: Add muliticast address

.. code-block:: console

   # ip maddr add 01:00:5e:00:00:05 dev hsr0
   # ip maddr show dev hsr0
   2:      hsr0
   link  01:00:5e:00:00:01
   link  01:80:c2:00:00:00
   link  01:80:c2:00:00:03
   link  01:80:c2:00:00:0e
   link  01:00:5e:00:00:fc
   link  01:00:5e:00:00:05 static
   inet  224.0.0.252
   inet  224.0.0.1

.. rubric:: Delete muliticast address

.. code-block:: console

   # ip maddr del 01:00:5e:00:00:05 dev hsr0
