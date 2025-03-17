===================
HSR Offload
===================

.. rubric:: **Introduction**

Redundant and reliable communication is necessary for the highly critical nature of grid infrastructure where network failures can lead to a disruption in electricity distribution. The international standard IEC 61850 addresses this importance and defines communication protocols that provide this redundancy and reliability needed within these grid substations. High-availability Seamless Redundancy (HSR) and Parallel Redundancy Protocol (PRP) are communication protocols defined by this standard, and they are the preferred protocols in today’s industry because there is no downtime or packet loss when a link failure occurs. In terms of current offload support, HSR will be the main focus. As mentioned in the HSR PRP Non-offload Section of these release notes, HSR is a protocol that supports redundant network connections, usually configured as a ring with Ethernet frames being sent in both directions. If one path around the ring fails, the other duplicated packet will still reach the intended destination. 

When implementing HSR solutions in grid substations, traditionally, FPGAs and ASICs were used to support the HSR standard, but with modern processors and hardware accelerators, the AM64x provides a more cost-effective solution for implementing substation requirements, including HSR. Offloading is the process of transferring tasks away from the CPU to another processing unit. In the case of the AM64x Sitara Processor, HSR tasks can be offloaded from the A53 cores to the PRU_ICSSG. 

.. rubric:: **Linux HSR Offload Support**
HSR framework in Linux allows offloading below functionalities to the device:
   •  hsr-fwd-offload: For forwarding HSR frames one port to another i.e. port-to-port forwarding 
   •	hsr-dup-offload: Duplicate the outgoing HSR frame
   •	hsr-tag-ins-offload: Unique tag to identify HSR frames
   •	hsr-tag-rm-offload: Removes the HSR tags

The ICSSG HSR firmware supports these features which offloads these capabilities from the HSR driver in software to the PRU-ICSSG. Cut-through switching improves HSR latency but would need to be implemented separately. 


To enable offloading using below commands
To enable port-to-port offload

.. code-block:: console

  ethtool -K <interface> hsr-fwd-offload on

To enable Tx packet duplication

.. code-block:: console

  ethtool -K <interface> hsr-fwd-offload on
  ethtool -K <interface> hsr-dup-offload on

.. note::
   The ICSSG HSR firmware is designed to always carry out port-to-port
   forwarding. So whenever any of the HSR features are to be offloaded, the
   port-to-port forwarding must also be offloaded. It is not possible to offload
   only Tx packet duplication functionality.

The below script sets up an HSR interface with the port-to-port
forwarding and Tx packet duplication offloaded

.. code-block:: bash

  #!/bin/sh

  #For non offload - sh hsr_setup.sh hsr_sw <INTF_A> <INTF_B> <HSR_INTF_IP_ADDR>
  #For offload - sh hsr_setup.sh hsr_hw <INTF_A> <INTF_B> <HSR_INTF_IP_ADDR>

  if [ "$#" != "4" ]
  then
          echo "$0 <hsr_sw/hsr_hw> <intf1> <intf2> <ip addr>"
          exit
  fi

  if [ "$1" != "hsr_sw" ] && [ "$1" != "hsr_hw" ]
  then
          echo "$0 <hsr_sw|hsr_hw>"
          exit
  fi

  if=hsr0

  ifa=$2
  ifb=$3

  ip=$4
  mac=$(ifconfig "$ifa" | grep ether | cut -d " " -f 10)

  echo "ip=$ip"
  echo "if=$if"
  echo "mac=$mac"
  echo "slave-a=$ifa"
  echo "slave-b=$ifb"

  ip link set hsr0 down
  ip link delete hsr0  2> /dev/null

  if [ "$1" = "hsr_hw" ]
  then
          ethtool -k "$ifa" | grep hsr
          ethtool -K "$ifa" hsr-fwd-offload on
          ethtool -K "$ifa" hsr-dup-offload on
          ethtool -K "$ifa" hsr-tag-ins-offload on
          ethtool -K "$ifa" hsr-tag-rm-offload on
          ethtool -k "$ifa" | grep hsr

          ethtool -k "$ifb" | grep hsr
          ethtool -K "$ifb" hsr-fwd-offload on
          ethtool -K "$ifb" hsr-dup-offload on
          ethtool -K "$ifb" hsr-tag-ins-offload on
          ethtool -K "$ifb" hsr-tag-rm-offload on
          ethtool -k "$ifb" | grep hsr
  fi

  ip link set dev "$ifa" address "$mac"
  ip link set dev "$ifb" address "$mac"

  ip link add name $if type hsr slave1 "$ifa" slave2 "$ifb" supervision 45 version 1

  sleep 3

  ip addr add "$ip"/24 dev $if
  ip link set $if up

To create HSR interface with IP address 192.168.2.20 using eth1 and eth2,
run the script by passing the arguments as below

.. code-block:: console

  sh hsr_setup.sh hsr_hw eth1 eth2 192.168.2.20

.. rubric:: *Multicast Filtering*

All multi-cast addresses not registered will be filtered out.

.. rubric:: Multicast Add/Delete

Multicast MAC address can be added/deleted using ip maddr commands or Linux socket ioctl SIOCADDMULTI/SIOCDELMULTI.

.. rubric:: Show multicast address

Show current list of multicast address for the HSR interface

.. code-block:: console

  ip maddr show dev <hsr_intf>

Example:

.. code-block:: console

  # ip maddr show dev hsr0
  7:      hsr0
          link  33:33:00:00:00:01 users 3
          link  01:00:5e:00:00:01 users 3
          link  33:33:ff:1e:e8:10 users 3
          link  01:00:5e:00:00:fb users 3
          link  01:00:5e:00:00:fc users 3
          link  33:33:00:00:00:fb users 3
          link  33:33:00:01:00:03 users 3
          inet  224.0.0.252
          inet  224.0.0.251
          inet  224.0.0.1
          inet6 ff02::1:3
          inet6 ff02::fb
          inet6 ff02::1:ff1e:e810
          inet6 ff02::1
          inet6 ff01::1

.. rubric:: Add multicast address

Add a multicast address

.. code-block:: console

  ip maddr add <multicast_mac_addr> dev <hsr_intf>

Example: To add a multicast address and display the list in HSR and slave ports

.. code-block:: console

  # ip maddr add 01:80:c4:00:00:0e dev hsr0
  # ip maddr show dev hsr0
  7:      hsr0
          link  33:33:00:00:00:01 users 3
          link  01:00:5e:00:00:01 users 3
          link  33:33:ff:1e:e8:10 users 3
          link  01:00:5e:00:00:fb users 3
          link  01:00:5e:00:00:fc users 3
          link  33:33:00:00:00:fb users 3
          link  33:33:00:01:00:03 users 3
          link  01:80:c4:00:00:0e users 3 static
          inet  224.0.0.252
          inet  224.0.0.251
          inet  224.0.0.1
          inet6 ff02::1:3
          inet6 ff02::fb
          inet6 ff02::1:ff1e:e810
          inet6 ff02::1
          inet6 ff01::1

  # ip maddr show dev eth1
  5:      eth1
          link  01:00:5e:00:00:01 users 2
          link  33:33:00:00:00:01 users 2
          link  33:33:ff:1e:e8:10 users 2
          link  01:80:c2:00:00:00
          link  01:80:c2:00:00:03
          link  01:80:c2:00:00:0e
          link  33:33:00:00:00:fb users 2
          link  33:33:00:01:00:03 users 2
          link  01:00:5e:00:00:fb
          link  01:00:5e:00:00:fc
          link  01:80:c4:00:00:0e
          inet  224.0.0.1
          inet6 ff02::1:3
          inet6 ff02::fb
          inet6 ff02::1:ff1e:e810
          inet6 ff02::1 users 2
          inet6 ff01::1

  # ip maddr show dev eth2
  6:      eth2
          link  01:00:5e:00:00:01 users 2
          link  33:33:00:00:00:01 users 2
          link  33:33:ff:1e:e8:10 users 2
          link  01:80:c2:00:00:00
          link  01:80:c2:00:00:03
          link  01:80:c2:00:00:0e
          link  01:00:5e:00:00:fb
          link  01:00:5e:00:00:fc
          link  33:33:00:00:00:fb users 2
          link  33:33:00:01:00:03 users 2
          link  01:80:c4:00:00:0e
          inet  224.0.0.1
          inet6 ff02::1:3
          inet6 ff02::fb
          inet6 ff02::1:ff1e:e810
          inet6 ff02::1 users 2
          inet6 ff01::1

.. rubric:: Delete multicast address

Delete a multicast address

.. code-block:: console

  ip maddr del <multicast_mac_addr> dev <hsr_intf>

Example: To delete an added multicast address and dislay the list of HSR and
slave intefaces.

.. code-block:: console

  # ip maddr del 01:80:c4:00:00:0e dev hsr0

  # ip maddr show dev hsr0
  7:      hsr0
          link  33:33:00:00:00:01 users 3
          link  01:00:5e:00:00:01 users 3
          link  33:33:ff:1e:e8:10 users 3
          link  01:00:5e:00:00:fb users 3
          link  01:00:5e:00:00:fc users 3
          link  33:33:00:00:00:fb users 3
          link  33:33:00:01:00:03 users 3
          inet  224.0.0.252
          inet  224.0.0.251
          inet  224.0.0.1
          inet6 ff02::1:3
          inet6 ff02::fb
          inet6 ff02::1:ff1e:e810
          inet6 ff02::1
          inet6 ff01::1

  # ip maddr show dev eth1
  5:      eth1
          link  01:00:5e:00:00:01 users 2
          link  33:33:00:00:00:01 users 2
          link  33:33:ff:1e:e8:10 users 2
          link  01:80:c2:00:00:00
          link  01:80:c2:00:00:03
          link  01:80:c2:00:00:0e
          link  33:33:00:00:00:fb users 2
          link  33:33:00:01:00:03 users 2
          link  01:00:5e:00:00:fb
          link  01:00:5e:00:00:fc
          inet  224.0.0.1
          inet6 ff02::1:3
          inet6 ff02::fb
          inet6 ff02::1:ff1e:e810
          inet6 ff02::1 users 2
          inet6 ff01::1

  # ip maddr show dev eth2
  6:      eth2
          link  01:00:5e:00:00:01 users 2
          link  33:33:00:00:00:01 users 2
          link  33:33:ff:1e:e8:10 users 2
          link  01:80:c2:00:00:00
          link  01:80:c2:00:00:03
          link  01:80:c2:00:00:0e
          link  01:00:5e:00:00:fb
          link  01:00:5e:00:00:fc
          link  33:33:00:00:00:fb users 2
          link  33:33:00:01:00:03 users 2
          inet  224.0.0.1
          inet6 ff02::1:3
          inet6 ff02::fb
          inet6 ff02::1:ff1e:e810
          inet6 ff02::1 users 2
          inet6 ff01::1

.. rubric:: *Multicast Filtering for VLAN Interfaces*

Multicast filtering for VLAN interfaces is also supported.

Show current list of multicast address for the HSR VLAN interface

.. code-block:: console

   ip maddr show dev <hsr_vlan_intf>

Example:

.. code-block:: console

   # ip maddr show dev hsr0.5

Add multicast address for the HSR VLAN interface

.. code-block:: console

   ip maddr add <multicast_mac_addr> dev <hsr_vlan_intf>

Example:

.. code-block:: console

   # ip maddr add 01:80:c4:00:00:0e dev hsr0.5

Delete multicast address for the HSR VLAN interface

.. code-block:: console

   ip maddr del <multicast_mac_addr> dev <hsr_vlan_intf>

Example:

.. code-block:: console

   # ip maddr del 01:80:c4:00:00:0e dev hsr0.5

.. rubric:: Performance

This section describes the throughput and CPU usage metrics in the offload case

.. rubric:: Setup

A sample test setup is as show below

.. Image:: /images/HSR_Offload_Setup_AM64x.png
  :width: 400

.. rubric:: Test Procedure

#.  Connect the LAN  cables between the DANH as shown in the Section 1

#.  Execute the commands to setup and create HSR interface

     #. To setup HSR non-offload on Node A and Node C,

	.. code-block:: console

           sh hsr_setup.sh hsr_sw <INTF_A> <INTF_B> <HSR_INTF_IP_ADDR>

     #. To Setup HSR offload on Node B,

        .. code-block:: console

           sh hsr_setup.sh hsr_hw <INTF_A> <INTF_B> <HSR_INTF_IP_ADDR>

#.  Confirm ping across all Nodes

     a. Node A < - - > Node B
     b. Node B < - - > Node C
     c. Node C < - - > Node A

#.  Disconnect the LAN cable between Node A and Node C

#.  Monitor the CPU usage on Node B

    .. code-block:: console

       mpstat -P ALL 1

#.  Run iperf3 server on Node C

    .. code-block:: console

       iperf3 -s -i 1

#.  Run iperf3 client on Node A for 60 secs

    .. code-block:: console

       iperf3 -c -1 -t 60 <Node_C_IP_Addr>

.. rubric:: CPU Usage on Node B

CPU usage at Node B found to be negligible

.. code-block:: text

  ** Snippet from the continuous stats **
  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest   %idle
  all    0.00    0.00    0.50    0.00    0.00    0.00    0.00    0.00   99.50
    0    0.00    0.00    1.00    0.00    0.00    0.00    0.00    0.00   99.00
    1    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00  100.00

  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest   %idle
  all    0.50    0.00    0.00    0.00    0.00    0.00    0.00    0.00   99.50
    0    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00  100.00
    1    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00  100.00

.. rubric:: Througput at Node A

.. list-table:: Throughput performance
   :widths: 25 25

   * - Sender
     - Receiver
   * - 505 Mbits/sec
     - 504 Mbits/sec
