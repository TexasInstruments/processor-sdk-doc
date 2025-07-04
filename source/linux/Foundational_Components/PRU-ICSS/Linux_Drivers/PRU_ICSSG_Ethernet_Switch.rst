**********************************
PRU_ICSSG Two Port Ethernet Switch
**********************************

PRU_ICSSG can operate as VLAN aware Switch mode with two external physical ports
and one internal host port. By default, interfaces come up in Dual independent
EMAC mode and can be changed to operate in Switch mode at runtime.
Note that changing from Dual EMAC to Switch mode needs loading of
different firmwares to various PRU cores and thus have to follow
specific sequence as shown in below sections:

Enabling Switch mode
""""""""""""""""""""

Example assuming ETH1 and ETH2 as ICSSG0 interfaces:

.. code-block:: console

 ip link add name br0 type bridge
 ip link set dev eth1 master br0
 ip link set dev eth2 master br0
 ip link set dev br0 up
 bridge vlan add dev br0 vid 1 pvid untagged self

Going back to Dual EMAC mode
""""""""""""""""""""""""""""

.. code-block:: console

 ip link set dev br0 down
 ip link set dev eth1 nomaster
 ip link set dev eth2 nomaster
 ip link del name br0 type bridge

Turn On/Off Spanning Tree Protocol (STP)
""""""""""""""""""""""""""""""""""""""""

.. code-block:: console

	ip link set dev br0 type bridge stp_state 1/0

VLAN configuration
""""""""""""""""""

.. code-block:: console

  bridge vlan add dev br0 vid 1 pvid untagged self <---- add cpu port to VLAN 1

This step is mandatory for bridge/default_pvid.

Adding extra VLANs
""""""""""""""""""

 1. untagged::

	bridge vlan add dev eth1 vid 100 pvid untagged master
	bridge vlan add dev eth1 vid 100 pvid untagged master
	bridge vlan add dev br0 vid 100 pvid untagged self <---- Add cpu port to VLAN100

 2. tagged::

	bridge vlan add dev eth1 vid 100 master
	bridge vlan add dev eth1 vid 100 master
	bridge vlan add dev br0 vid 100 pvid tagged self <---- Add cpu port to VLAN100

Forwarding Data Bases (FDBs)
""""""""""""""""""""""""""""

Forwarding entries for MAC addresses are automatically added on the
appropriate switch port upon detection as default operation as an
unmanaged bridge. For managed bridge operation manually add FDB entries
as required.

Manually adding FDBs::

    bridge fdb add aa:bb:cc:dd:ee:ff dev eth1 master vlan 100
    bridge fdb add aa:bb:cc:dd:ee:fe dev eth1 master <---- Add on all VLANs

Multicast Data Bases (MDBs)
"""""""""""""""""""""""""""

Multicast entries are automatically added on the appropriate switch port
upon detection as default operation as an unmanaged bridge. For managed
bridge operation manually add MDB entries as required.

Manually adding MDBs::

  bridge mdb add dev br0 port eth1 grp 239.1.1.1 permanent vid 100
  bridge mdb add dev br0 port eth1 grp 239.1.1.1 permanent <---- Add on all VLANs

Multicast flooding
""""""""""""""""""

CPU port mcast_flooding is always on

Turning flooding on/off on switch ports::

  bridge link set dev eth1 mcast_flood on/off

Limitations of switch mode offloading support
"""""""""""""""""""""""""""""""""""""""""""""

* VLAN offloading is limited to 0-256 VIDs.
* MDB/FDB static entries are limited to 511 entries and different FDBs can
  hash to same bucket and thus may not be completely offloaded

Cut Through Forwarding
""""""""""""""""""""""

.. Caution::

    The Cut Through configuration interface could be changed significantly in the future depending on Linux Kernel mainline development.

ICSSG Switch firmware now supports cut through forwarding. Cut Through feature allows forwarding packet from one external port to another without being stored in Port FIFOs thus reducing overall latency for packet forwarding.

**Limitations**

#. Feature is not available in dual EMAC mode.
#. Cut Through forwarding is only supported between external ports and no support for Cut Through to host port currently.
#. Cut Through is not supported with 10/100 half-duplex.
#. Cut Through is not supported with any form of flow control.
#. If Intersperced Express Traffic (IET) is enabled, then Cut Through can only be enabled on an express priority queue and not on preemptible queues.

The devlink command to enable cut-through takes a u16 value. All 16 bits of it represent queues. BIT 0 to BIT 7 are slice0 queues where as BIT 8 to BIT 15 are slice1 queues. To enable cut-through forwarding in both directions, cut-through will need to be enabled on both slice0 and slice1.

In general, to enable cut through for slice0 qM, qN queues and slice1 qX, qY queues, pass the value :math:`2^M + 2^N + 2^{8+X} + 2^{8+Y}` to the devlink command.

Assuming eth1 and eth2 are the active ports of ICSSG1 on AM64xx-EVM, to enable cut through run below commands,

.. code-block:: console

   ip link set eth1 down
   ip link set eth2 down

   # To enable cut thru for slice0 q0
   devlink dev param set platform/icssg1-eth name cut_thru value 1 cmode runtime

   # To enable cut thru for slice0 q1
   devlink dev param set platform/icssg1-eth name cut_thru value 2 cmode runtime

   # To enable cut thru for slice0 q0, q1
   devlink dev param set platform/icssg1-eth name cut_thru value 3 cmode runtime

   # To enable cut thru for slice0 q0, q1 and slice1 q0, q1
   devlink dev param set platform/icssg1-eth name cut_thru value 771 cmode runtime

   ip link set eth1 up
   ip link set eth2 up

To show the current cut through status, run the below command,

.. code-block:: console

   devlink dev param show platform/icssg1-eth name cut_thru

   platform/icssg1-eth:
    name cut_thru type driver-specific
      values:
        cmode runtime value 771

Here the value is shown as 771 (Binary 0000 0011 0000 0011). This means that cut through is enabled for q0, q1 of slice0 and q0, q1 of slice1. As bit 0,1,8 and 9 are set in the binary representation of the value 711.

To disable cut through on all queues

.. code-block:: console

   devlink dev param set platform/icssg1-eth name cut_thru value 0 cmode runtime

PTP
"""
PTP can be run during switch mode. To run PTP in switch mode, 3 AM64x EVMs need to be connected with middle EVM acting as the switch. Use the following ptp config file on all slave EVMs. For Master EVM, priority1 filed needs to be changed.

.. code-block:: text
   :caption: gPTP.cfg

   # 802.1AS example configuration containing those attributes which
   # differ from the defaults.  See the file, default.cfg, for the
   # complete list of available options.
   #
   [global]
   gmCapable 1
   priority1 248
   priority2 248
   logAnnounceInterval 0
   logSyncInterval -3
   syncReceiptTimeout 3
   neighborPropDelayThresh 800
   min_neighbor_prop_delay -20000000
   assume_two_step 1
   path_trace_enabled 1
   follow_up_info 1
   transportSpecific 0x1
   ptp_dst_mac 01:80:C2:00:00:0E
   network_transport L2
   delay_mechanism P2P
   ingressLatency 88
   egressLatency 288

**Steps:**

1. On EVM1 run below command assuming eth1 is the ICSSG interface connected and ptp2 is the device associated with it.

   .. code-block:: console

      ptp4l -P -2 -H -i eth1 -f gPTP.cfg --step_threshold=1 -m -q -p /dev/ptp2

2. On EVM3 run below command assuming eth2 is the ICSSG interface connected and ptp2 is the device associated with it.

   .. code-block:: console

      ptp4l -P -2 -H -i eth2 -f gPTP.cfg --step_threshold=1 -m -q -p /dev/ptp2

3. On EVM2 acting as the switch run below command assuming eth1 and eth2 are the ICSSG interfaces connected and ptp2 is the device associated with them.

   .. code-block:: console

      # Edit priority1 of EVM2 to make sure it runs as master.
      sed -i 's/priority1 248/priority1 100/g' gPTP.cfg

      # Add mdb entry for switch interface with multicast mac address used for forwarding PTP packets.
      # This address is same as ptp_dst_mac field in gPTP.cfg file.
      bridge mdb add dev br0 port br0 grp $ptp_dst_mac permanent vid 1

      # Start PTP on Master EVM
      ptp4l -P -2 -H -i eth1 -i eth2 -f gPTP.cfg --step_threshold=1 -m -q -p /dev/ptp2

**Observed Outputs:**

1. On EVM1

   .. code-block:: console

      root@am64xx-evm:~# cat gPTP.cfg | grep priority
      priority1               248
      priority2               248
      root@am64xx-evm:~# ptp4l -P -2 -H -i eth1 -f gPTP.cfg --step_threshold=1 -m -q -p /dev/ptp2
      ptp4l[3673.262]: selected /dev/ptp2 as PTP clock
      ptp4l[3673.296]: port 1: INITIALIZING to LISTENING on INIT_COMPLETE
      ptp4l[3673.297]: port 0: INITIALIZING to LISTENING on INIT_COMPLETE
      ptp4l[3676.325]: port 1: LISTENING to MASTER on ANNOUNCE_RECEIPT_TIMEOUT_EXPIRES
      ptp4l[3676.325]: selected local clock 70ff76.fffe.1e2db3 as best master
      ptp4l[3676.325]: port 1: assuming the grand master role
      ptp4l[3677.050]: port 1: new foreign master 70ff76.fffe.1f3f8e-1
      ptp4l[3679.050]: selected best master clock 70ff76.fffe.1f3f8e
      ptp4l[3679.050]: port 1: MASTER to UNCALIBRATED on RS_SLAVE
      ptp4l[3679.433]: port 1: UNCALIBRATED to SLAVE on MASTER_CLOCK_SELECTED
      ptp4l[3680.183]: rms 11123 max 14721 freq  +9512 +/- 7654 delay    83 +/-   0
      ptp4l[3681.184]: rms 2050 max 3143 freq  +2824 +/- 2781 delay    83 +/-   0
      ptp4l[3682.184]: rms 3425 max 3591 freq  -3401 +/- 910 delay    83 +/-   0
      ptp4l[3683.185]: rms 2175 max 2887 freq  -4622 +/-  87 delay    83 +/-   0
      ptp4l[3684.185]: rms  705 max 1163 freq  -3960 +/- 252 delay    83 +/-   0
      ptp4l[3685.185]: rms  124 max  196 freq  -3218 +/- 159 delay    84 +/-   0
      ptp4l[3686.186]: rms  203 max  216 freq  -2865 +/-  49 delay    84 +/-   0
      ptp4l[3687.186]: rms  121 max  156 freq  -2810 +/-   8 delay    84 +/-   0
      ptp4l[3688.186]: rms   39 max   64 freq  -2846 +/-  13 delay    84 +/-   0
      ptp4l[3689.187]: rms    6 max   12 freq  -2886 +/-   8 delay    84 +/-   0
      ptp4l[3690.187]: rms   14 max   20 freq  -2910 +/-   7 delay    84 +/-   0
      ptp4l[3691.188]: rms    7 max   12 freq  -2911 +/-   5 delay    84 +/-   0
      ptp4l[3692.188]: rms    5 max    9 freq  -2909 +/-   6 delay    85 +/-   0
      ptp4l[3693.189]: rms    4 max    8 freq  -2908 +/-   6 delay    84 +/-   0
      ptp4l[3694.189]: rms    5 max    7 freq  -2907 +/-   7 delay    85 +/-   0
      ptp4l[3695.189]: rms    3 max    8 freq  -2911 +/-   4 delay    84 +/-   0
      ptp4l[3696.190]: rms    4 max    8 freq  -2913 +/-   5 delay    84 +/-   0
      ptp4l[3697.190]: rms    3 max    4 freq  -2908 +/-   4 delay    84 +/-   0
      ptp4l[3698.191]: rms    4 max    9 freq  -2908 +/-   6 delay    83 +/-   0
      ptp4l[3699.191]: rms    5 max    9 freq  -2905 +/-   6 delay    83 +/-   0
      ptp4l[3700.191]: rms    5 max    9 freq  -2913 +/-   5 delay    85 +/-   0
      ptp4l[3701.192]: rms    4 max    7 freq  -2911 +/-   5 delay    83 +/-   0
      ptp4l[3702.192]: rms    4 max    5 freq  -2908 +/-   5 delay    83 +/-   0
      ptp4l[3703.192]: rms    5 max    8 freq  -2905 +/-   6 delay    84 +/-   0
      ptp4l[3704.193]: rms    6 max    8 freq  -2897 +/-   3 delay    84 +/-   0
      ptp4l[3705.193]: rms    5 max    8 freq  -2898 +/-   7 delay    84 +/-   0
      ptp4l[3706.193]: rms    5 max   12 freq  -2904 +/-   6 delay    84 +/-   0
      ptp4l[3707.194]: rms    4 max    9 freq  -2907 +/-   5 delay    85 +/-   0
      ptp4l[3708.194]: rms    3 max    6 freq  -2907 +/-   4 delay    86 +/-   0
      ptp4l[3709.195]: rms    5 max    7 freq  -2905 +/-   7 delay    85 +/-   0

2. On EVM2 actings as switch

   .. code-block:: console

      root@am64xx-evm:~# cat gPTP.cfg | grep priority
      priority1               100
      priority2               248
      root@am64xx-evm:~# ptp4l -P -2 -H -i eth1 -i eth2 -f gPTP.cfg --step_threshold=1 -m -q -p /dev/ptp2
      ptp4l[3635.479]: selected /dev/ptp2 as PTP clock
      ptp4l[3635.516]: port 1: INITIALIZING to LISTENING on INIT_COMPLETE
      ptp4l[3635.548]: port 2: INITIALIZING to LISTENING on INIT_COMPLETE
      ptp4l[3635.549]: port 0: INITIALIZING to LISTENING on INIT_COMPLETE
      ptp4l[3638.522]: port 1: LISTENING to MASTER on ANNOUNCE_RECEIPT_TIMEOUT_EXPIRES
      ptp4l[3638.522]: selected local clock 70ff76.fffe.1f3f8e as best master
      ptp4l[3638.522]: port 1: assuming the grand master role
      ptp4l[3639.278]: port 2: LISTENING to MASTER on ANNOUNCE_RECEIPT_TIMEOUT_EXPIRES
      ptp4l[3639.278]: selected local clock 70ff76.fffe.1f3f8e as best master
      ptp4l[3639.278]: port 1: assuming the grand master role
      ptp4l[3639.278]: port 2: assuming the grand master role
      ptp4l[3660.790]: port 2: new foreign master 70ff76.fffe.1f3e6a-1
      ptp4l[3662.790]: selected best master clock 70ff76.fffe.1f3e6a
      ptp4l[3662.790]: port 1: assuming the grand master role
      ptp4l[3662.791]: port 2: assuming the grand master role
      ptp4l[3663.800]: port 1: new foreign master 70ff76.fffe.1e2db3-1
      ptp4l[3665.800]: selected best master clock 70ff76.fffe.1e2db3
      ptp4l[3665.800]: port 1: assuming the grand master role
      ptp4l[3665.800]: port 2: assuming the grand master role

3. On EVM3

   .. code-block:: console

      root@am64xx-evm:~# cat gPTP.cfg | grep priority
      priority1               248
      priority2               248
      root@am64xx-evm:~# ptp4l -P -2 -H -i eth2 -f gPTP.cfg --step_threshold=1 -m -q -p /dev/ptp2
      ptp4l[3651.298]: selected /dev/ptp2 as PTP clock
      ptp4l[3651.336]: port 1: INITIALIZING to LISTENING on INIT_COMPLETE
      ptp4l[3651.337]: port 0: INITIALIZING to LISTENING on INIT_COMPLETE
      ptp4l[3654.775]: port 1: LISTENING to MASTER on ANNOUNCE_RECEIPT_TIMEOUT_EXPIRES
      ptp4l[3654.775]: selected local clock 70ff76.fffe.1f3e6a as best master
      ptp4l[3654.775]: port 1: assuming the grand master role
      ptp4l[3655.266]: port 1: new foreign master 70ff76.fffe.1f3f8e-2
      ptp4l[3657.266]: selected best master clock 70ff76.fffe.1f3f8e
      ptp4l[3657.266]: port 1: MASTER to UNCALIBRATED on RS_SLAVE
      ptp4l[3657.520]: port 1: UNCALIBRATED to SLAVE on MASTER_CLOCK_SELECTED
      ptp4l[3658.270]: rms 6047 max 8004 freq  +5665 +/- 4160 delay    88 +/-   0
      ptp4l[3659.271]: rms 1112 max 1709 freq  +2037 +/- 1510 delay    89 +/-   0
      ptp4l[3660.271]: rms 1865 max 1953 freq  -1356 +/- 501 delay    89 +/-   0
      ptp4l[3661.271]: rms 1190 max 1582 freq  -2032 +/-  45 delay    90 +/-   0
      ptp4l[3662.272]: rms  386 max  637 freq  -1668 +/- 142 delay    89 +/-   0
      ptp4l[3663.272]: rms   71 max  111 freq  -1256 +/-  89 delay    89 +/-   0
      ptp4l[3664.272]: rms  109 max  119 freq  -1070 +/-  27 delay    89 +/-   0
      ptp4l[3665.273]: rms   67 max   83 freq  -1037 +/-   5 delay    89 +/-   0
      ptp4l[3666.273]: rms   22 max   35 freq  -1056 +/-   8 delay    89 +/-   0
      ptp4l[3667.273]: rms    6 max   11 freq  -1073 +/-   8 delay    89 +/-   0
      ptp4l[3668.274]: rms   10 max   13 freq  -1094 +/-   4 delay    89 +/-   0
      ptp4l[3669.274]: rms    3 max    5 freq  -1090 +/-   3 delay    89 +/-   0
      ptp4l[3670.274]: rms    3 max    5 freq  -1087 +/-   4 delay    89 +/-   0
      ptp4l[3671.274]: rms    5 max    7 freq  -1086 +/-   6 delay    89 +/-   0
      ptp4l[3672.275]: rms    4 max    7 freq  -1089 +/-   5 delay    89 +/-   0
      ptp4l[3673.275]: rms    5 max    7 freq  -1087 +/-   7 delay    89 +/-   0
      ptp4l[3674.275]: rms    3 max    4 freq  -1088 +/-   4 delay    88 +/-   0
      ptp4l[3675.276]: rms    4 max    8 freq  -1091 +/-   5 delay    88 +/-   0
      ptp4l[3676.276]: rms    5 max    6 freq  -1084 +/-   5 delay    90 +/-   0
      ptp4l[3677.276]: rms    3 max    6 freq  -1085 +/-   5 delay    90 +/-   0
      ptp4l[3678.276]: rms    5 max   10 freq  -1084 +/-   7 delay    90 +/-   0
      ptp4l[3679.277]: rms    4 max    9 freq  -1088 +/-   5 delay    89 +/-   0
      ptp4l[3680.277]: rms    5 max    8 freq  -1092 +/-   5 delay    88 +/-   0
      ptp4l[3681.277]: rms    3 max    5 freq  -1089 +/-   4 delay    89 +/-   0
      ptp4l[3682.277]: rms    5 max    8 freq  -1084 +/-   6 delay    88 +/-   0
      ptp4l[3683.278]: rms    4 max    7 freq  -1088 +/-   6 delay    89 +/-   0
      ptp4l[3684.278]: rms    5 max    7 freq  -1086 +/-   7 delay    89 +/-   0
      ptp4l[3685.278]: rms    3 max    8 freq  -1087 +/-   5 delay    88 +/-   0
      ptp4l[3686.279]: rms    4 max    8 freq  -1088 +/-   5 delay    88 +/-   0
      ptp4l[3687.279]: rms    4 max    8 freq  -1088 +/-   5 delay    88 +/-   0


**Results:** It can be observed that the clocks on Slave devices are getting synchronised with the clock on Master device.

SRAM Requirement
""""""""""""""""

* The ICSSG Ethernet driver can be used in switch mode. Two icssg ports are used per switch.
* SRAM Required for each switch (per two ports) is 256 KB.
* For each ICSSG switch, the SRAM required needs to be contiguous.
* PRUETH only uses the required amount of SRAM from the SRAM/MSMC pool. If PRUETH doesn't get the required amount of SRAM, the prueth_probe() API will return with -ENOMEM error.
