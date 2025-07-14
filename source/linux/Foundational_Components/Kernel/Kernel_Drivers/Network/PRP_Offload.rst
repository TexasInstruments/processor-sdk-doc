===================
PRP Offload
===================

.. rubric:: **Introduction**

HSR (High-availability Seamless Redundancy) framework in Linux supports HSR and PRP (Parallel Redundancy Protocol) modes of redundancy by using 2 ports.
It also allows to offload the below functionalities of PRP mode to the underlying hardware/device:

- hsr-tag-ins-offload: Add PRP trailer to the frame
- hsr-dup-offload: Duplicate the outgoing PRP frame
- hsr-tag-rm-offload: Remove PRP trailer from the frame

The ICSSG PRP firmware supports offloading of all above functionalities saving overhead from the driver.

.. note::

   The offload of functionality hsr-fwd-offload should also be enabled for correct driver configuration.

The below script sets up a PRP interface with all possible offload functionalities enabled

.. code-block:: bash

   #!/bin/sh

   #For non offload - sh prp_setup.sh prp_sw <INTF_A> <INTF_B> <PRP_INTF_IP_ADDR>
   #For offload - sh prp_setup.sh prp_hw <INTF_A> <INTF_B> <PRP_INTF_IP_ADDR>

   if [ "$#" != "4" ]
   then
         echo "$0 <prp_sw/prp_hw> <intf1> <intf2> <ip addr>"
         exit
   fi

   if [ "$1" != "prp_sw" ] && [ "$1" != "prp_hw" ]
   then
         echo "$0 <prp_sw|prp_hw>"
         exit
   fi

   if=prp0

   ifa=$2
   ifb=$3

   ip=$4
   mac=$(ifconfig "$ifa" | grep ether | cut -d " " -f 10)

   echo "ip=$ip"
   echo "if=$if"
   echo "mac=$mac"
   echo "slave-a=$ifa"
   echo "slave-b=$ifb"

   ip link set $if down
   ip link delete $if  2> /dev/null

   if [ "$1" = "prp_hw" ]
   then
         echo "Available offload features for $ifa: "
         ethtool -k "$ifa" | grep hsr
         ethtool -K "$ifa" hsr-fwd-offload on
         ethtool -K "$ifa" hsr-dup-offload on
         ethtool -K "$ifa" hsr-tag-ins-offload on
         ethtool -K "$ifa" hsr-tag-rm-offload on
         echo "Enabled offload features for $ifa: "
         ethtool -k "$ifa" | grep hsr

         echo "Available offload features for $ifb: "
         ethtool -k "$ifb" | grep hsr
         ethtool -K "$ifb" hsr-fwd-offload on
         ethtool -K "$ifb" hsr-dup-offload on
         ethtool -K "$ifb" hsr-tag-ins-offload on
         ethtool -K "$ifb" hsr-tag-rm-offload on
         echo "Enabled offload features for $ifb: "
         ethtool -k "$ifb" | grep hsr
   fi

   ip link set dev "$ifa" address "$mac"
   ip link set dev "$ifb" address "$mac"

   ip link add name $if type hsr slave1 "$ifa" slave2 "$ifb" supervision 45 proto 1

   sleep 3

   ip addr add "$ip"/24 dev $if
   ip link set $if up

To create PRP interface with IP address 192.168.1.10 using eth1 and eth2,
run the script by passing the arguments as below

.. code-block:: console

   sh prp_setup.sh prp_hw eth1 eth2 192.168.1.10

.. rubric:: *Multicast Filtering*

All multi-cast addresses not registered will be filtered out.

.. rubric:: Multicast Add/Delete

Multicast MAC address can be added/deleted using ip maddr commands or Linux socket ioctl SIOCADDMULTI/SIOCDELMULTI.

.. rubric:: Show multicast address

Show current list of multicast address for the PRP interface

.. code-block:: console

   ip maddr show dev <prp_intf>

Example:

.. code-block:: console

   # ip maddr show dev prp0
   7:      prp0
            link  33:33:00:00:00:01 users 3
            link  01:80:c2:00:00:0e users 3 static
            link  01:80:c2:00:00:03 users 3 static
            link  01:80:c2:00:00:00 users 3 static
            link  01:00:5e:00:00:01 users 3
            link  33:33:ff:1e:a0:a8 users 3
            link  01:00:5e:00:00:fb users 3
            link  33:33:00:00:00:fb users 3
            inet  224.0.0.251
            inet  224.0.0.1
            inet6 ff02::fb
            inet6 ff02::1:ff1e:a0a8
            inet6 ff02::1
            inet6 ff01::1

.. rubric:: Add multicast address

Add a multicast address

.. code-block:: console

   ip maddr add <multicast_mac_addr> dev <prp_intf>

Example: To add a multicast address and display the list in PRP and slave ports

.. code-block:: console

   # ip maddr add 01:80:c4:00:00:0e dev prp0
   # ip maddr show dev prp0
   7:      prp0
            link  33:33:00:00:00:01 users 3
            link  01:80:c2:00:00:0e users 3 static
            link  01:80:c2:00:00:03 users 3 static
            link  01:80:c2:00:00:00 users 3 static
            link  01:00:5e:00:00:01 users 3
            link  33:33:ff:1e:a0:a8 users 3
            link  01:00:5e:00:00:fb users 3
            link  33:33:00:00:00:fb users 3
            link  01:80:c4:00:00:0e users 3 static
            inet  224.0.0.251
            inet  224.0.0.1
            inet6 ff02::fb
            inet6 ff02::1:ff1e:a0a8
            inet6 ff02::1
            inet6 ff01::1

   # ip maddr show dev eth1
   5:      eth1
            link  33:33:00:00:00:01 users 3
            link  01:00:5e:00:00:01 users 3
            link  01:80:c2:00:00:0e users 4 static
            link  01:80:c2:00:00:03 users 4 static
            link  01:80:c2:00:00:00 users 4 static
            link  33:33:ff:1e:a0:a8 users 3
            link  33:33:00:00:00:fb users 3
            link  01:00:5e:00:00:fb users 2
            link  01:80:c4:00:00:0e users 2
            inet  224.0.0.1
            inet6 ff02::fb
            inet6 ff02::1:ff1e:a0a8
            inet6 ff02::1 users 2
            inet6 ff01::1

   # ip maddr show dev eth2
   6:      eth2
            link  33:33:00:00:00:01 users 3
            link  01:00:5e:00:00:01 users 3
            link  01:80:c2:00:00:0e users 4 static
            link  01:80:c2:00:00:03 users 4 static
            link  01:80:c2:00:00:00 users 4 static
            link  33:33:ff:1e:a0:a7 users 2
            link  33:33:00:00:00:fb users 3
            link  33:33:ff:1e:a0:a8 users 2
            link  01:00:5e:00:00:fb users 2
            link  01:80:c4:00:00:0e users 2
            inet  224.0.0.1
            inet6 ff02::fb
            inet6 ff02::1:ff1e:a0a7
            inet6 ff02::1 users 2
            inet6 ff01::1

.. rubric:: Delete multicast address

Delete a multicast address

.. code-block:: console

   ip maddr del <multicast_mac_addr> dev <prp_intf>

Example: To delete an added multicast address and dislay the list of PRP and
slave intefaces.

.. code-block:: console

   # ip maddr del 01:80:c4:00:00:0e dev prp0
   # ip maddr show dev prp0
   7:      prp0
            link  33:33:00:00:00:01 users 3
            link  01:80:c2:00:00:0e users 3 static
            link  01:80:c2:00:00:03 users 3 static
            link  01:80:c2:00:00:00 users 3 static
            link  01:00:5e:00:00:01 users 3
            link  33:33:ff:1e:a0:a8 users 3
            link  01:00:5e:00:00:fb users 3
            link  33:33:00:00:00:fb users 3
            inet  224.0.0.251
            inet  224.0.0.1
            inet6 ff02::fb
            inet6 ff02::1:ff1e:a0a8
            inet6 ff02::1
            inet6 ff01::1

   # ip maddr show dev eth1
   5:      eth1
            link  33:33:00:00:00:01 users 3
            link  01:00:5e:00:00:01 users 3
            link  01:80:c2:00:00:0e users 4 static
            link  01:80:c2:00:00:03 users 4 static
            link  01:80:c2:00:00:00 users 4 static
            link  33:33:ff:1e:a0:a8 users 3
            link  33:33:00:00:00:fb users 3
            link  01:00:5e:00:00:fb users 2
            inet  224.0.0.1
            inet6 ff02::fb
            inet6 ff02::1:ff1e:a0a8
            inet6 ff02::1 users 2
            inet6 ff01::1

   # ip maddr show dev eth2
   6:      eth2
            link  33:33:00:00:00:01 users 3
            link  01:00:5e:00:00:01 users 3
            link  01:80:c2:00:00:0e users 4 static
            link  01:80:c2:00:00:03 users 4 static
            link  01:80:c2:00:00:00 users 4 static
            link  33:33:ff:1e:a0:a7 users 2
            link  33:33:00:00:00:fb users 3
            link  33:33:ff:1e:a0:a8 users 2
            link  01:00:5e:00:00:fb users 2
            inet  224.0.0.1
            inet6 ff02::fb
            inet6 ff02::1:ff1e:a0a7
            inet6 ff02::1 users 2
            inet6 ff01::1

.. rubric:: *Multicast Filtering for VLAN Interfaces*

Multicast filtering for VLAN interfaces is also supported.

Show current list of multicast address for the PRP VLAN interface

.. code-block:: console

   ip maddr show dev <prp_vlan_intf>

Example:

.. code-block:: console

   # ip maddr show dev prp0.5

Add multicast address for the PRP VLAN interface

.. code-block:: console

   ip maddr add <multicast_mac_addr> dev <prp_vlan_intf>

Example:

.. code-block:: console

   # ip maddr add 01:80:c4:00:00:0e dev prp0.5

Delete multicast address for the PRP VLAN interface

.. code-block:: console

   ip maddr del <multicast_mac_addr> dev <prp_vlan_intf>

Example:

.. code-block:: console

   # ip maddr del 01:80:c4:00:00:0e dev prp0.5

.. rubric:: Performance

This section describes the throughput and CPU usage metrics in the offload case

.. rubric:: Setup

A sample test setup is as shown below

.. Image:: /images/AM64_PRP_Setup.jpg
   :width: 400

.. rubric:: Test Procedure

#. Connect the LAN cables between the DANP DUTs as shown in the setup image

#. Execute the commands to setup and create PRP interface

   .. code-block:: console

      sh prp_setup.sh prp_hw <INTF_A> <INTF_B> <PRP_INTF_IP_ADDR>

#. Confirm ping across all Nodes

   #. Node A < - - > Node B
   #. Node B < - - > Node C
   #. Node C < - - > Node A

#. Disconnect one of the cable for a node and retry

#. Monitor the CPU usage on DUTs

   .. code-block:: console

      mpstat -P ALL 1

#. Run iperf3 server on Node C

   .. code-block:: console

      iperf3 -s

#. Run iperf3 client on Node A for 60 secs

   .. code-block:: console

      iperf3 -c -t60 <Node_C_IP_Addr>

.. rubric:: Throughput at Node A

.. list-table:: Throughput performance
   :widths: 25 25

   * - Sender
     - Receiver
   * - 610 Mbits/sec
     - 605 Mbits/sec
