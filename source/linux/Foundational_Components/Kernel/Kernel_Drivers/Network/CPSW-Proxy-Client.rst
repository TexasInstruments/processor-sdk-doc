.. _cpsw_proxy_client:

CPSW Proxy Client
-----------------

.. contents:: :local:
   :depth: 3

Introduction
============

The CPSW Proxy Client driver in Linux interfaces with Ethernet Switch Firmware (EthFw)
via RPMsg using the Linux Remoteproc framework. The CPSW Ethernet Switch on the SoC
is configured by EthFw which acts as the Server and provides services to Clients on
remote cores with the Linux Client on A53 / A72 core being the CPSW Proxy Client and
the driver corresponding to it located at:
drivers/net/ethernet/ti/cpsw-proxy-client.c
in the SDK's Linux Source.

The CPSW Proxy Client driver registers itself with the RPMsg framework and is probed
when EthFw announces the endpoint name "ti.ethfw.ethdevice" over the RPMsg-bus.
On being probed, the CPSW Proxy Client driver begins querying EthFw for the resources
available for its use. All the ABIs used for RPMsg communication between EthFw and the
CPSW Proxy Client driver are defined in:
drivers/net/ethernet/ti/eth_remote_msg.h
in the SDK's Linux Source.

The network data is sent/received over DMA Channels allocated for the Linux Client's use.
The allocated channels are communicated to the Client over RPMsg.

.. note::

   More details about EthFw can be found at:
   `Ethernet Firmware User Guide <https://software-dl.ti.com/jacinto7/esd/processor-sdk-rtos-jacinto7/latest/exports/docs/ethfw/docs/user_guide/ethfw_c_ug_top.html>`__

.. note::

   With the migration of EthFw to the standard RPMsg framework, the RPMsg-Kdrv framework is no longer required.
   The cpsw-proxy-client.c driver is the new Linux Client driver for the now deprecated j721e-cpsw-virt-mac.c driver.
   Any logs corresponding to the older "j721e-cpsw-virt-mac.c" driver may be safely ignored.

Terminology
"""""""""""

Virtual Port
   A virtual port refers to the Software View of an Ethernet port.

Virtual MAC Only Port
   A virtual MAC only port refers to a dedicated physical port for Linux's use.
   This corresponds to MAC Mode of operation in Ethernet Terminology where there
   is no broadcast traffic from other Physical Ports being forwarded to Linux and
   at the same time there is no broadcast traffic from Linux being sent out of other
   Physical ports.

Virtual Switch Port
   A virtual Switch Port refers to a group of physical ports with Switching enabled across
   them implying that any traffic sent from Linux using the Network interface
   corresponding to the Virtual Switch Port could potentially exit out of any of
   the group of physical ports based on the ALE's (Address Lookup Engine) decision.

Network Interface
   The user-visible interface in Linux userspace exposed to applications which serves as
   the entry/exit point for traffic to/from the Virtual Ports. A single network interface
   maps to either a Virtual MAC Only Port (implying a single physical port) or a Virtual
   Switch Port (implying a group of physical ports enabling the Switching functionality).

Configuration
"""""""""""""

All resources are allocated by EthFw to the Linux Client. Therefore all configuration has
to be performed only in EthFw and no changes are necessary in the Linux Client. It is possible
to configure the number of MAC Only Ports and Switch Ports allocated to Linux Client providing
flexibility based on the use-case.

.. _cpsw_proxy_client_enable:

Enabling CPSW Proxy Client Driver for Linux
"""""""""""""""""""""""""""""""""""""""""""

The following Linux build config need to be enabled for availing the CPSW Proxy Client
functionality:

.. code-block:: text

   CONFIG_TI_CPSW_PROXY_CLIENT

The CPSW Proxy Client functionality is enabled by applying the corresponding Linux device-tree
overlay at U-Boot prompt.

To enable Linux CPSW Proxy Client functionality, save the following command in uEnv.txt:

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   .. code-block:: text

      name_overlays="ti/k3-am62p5-sk-ethfw.dtbo"

.. ifconfig:: CONFIG_part_variant in ('J721E')

   .. code-block:: text

      name_overlays="ti/k3-j721e-evm-ethfw.dtbo"

.. ifconfig:: CONFIG_part_variant in ('J7200')

   .. code-block:: text

      name_overlays="ti/k3-j7200-evm-ethfw.dtbo"

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

   .. code-block:: text

      name_overlays="ti/k3-j784s4-evm-ethfw.dtbo"

.. note::

   The overlays have to be applied to ensure that Linux doesn't override the Serdes configuration
   and also to reserve Shared Memory for EthFw.

Execution Flow
""""""""""""""

1. The CPSW Proxy Client driver registers itself with the Linux RPMsg Framework as an RPMsg Endpoint.
2. EthFw announces the endpoint name "ti.ethfw.ethdevice" over the RPMsg-bus resulting in the CPSW Proxy
   Client driver getting probed.
3. On being probed, the CPSW Proxy Client driver requests EthFw for details regarding the number of Virtual
   Ports as well as their types.
4. In response to the request, EthFw replies with details regarding the allocated Virtual Ports and their
   types.
5. With the knowledge of the available Virtual Ports, the Client driver requests details of the allocated
   DMA Channels and MAC Addresses corresponding to each of the Virtual Ports.
6. The Client driver receives the details from EthFw and proceeds to request the creation of the DMA Channels
   using the Linux DMA APIs for requesting the DMA driver correspondig to the SoC.
7. The Client driver proceeds with the creation of one Network Interface per Virtual Port and registers the MAC
   Address corresponding to the Virtual Port with the Linux Network Subsystem.
8. In the case of Virtual Ports that are Switch Ports, the Client driver registers the IP Address allocated to
   the Network Interface with EthFw. The Network Interface could obtain an IP Address either through DHCP protocol
   or could be assigned a static IP Address from userspace as well.
9. At this point all Network Interfaces corresponding to the Virtual Ports are up and functional and can transmit
   and receive Network Traffic from the Ethernet Ports corresponding to the CPSW Ethernet Switch that is managed
   by EthFw.

Interpreting the boot logs
"""""""""""""""""""""""""""

The CPSW Proxy Client driver logs can be filtered using the command:

.. code-block:: console

   dmesg | grep ti_cpsw_proxy_client

If the driver is probed successfully, something similar to the following content will show up in the filtered logs
based on the configuration performed on EthFw for the allocation of Virtual Ports to the Linux Client:

.. code-block:: console

   ti_cpsw_proxy_client virtio2.ti.ethfw.ethdevice.-1.101: 1 Virtual Switch Port(s), 1 Virtual MAC Only P
   ti_cpsw_proxy_client virtio2.ti.ethfw.ethdevice.-1.101: Virt Port: 0, Type: Switch Port, Iface: eth1, Num TX: 2, Num RX: 1, Token: 0
   ti_cpsw_proxy_client virtio2.ti.ethfw.ethdevice.-1.101: Virt Port: 4, Type: MAC Port, Iface: eth2, Num TX: 1, Num RX: 1, Token: 400

The logs indicate that 1 Virtual Switch Port and 1 Virtual MAC Only Port have been allocated to the Linux Client.
Therefore the CPSW Proxy Client driver shall create two interfaces corresponding to each of the Virtual Ports.
The logs indicate that the network interface "eth1" corresponds to the "Switch Port" as indicated in the "Type" field.
Similarly, the network interface "eth2" corresponds to the "MAC Port" (MAC Only Port). Additionally, the interface eth1
has been allocated "2" TX DMA Channels and "1" RX DMA Flow, while the interface eth2 has been allocated "1" TX DMA Channel
and "1" RX DMA Flow.

Features
""""""""

Fetching/Setting IP Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each interface can either get an IP address dynamically allocated to it by a DHCP server using the command:

.. code-block:: console

   udhcpc -i <ethX>

Or it can be assigned a Static IP address manually using the command:

.. code-block:: console

   ifconfig <ethX> <IP-Address>

Setting MAC Address
^^^^^^^^^^^^^^^^^^^

MAC Address can be assigned to interfaces using the commands:

.. code-block:: console

   ifconfig <ethX> down
   ifconfig <ethX> hw ether <MAC-Address>
   ifconfig <ethX> up

Multicast Filtering
^^^^^^^^^^^^^^^^^^^

EthFW supports Multicast Filtering which allows offloading Multicast addresses to CPSW Ethernet Switch thereby allowing Multicast
addresses to be forwarded to Linux.

EthFW supports the following logical types of Multicast addresses:

*Exclusive Multicast Addresses*
   Traffic with such multicast addresses will be directed exclusively to
   Linux via the Linux Client driver.

*Shared Multicast Addresses*
   Traffic with such multicast addresses will be delivered to Linux host
   by other means (i.e. shared memory based TAP interface). Shared multicast
   addresses are used to deliver traffic to more than one core on the
   |__PART_FAMILY_NAME__| SoC. The TAP interface is not implemented by the
   CPSW Proxy Client driver. The TAP interface has to be present and enabled
   in order to receive the traffic corresponding to the Shared Multicast
   Addresses. For more details on the TAP interface, please refer to:
   `TAP interface for intercore traffic <https://software-dl.ti.com/jacinto7/esd/processor-sdk-rtos-jacinto7/latest/exports/docs/ethfw/docs/user_guide/ethfw_c_ug_top.html#ethfw_intercore_a72client>`__

*Reserved Multicast Addresses*
   Traffic with such multicast addresses is reserved and intended to be
   consumed by EthFW only.

The CPSW Proxy Client driver offloads all requested multicast addresses irrespective
of their type. Reserved multicast addresses which are offloaded are treated as NOP
by EthFw.

Multicast MAC addresses can be added/deleted using the *ip maddr* command:

.. code-block:: console

   # Add Multicast address <Multicast-Address>
   ip maddr add <Multicast-Address> dev <ethX>

   # Check if entry has been added successfully
   ip maddr show dev <ethX>

   # Delete Multicast address <Multicast-Address>
   ip maddr del <Multicast-Address> dev <ethX>

TX QoS
^^^^^^

QoS on the transmit path from the Client to the external network consists of two stages:

#. TX DMA Channel QoS
#. CPSW MAC Port FIFO QoS

Stage-1: TX DMA Channel QoS
'''''''''''''''''''''''''''

EthFw supports allocating multiple TX DMA Channels to a Virtual Port used by the Linux Client.
The presence of multiple TX DMA Channels allows the client to enable QoS functionality by
distributing the traffic across the DMA Channels on the transmit path by using the mapping between
the traffic priority and the DMA Channel. The "tc" framework in Linux is used to specify this mapping
between the traffic priority (DSCP to SKB priority) and the traffic class (DMA Channel).
There are as many traffic classes as the TX DMA Channels available for the interface.
Traffic classes range from 0 to N-1 where N is the number of TX DMA Channels.

Consider the example of the interface eth1 having 2 TX DMA Channels. For the mapping defined as:

.. code-block:: text

   Priorities 0, 1, 2 and 3 belong to TC 0 (Traffic Class 0 => TX DMA Channel 0)
   Priorities 4, 5, 6 and 7 belong to TC 1 (Traffic Class 1 => TX DMA Channel 1)

the corresponding "tc" command to be run in userspace is:

.. code-block:: console

   tc qdisc add dev eth1 handle 100: parent root mqprio num_tc 2 \
   map 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0 queues 1@0 1@1 hw 0

For more details on the above command, please refer: `tc-mqprio <https://man7.org/linux/man-pages/man8/tc-mqprio.8.html>`__

With the above command executed, all traffic transmitted on the eth1 interface from the Client
having SKB priorities 0,1,2 and 3 will be sent using TX DMA Channel 0 of the eth1 interface while
traffic having SKB priorities 4,5,6 and 7 will be sent using TX DMA Channel 1 of the eth1 interface.

.. note::

   | Bits 3 to 5 of the DSCP value are used to determine the SKB priority in Linux.
   | The DSCP value can be chosen accordingly to achieve the desired SKB priority and TX QoS functionality.
   | SKB priority = ((DSCP >> 3) & 0x7)

Stage-2: CPSW MAC Port FIFO QoS
''''''''''''''''''''''''''''''''

When the DSCP tagged traffic sent from the Client over the TX DMA Channels is received by the
CPSW Host Port, the DSCP priority of the traffic is used to determine the FIFO in the Egress MAC Port
that the traffic has to be queued into. Each MAC Port has 8 TX FIFOs corresponding to 8 priorities.
Traffic from different Clients having the same DSCP priority and egressing on the same MAC Port
will be queued in the same TX FIFO of the MAC Port, thereby providing uniform QoS across clients.
