CBS
===

.. contents:: :local:
    :depth: 3

Introduction
------------

The K3 CPSW HW supports 2 level of traffic 802.1Qav shapers which are bound to TX DMA channels on Host Port and External Ports FIFOs which represent HW traffic
classes. The HW shapers allows to configure Committed Information Rate (guaranteed) and Excess Information Rate (non guaranteed) per TX DMA channels or External Ports Fifos.

The CPSWxG driver allows to perform Traffic Rate Limiting/shaping at:

* Host port ingress Rate Limiting, by configuring per TX DMA channels shaper. Only committed information rate is supported.
* Switch egress, Ethernet Port Transmit Rate Limiting, by configuring per TX FIFO shaper. Both committed and excess information rate is supported.

The number of Host port TX DMA channels is configurable (up to 8) through ethtool commands:- -L.
The Host port TX DMA channels processing mode has to be switched in Fixed priority mode through ethtool commands: –set-priv-flags.
Also note that –set-priv-flags and -L ethtool commands can be execute only when all Ethernet interfaces are down.

The Linux TC MQPRIO Qdisc can be used for mapping of packet priorities to traffic classes and routing packets to dedicated TX DMA channels or External Ports FIFOs.

Host port ingress Rate Limiting offload
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The netdev sysfs **tx_maxrate** parameter can be used to configure rate limit in Mbit/s per TX DMA channel.
The rate for shapers has to be set a little bit more then potential incoming rate, and real rates can differ, due to discreetness.

.. code:: console

   echo 100 > /sys/class/net/eth2/queues/tx-7/tx_maxrate

.. rubric:: Host port ingress Rate Limiting offload example

In this example Rate Limiting is enabled only for Host port TX channels.

* tc filters are used to assign pri for iperf3 traffic using port as filter value
* pri7 traffic routed to TX DMA channel 7, rate limit 100Mbit
* pri6 traffic routed to TX DMA channel 6, rate limit 200Mbit
* pri0-5 traffic routed to TX DMA channel 0

.. code:: console

   ip link set dev eth0 down
   ethtool -L eth0 tx 8
   ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
   ip link set dev eth0 up

   tc qdisc replace dev eth0 handle 100: parent root mqprio num_tc 3 \
   map 0 0 0 0 0 0 1 2 0 0 0 0 0 0 0 0 queues 1@0 1@6 1@7 hw 0

   echo 106 > /sys/class/net/eth0/queues/tx-7/tx_maxrate
   echo 212 > /sys/class/net/eth0/queues/tx-6/tx_maxrate

   tc qdisc add dev eth0 clsact
   tc filter add dev eth0 egress protocol ip prio 1 u32 match ip dport 5001 0xffff action skbedit priority 7
   tc filter add dev eth0 egress protocol ip prio 1 u32 match ip dport 5002 0xffff action skbedit priority 6

   iperf3 -c 192.168.1.2 -t10 -p5001 -Tpri7 & \
   iperf3 -c 192.168.1.2 -t10 -p5002 -Tpri6 & \
   iperf3 -c 192.168.1.2 -t10 -p5003 -Tpri0

   #result
   pri0:  - - - - - - - - - - - - - - - - - - - - - - - - -
   pri0:  [ ID] Interval           Transfer     Bitrate         Retr
   pri0:  [  5]   0.00-10.00  sec   767 MBytes   644 Mbits/sec    0             sender
   pri0:  [  5]   0.00-10.00  sec   766 MBytes   642 Mbits/sec                  receiver

   pri6:  - - - - - - - - - - - - - - - - - - - - - - - - -
   pri6:  [ ID] Interval           Transfer     Bitrate         Retr
   pri6:  [  5]   0.00-10.00  sec   238 MBytes   200 Mbits/sec    0             sender
   pri6:  [  5]   0.00-10.01  sec   238 MBytes   199 Mbits/sec                  receiver

   pri7:  - - - - - - - - - - - - - - - - - - - - - - - - -
   pri7:  [ ID] Interval           Transfer     Bitrate         Retr
   pri7:  [  5]   0.00-10.00  sec   120 MBytes   101 Mbits/sec    0             sender
   pri7:  [  5]   0.00-10.01  sec   119 MBytes  99.9 Mbits/sec                  receiver

   #statistic
   tx_pri0: 2819633
   tx_pri1: 2
   tx_pri2: 0
   tx_pri3: 102
   tx_pri4: 26
   tx_pri5: 0
   tx_pri6: 847449
   tx_pri7: 1237148

Switch egress, Ethernet Port Transmit Rate Limiting offload
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Linux MQPRIO Qdisc in channel offload mode can be used for mapping of packet priorities to traffic classes and configuring rate limit in Mbit/s per External Ports FIFOs.
The MQPRIO Qdisc **shaper bw_rlimit min_rate and max_rate** parameters can be used to configure External Ports FIFO shapers.

* the traffic class (TC) in terms of MQPRIO Qdisc is mapped 1:1 to External Ports FIFO. TC0 is lowest priority.
* MQPRIO Qdisk offload is expected to work with VALN/priority tagged traffic first of all and untagged traffic has to be mapped only to TC0.
* to handle properly untagged traffic from Host Port the 1:1 mapping has to be preserved between packet priority and Host TX DMA channel used to send packet
* VALN/priority tagged packets mapped to TC0 will exit switch with VALN tag.
* if Host sends traffic to the same, rate limited External Ports FIFO then corresponding Host TX DMA channel shapers has to be enabled and its rate has to be set equal or less than External Ports FIFO rate
* the rate for shapers has to be set a little bit more then potential incoming rate, and real rates can differ, due to discreetness.

.. code:: console

   tc qdisc add dev eth0 parent root handle 100: mqprio num_tc 3 \
   map 0 0 0 0 0 0 1 2 0 0 0 0 0 0 0 0 \
   queues 1@0 1@6 1@7 hw 1 mode channel \
   shaper bw_rlimit min_rate 0 212mbit 106mbit max_rate 0 250mbit 150mbit

.. rubric::  Switch egress, Ethernet Port Transmit Rate Limiting example

In this example Rate Limiting is enabled for Host port TX channels and External Ports FIFO.

* tc filters are used to assign pri for iperf3 traffic using port as filter value
* untagged traffic
* pri7 traffic routed to TX DMA channel 7, rate limit 100Mbit
* pri6 traffic routed to TX DMA channel 6, rate limit 200Mbit
* pri0-5 traffic routed to TX DMA channel 0
* pri7 traffic mapped to TC2, External Ports FIFO2, cir=100Mbit, eir=150Mbit
* pri6 traffic mapped to TC1, External Ports FIFO1, cir=200Mbit, eir=250Mbit
* pri0-5 traffic mapped to TC1, External Ports FIFO0

.. code:: console

   ip link set dev eth0 down
   ethtool -L eth0 tx 8
   ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
   ip link set dev eth0 up

   tc qdisc add dev eth0 parent root handle 100: mqprio num_tc 3 \
   map 0 0 0 0 0 0 1 2 0 0 0 0 0 0 0 0 \
   queues 1@0 1@6 1@7 hw 1 mode channel \
   shaper bw_rlimit min_rate 0 212mbit 106mbit max_rate 0 250mbit 150mbit

   echo 106 > /sys/class/net/eth0/queues/tx-7/tx_maxrate
   echo 212 > /sys/class/net/eth0/queues/tx-6/tx_maxrate

   tc qdisc add dev eth0 clsact
   tc filter add dev eth0 egress protocol ip prio 1 u32 match ip dport 5001 0xffff action skbedit priority 7
   tc filter add dev eth0 egress protocol ip prio 1 u32 match ip dport 5002 0xffff action skbedit priority 6

   iperf3 -c 192.168.1.2 -t10 -p5001 -Tpri7 & \
   iperf3 -c 192.168.1.2 -t10 -p5002 -Tpri6 & \
   iperf3 -c 192.168.1.2 -t10 -p5003 -Tpri0

   #result
   pri7:  - - - - - - - - - - - - - - - - - - - - - - - - -
   pri7:  [ ID] Interval           Transfer     Bitrate         Retr
   pri7:  [  5]   0.00-10.00  sec   120 MBytes   100 Mbits/sec    0             sender
   pri7:  [  5]   0.00-10.00  sec   119 MBytes  99.9 Mbits/sec                  receiver

   pri6:  - - - - - - - - - - - - - - - - - - - - - - - - -
   pri6:  [ ID] Interval           Transfer     Bitrate         Retr
   pri6:  [  5]   0.00-10.00  sec   238 MBytes   200 Mbits/sec    0             sender
   pri6:  [  5]   0.00-10.00  sec   238 MBytes   199 Mbits/sec                  receiver

   pri0:  - - - - - - - - - - - - - - - - - - - - - - - - -
   pri0:  [ ID] Interval           Transfer     Bitrate         Retr
   pri0:  [  5]   0.00-10.00  sec   767 MBytes   643 Mbits/sec    0             sender
   pri0:  [  5]   0.00-10.00  sec   766 MBytes   642 Mbits/sec                  receiver

   #statistic
   tx_pri0: 2012441
   tx_pri1: 172147
   tx_pri2: 259038
   tx_pri3: 0
   tx_pri4: 2
   tx_pri5: 9
   tx_pri6: 0
   tx_pri7: 0

CBS in MAC mode
---------------

Rate-limiting Host Port Ingress on AM625-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connect eth0 of AM625-SK to eth1 of J7VCL.

**Steps:**

1. Create and run the following script on AM625-SK:

.. code:: console

    #!/bin/sh

    ifconfig eth0 down
    ifconfig eth1 down
    ethtool -L eth0 tx 8
    ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
    ifconfig eth0 up
    ifconfig eth0 192.168.1.1

    sleep 10

    tc qdisc replace dev eth0 handle 100: parent root mqprio num_tc 3 \
    map 0 0 0 0 0 0 1 2 0 0 0 0 0 0 0 0 queues 1@0 1@6 1@7 hw 0

    echo 106 > /sys/class/net/eth0/queues/tx-7/tx_maxrate
    echo 212 > /sys/class/net/eth0/queues/tx-6/tx_maxrate

    tc qdisc add dev eth0 clsact
    tc filter add dev eth0 egress protocol ip prio 1 u32 match ip dport 5001 0xffff action skbedit priority 7
    tc filter add dev eth0 egress protocol ip prio 1 u32 match ip dport 5002 0xffff action skbedit priority 6

In the above script,  the tx queues that send data to the host port are rate-
limited using the following commands:

.. code:: console

    # Rate limit tx queue 7 of eth0 to 106 Mbps
    echo 106 > /sys/class/net/eth0/queues/tx-7/tx_maxrate
    # Rate limit tx queue 6 of eth0 to 212 Mbps
    echo 212 > /sys/class/net/eth0/queues/tx-6/tx_maxrate

2. Next, assign IP address of 192.168.1.2 to Port-1 of the CPSW5G ports on J7VCL using:

.. code:: console

    ifconfig eth1 192.168.1.2

3. Next, start an iperf server on J7VCL by running:

.. code:: console

    iperf3 -s -p 5001&
    iperf3 -s -p 5002&
    iperf3 -s -p 5003&

4. Now, run the iperf client on AM625-SK using:

.. code:: console

    iperf3 -c 192.168.1.2 -t10 -p5001 -Tpri7 & \
    iperf3 -c 192.168.1.2 -t10 -p5002 -Tpri6 & \
    iperf3 -c 192.168.1.2 -t10 -p5003 -Tpri0

**Results:**

On AM625-SK:

.. code:: console

    pri0:  - - - - - - - - - - - - - - - - - - - - - - - - -
    pri0:  [ ID] Interval           Transfer     Bitrate         Retr
    pri0:  [  5]   0.00-10.00  sec   738 MBytes   619 Mbits/sec  162             sender
    pri0:  [  5]   0.00-10.00  sec   735 MBytes   617 Mbits/sec                  receiver
    pri0:
    pri0:  iperf Done.
    pri6:  - - - - - - - - - - - - - - - - - - - - - - - - -
    pri6:  [ ID] Interval           Transfer     Bitrate         Retr
    pri6:  [  5]   0.00-10.00  sec   221 MBytes   185 Mbits/sec   69             sender
    pri6:  [  5]   0.00-10.01  sec   220 MBytes   184 Mbits/sec                  receiver
    pri6:
    pri6:  iperf Done.
    pri7:  - - - - - - - - - - - - - - - - - - - - - - - - -
    pri7:  [ ID] Interval           Transfer     Bitrate         Retr
    pri7:  [  5]   0.00-10.00  sec   115 MBytes  96.5 Mbits/sec   37             sender
    pri7:  [  5]   0.00-10.01  sec   114 MBytes  95.9 Mbits/sec                  receiver
    pri7:
    pri7:  iperf Done.

Rate-limiting Host Port Ingress on J7VCL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connect eth1 of J7VCL to eth0 of AM625-SK.

**Steps:**

1. Create and run the following script on J7VCL:

.. code:: bash

    #!/bin/sh

    ifconfig eth1 down
    ifconfig eth2 down
    ifconfig eth3 down
    ifconfig eth4 down
    ethtool -L eth1 tx 8
    ethtool --set-priv-flags eth1 p0-rx-ptype-rrobin off
    ifconfig eth1 up
    ifconfig eth1 192.168.1.1

    sleep 10

    tc qdisc replace dev eth1 handle 100: parent root mqprio num_tc 3 \
    map 0 0 0 0 0 0 1 2 0 0 0 0 0 0 0 0 queues 1@0 1@6 1@7 hw 0

    echo 106 > /sys/class/net/eth1/queues/tx-7/tx_maxrate
    echo 212 > /sys/class/net/eth1/queues/tx-6/tx_maxrate

    tc qdisc add dev eth1 clsact
    tc filter add dev eth1 egress protocol ip prio 1 u32 match ip dport 5001 0xffff action skbedit priority 7
    tc filter add dev eth1 egress protocol ip prio 1 u32 match ip dport 5002 0xffff action skbedit priority 6

In the above script,  the tx queues that send data to the host port are rate-
limited using the following commands:

.. code:: console

    # Rate limit tx queue 7 of eth0 to 106 Mbps
    echo 106 > /sys/class/net/eth0/queues/tx-7/tx_maxrate
    # Rate limit tx queue 6 of eth0 to 212 Mbps
    echo 212 > /sys/class/net/eth0/queues/tx-6/tx_maxrate

2. Next, assign IP address of 192.168.1.2 to Port-1 of the CPSW3G ports on AM625-SK using:

.. code:: console

    ifconfig eth0 192.168.1.2

3. Next, start an iperf server on AM625-SK by running:

.. code:: console

    iperf3 -s -p 5001&
    iperf3 -s -p 5002&
    iperf3 -s -p 5003&

4. Now, run the iperf client on J7VCL using:

.. code:: console

    iperf3 -c 192.168.1.2 -t10 -p5001 -Tpri7 & \
    iperf3 -c 192.168.1.2 -t10 -p5002 -Tpri6 & \
    iperf3 -c 192.168.1.2 -t10 -p5003 -Tpri0

**Results:**

On J7VCL:

.. code:: console

    pri0:  - - - - - - - - - - - - - - - - - - - - - - - - -
    pri0:  [ ID] Interval           Transfer     Bitrate         Retr
    pri0:  [  5]   0.00-10.00  sec   759 MBytes   637 Mbits/sec    0             sender
    pri0:  [  5]   0.00-10.00  sec   756 MBytes   635 Mbits/sec                  receiver
    pri0:
    pri0:  iperf Done.
    pri7:  - - - - - - - - - - - - - - - - - - - - - - - - -
    pri7:  [ ID] Interval           Transfer     Bitrate         Retr
    pri7:  [  5]   0.00-10.00  sec   118 MBytes  98.7 Mbits/sec    0             sender
    pri7:  [  5]   0.00-10.01  sec   117 MBytes  97.9 Mbits/sec                  receiver
    pri7:
    pri7:  iperf Done.
    pri6:  - - - - - - - - - - - - - - - - - - - - - - - - -
    pri6:  [ ID] Interval           Transfer     Bitrate         Retr
    pri6:  [  5]   0.00-10.00  sec   234 MBytes   196 Mbits/sec    0             sender
    pri6:  [  5]   0.00-10.01  sec   233 MBytes   195 Mbits/sec                  receiver
    pri6:
    pri6:  iperf Done.

Rate-limiting Switch Egress on AM625-SK (Data sent from Host Port of AM625-SK to J7VCL)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connect eth0 of AM625-SK to eth1 of J7VCL.

**Steps:**

1. Create and run the following script on AM625-SK:

.. code:: sh

    #!/bin/sh

    ifconfig eth0 down
    ifconfig eth1 down
    ethtool -L eth0 tx 8
    ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
    ifconfig eth0 up
    ifconfig eth0 192.168.1.1

    sleep 10

    tc qdisc add dev eth0 parent root handle 100: mqprio num_tc 3 \
    map 0 0 0 0 0 0 1 2 0 0 0 0 0 0 0 0 \
    queues 1@0 1@6 1@7 hw 1 mode channel \
    shaper bw_rlimit min_rate 0 212mbit 106mbit max_rate 0 250mbit 150mbit

    echo 106 > /sys/class/net/eth0/queues/tx-7/tx_maxrate
    echo 212 > /sys/class/net/eth0/queues/tx-6/tx_maxrate

    tc qdisc add dev eth0 clsact
    tc filter add dev eth0 egress protocol ip prio 1 u32 match ip dport 5001 0xffff action skbedit priority 7
    tc filter add dev eth0 egress protocol ip prio 1 u32 match ip dport 5002 0xffff action skbedit priority 6

2. Assign IP address of 192.168.1.2 to Port-1 of the CPSW5G ports on J7VCL using:

.. code:: console

    ifconfig eth1 192.168.1.2

3. Next, start an iperf server on J7VCL using:

.. code:: console

    iperf3 -s -p 5001&
    iperf3 -s -p 5002&
    iperf3 -s -p 5003&

4. Now, run the iperf client on AM625-SK using:

.. code:: console

    iperf3 -c 192.168.1.2 -t10 -p5001 -Tpri7 & \
    iperf3 -c 192.168.1.2 -t10 -p5002 -Tpri6 & \
    iperf3 -c 192.168.1.2 -t10 -p5003 -Tpri0

**Results:**

On AM625-SK:

.. code:: console

    pri7:  - - - - - - - - - - - - - - - - - - - - - - - - -
    pri7:  [ ID] Interval           Transfer     Bitrate         Retr
    pri7:  [  5]   0.00-10.00  sec   116 MBytes  97.1 Mbits/sec   17             sender
    pri7:  [  5]   0.00-10.00  sec   115 MBytes  96.5 Mbits/sec                  receiver
    pri7:
    pri7:  iperf Done.
    pri6:  - - - - - - - - - - - - - - - - - - - - - - - - -
    pri6:  [ ID] Interval           Transfer     Bitrate         Retr
    pri6:  [  5]   0.00-10.00  sec   226 MBytes   190 Mbits/sec   33             sender
    pri6:  [  5]   0.00-10.01  sec   225 MBytes   189 Mbits/sec                  receiver
    pri6:
    pri6:  iperf Done.
    pri0:  - - - - - - - - - - - - - - - - - - - - - - - - -
    pri0:  [ ID] Interval           Transfer     Bitrate         Retr
    pri0:  [  5]   0.00-10.00  sec   716 MBytes   601 Mbits/sec   42             sender
    pri0:  [  5]   0.00-10.00  sec   714 MBytes   598 Mbits/sec                  receiver
    pri0:
    pri0:  iperf Done.

Rate-limiting Switch Egress on J7VCL (Data sent from Host Port of J7VCL to AM625-SK)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connect eth1 of J7VCL to eth0 of AM625-SK.

**Steps:**

1. Create and run the following script on J7VCL:

.. code:: sh

    #!/bin/sh

    ifconfig eth1 down
    ifconfig eth2 down
    ifconfig eth3 down
    ifconfig eth4 down
    ethtool -L eth1 tx 8
    ethtool --set-priv-flags eth1 p0-rx-ptype-rrobin off
    ifconfig eth1 up
    ifconfig eth1 192.168.1.1

    sleep 10

    tc qdisc add dev eth1 parent root handle 100: mqprio num_tc 3 \
    map 0 0 0 0 0 0 1 2 0 0 0 0 0 0 0 0 \
    queues 1@0 1@6 1@7 hw 1 mode channel \
    shaper bw_rlimit min_rate 0 212mbit 106mbit max_rate 0 250mbit 150mbit

    echo 106 > /sys/class/net/eth1/queues/tx-7/tx_maxrate
    echo 212 > /sys/class/net/eth1/queues/tx-6/tx_maxrate

    tc qdisc add dev eth1 clsact
    tc filter add dev eth1 egress protocol ip prio 1 u32 match ip dport 5001 0xffff action skbedit priority 7
    tc filter add dev eth1 egress protocol ip prio 1 u32 match ip dport 5002 0xffff action skbedit priority 6

2. Assign IP address of 192.168.1.2 to Port-1 of the CPSW3G ports on AM625-SK using:

.. code:: console

    ifconfig eth0 192.168.1.2

3. Next, start an iperf server on AM625-SK using:

.. code:: console

    iperf3 -s -p 5001&
    iperf3 -s -p 5002&
    iperf3 -s -p 5003&

4. Now, run the iperf client on J7VCL using:

.. code:: console

    iperf3 -c 192.168.1.2 -t10 -p5001 -Tpri7 & \
    iperf3 -c 192.168.1.2 -t10 -p5002 -Tpri6 & \
    iperf3 -c 192.168.1.2 -t10 -p5003 -Tpri0

**Results:**

On J7VCL:

.. code:: console

    pri0:  - - - - - - - - - - - - - - - - - - - - - - - - -
    pri0:  [ ID] Interval           Transfer     Bitrate         Retr
    pri0:  [  5]   0.00-10.00  sec   746 MBytes   626 Mbits/sec    0             sender
    pri0:  [  5]   0.00-10.00  sec   744 MBytes   624 Mbits/sec                  receiver
    pri0:
    pri0:  iperf Done.
    pri6:  - - - - - - - - - - - - - - - - - - - - - - - - -
    pri6:  [ ID] Interval           Transfer     Bitrate         Retr
    pri6:  [  5]   0.00-10.00  sec   234 MBytes   196 Mbits/sec    0             sender
    pri6:  [  5]   0.00-10.01  sec   233 MBytes   195 Mbits/sec                  receiver
    pri6:
    pri6:  iperf Done.
    pri7:  - - - - - - - - - - - - - - - - - - - - - - - - -
    pri7:  [ ID] Interval           Transfer     Bitrate         Retr
    pri7:  [  5]   0.00-10.00  sec   119 MBytes  99.4 Mbits/sec    0             sender
    pri7:  [  5]   0.00-10.01  sec   117 MBytes  98.3 Mbits/sec                  receiver
    pri7:
    pri7:  iperf Done.

CBS in Switch mode
------------------

Rate-limiting is implemented on the sender and the switch, with the rate-
limiting on the switch being stricter than the sender. This is done due
to the size limit of the TX FIFO queue.

.. note::

    All three devices (AM625-SK, AM64-SK and J7VCL) must be a part of the
    same VLAN, to ensure that the priority field is included in the
    packets, enabling the switch to identify the priority and rate-limit
    traffic accordingly.

Rate limiting Switch Egress on AM625-SK (Data sent from AM64-SK to J7VCL via AM625-SK switch)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connect AM64-SK's eth0 to AM625-SK's eth0 and J7VCL's eth1 to AM625-SK's
eth1.

**Steps:**

1. Create and run the following script on AM625-SK:

.. code:: sh

    #!/bin/sh
    ifconfig eth0 down
    ifconfig eth1 down
    ethtool -L eth1 tx 8
    ethtool --set-priv-flags eth1 p0-rx-ptype-rrobin off

    devlink dev param set platform/8000000.ethernet name switch_mode value true cmode runtime
    ip link add name br0 type bridge
    ip link set dev br0 type bridge ageing_time 1000
    ip link set dev eth0 up
    ip link set dev eth1 up
    sleep 10

    ip link set dev eth0 master br0
    ip link set dev eth1 master br0
    ip link set dev br0 up
    ip link set dev br0 type bridge vlan_filtering 1
    bridge vlan add dev br0 vid 1 self
    bridge vlan add dev br0 vid 1 pvid untagged self
    bridge vlan add dev eth0 vid 100 master
    bridge vlan add dev eth1 vid 100 master


    tc qdisc add dev eth1 parent root handle 100: mqprio num_tc 3 \
    map 0 0 0 0 0 0 1 2 0 0 0 0 0 0 0 0 \
    queues 1@0 1@6 1@7 hw 1 mode channel \
    shaper bw_rlimit min_rate 99mbit 211mbit 105mbit max_rate 100mbit 212mbit 106mbit

2. Create and run the following script on AM64-SK:

.. code:: sh

    #!/bin/sh

    ifconfig eth0 down
    ifconfig eth1 down
    ethtool -L eth0 tx 8
    ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
    ifconfig eth0 up
    sleep 5

    ip link add link eth0 name eth0.100 type vlan id 100
    ip link set eth0.100 type vlan egress 0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7
    sleep 5
    ifconfig eth0.100 192.168.1.1 netmask 255.255.255.0
    sleep 2

    echo 106 > /sys/class/net/eth0/queues/tx-7/tx_maxrate
    echo 212 > /sys/class/net/eth0/queues/tx-6/tx_maxrate

    tc qdisc add dev eth0.100 clsact
    tc filter add dev eth0.100 egress protocol ip prio 1 u32 match ip dport 5001 0xffff action skbedit priority 7
    tc filter add dev eth0.100 egress protocol ip prio 1 u32 match ip dport 5002 0xffff action skbedit priority 6

    tc qdisc add dev eth0 parent root handle 100: mqprio num_tc 3 \
    map 0 0 0 0 0 0 1 2 0 0 0 0 0 0 0 0 \
    queues 1@0 1@6 1@7 hw 1 mode channel \
    shaper bw_rlimit min_rate 101mbit 213mbit 107mbit max_rate 102mbit 214mbit 108mbit

3. Create and run the following scripts on J7VCL:

.. code:: console

    #!/bin/sh

    ip link add link eth1 name eth1.100 type vlan id 100
    sleep 5
    ifconfig eth1.100 192.168.1.2 netmask 255.255.255.0
    sleep 2
    iperf3 -s -p 5001&
    iperf3 -s -p 5002&
    iperf3 -s -p 5003&

4. Now, run the iperf client on AM64-SK using the following commands:

.. code:: console

    iperf3 -c 192.168.1.2 -u -b108M -t10 -p5001 -Tpri7 & \
    iperf3 -c 192.168.1.2 -u -b214M -t10 -p5002 -Tpri6 & \
    iperf3 -c 192.168.1.2 -u -b102M -t10 -p5003 -Tpri0

**Results:**

.. code:: console

    pri7:  - - - - - - - - - - - - - - - - - - - - - - - - -
    pri7:  [ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
    pri7:  [  5]   0.00-10.00  sec   120 MBytes   101 Mbits/sec  0.000 ms  0/87099 (0%)  sender
    pri7:  [  5]   0.00-10.01  sec   115 MBytes  96.6 Mbits/sec  0.027 ms  3682/87099 (4.2%)  receiver
    pri7:
    pri7:  iperf Done.
    pri6:  - - - - - - - - - - - - - - - - - - - - - - - - -
    pri6:  [ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
    pri6:  [  5]   0.00-10.00  sec   241 MBytes   202 Mbits/sec  0.000 ms  0/174308 (0%)  sender
    pri6:  [  5]   0.00-10.00  sec   228 MBytes   191 Mbits/sec  0.104 ms  9203/174308 (5.3%)  receiver
    pri6:
    pri6:  iperf Done.
    pri0:  - - - - - - - - - - - - - - - - - - - - - - - - -
    pri0:  [ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
    pri0:  [  5]   0.00-10.00  sec   116 MBytes  97.3 Mbits/sec  0.000 ms  0/84000 (0%)  sender
    pri0:  [  5]   0.00-10.00  sec   114 MBytes  95.3 Mbits/sec  0.028 ms  1700/83958 (2%)  receiver
    pri0:
    pri0:  iperf Done.

Rate-limiting Switch Egress on J7VCL (Data sent from AM64-SK to AM625-SK via J7VCL switch)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connect AM64-SK's eth0 to J7VCL's eth1 and AM625-SK's eth0 to J7VCL's eth2.

**Steps:**

1. Create and run the following script on J7VCL:

.. code:: console

    #!/bin/sh
    ifconfig eth1 down
    ifconfig eth2 down
    ifconfig eth3 down
    ifconfig eth4 down
    ethtool -L eth2 tx 8
    ethtool --set-priv-flags eth2 p0-rx-ptype-rrobin off

    devlink dev param set platform/c000000.ethernet name switch_mode value true cmode runtime
    ip link add name br0 type bridge
    ip link set dev br0 type bridge ageing_time 1000
    ip link set dev eth1 up
    ip link set dev eth2 up
    sleep 10

    ip link set dev eth1 master br0
    ip link set dev eth2 master br0
    ip link set dev br0 up
    ip link set dev br0 type bridge vlan_filtering 1
    bridge vlan add dev br0 vid 1 self
    bridge vlan add dev br0 vid 1 pvid untagged self
    bridge vlan add dev eth1 vid 100 master
    bridge vlan add dev eth2 vid 100 master


    tc qdisc add dev eth2 parent root handle 100: mqprio num_tc 3 \
    map 0 0 0 0 0 0 1 2 0 0 0 0 0 0 0 0 \
    queues 1@0 1@6 1@7 hw 1 mode channel \
    shaper bw_rlimit min_rate 99mbit 211mbit 105mbit max_rate 100mbit 212mbit 106mbit

2. Create and run the following script on AM64-SK:

.. code:: console

    #!/bin/sh

    ifconfig eth0 down
    ifconfig eth1 down
    ethtool -L eth0 tx 8
    ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
    ifconfig eth0 up
    sleep 5

    ip link add link eth0 name eth0.100 type vlan id 100
    ip link set eth0.100 type vlan egress 0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7
    sleep 5
    ifconfig eth0.100 192.168.1.1 netmask 255.255.255.0
    sleep 2

    echo 106 > /sys/class/net/eth0/queues/tx-7/tx_maxrate
    echo 212 > /sys/class/net/eth0/queues/tx-6/tx_maxrate

    tc qdisc add dev eth0.100 clsact
    tc filter add dev eth0.100 egress protocol ip prio 1 u32 match ip dport 5001 0xffff action skbedit priority 7
    tc filter add dev eth0.100 egress protocol ip prio 1 u32 match ip dport 5002 0xffff action skbedit priority 6

    tc qdisc add dev eth0 parent root handle 100: mqprio num_tc 3 \
    map 0 0 0 0 0 0 1 2 0 0 0 0 0 0 0 0 \
    queues 1@0 1@6 1@7 hw 1 mode channel \
    shaper bw_rlimit min_rate 101mbit 213mbit 107mbit max_rate 102mbit 214mbit 108mbit

3. Create and run the following script on AM625-SK:

.. code:: console

    #!/bin/sh

    ip link add link eth0 name eth0.100 type vlan id 100
    sleep 5
    ifconfig eth0.100 192.168.1.2 netmask 255.255.255.0
    sleep 2
    iperf3 -s -p 5001&
    iperf3 -s -p 5002&
    iperf3 -s -p 5003&

4. Now, run the iperf client on AM64-SK using the following commands:

.. code:: console

    iperf3 -c 192.168.1.2 -u -b108M -t10 -p5001 -Tpri7 & \
    iperf3 -c 192.168.1.2 -u -b214M -t10 -p5002 -Tpri6 & \
    iperf3 -c 192.168.1.2 -u -b102M -t10 -p5003 -Tpri0

**Results:**

.. code:: console

    pri6:  - - - - - - - - - - - - - - - - - - - - - - - - -
    pri6:  [ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
    pri6:  [  5]   0.00-10.00  sec   240 MBytes   201 Mbits/sec  0.000 ms  0/173574 (0%)  sender
    pri6:  [  5]   0.00-10.03  sec   215 MBytes   180 Mbits/sec  0.083 ms  18116/173574 (10%)  receiver
    pri6:
    pri6:  iperf Done.
    pri7:  - - - - - - - - - - - - - - - - - - - - - - - - -
    pri7:  [ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
    pri7:  [  5]   0.00-10.00  sec   120 MBytes   101 Mbits/sec  0.000 ms  0/86842 (0%)  sender
    pri7:  [  5]   0.00-10.05  sec   117 MBytes  97.5 Mbits/sec  0.010 ms  2279/86842 (2.6%)  receiver
    pri7:
    pri7:  iperf Done.
    pri0:  - - - - - - - - - - - - - - - - - - - - - - - - -
    pri0:  [ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
    pri0:  [  5]   0.00-10.00  sec   116 MBytes  97.2 Mbits/sec  0.000 ms  0/83913 (0%)  sender
    pri0:  [  5]   0.00-10.01  sec   113 MBytes  95.1 Mbits/sec  0.009 ms  1683/83848 (2%)  receiver
    pri0:
    pri0:  iperf Done.
