.. _kernel_driver_cpsw2g_iet:

IET
===

.. contents:: :local:
    :depth: 2

Introduction
------------

CPSW h/w support Intersperse Express Traffic (IET, defined in P802.3br/D2.0 spec which later is included in IEEE 802.3 2018) Frame preemption (FPE) feature and also to allow MAC layer to Verify if the peer supports IET MAC merge layer or not. MAC merge layer is responsible for preempting the transmission of frame from a preemptible queue if there is frame waiting for transmission at a higher priority Express queue. The h/w sends an initial segment of the frame satisfying min fragment size requirement and then schedule frame from the Express queue for transmission. Finally when no more frames available at the Express queue, it will resume transmission of remaining segments of the frame of the preemptible queue which was preempted. At the peer end, the segments are re-assembled and delivered to the MAC interface.

IET FPE feature is configured for a port through :code:`ethtool --set-mm`. Driver configures IET FPE for a port when network device is opened (ndo_open()) if user has turned ON the pmac-enabled flag. Note that since IET is a common feature applicable to all slave ports, this has to be done before the network ports of the CPSW2g are brought up. The user may also turn ON the IET mac-verify flag if the peer device connected to CPSW2g port is also capable of verifying MAC merge/FPE capability by turning ON verify-enabled flag using :code:`ethtool --set-mm` command. For this, driver schedules a worker thread to do the MAC/Verify process as soon as the Link is up and IET mac-verify priv flag is set.  It resets the LINKFAIL bit and check if the Verify succeeds or not.  On failure, the MAC Verify state machine is reset by toggling LINKFAIL bit and process repeats for 20 times before bailing out. If IET mac-verify priv flag is not set, driver assumes that peer is capable of supporting FPE, but not able to do MAC Verify. So it configures the device into force mode. User needs to verify that peer device is capable of supporting IET FPE to use force mode.

Driver assumes highest priority h/w Queue as the express Queue and configures lower queues (Q0-QN-2, where N is the maximum number of queues configured) as preemptible queues by programming the PN_REG_IET_CTRL register if the MAC Verify succeeds or if the force mode is enabled. p0-rx-ptype-rrobin flag should be turned off before using IET feature. i.e CPSW2g h/w should be programmed into strict priority mode for IET to work.

To enable IET FPE with MAC Verify, do

.. code:: console

   ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
   ethtool --set-mm eth0 pmac-enabled on tx-enabled on verify-enabled on verify-time 10 tx-min-frag-size 124

To enable IET FPE with no MAC Verify (Force mode)

.. code:: console

   ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
   ethtool --set-mm eth0 pmac-enabled on tx-enabled on verify-enabled off tx-min-frag-size 124

To disable IET FPE and restore rrobin mode

.. code:: console

   ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin on

.. rubric:: Example session to enable IET FPE with MAC Verify.
   :name: iet-mac-verify

Assume 2 AM65x IDKs are connected back to back over MCU Ethernet port (typically eth0 interface. Example assumes 2 h/w queues configured. Q1 will be express queue and Q0 the preemption queue in this configuration.

.. code:: console

   # bring down all interfaces associated with the same CPSW instance to update tx channels
   root@evm:~# ip link set dev eth0 down
   [   84.543137] am65-cpsw-nuss 46000000.ethernet eth0: Link is Down
   root@evm:~# ethtool -L eth0 tx 2
   root@evm:~# ethtool -l eth0
   Channel parameters for eth0:
   Pre-set maximums:
   RX:             1
   TX:             8
   Other:          0
   Combined:       0
   Current hardware settings:
   RX:             1
   TX:             2
   Other:          0
   Combined:       0
   @evm:~# ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
   root@evm:~# ethtool --set-priv-flags eth0 iet-frame-preemption on
   root@evm:~# ethtool --show-priv-flags eth0
   Private flags for eth0:
   p0-rx-ptype-rrobin: off
   cut-thru          : off
   root@evm:~# ethtool --set-mm eth0 pmac-enabled on tx-enabled on verify-enabled off verify-time 10 tx-min-frag-size 124
   root@evm:~# ethtool -show-mm eth0
   root@am62axx-evm:~# ethtool --show-mm eth0
      MAC Merge layer state for eth0:
      pMAC enabled: on
      TX enabled: on
      TX active: on
      TX minimum fragment size: 124
      RX minimum fragment size: 124
      Verify enabled: on
      Verify time: 10
      Max verify time: 128
      Verification status: SUCCEEDED
   root@evm:~# ip link set dev eth0 up
   [  409.666959] am65-cpsw-nuss 46000000.ethernet eth0: PHY [46000f00.mdio:00] driver [TI DP83867] (irq=POLL)
   [  409.676453] am65-cpsw-nuss 46000000.ethernet eth0: configuring for phy/rgmii-rxid link mode

.. rubric:: Example session to enable IET FPE with no MAC Verify (Force mode)
   :name: iet-no-mac-verify

.. code:: console

   root@evm:~# ip link set dev eth0 down
   [  394.590576] am65-cpsw-nuss 46000000.ethernet eth0: Link is Down
   root@evm:~# ethtool --set-mm eth0 pmac-enabled on tx-enabled on verify-enabled off tx-min-frag-size 124
   root@evm:~# ethtool --show-mm eth0
      MAC Merge layer state for eth0:
      pMAC enabled: on
      TX enabled: on
      TX active: on
      TX minimum fragment size: 124
      RX minimum fragment size: 124
      Verify enabled: off
      Verify time: 0
      Max verify time: 128
      Verification status: DISABLED
   root@evm:~#
   root@evm:~# ip link set dev eth0 up
   root@evm:~# ip addr add 192.168.100.20/24 dev eth0
   [  500.502660] TI DP83867 46000f00.mdio:00: attached PHY driver [TI DP83867] (mii_bus:phy_addr=46000f00.mdio:00, irq=POLL)
   root@evm:~# [  500.516232] am65-cpsw-nuss 46000000.ethernet eth0: Link is Down
   root@evm:~# [  552.738077] am65-cpsw-nuss 46000000.ethernet eth0: IET Enable Force mode
   [  552.744839] am65-cpsw-nuss 46000000.ethernet eth0: Link is Up - 1Gbps/Full - flow control off
   [  552.753434] IPv6: ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready

.. rubric:: IET FPE example
   :name: iep-fpe-testing

Highest priority Queue is Express queue. I.e if there are 8 queues configured through ethtool -L command, Q7 will be express and Q0-Q6 will be preemptible. Similarly if 4 queues are configured then Q3 will be express queue and Q0-Q2 will be preemptible queues. See below an example on how to verify preemption is happening in the hardware.  Setup requires 2 IDKs (Example AM65x) connected over MCU Ethernet/CPSW2g port. Assume that IET is enabled on both IDKs as in previous sections and either Force mode or MAC Verify mode is enabled. As soon as the Link comes up, the IET FPE gets enabled. The test requires MQPRIO qdisc to be configured at the Talker DUT's eth0 port and enable classifier to map UDP frames with specific port to be to a given traffic class. Traffic class is used as the index to direct traffic to the specific h/w queue. CPSW2g stats module provide a statistics counter for following that can be used to verify the IET FPE is functional:-

* MACMergeFrameAssOkCount - Increments at the receiver if re-assembly of MAC fragments are successful.
* MACMergeFragCountRx - Incremenets at the receiver if MAC fragments are received due to preemption
* MACMergeFragCountTx - Increments at the sender side if fragments are created due to frame preemption.

So to test, need to have traffic at the preemption queue as well as at the express queue and use the above statistics counters to verify if fragmentation happens at the sender side and re-assembly at the receiver side. Below logs provide some example usage.

.. code:: console

   # At the Talker side
   # Set up mqprio qdisc at eth0 - 2 Queues configured. Q0 - preemption queue and Q1 express queue
   root@evm:~# tc qdisc replace dev eth0 handle 100: parent root mqprio num_tc 2  map 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 queues 1@0
   1@1 hw 1 mode dcb fp P E
   root@evm:~# tc -g class show dev eth0
   +---(100:ffe1) mqprio
   |    +---(100:2) mqprio
   |
   +---(100:ffe0) mqprio
      +---(100:1) mqprio
   # Enable classifier at net core
   root@evm:~# tc qdisc add dev eth0 clsact
   # Add tc filter rule to mark packet priority based on destination UDP port number - Port 5002 mapped to prio 2
   # From above mqprio settings, TC at index 2 is 0. So this TC packets go to Q0
   root@evm:~# tc filter add dev eth0 egress protocol ip prio 1 u32 match ip dport 5002 0xffff action skbedit priority 2
   [  285.576105] u32 classifier
   [  285.578910]     input device check on
   [  285.582640]     Actions configured
   # Add tc filter rule to map packets with UDP port number - Port 5003 to prio 3
   # From above mqprio settings, TC at index 3 is 1. So this TC packets go to Q1
   root@evm:~# tc filter add dev eth0 egress protocol ip prio 1 u32 match ip dport 5003 0xffff action skbedit priority 3
   root@evm:~#
   root@evm:~# ip addr add 192.168.100.20/24 dev eth0

   # At the Listener DUT, setup ip address and run iperf3 server session listening to port 5002 and 5003.
   # ip addr add 192.168.100.30/24 dev eth0
   root@evm:~# iperf3 -s -i30 -p5002&
   [1] 1224
   root@evm:~# iperf3 -s -i30 -p5003&
   -----------------------------------------------------------
   Server listening on 5002
   -----------------------------------------------------------
   [2] 1225
   -----------------------------------------------------------
   Server listening on 5003
   -----------------------------------------------------------
   root@evm:~#
   # At Listener DUT start iperf3 client session to port 5002 and 5003
   root@evm:~# iperf3 -c 192.168.100.30 -u -b200M -l1472 -u -t30 -i30 -p5002&
   [1] 1050
   root@evm:~# iperf3 -c 192.168.100.30 -u -b50M -l1472 -u -t30 -i30 -p5003&
   [2] 1051
   root@evm:~#
   root@evm:~# warning: UDP block size 1472 exceeds TCP MSS 1448, may result in fragmentation / drops
   warning: UDP block size 1472 exceeds TCP MSS 1448, may result in fragmentation / drops
   Connecting to host 192.168.100.30, port 5003
   Connecting to host 192.168.100.30, port 5002
   [  5] local 192.168.100.20 port 60646 connected to 192.168.100.30 port 5003
   [  5] local 192.168.100.20 port 39515 connected to 192.168.100.30 port 5002

   # Now at the Talker DUT, dump statistics counter for Q0 and Q1 as well as IET statistics
   root@evm:~# ethtool -S eth0 | grep 'tx_pri1'
      p0_tx_pri1: 0
      p0_tx_pri1_bcnt: 0
      p0_tx_pri1_drop: 0
      p0_tx_pri1_drop_bcnt: 0
      tx_pri1: 127389
      tx_pri1_bcnt: 193355263
      tx_pri1_drop: 0
      tx_pri1_drop_bcnt: 0
   root@evm:~# ethtool -S eth0 | grep 'tx_pri0'
      p0_tx_pri0: 89
      p0_tx_pri0_bcnt: 19477
      p0_tx_pri0_drop: 0
      p0_tx_pri0_drop_bcnt: 0
      tx_pri0: 509615
      tx_pri0_bcnt: 773438803
      tx_pri0_drop: 0
      tx_pri0_drop_bcnt: 0
   root@evm:~# ethtool -I --show-mm eth0
      MAC Merge layer state for eth0:
      pMAC enabled: on
      TX enabled: on
      TX active: on
      TX minimum fragment size: 124
      RX minimum fragment size: 124
      Verify enabled: on
      Verify time: 10
      Max verify time: 128
      Verification status: SUCCEEDED
      Statistics:
         MACMergeFrameAssErrorCount: 0
         MACMergeFrameSmdErrorCount: 0
         MACMergeFrameAssOkCount: 0
         MACMergeFragCountRx: 0
         MACMergeFragCountTx: 17952
         MACMergeHoldCount: 0

   # As seen, MACMergeFragCountTx statistics counter increments at the Talker showing fragmentation at the Talker
   # Also dump the statistics at the listener DUT
   root@evm:~# ethtool -I --show-mm eth0
      MAC Merge layer state for eth0:
      pMAC enabled: on
      TX enabled: on
      TX active: on
      TX minimum fragment size: 124
      RX minimum fragment size: 124
      Verify enabled: on
      Verify time: 10
      Max verify time: 128
      Verification status: SUCCEEDED
      Statistics:
         MACMergeFrameAssErrorCount: 0
         MACMergeFrameSmdErrorCount: 48
         MACMergeFrameAssOkCount: 14507
         MACMergeFragCountRx: 17952
         MACMergeFragCountTx: 0
         MACMergeHoldCount: 0
 # As seen, MACMergeFragCountRx and MACMergeFrameAssOkCount statistics counter increments at the Listener showing re-assembly at the Listener

.. rubric:: Using IET together with EST
   :name: iet-with-est

Express and preemption queues/Gates may be used as part of the EST schedule. If only Preemption queues are in a schedule entry, preceding an entry with Express queue, the guard band requirement reduces to 2048 nsec (0x100 = 256 * 8) so that packets don't spill over to the next sched-entry. Otherwise, the guard band required is as explained in the EST section.

Warning: IET with Fixed-Link Interface
--------------------------------------

If one of the interfaces which takes part in IET is in fixed-link mode,
then do NOT enable MAC verify for IET on either of the devices
connected to each other directly by the LAN cable. This is because, in
the case of fixed-link, the link state cannot be detected by interfaces
on either side of the link. The process of IET MAC Verification depends
on the link state being toggled, with the verification starting
immediately after the link comes up and lasting for 1 second. Thus,
unless this process starts roughly simultaneously on both interfaces
connected over the link (Which would happen in the non fixed-link case),
IET MAC Verification would fail with a Timeout message, thereby causing
frame fragmentation to fail.

Thus, if either of the interfaces that are directly connected by a LAN
cable, is in fixed-link mode, then do NOT enable MAC verify on BOTH the
interfaces. Simply enable IET Frame Preemption on both devices and IET
will work. The rest of the steps are the same as documented in the
upcoming sectionss.

IET MAC Verification in ethtool --set-mm corresponds to:

.. code:: console

   verify-enabled

IET Frame Preemption in ethtool --set-mm corresponds to:

.. code:: console

   pmac-enabled

IET in MAC mode
---------------

AM625-SK fragments frames and J7VCL assembles them
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connect eth0 of AM625-SK to eth0 of J7VCL.

**Steps:**

1. Create and run the following script on J7VCL:

.. code:: sh

   #!/bin/sh

   ifconfig eth0 down
   ethtool -L eth0 tx 4
   ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
   ethtool --set-mm eth0 pmac-enabled on tx-enabled on verify-enabled on verify-time 10 tx-min-frag-size 124
   ifconfig eth0 up
   sleep 5

   iperf3 -s -i30 -p5002&
   iperf3 -s -i30 -p5003&

2. Create and run the following script on AM625-SK:

.. code:: sh

   #!/bin/sh

   ifconfig eth0 down
   ifconfig eth1 down
   ethtool -L eth0 tx 4
   ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
   ethtool --set-mm eth0 pmac-enabled on tx-enabled on verify-enabled on verify-time 10 tx-min-frag-size 124
   ifconfig eth0 up
   sleep 5

   tc qdisc replace dev eth0 handle 100: parent root mqprio \
   num_tc 4 \
   map 0 1 2 3 \
   queues 1@0 1@1 1@2 1@3 \
   hw 1 \
   mode dcb \
   fp P P P E

   tc -g class show dev eth0
   tc qdisc add dev eth0 clsact
   tc filter add dev eth0 egress protocol ip prio 1 u32 match ip dport 5002 0xffff action skbedit priority 2
   tc filter add dev eth0 egress protocol ip prio 1 u32 match ip dport 5003 0xffff action skbedit priority 3
   ip addr add 192.168.100.20/24 dev eth0
   sleep 2

3. On J7VCL, run the following command:

.. code:: console

   ifconfig eth0 192.168.100.30

4. Now, run the following commands on AM625-SK:

.. code:: console

   iperf3 -c 192.168.100.30 -u -b200M -l1472 -u -t30 -i30 -p5002&
   iperf3 -c 192.168.100.30 -u -b50M -l1472 -u -t30 -i30 -p5003&

**Results:**

On AM625-SK (Sender):

.. code:: console

   root@am62xx-evm:~# ethtool -S eth0 | grep tx_pri0
      p0_tx_pri0: 66
      p0_tx_pri0_bcnt: 12944
      p0_tx_pri0_drop: 0
      p0_tx_pri0_drop_bcnt: 0
      tx_pri0: 66
      tx_pri0_bcnt: 11540
      tx_pri0_drop: 0
      tx_pri0_drop_bcnt: 0
   root@am62xx-evm:~# ethtool -S eth0 | grep tx_pri2
      p0_tx_pri2: 0
      p0_tx_pri2_bcnt: 0
      p0_tx_pri2_drop: 0
      p0_tx_pri2_drop_bcnt: 0
      tx_pri2: 509514
      tx_pri2_bcnt: 773419566
      tx_pri2_drop: 0
      tx_pri2_drop_bcnt: 0
   root@am62xx-evm:~# ethtool -S eth0 | grep tx_pri3
      p0_tx_pri3: 0
      p0_tx_pri3_bcnt: 0
      p0_tx_pri3_drop: 0
      p0_tx_pri3_drop_bcnt: 0
      tx_pri3: 127389
      tx_pri3_bcnt: 193355280
      tx_pri3_drop: 0
      tx_pri3_drop_bcnt: 0
   root@am62xx-evm:~# ethtool -I --show-mm eth0
      MAC Merge layer state for eth0:
      pMAC enabled: on
      TX enabled: on
      TX active: on
      TX minimum fragment size: 124
      RX minimum fragment size: 124
      Verify enabled: on
      Verify time: 10
      Max verify time: 128
      Verification status: SUCCEEDED
      Statistics:
         MACMergeFrameAssErrorCount: 0
         MACMergeFrameSmdErrorCount: 0
         MACMergeFrameAssOkCount: 0
         MACMergeFragCountRx: 0
         MACMergeFragCountTx: 112
         MACMergeHoldCount: 0

On J7ES (Receiver):

.. code:: console

   root@j7200-evm:~# ethtool -I --show-mm eth0
      MAC Merge layer state for eth0:
      pMAC enabled: on
      TX enabled: on
      TX active: off
      TX minimum fragment size: 124
      RX minimum fragment size: 124
      Verify enabled: on
      Verify time: 10
      Max verify time: 128
      Verification status: SUCCEEDED
      Statistics:
         MACMergeFrameAssErrorCount: 0
         MACMergeFrameSmdErrorCount: 0
         MACMergeFrameAssOkCount: 104
         MACMergeFragCountRx: 112
         MACMergeFragCountTx: 0
         MACMergeHoldCount: 0

**Explanation:**

.. code:: text

   On AM625-SK, the higher priority traffic preempts the lower priority
   traffic, thereby resulting in the fragmentation of frames of lower
   priority. This can be seen in the MACMergeFragCountTx statistic on
   AM625-SK.

   Similarly, on J7VCL, the received fragmented frames can be observed
   in the MACMergeFragCountRx statistic, while the assembled frames can
   be seen in the MACMergeFrameAssOkCount statistic.

J7VCL fragments frames and AM625-SK assembles them
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connect eth0 of J7VCL to eth0 of AM625-SK.

**Steps:**

1. Create and run the following script on AM625-SK:

.. code:: sh

   #!/bin/sh

   ifconfig eth0 down
   ifconfig eth1 down
   ethtool -L eth0 tx 4
   ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
   ethtool --set-mm eth0 pmac-enabled on tx-enabled on verify-enabled on verify-time 10 tx-min-frag-size 124
   ifconfig eth0 up
   sleep 5

   iperf3 -s -i30 -p5002&
   iperf3 -s -i30 -p5003&

2. Create and run the following script on J7VCL:

.. code:: sh

   #!/bin/sh

   ifconfig eth0 down
   ethtool -L eth0 tx 4
   ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
   ethtool --set-mm eth0 pmac-enabled on tx-enabled on verify-enabled on verify-time 10 tx-min-frag-size 124
   ifconfig eth0 up
   sleep 5

   tc qdisc replace dev eth0 handle 100: parent root mqprio \
      num_tc 4 \
      map 0 1 2 3 \
      queues 1@0 1@1 1@2 1@3 \
      hw 1 \
      mode dcb \
      fp P P P E

   tc -g class show dev eth0
   tc qdisc add dev eth0 clsact
   tc filter add dev eth0 egress protocol ip prio 1 u32 match ip dport 5002 0xffff action skbedit priority 2
   tc filter add dev eth0 egress protocol ip prio 1 u32 match ip dport 5003 0xffff action skbedit priority 3
   ip addr add 192.168.100.20/24 dev eth0
   sleep 2

3. Run the following command on AM625-SK:

.. code:: console

   ifconfig eth0 192.168.100.30

4. Next, run the following commands on J7VCL:

.. code:: console

   iperf3 -c 192.168.100.30 -u -b200M -l1472 -u -t30 -i30 -p5002&
   iperf3 -c 192.168.100.30 -u -b50M -l1472 -u -t30 -i30 -p5003&

**Results:**

On J7VCL (Sender):

.. code:: console

   root@j7200-evm:~# ethtool -S eth0 | grep tx_pri0
      p0_tx_pri0: 0
      p0_tx_pri0_bcnt: 0
      p0_tx_pri0_drop: 0
      p0_tx_pri0_drop_bcnt: 0
      tx_pri0: 63
      tx_pri0_bcnt: 11010
      tx_pri0_drop: 0
      tx_pri0_drop_bcnt: 0
   root@j7200-evm:~# ethtool -S eth0 | grep tx_pri1
      p0_tx_pri1: 0
      p0_tx_pri1_bcnt: 0
      p0_tx_pri1_drop: 0
      p0_tx_pri1_drop_bcnt: 0
      tx_pri1: 0
      tx_pri1_bcnt: 0
      tx_pri1_drop: 0
      tx_pri1_drop_bcnt: 0
   root@j7200-evm:~# ethtool -S eth0 | grep tx_pri2
      p0_tx_pri2: 0
      p0_tx_pri2_bcnt: 0
      p0_tx_pri2_drop: 0
      p0_tx_pri2_drop_bcnt: 0
      tx_pri2: 509514
      tx_pri2_bcnt: 773418133
      tx_pri2_drop: 0
      tx_pri2_drop_bcnt: 0
   root@j7200-evm:~# ethtool -I --show-mm eth0
   MAC Merge layer state for eth0:
   pMAC enabled: on
   TX enabled: on
   TX active: on
   TX minimum fragment size: 124
   RX minimum fragment size: 124
   Verify enabled: on
   Verify time: 10
   Max verify time: 128
   Verification status: SUCCEEDED
   Statistics:
      MACMergeFrameAssErrorCount: 0
      MACMergeFrameSmdErrorCount: 0
      MACMergeFrameAssOkCount: 0
      MACMergeFragCountRx: 0
      MACMergeFragCountTx: 1403
      MACMergeHoldCount: 0

On AM625-SK (Receiver):

.. code:: console

   root@am62xx-evm:~# ethtool -I --show-mm eth0
   MAC Merge layer state for eth0:
   pMAC enabled: on
   TX enabled: on
   TX active: on
   TX minimum fragment size: 124
   RX minimum fragment size: 124
   Verify enabled: on
   Verify time: 10
   Max verify time: 128
   Verification status: SUCCEEDED
   Statistics:
      MACMergeFrameAssErrorCount: 0
      MACMergeFrameSmdErrorCount: 0
      MACMergeFrameAssOkCount: 365
      MACMergeFragCountRx: 892
      MACMergeFragCountTx: 0
      MACMergeHoldCount: 0

**Explanation:**

.. code:: text

   On J7VCL, the higher priority traffic preempts the lower priority
   traffic, thereby resulting in the fragmentation of frames of lower
   priority. This can be seen in the MACMergeFragCountTx statistic on
   J7VCL.

   Similarly, on AM625-SK, the received fragmented frames can be observed
   in the MACMergeFragCountRx statistic, while the assembled frames can
   be seen in the MACMergeFrameAssOkCount statistic.

IET in Switch mode
------------------

3 Devices are connected: Sender, Switch and Receiver.

3 Cases:

1. Frame is preempted on Sender and Assembled on Switch Ingress Port.
2. Frame is preempted on Switch Egress Port and Assembled on Receiver.
3. Frame is preempted on Sender and Assembled on Switch Ingress Port, and also, frame is preempted on Switch Egress Port and Assembled on Receiver.

Devices Used:

1. AM625-SK (As Switch/Sender)
2. J7VCL (As Switch/Sender)
3. J7ES (As Receiver)

CASE-1: Frame is preempted on Sender and Assembled on Switch Ingress Port
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Preemption on J7VCL (Sender) and Assembly on AM625-SK (Switch) Ingress Port and sent to J7ES (Receiver)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Connect eth0 of J7VCL to eth0 of AM625-SK and eth0 of J7ES to eth2 of AM625-SK.

**Steps:**

1. On AM625-SK, create and run the following script:

.. code:: sh

   #!/bin/sh

   ifconfig eth0 down
   ifconfig eth1 down
   ethtool -L eth0 tx 4
   ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
   ethtool --set-mm eth0 pmac-enabled on tx-enabled on verify-enabled on verify-time 10 tx-min-frag-size 124
   ifconfig eth0 up
   ifconfig eth1 up
   sleep 5

   devlink dev param set platform/8000000.ethernet name switch_mode value true cmode runtime
   ip link add name br0 type bridge
   ip link set dev br0 type bridge ageing_time 1000
   ip link set dev eth0 up
   ip link set dev eth1 up
   ip link set dev eth0 master br0
   ip link set dev eth1 master br0
   ip link set dev br0 up
   ip link set dev br0 type bridge vlan_filtering 1
   bridge vlan add dev br0 vid 1 self
   bridge vlan add dev br0 vid 1 pvid untagged self

2. On J7VCL, create and run the following script:

.. code:: sh

   #!/bin/sh

   ifconfig eth0 down
   ethtool -L eth0 tx 4
   ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
   ethtool --set-mm eth0 pmac-enabled on tx-enabled on verify-enabled on verify-time 10 tx-min-frag-size 124
   ifconfig eth0 up
   sleep 5

   tc qdisc replace dev eth0 handle 100: parent root mqprio \
   num_tc 4 \
   map 0 1 2 3 \
   queues 1@0 1@1 1@2 1@3 \
   hw 1 \
   mode dcb \
   fp P P P E

   tc -g class show dev eth0
   tc qdisc add dev eth0 clsact
   tc filter add dev eth0 egress protocol ip prio 1 u32 match ip dport 5002 0xffff action skbedit priority 2
   tc filter add dev eth0 egress protocol ip prio 1 u32 match ip dport 5003 0xffff action skbedit priority 3
   ifconfig eth0 192.168.100.20 netmask 255.255.255.0
   sleep 2

3.  On J7ES (Receiver), run the following commands:

.. code:: console

   ifconfig eth0 192.168.3.102
   iperf3 -s -i30 -p5002& \
   iperf3 -s -i30 -p5003&

4. Then, on J7VCL (Sender), run the following commands:

.. code:: console

   iperf3 -c 192.168.3.102 -u -b200M -l1472 -u -t5 -i30 -p5002&
   iperf3 -c 192.168.3.102 -u -b50M -l1472 -u -t5 -i30 -p5003&

**Results:**

On J7VCL (Sender):

.. code:: console

   root@j7200-evm:~/iet# ethtool -S eth0 | grep tx_pri0
      p0_tx_pri0: 0
      p0_tx_pri0_bcnt: 0
      p0_tx_pri0_drop: 0
      p0_tx_pri0_drop_bcnt: 0
      tx_pri0: 95
      tx_pri0_bcnt: 16582
      tx_pri0_drop: 0
      tx_pri0_drop_bcnt: 0
   root@j7200-evm:~/iet# ethtool -S eth0 | grep tx_pri2
      p0_tx_pri2: 0
      p0_tx_pri2_bcnt: 0
      p0_tx_pri2_drop: 0
      p0_tx_pri2_drop_bcnt: 0
      tx_pri2: 1019024
      tx_pri2_bcnt: 1546835971
      tx_pri2_drop: 0
      tx_pri2_drop_bcnt: 0
   root@j7200-evm:~/iet# ethtool -S eth0 | grep tx_pri3
      p0_tx_pri3: 0
      p0_tx_pri3_bcnt: 0
      p0_tx_pri3_drop: 0
      p0_tx_pri3_drop_bcnt: 0
      tx_pri3: 254780
      tx_pri3_bcnt: 386710678
      tx_pri3_drop: 0
      tx_pri3_drop_bcnt: 0
   root@j7200-evm:~/iet# ethtool -I --show-mm eth0
      MAC Merge layer state for eth0:
      pMAC enabled: on
      TX enabled: on
      TX active: on
      TX minimum fragment size: 124
      RX minimum fragment size: 124
      Verify enabled: on
      Verify time: 10
      Max verify time: 128
      Verification status: SUCCEEDED
      Statistics:
         MACMergeFrameAssErrorCount: 0
         MACMergeFrameSmdErrorCount: 38
         MACMergeFrameAssOkCount: 0
         MACMergeFragCountRx: 0
         MACMergeFragCountTx: 1637
         MACMergeHoldCount: 0

On AM625-SK (Switch):

.. code:: console

   root@am62xx-evm:~/iet# ethtool -I --show-mm eth0
   MAC Merge layer state for eth0:
   pMAC enabled: on
   TX enabled: on
   TX active: on
   TX minimum fragment size: 124
   RX minimum fragment size: 124
   Verify enabled: on
   Verify time: 10
   Max verify time: 128
   Verification status: SUCCEEDED
   Statistics:
      MACMergeFrameAssErrorCount: 0
      MACMergeFrameSmdErrorCount: 0
      MACMergeFrameAssOkCount: 610
      MACMergeFragCountRx: 1637
      MACMergeFragCountTx: 0
      MACMergeHoldCount: 0

Preemption on AM625-SK (Sender) and Assembly on J7VCL (Switch) Ingress Port and sent to J7ES (Receiver)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Connect eth0 of AM625-SK to eth1 of J7VCL and eth0 of J7ES to eth2 of J7VCL.

**Steps:**

1. On J7VCL, create and run the following script:

.. code:: sh

   #!/bin/sh

   ifconfig eth0 down
   ifconfig eth1 down
   ifconfig eth2 down
   ifconfig eth3 down
   ifconfig eth4 down
   ethtool -L eth1 tx 4
   ethtool --set-priv-flags eth1 p0-rx-ptype-rrobin off
   ethtool --set-mm eth1 pmac-enabled on tx-enabled on verify-enabled on verify-time 10 tx-min-frag-size 124
   ifconfig eth1 up
   ifconfig eth2 up
   sleep 10

   devlink dev param set platform/c000000.ethernet name switch_mode value true cmode runtime
   ip link add name br0 type bridge
   ip link set dev br0 type bridge ageing_time 1000
   ip link set dev eth1 up
   ip link set dev eth2 up
   ip link set dev eth1 master br0
   ip link set dev eth2 master br0
   ip link set dev br0 up
   ip link set dev br0 type bridge vlan_filtering 1
   bridge vlan add dev br0 vid 1 self
   bridge vlan add dev br0 vid 1 pvid untagged self

2. On AM625-SK, create and run the following script:

.. code:: sh

   #!/bin/sh
   #iet-setup-mqprio.sh

   ifconfig eth0 down
   ethtool -L eth0 tx 4
   ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
   ethtool --set-mm eth0 pmac-enabled on tx-enabled on verify-enabled on verify-time 10 tx-min-frag-size 124
   ifconfig eth0 up
   sleep 10

   tc qdisc add dev eth0 handle 100: root mqprio \
   num_tc 4 \
   map 0 1 2 3 \
   queues 1@0 1@1 1@2 1@3 \
   hw 1 \
   mode dcb \
   fp P P P E

   tc -g class show dev eth0
   tc qdisc add dev eth0 clsact
   tc filter add dev eth0 egress protocol ip prio 1 u32 match ip dport 5002 0xffff action skbedit priority 2
   tc filter add dev eth0 egress protocol ip prio 1 u32 match ip dport 5003 0xffff action skbedit priority 3
   ip addr add 192.168.100.20/24 dev eth0

3. On J7ES, run the following commands:

.. code:: console

   ifconfig eth0 192.168.100.30
   iperf3 -s -i30 -p5002& \
   iperf3 -s -i30 -p5003&

4. Then, on AM625-SK, run the following commands:

.. code:: console

   iperf3 -c 192.168.100.30 -u -b200M -l1472 -u -t30 -i30 -p5002& \
   iperf3 -c 192.168.100.30 -u -b50M -l1472 -u -t30 -i30 -p5003&

**Results:**

On AM625-SK (Sender):

.. code:: console

   root@am62xx-evm:~/iet2# ethtool -S eth0 | grep tx_pri0
      p0_tx_pri0: 79
      p0_tx_pri0_bcnt: 16681
      p0_tx_pri0_drop: 0
      p0_tx_pri0_drop_bcnt: 0
      tx_pri0: 82
      tx_pri0_bcnt: 14821
      tx_pri0_drop: 0
      tx_pri0_drop_bcnt: 0
   root@am62xx-evm:~/iet2# ethtool -S eth0 | grep tx_pri2
      p0_tx_pri2: 0
      p0_tx_pri2_bcnt: 0
      p0_tx_pri2_drop: 0
      p0_tx_pri2_drop_bcnt: 0
      tx_pri2: 509516
      tx_pri2_bcnt: 773422600
      tx_pri2_drop: 0
      tx_pri2_drop_bcnt: 0
   root@am62xx-evm:~/iet2# ethtool -S eth0 | grep tx_pri3
      p0_tx_pri3: 0
      p0_tx_pri3_bcnt: 0
      p0_tx_pri3_drop: 0
      p0_tx_pri3_drop_bcnt: 0
      tx_pri3: 127389
      tx_pri3_bcnt: 193355280
      tx_pri3_drop: 0
      tx_pri3_drop_bcnt: 0
   root@am62xx-evm:~/iet2# ethtool -I --show-mm eth0
      MAC Merge layer state for eth0:
      pMAC enabled: on
      TX enabled: on
      TX active: on
      TX minimum fragment size: 124
      RX minimum fragment size: 124
      Verify enabled: on
      Verify time: 10
      Max verify time: 128
      Verification status: SUCCEEDED
      Statistics:
         MACMergeFrameAssErrorCount: 0
         MACMergeFrameSmdErrorCount: 57
         MACMergeFrameAssOkCount: 0
         MACMergeFragCountRx: 0
         MACMergeFragCountTx: 112392
         MACMergeHoldCount: 0

On J7VCL (Switch):

.. code:: console

   root@j7200-evm:~/iet2# ethtool -I --show-mm eth1
   MAC Merge layer state for eth1:
   pMAC enabled: on
   TX enabled: on
   TX active: on
   TX minimum fragment size: 124
   RX minimum fragment size: 124
   Verify enabled: on
   Verify time: 10
   Max verify time: 128
   Verification status: SUCCEEDED
   Statistics:
      MACMergeFrameAssErrorCount: 0
      MACMergeFrameSmdErrorCount: 49
      MACMergeFrameAssOkCount: 40745
      MACMergeFragCountRx: 112392
      MACMergeFragCountTx: 0
      MACMergeHoldCount: 0

CASE-2: Frame is preempted on Switch Egress Port and Assembled on Receiver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. important::

   For the following tests, all interfaces which are a part of the test
   need to be a part of the same VLAN, since the switch needs to receive
   priority of the frames in order to perform preemption.

In addition to the Sender, the Switch's Host Port also transmits traffic
of lower priority to the receiver. This is done to ensure a higher chance
of frame preemption and therefore frame fragmentation on the Switch' Egress
Port.

Highest priority frame sent by J7VCL with preemption on AM625-SK's (Switch) Egress Port and Assembly on J7ES
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Connect eth0 of J7VCL to eth0 of AM625-SK and eth0 of J7ES to eth1 of
AM625-SK.

**Steps:**

1. On AM625-SK, create and run the following script:

.. code:: sh

   #!/bin/sh
   #iet-setup-mqprio.sh

   ifconfig eth0 down
   ifconfig eth1 down
   ethtool -L eth1 tx 4
   ethtool --set-priv-flags eth1 p0-rx-ptype-rrobin off
   ethtool --set-mm eth1 pmac-enabled on tx-enabled on verify-enabled on verify-time 10 tx-min-frag-size 124
   ifconfig eth0 up
   ifconfig eth1 up
   sleep 10

   tc qdisc add dev eth1 handle 100: root mqprio \
   num_tc 4 \
   map 0 1 2 3 \
   queues 1@0 1@1 1@2 1@3 \
   hw 1 \
   mode dcb \
   fp P P P E

   tc -g class show dev eth1


   devlink dev param set platform/8000000.ethernet name switch_mode value true cmode runtime
   ip link add name br0 type bridge
   ip link set dev br0 type bridge ageing_time 1000
   ip link set dev eth0 up
   ip link set dev eth1 up
   ip link set dev eth0 master br0
   ip link set dev eth1 master br0
   ip link set dev br0 up
   sleep 2

   ip link set dev br0 type bridge vlan_filtering 1
   bridge vlan add dev br0 vid 100 self
   bridge vlan add dev br0 vid 100 pvid tagged self
   bridge vlan add dev eth0 vid 100 master
   bridge vlan add dev eth1 vid 100 master
   sleep 2

   ip link add link br0 name br0.100 type vlan id 100
   ip link set br0.100 type vlan egress 0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7
   sleep 2

   tc qdisc add dev br0.100 clsact
   tc filter add dev br0.100 egress protocol ip prio 1 u32 match ip dport 5002 0xffff action skbedit priority 2
   sleep 2

2. On J7ES, create and run the following script:

.. code:: sh

   #!/bin/sh
   #iet-setup-mqprio.sh

   ifconfig eth0 down
   ethtool -L eth0 tx 4
   ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
   ethtool --set-mm eth0 pmac-enabled on tx-enabled on verify-enabled on verify-time 10 tx-min-frag-size 124
   ifconfig eth0 up
   sleep 10

   ip link add link eth0 name eth0.100 type vlan id 100
   sleep 5
   ifconfig eth0.100 192.168.100.30
   iperf3 -s -i30 -p5001&
   iperf3 -s -i30 -p5002&
   iperf3 -s -i30 -p5003&

3. On J7VCL, create and run the following script:

.. code:: sh

   #!/bin/sh
   #iet-setup-mqprio.sh

   ifconfig eth0 down
   ethtool -L eth0 tx 4
   ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
   ethtool --set-mm eth0 pmac-enabled on tx-enabled on verify-enabled on verify-time 10 tx-min-frag-size 124
   ifconfig eth0 up
   sleep 10
   ip link add link eth0 name eth0.100 type vlan id 100
   ip link set eth0.100 type vlan egress 0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7
   sleep 5

   tc qdisc add dev eth0.100 clsact
   tc filter add dev eth0.100 egress protocol ip prio 1 u32 match ip dport 5003 0xffff action skbedit priority 3
   ifconfig eth0.100 192.168.100.20 netmask 255.255.255.0
   sleep 2

4. Run the following commands on AM625-SK:

.. code:: console

   ifconfig br0.100 192.168.100.10
   sleep 10
   iperf3 -c 192.168.100.30 -u -b100M -l1472 t30 -i30 -p5001& \
   iperf3 -c 192.168.100.30 -u -b100M -l1472 t30 -i30 -p5002&

5. Now, on J7VCL, run the following command:

.. code:: console

   iperf3 -c 192.168.100.30 -u -b50M -l1472 -t30 -i30 -p5003&

**Results:**

On AM625-SK (Switch):

.. code:: console

   root@am62xx-evm:~/iet2# ethtool -S eth1 | grep tx_pri0
      p0_tx_pri0: 161
      p0_tx_pri0_bcnt: 30611
      p0_tx_pri0_drop: 0
      p0_tx_pri0_drop_bcnt: 0
      tx_pri0: 254911
      tx_pri0_bcnt: 387757114
      tx_pri0_drop: 0
      tx_pri0_drop_bcnt: 0
   root@am62xx-evm:~/iet2# ethtool -S eth1 | grep tx_pri2
      p0_tx_pri2: 0
      p0_tx_pri2_bcnt: 0
      p0_tx_pri2_drop: 0
      p0_tx_pri2_drop_bcnt: 0
      tx_pri2: 254764
      tx_pri2_bcnt: 387729583
      tx_pri2_drop: 0
      tx_pri2_drop_bcnt: 0
   root@am62xx-evm:~/iet2# ethtool -S eth1 | grep tx_pri3
      p0_tx_pri3: 0
      p0_tx_pri3_bcnt: 0
      p0_tx_pri3_drop: 0
      p0_tx_pri3_drop_bcnt: 0
      tx_pri3: 126634
      tx_pri3_bcnt: 192715723
      tx_pri3_drop: 0
      tx_pri3_drop_bcnt: 0
   root@am62xx-evm:~/iet2# ethtool -I --show-mm eth1
      MAC Merge layer state for eth1:
      pMAC enabled: on
      TX enabled: on
      TX active: on
      TX minimum fragment size: 124
      RX minimum fragment size: 124
      Verify enabled: on
      Verify time: 10
      Max verify time: 128
      Verification status: SUCCEEDED
      Statistics:
         MACMergeFrameAssErrorCount: 0
         MACMergeFrameSmdErrorCount: 0
         MACMergeFrameAssOkCount: 0
         MACMergeFragCountRx: 0
         MACMergeFragCountTx: 35437
         MACMergeHoldCount: 0

On J7ES (Receiver):

.. code:: console

   root@j721e-evm:~/iet2# ethtool -I --show-mm eth0
   MAC Merge layer state for eth0:
   pMAC enabled: on
   TX enabled: on
   TX active: on
   TX minimum fragment size: 124
   RX minimum fragment size: 124
   Verify enabled: on
   Verify time: 10
   Max verify time: 128
   Verification status: SUCCEEDED
   Statistics:
      MACMergeFrameAssErrorCount: 0
      MACMergeFrameSmdErrorCount: 89
      MACMergeFrameAssOkCount: 28362
      MACMergeFragCountRx: 35437
      MACMergeFragCountTx: 0
      MACMergeHoldCount: 0

Highest priority frame sent by AM625-SK with preemption on J7VCL's (Switch) Egress Port and Assembly on AM64-SK
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Connect eth0 of AM625-SK to eth1 of J7VCL and eth0 of J7ES to eth2 of
J7VCL.

**Steps:**

1. Create and run the following script on J7VCL:

.. code:: sh

   #!/bin/sh

   ifconfig eth1 down
   ifconfig eth2 down
   ifconfig eth3 down
   ifconfig eth4 down
   ethtool -L eth2 tx 4
   ethtool --set-priv-flags eth2 p0-rx-ptype-rrobin off
   ethtool --set-mm eth2 pmac-enabled on tx-enabled on verify-enabled on verify-time 10 tx-min-frag-size 124
   ifconfig eth1 up
   ifconfig eth2 up
   sleep 5

   tc qdisc replace dev eth2 handle 100: parent root mqprio \
   num_tc 4 \
   map 0 1 2 3 \
   queues 1@0 1@1 1@2 1@3 \
   hw 1 \
   mode dcb \
   fp P P P E

   tc -g class show dev eth2

   devlink dev param set platform/c000000.ethernet name switch_mode value true cmode runtime
   ip link add name br0 type bridge
   ip link set dev br0 type bridge ageing_time 1000
   ip link set dev eth1 up
   ip link set dev eth2 up
   ip link set dev eth1 master br0
   ip link set dev eth2 master br0
   ip link set dev br0 up
   sleep 2

   ip link set dev br0 type bridge vlan_filtering 1
   bridge vlan add dev br0 vid 100 self
   bridge vlan add dev br0 vid 100 pvid tagged self
   bridge vlan add dev eth1 vid 100 master
   bridge vlan add dev eth2 vid 100 master
   sleep 2

   ip link add link br0 name br0.100 type vlan id 100
   ip link set br0.100 type vlan egress 0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7
   sleep 2

   tc qdisc add dev br0.100 clsact
   tc filter add dev br0.100 egress protocol ip prio 1 u32 match ip dport 5002 0xffff action skbedit priority 2
   sleep 2

2. Create and run the following script on J7ES:

.. code:: sh

   #!/bin/sh
   #iet-setup-mqprio.sh

   ifconfig eth0 down
   ethtool -L eth0 tx 4
   ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
   ethtool --set-mm eth0 pmac-enabled on tx-enabled on verify-enabled on verify-time 10 tx-min-frag-siz4
   ifconfig eth0 up
   sleep 10

   ip link add link eth0 name eth0.100 type vlan id 100
   sleep 5
   ifconfig eth0.100 192.168.100.30
   iperf3 -s -i30 -p5001&
   iperf3 -s -i30 -p5002&
   iperf3 -s -i30 -p5003&

3. Create and run the following script on AM625-SK:

.. code:: sh

   #!/bin/sh
   #iet-setup-mqprio.sh

   ifconfig eth0 down
   ethtool -L eth0 tx 4
   ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
   ethtool --set-mm eth0 pmac-enabled on tx-enabled on verify-enabled on verify-time 10 tx-min-frag-size 124
   ifconfig eth0 up
   sleep 10
   ip link add link eth0 name eth0.100 type vlan id 100
   ip link set eth0.100 type vlan egress 0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7
   sleep 5

   tc qdisc add dev eth0.100 clsact
   tc filter add dev eth0.100 egress protocol ip prio 1 u32 match ip dport 5003 0xffff action skbedit p3
   ifconfig eth0.100 192.168.100.20 netmask 255.255.255.0
   sleep 2

4. Run the following commands on J7VCL:

.. code:: console

   ifconfig br0.100 192.168.100.10
   sleep 10
   iperf3 -c 192.168.100.30 -u -b100M -l1472 t30 -i30 -p5001&
   iperf3 -c 192.168.100.30 -u -b100M -l1472 t30 -i30 -p5002&

5. Now, run the following command on AM625-SK:

.. code:: console

   iperf3 -c 192.168.100.30 -u -b50M -l1472 -t30 -i30 -p5003&

**Results:**

On J7VCL (Switch):

.. code:: console

   root@j7200-evm:~/iet2# ethtool -S eth2 | grep tx_pri0
      p0_tx_pri0: 156
      p0_tx_pri0_bcnt: 29465
      p0_tx_pri0_drop: 0
      p0_tx_pri0_drop_bcnt: 0
      tx_pri0: 254971
      tx_pri0_bcnt: 387767517
      tx_pri0_drop: 0
      tx_pri0_drop_bcnt: 0
   root@j7200-evm:~/iet2# ethtool -S eth2 | grep tx_pri2
      p0_tx_pri2: 0
      p0_tx_pri2_bcnt: 0
      p0_tx_pri2_drop: 0
      p0_tx_pri2_drop_bcnt: 0
      tx_pri2: 254765
      tx_pri2_bcnt: 387729655
      tx_pri2_drop: 0
      tx_pri2_drop_bcnt: 0
   root@j7200-evm:~/iet2# ethtool -S eth2 | grep tx_pri3
      p0_tx_pri3: 0
      p0_tx_pri3_bcnt: 0
      p0_tx_pri3_drop: 0
      p0_tx_pri3_drop_bcnt: 0
      tx_pri3: 127385
      tx_pri3_bcnt: 193858727
      tx_pri3_drop: 0
      tx_pri3_drop_bcnt: 0
   root@j7200-evm:~/iet2# ethtool -I --show-mm eth2
      MAC Merge layer state for eth2:
      pMAC enabled: on
      TX enabled: on
      TX active: on
      TX minimum fragment size: 124
      RX minimum fragment size: 124
      Verify enabled: on
      Verify time: 10
      Max verify time: 128
      Verification status: SUCCEEDED
      Statistics:
         MACMergeFrameAssErrorCount: 0
         MACMergeFrameSmdErrorCount: 1
         MACMergeFrameAssOkCount: 0
         MACMergeFragCountRx: 0
         MACMergeFragCountTx: 242
         MACMergeHoldCount: 0

On J7ES (Receiver):

.. code:: console

   root@j721e-evm:~/iet2# ethtool -I --show-mm eth0
   MAC Merge layer state for eth0:
   pMAC enabled: on
   TX enabled: on
   TX active: on
   TX minimum fragment size: 124
   RX minimum fragment size: 124
   Verify enabled: on
   Verify time: 10
   Max verify time: 128
   Verification status: SUCCEEDED
   Statistics:
      MACMergeFrameAssErrorCount: 0
      MACMergeFrameSmdErrorCount: 121
      MACMergeFrameAssOkCount: 125
      MACMergeFragCountRx: 242
      MACMergeFragCountTx: 0
      MACMergeHoldCount: 0

CASE-3: Frame is preempted on both Sender and Switch Egress Port
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. important::

   For the following tests, all interfaces which are a part of the test
   need to be a part of the same VLAN, since the switch needs to receive
   priority of the frames in order to perform preemption.

In addition to the Sender, the Switch's Host Port also transmits traffic
of lower priority to the receiver. This is done to ensure a higher chance
of frame preemption and therefore frame fragmentation on the Switch' Egress
Port.

CASE-3 is the same as CASE-1 and CASE-2 combined.

Frame sent by J7VCL with preemption on J7VCL Egress Port and Assembled on AM625-SK's (Switch) Ingress Port followed by preemption on AM625-SK's (Switch) Egress Port and Assembled on J7ES
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Connect eth0 of J7VCL to eth0 of AM625-SK and eth0 of J7ES to eth1 of
AM625-SK

**Steps:**

1. Create and run the following script on AM625-SK:

.. code:: sh

   #!/bin/sh

   ifconfig eth0 down
   ifconfig eth1 down
   ethtool -L eth0 tx 4
   ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
   ethtool --set-mm eth0 pmac-enabled on tx-enabled on verify-enabled on verify-time 10 tx-min-frag-size 124
   ethtool -L eth1 tx 4
   ethtool --set-priv-flags eth1 p0-rx-ptype-rrobin off
   ethtool --set-mm eth1 pmac-enabled on tx-enabled on verify-enabled on verify-time 10 tx-min-frag-size 124
   ifconfig eth0 up
   ifconfig eth1 up
   sleep 5

   tc qdisc replace dev eth1 handle 100: parent root mqprio \
      num_tc 4 \
      map 0 1 2 3 \
      queues 1@0 1@1 1@2 1@3 \
      hw 1 \
      mode dcb \
      fp P P P E

   tc -g class show dev eth1

   devlink dev param set platform/8000000.ethernet name switch_mode value true cmode runtime
   ip link add name br0 type bridge
   ip link set dev br0 type bridge ageing_time 1000
   ip link set dev eth0 up
   ip link set dev eth1 up
   ip link set dev eth0 master br0
   ip link set dev eth1 master br0
   ip link set dev br0 up
   sleep 2

   ip link set dev br0 type bridge vlan_filtering 1
   bridge vlan add dev br0 vid 100 self
   bridge vlan add dev br0 vid 100 pvid tagged self
   bridge vlan add dev eth0 vid 100 master
   bridge vlan add dev eth1 vid 100 master
   sleep 2

   ip link add link br0 name br0.100 type vlan id 100
   ip link set br0.100 type vlan egress 0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7
   sleep 2

   tc qdisc add dev br0.100 clsact
   tc filter add dev br0.100 egress protocol ip prio 1 u32 match ip dport 5002 0xffff action skbedit priority 2
   sleep 2

2. Create and run the following script on J7ES:

.. code:: sh

   #!/bin/sh

   ifconfig eth0 down
   ethtool -L eth0 tx 4
   ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
   ethtool --set-mm eth0 pmac-enabled on tx-enabled on verify-enabled on verify-time 10 tx-min-frag-size 124
   ifconfig eth0 up
   sleep 5

   ip link add link eth0 name eth0.100 type vlan id 100
   sleep 5
   ifconfig eth0.100 192.168.100.30
   iperf3 -s -i30 -p5001&
   iperf3 -s -i30 -p5002&
   iperf3 -s -i30 -p5003&
   iperf3 -s -i30 -p5004&
   iperf3 -s -i30 -p5005&

3. Create and run the following script on J7VCL:

.. code:: sh

   #!/bin/sh

   ifconfig eth0 down
   ethtool -L eth0 tx 4
   ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
   ethtool --set-mm eth0 pmac-enabled on tx-enabled on verify-enabled on verify-time 10 tx-min-frag-size 124
   ifconfig eth0 up
   sleep 5

   tc qdisc replace dev eth0 handle 100: parent root mqprio \
      num_tc 4 \
      map 0 1 2 3 \
      queues 1@0 1@1 1@2 1@3 \
      hw 1 \
      mode dcb \
      fp P P P E

   ip link add link eth0 name eth0.100 type vlan id 100
   ip link set eth0.100 type vlan egress 0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7
   sleep 5

   tc qdisc add dev eth0.100 clsact
   tc filter add dev eth0.100 egress protocol ip prio 1 u32 match ip dport 5003 0xffff action skbedit priority 3
   tc filter add dev eth0.100 egress protocol ip prio 1 u32 match ip dport 5002 0xffff action skbedit priority 2
   ifconfig eth0.100 192.168.100.20 netmask 255.255.255.0
   sleep 2

4. Run the following commands on AM625-SK (Switch):

.. code:: console

   ifconfig br0.100 192.168.100.10
   sleep 10
   iperf3 -c 192.168.100.30 -u -b100M -l1472 t30 -i30 -p5001& \
   iperf3 -c 192.168.100.30 -u -b100M -l1472 t30 -i30 -p5002&

5. Now, run the following commands on J7VCL(Sender):

.. code:: console

   iperf3 -c 192.168.100.30 -u -b100M -l1472 -t30 -i30 -p5003& \
   iperf3 -c 192.168.100.30 -u -b50M -l1472 -t30 -i30 -p5004& \
   iperf3 -c 192.168.100.30 -u -b100M -l1472 -t30 -i30 -p5005&

**Results:**

On J7VCL (Sender):

.. code:: console

   root@j7200-evm:~/iet2# ethtool -I --show-mm eth0
   MAC Merge layer state for eth0:
   pMAC enabled: on
   TX enabled: on
   TX active: on
   TX minimum fragment size: 124
   RX minimum fragment size: 124
   Verify enabled: on
   Verify time: 10
   Max verify time: 128
   Verification status: SUCCEEDED
   Statistics:
      MACMergeFrameAssErrorCount: 0
      MACMergeFrameSmdErrorCount: 45
      MACMergeFrameAssOkCount: 0
      MACMergeFragCountRx: 0
      MACMergeFragCountTx: 52531
      MACMergeHoldCount: 0

On AM625-SK (Switch):

.. code:: console

   root@am62xx-evm:~/iet2# ethtool -I --show-mm eth0
   MAC Merge layer state for eth0:
   pMAC enabled: on
   TX enabled: on
   TX active: on
   TX minimum fragment size: 124
   RX minimum fragment size: 124
   Verify enabled: on
   Verify time: 10
   Max verify time: 128
   Verification status: SUCCEEDED
   Statistics:
      MACMergeFrameAssErrorCount: 2
      MACMergeFrameSmdErrorCount: 96
      MACMergeFrameAssOkCount: 10420
      MACMergeFragCountRx: 52523
      MACMergeFragCountTx: 0
      MACMergeHoldCount: 0

   root@am62xx-evm:~/iet2# ethtool -I --show-mm eth1
   MAC Merge layer state for eth1:
   pMAC enabled: on
   TX enabled: on
   TX active: on
   TX minimum fragment size: 124
   RX minimum fragment size: 124
   Verify enabled: on
   Verify time: 10
   Max verify time: 128
   Verification status: SUCCEEDED
   Statistics:
      MACMergeFrameAssErrorCount: 0
      MACMergeFrameSmdErrorCount: 0
      MACMergeFrameAssOkCount: 0
      MACMergeFragCountRx: 0
      MACMergeFragCountTx: 50371
      MACMergeHoldCount: 0

On J7ES (Receiver):

.. code:: console

   root@j721e-evm:~/iet2# ethtool -I --show-mm eth0
   MAC Merge layer state for eth0:
   pMAC enabled: on
   TX enabled: on
   TX active: on
   TX minimum fragment size: 124
   RX minimum fragment size: 124
   Verify enabled: on
   Verify time: 10
   Max verify time: 128
   Verification status: SUCCEEDED
   Statistics:
      MACMergeFrameAssErrorCount: 0
      MACMergeFrameSmdErrorCount: 76
      MACMergeFrameAssOkCount: 30473
      MACMergeFragCountRx: 50371
      MACMergeFragCountTx: 0
      MACMergeHoldCount: 0

Frame sent by AM625-SK with preemption on AM625-SK Egress Port and Assembled on J7VCL's (Switch) Ingress Port followed by preemption on J7VCL's (Switch) Egress Port and Assembled on J7ES
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Connect eth1 of J7VCL to eth0 of AM625-SK and eth0 of AM64-SK to eth1 of
AM625-SK.

**Steps:**

1. Create and run the following script on J7VCL:

.. code:: sh

   #!/bin/sh

   ifconfig eth1 down
   ifconfig eth2 down
   ifconfig eth3 down
   ifconfig eth4 down
   ethtool -L eth1 tx 4
   ethtool --set-priv-flags eth1 p0-rx-ptype-rrobin off
   ethtool --set-mm eth1 pmac-enabled on tx-enabled on verify-enabled on verify-time 10 tx-min-frag-size 124
   ethtool -L eth2 tx 4
   ethtool --set-priv-flags eth2 p0-rx-ptype-rrobin off
   ethtool --set-mm eth2 pmac-enabled on tx-enabled on verify-enabled on verify-time 10 tx-min-frag-size 124
   ifconfig eth1 up
   ifconfig eth2 up
   sleep 5

   tc qdisc replace dev eth2 handle 100: parent root mqprio \
   num_tc 4 \
   map 0 1 2 3 \
   queues 1@0 1@1 1@2 1@3 \
   hw 1 \
   mode dcb \
   fp P P P E

   tc -g class show dev eth2

   devlink dev param set platform/c000000.ethernet name switch_mode value true cmode runtime
   ip link add name br0 type bridge
   ip link set dev br0 type bridge ageing_time 1000
   ip link set dev eth1 up
   ip link set dev eth2 up
   ip link set dev eth1 master br0
   ip link set dev eth2 master br0
   ip link set dev br0 up
   sleep 2

   ip link set dev br0 type bridge vlan_filtering 1
   bridge vlan add dev br0 vid 100 self
   bridge vlan add dev br0 vid 100 pvid tagged self
   bridge vlan add dev eth1 vid 100 master
   bridge vlan add dev eth2 vid 100 master
   sleep 2

   ip link add link br0 name br0.100 type vlan id 100
   ip link set br0.100 type vlan egress 0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7
   sleep 2

   tc qdisc add dev br0.100 clsact
   tc filter add dev br0.100 egress protocol ip prio 1 u32 match ip dport 5002 0xffff action skbedit priority 2
   sleep 2

2. Create and run the following script on J7ES:

.. code:: console

   ifconfig eth0 down
   ethtool -L eth0 tx 4
   ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
   ethtool --set-mm eth0 pmac-enabled on tx-enabled on verify-enabled on verify-time 10 tx-min-frag-size 124
   ifconfig eth0 up
   sleep 5

   ip link add link eth0 name eth0.100 type vlan id 100
   sleep 5
   ifconfig eth0.100 192.168.100.30
   iperf3 -s -i30 -p5001&
   iperf3 -s -i30 -p5002&
   iperf3 -s -i30 -p5003&
   iperf3 -s -i30 -p5004&
   iperf3 -s -i30 -p5005&

3. Create and run the following script on J7VCL:

.. code:: sh

   #!/bin/sh

   ifconfig eth0 down
   ethtool -L eth0 tx 4
   ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
   ethtool --set-mm eth0 pmac-enabled on tx-enabled on verify-enabled on verify-time 10 tx-min-frag-size 124
   ifconfig eth0 up
   sleep 5

   tc qdisc replace dev eth0 handle 100: parent root mqprio \
      num_tc 4 \
      map 0 1 2 3 \
      queues 1@0 1@1 1@2 1@3 \
      hw 1 \
      mode dcb \
      fp P P P E

   ip link add link eth0 name eth0.100 type vlan id 100
   ip link set eth0.100 type vlan egress 0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7
   sleep 5

   tc qdisc add dev eth0.100 clsact
   tc filter add dev eth0.100 egress protocol ip prio 1 u32 match ip dport 5003 0xffff action skbedit priority 3
   tc filter add dev eth0.100 egress protocol ip prio 1 u32 match ip dport 5002 0xffff action skbedit priority 2
   ifconfig eth0.100 192.168.100.20 netmask 255.255.255.0
   sleep 2

4. Run the following commands on AM625-SK:

.. code:: console

   ifconfig br0.100 192.168.100.10
   sleep 10
   iperf3 -c 192.168.100.30 -u -b100M -l1472 t30 -i30 -p5001& \
   iperf3 -c 192.168.100.30 -u -b100M -l1472 t30 -i30 -p5002&

5. Now, run the following commands on J7VCL:

.. code:: console

   iperf3 -c 192.168.100.30 -u -b100M -l1472 -t30 -i30 -p5003& \
   iperf3 -c 192.168.100.30 -u -b50M -l1472 -t30 -i30 -p5004& \
   iperf3 -c 192.168.100.30 -u -b100M -l1472 -t30 -i30 -p5005&

**Results:**

On AM625-SK (Sender):

.. code:: console

   root@am62xx-evm:~/iet2# ethtool -I --show-mm eth0
   MAC Merge layer state for eth0:
   pMAC enabled: on
   TX enabled: on
   TX active: on
   TX minimum fragment size: 124
   RX minimum fragment size: 124
   Verify enabled: on
   Verify time: 10
   Max verify time: 128
   Verification status: SUCCEEDED
   Statistics:
      MACMergeFrameAssErrorCount: 0
      MACMergeFrameSmdErrorCount: 43
      MACMergeFrameAssOkCount: 0
      MACMergeFragCountRx: 0
      MACMergeFragCountTx: 160658
      MACMergeHoldCount: 0

On J7VCL (Switch):

.. code:: console

   root@j7200-evm:~/iet2# ethtool -I --show-mm eth1
   MAC Merge layer state for eth1:
   pMAC enabled: on
   TX enabled: on
   TX active: on
   TX minimum fragment size: 124
   RX minimum fragment size: 124
   Verify enabled: on
   Verify time: 10
   Max verify time: 128
   Verification status: SUCCEEDED
   Statistics:
      MACMergeFrameAssErrorCount: 0
      MACMergeFrameSmdErrorCount: 2
      MACMergeFrameAssOkCount: 69784
      MACMergeFragCountRx: 160658
      MACMergeFragCountTx: 0
      MACMergeHoldCount: 0

   root@j7200-evm:~/iet2# ethtool -I --show-mm eth2
   MAC Merge layer state for eth2:
   pMAC enabled: on
   TX enabled: on
   TX active: on
   TX minimum fragment size: 124
   RX minimum fragment size: 124
   Verify enabled: on
   Verify time: 10
   Max verify time: 128
   Verification status: SUCCEEDED
   Statistics:
      MACMergeFrameAssErrorCount: 0
      MACMergeFrameSmdErrorCount: 1
      MACMergeFrameAssOkCount: 0
      MACMergeFragCountRx: 0
      MACMergeFragCountTx: 161005
      MACMergeHoldCount: 0

On J7ES (Receiver):

.. code:: console

   root@j721e-evm:~/iet2# ethtool -I --show-mm eth0
   MAC Merge layer state for eth0:
   pMAC enabled: on
   TX enabled: on
   TX active: on
   TX minimum fragment size: 124
   RX minimum fragment size: 124
   Verify enabled: on
   Verify time: 10
   Max verify time: 128
   Verification status: SUCCEEDED
   Statistics:
      MACMergeFrameAssErrorCount: 31
      MACMergeFrameSmdErrorCount: 3195
      MACMergeFrameAssOkCount: 72757
      MACMergeFragCountRx: 160994
      MACMergeFragCountTx: 0
      MACMergeHoldCount: 0
