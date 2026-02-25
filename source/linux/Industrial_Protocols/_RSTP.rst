This is a simple demonstration example to setup a RSTP network which is
a mode of the mstpd daemon that is provided in the Processors Linux SDK
file system. This example setup is done from the Linux command line.
Users that require automatic interface, bridge and msptd daemon setup at
system initialization will need to do the steps necessary to implement
this initialization method.

.. note::

   RSTP functionality over PRU Ethernet is neither tested nor supported
   on AM335x and AM437x.

|
| If you need a background in the bridge utility that Linux supports
  please refer to this link.

https://wiki.linuxfoundation.org/networking/bridge

|
| The link above documents the kernel brctl utility that creates network
  bridges and the spanning tree protocol (STP) support provided by the
  kernel. To go beyond STP requires a user level daemon that will manage
  the tree topology and changes to that topology. The pre-built kernel
  binaries and file system do not require changes to use the mstpd
  daemon. RSTP mode of the mstpd daemon was tested on TI EVMs that have
  multiple CPSW or PRU ports. Multi-port boards will have dual mac mode
  enabled for the CPSW as out of the box configurations for TI EVMs.
  There are additional PRU-ICSS Ethernet ports available on the AM57x
  class IDK boards. This diagram shows one of the topologies used to
  test the setup.

|

.. Image:: /images/Cpsw_rstp_mstpd_topology_1.jpg

3 node ring demonstrating port blocking on low cost link

|

Please note that the topology was tested across CPSW only ports,
PRU-ICSS Ethernet only ports and a one CPSW and one PRU-ICSS port.

|
| To set up the environment shown above, first on each board bring up
  the interfaces that will be used for the bridge with the ifconfig
  command. Next on each board a bridge must be created and then add in
  the two interfaces to the bridge. The bridge is then enabled in STP
  mode. Then as a last configuration step use the mstpctl utility to
  transition the bridge from STP to RSTP mode.

|

Setup the ports, IP addresses are not used for the Ethernet ports in a
bridge.

|
| ifconfig eth0 up

ifconfig eth1 up

|
| Now create and setup bridge br0 using the brctl application.

|
| brctl create br0

brctl addif br0 eth0

brctl addif br0 eth1

ifconfig br0 up

|
| Now switch the bridge mode from stp to rstp using the mstpctl
  application

|
| mstpctl setforcevers br0 rstp

|
| Now look on each platform to verify where the root node is with these
  commands

|
| mstpctl showbridge

