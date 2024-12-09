NETCONF/YANG
============

.. contents:: :local:
    :depth: 3

Introduction
""""""""""""

NETCONF protocol defines a mechanism for network device management, retreiving configuration information and modifying device with new configuration data
It uses remote procedure call (RPC) messages encoded in XML for communication between server and client.
Server is the network device, while client is the application running as part of network manager.

For more information on NETCONF, please refer `RFC 6241 <https://www.rfc-editor.org/rfc/rfc6241>`_

YANG is a data modelling language used to model configuration and state data manipulated by the NETCONF, NETCONF remote procedure calls, and NETCONF notifications.
YANG is used to model the operations and content layers of NETCONF. The configuration data is stored in XML format. The YANG models define the nodes and
the possible range of values. The XML document provides the configuration data based on the nodes and its properties defined in the YANG models.

For more information on YANG, please refer `RFC 6020 <https://www.rfc-editor.org/rfc/rfc6020>`_

Netopeer2 is a server for implementing network configuration management based on the NETCONF Protocol. While NETCONF is the protocol specification, Netopeer2 is the open source project implementing the protocol. The Netopeer2 server uses sysrepo as a NETCONF datastore implementation.

Sysrepo is a YANG-based configuration and operational state data store for Unix/Linux applications. Applications can use sysrepo to store their configuration data modeled by YANG model.
The application in this SDK, **nw-configurator** is built using sysrepo libraries.

The Netopeer Server is available as part of the SDK. But the remote machine acting as the network manager must build and install the Netopeer Client in order to interact and configure the Server.

Installation on Remote Machine
""""""""""""""""""""""""""""""

.. note:: Skip this section if Netopeer Client will be run on another |__PART_FAMILY_NAME__|

Below are the steps to build and install the Netopeer Client and its dependencies on Ubuntu 18.04

**Install the below packages**

.. code-block:: console

 sudo apt-get install -y cmake build-essential bison flex libpcre3-dev libpcre2-dev libev-dev libavl-dev libprotobuf-c-dev
 sudo apt-get install -y protobuf-c-compiler swig python-dev lua5.2 pkg-config libpcre++-dev openssl libssl-dev libcrypto++-dev zlib1g-dev

**Install libyang:**

.. code-block:: console

 $ git clone https://github.com/CESNET/libyang.git
 $ cd libyang
 $ git checkout v2.1.4 -b v2.1.4
 $ mkdir build; cd build
 $ cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr ..
 $ make
 $ sudo make install

**Install libssh:**

.. code-block:: console

 $ git clone https://git.libssh.org/projects/libssh.git
 $ cd libssh
 $ git checkout libssh-0.10.0 -b libssh-0.10.0
 $ mkdir build; cd build
 $ cmake ..
 $ make
 $ sudo make install

**Install libnetconf2:**

.. code-block:: console

 $ git clone https://github.com/CESNET/libnetconf2.git
 $ cd libnetconf2
 $ git checkout v2.1.25 -b v2.1.25
 $ mkdir build; cd build
 $ cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr ..
 $ make
 $ sudo make install

.. note:: The version of libnetconf2 has dependency on libyang. When checking out a version of libnetconf2, make sure libnetconf2 and libyang versions are comptabile.

**Install sysrepo:**

.. code-block:: console

 $ git clone https://github.com/sysrepo/sysrepo.git
 $ cd sysrepo
 $ git checkout  v2.2.12 -b v2.2.12
 $ mkdir build; cd build
 $ cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr ..
 $ make
 $ sudo make install

.. note:: The version of sysrepo has dependency on libyang. When checking out a version of sysrepo, make sure sysrepo and libyang versions are comptabile.

**Install netopeer2:**

.. code-block:: console

 $ git clone https://github.com/CESNET/Netopeer2.git
 $ cd Netopeer2
 $ git checkout v2.1.42 -b v2.1.42
 $ cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .
 $ make
 $ sudo make install

Generic Execution
"""""""""""""""""

**Steps to follow on the Netconf Server side:**

1. Once the board is booted up, execute the below command to start the Netopeer Server

.. code-block:: console

 $ systemctl start sysrepod.service
 $ systemctl start netopeer2-serverd.service

The status of the services can be checked using

.. code-block:: console

  $ systemctl status sysrepod.service
  $ systemctl status netopeer2-serverd.service

**Steps to follow on the Netconf Client side:**

1. Start Netopeer Client

.. code-block:: console

 $ netopeer2-cli

Once the client app opens, the prompt will now turn into **>**

2. Connect to the netopeer2-server

.. code-block:: console

 > connect --ssh --host <IP_ADDR_OF_SERVER> --login root

3. To query the current configuration any datastore

.. code-block:: console

 > get-config --source <DATASTORE>

where DATASTORE could be "running, startup, candidate"

4. To validate the input XML

.. code-block:: console

 > validate --src-config=<ABSOLUTE_PATH_TO_CONFIG_XML_FILE>

5. To configure the datastore server by sending the XML file containing the configuration data

.. code-block:: console

 > edit-config --target <DATASTORE> --config=<ABSOLUTE_PATH_TO_CONFIG_XML_FILE>

where DATASTORE could be "running, startup, candidate"

copy-config operation could then be issued to copy the config from one datastore to another on the server

4. Disconnect from the netopeer2-server

.. code-block:: console

 > disconnect

5. Use the help command to list the supported operations

.. code-block:: console

  > help

Installing new YANG models
""""""""""""""""""""""""""
YANG need to be installed on the Netconf Server side and this can be done using the sysrepoctl utility.

Steps to install YANG model:

.. code-block:: console

 sysrepoctl -i <YANG_FILE>


Demonstration of the NETCONF/YANG support using the **nw-configurator** application

.. note ::

 The nw-configurator application has support only to configure the EST and the SDK comes pre-installed with TSN-EST YANG models.

The YANG model pertaining to EST that come pre-installed SDK is available at

https://github.com/YangModels/yang/blob/main/standard/ieee/published/802.1/ieee802-dot1q-sched.yang

The dependent YANG models are also installed.

Setup
^^^^^

The demo setup with a Remote Machine acting as a Netconf Client looks as below:

.. ifconfig:: CONFIG_part_variant in ('AM64X')

  .. Image:: /images/NETCONF_YANG_am64x.png

.. ifconfig:: CONFIG_part_variant in ('AM62X')

  .. Image:: /images/NETCONF_YANG_am62x.png

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

  .. Image:: /images/NETCONF_YANG_am62ax.png

1. The Remote Machine running Ubuntu 18.04 acts as the Remote Network Manager and runs the netopeer2-cli
2. The Receiver could be another |__PART_FAMILY_NAME__| or any machine equipped with a NIC that supports hardware timestampping.

The demo setup with another |__PART_FAMILY_NAME__| acting as a Netconf Client and Receiver looks as below:

.. ifconfig:: CONFIG_part_variant in ('AM64X')

  .. Image:: /images/NETCONF_YANG_wo_host_am64x.png

.. ifconfig:: CONFIG_part_variant in ('AM62X')

  .. Image:: /images/NETCONF_YANG_wo_host_am62x.png

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

  .. Image:: /images/NETCONF_YANG_wo_host_am62ax.png

**Steps to follow on the Netconf Server:**

1. Once the board is booted up, execute the below command to start the Netopeer Server

.. code-block:: console

 $ systemctl start sysrepod.service
 $ systemctl start netopeer2-serverd.service

The status of the services can be checked using

.. code-block:: console

 $ systemctl status sysrepod.service
 $ systemctl status netopeer2-serverd.service

2. Run the **nw-configurator** in the background

.. code-block:: console

 $ nw-configurator &

3. Pre-requisites

a. Show the current qdisc settings

.. code-block:: console

 $tc qdisc show dev eth0

b. Run the below commands

.. code-block:: console

 # Configure the Tx queues and disable Round Robin mode
 $ ifconfig eth0 down
 $ ifconfig eth1 down
 $ ethtool -L eth0 tx 3
 $ ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off
 $ ifconfig eth0 up
 $ ifconfig eth1 up

 #sync system time to CPSW CPTS
 $ phc2sys -s CLOCK_REALTIME -c eth0 -m -O 0 > /dev/null &

c. Display the updated qdisc settings. The settings will not have any gate schedule entries.

.. code-block:: console

 $ tc qdisc show dev eth0

**Steps to execute on the Netconf Client:**

1. Start Netopeer Client

.. code-block:: console

 $ netopeer-cli

Once the client app opens, the prompt will now become **>**

2. Connect to the netopeer2-server

.. code-block:: console

 > connect --ssh --host <IP_ADDR_OF_SERVER> --login root

3. Configure the server by sending the XML file containing the configuration data.
Create an XML document with the content presented at  `Sample XML based on EST YANG model`_

.. code-block:: console

 > edit-config --target running --config=<ABSOLUTE_PATH_TO_CONFIG_XML_FILE>

On success, a **OK** status will be displayed on the netopeer client

Check the updated qdisc settings on the |__PART_FAMILY_NAME__|

.. code-block:: console

 $ tc qdisc show dev eth0

**To test the gate entries in effect, follow the below steps**

1. Clone plget repo from: https://github.com/ikhorn/plget

2. Cross-compile for |__PART_FAMILY_NAME__| and Receiver executable using:

.. code-block:: console

 make ARCH=arm64 CROSS_COMPILE=aarch64-none-linux-gnu-


3. On the Receiver side,

a. Execute the plget tool over eth0 interface

.. code-block:: console

 ./plget -m rx-lat -f ipgap -n 128 -i eth0 -t ptpl2 -f hwts

4. On the |__PART_FAMILY_NAME__| side,

Transmit packets to Receiver

.. code-block:: console

 # NOTE: Replace 70:ff:76:1d:8c:08 with the MAC address of Receiver
 ./plget -i eth0 -m pkt-gen -p 3 -t ptpl2 -n 128 -a 70:ff:76:1d:8c:08 -l 512

Once the packets are transmitted from the |__PART_FAMILY_NAME__|, the logs are reported on the Receiver.

**Results observed on Receiver:**

.. code-block:: console

    hw rx time, us: packets 128:
    relative abs time 1280199778653 ns
    first packet abs time 1280199778653 ns
    ------------------------------------------------------------------------------------------------------------------------
                0 |        4.288 |        8.576 |       12.864 |        17.15 |       21.438 |       25.726 |       30.014 |
           34.302 |        38.59 |       42.878 |       47.166 |       51.454 |       55.742 |        60.03 |       64.318 |
           68.606 |       72.892 |        77.18 |       81.468 |       85.756 |       90.044 |       94.332 |        98.62 |
          102.908 |      107.196 |      111.484 |      115.772 |       120.06 |      124.346 |      499.988 |      504.276 |
          508.564 |      512.852 |       517.14 |      521.428 |      525.716 |      530.004 |      534.292 |       538.58 |
          542.868 |      547.156 |      551.442 |       555.73 |      560.026 |      564.314 |      568.602 |       572.89 |
          577.178 |      581.466 |      585.754 |      590.042 |       594.33 |      598.618 |      602.906 |      607.192 |
           611.48 |      615.768 |      620.056 |      624.344 |      999.986 |      1004.27 |      1008.56 |      1012.85 |
          1017.14 |      1021.43 |      1025.71 |         1030 |      1034.29 |      1038.58 |      1042.86 |      1047.15 |
          1051.44 |      1055.73 |      1060.02 |       1064.3 |      1068.59 |      1072.88 |      1077.17 |      1081.46 |
          1085.74 |      1090.03 |      1094.32 |      1098.61 |      1102.89 |      1107.18 |      1111.47 |      1115.76 |
          1120.05 |      1124.33 |      1499.98 |      1504.26 |      1508.55 |      1512.84 |      1517.13 |      1521.41 |
           1525.7 |      1529.99 |      1534.28 |      1538.57 |      1542.85 |      1547.14 |      1551.43 |      1555.72 |
          1560.01 |      1564.29 |      1568.58 |      1572.87 |      1577.16 |      1581.44 |      1585.73 |      1590.02 |
          1594.31 |       1598.6 |      1602.88 |      1607.17 |      1611.46 |      1615.75 |      1620.04 |      1624.32 |
          1999.96 |      2004.25 |      2008.54 |      2012.83 |      2017.12 |       2021.4 |      2025.69 |      2029.98 |
    ------------------------------------------------------------------------------------------------------------------------


    gap of hw rx time, us: packets 128:
    ------------------------------------------------------------------------------------------------------------------------
                0 |        4.288 |        4.288 |        4.288 |        4.286 |        4.288 |        4.288 |        4.288 |
            4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |
            4.288 |        4.286 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |
            4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.286 |      375.642 |        4.288 |
            4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |
            4.288 |        4.288 |        4.286 |        4.288 |        4.296 |        4.288 |        4.288 |        4.288 |
            4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.286 |
            4.288 |        4.288 |        4.288 |        4.288 |      375.642 |        4.288 |        4.288 |        4.288 |
            4.288 |        4.288 |        4.288 |        4.288 |        4.286 |        4.288 |        4.288 |        4.288 |
            4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |
            4.286 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |
            4.288 |        4.288 |      375.642 |        4.288 |        4.288 |        4.288 |        4.286 |        4.288 |
            4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |
            4.288 |        4.288 |        4.286 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |
            4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.286 |
          375.642 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |        4.288 |
    ------------------------------------------------------------------------------------------------------------------------
    max val(#30) = 375.64us
    min val(#4) = 4.29us
    peak-to-peak = 371.36us
    mean +- RMS = 15.98 +- 64.86 us

    Interface speed returned: 1000Mbps
    Frame size: 512
    Frame transmission time: 4096ns (4.096us)
    number of packets: 128
    RAW RATE = 256254.74kbps, PPS = 62562.2
    AVERAGE PERIOD = 15984.09ns (15.98us)

**Explanation:**

.. code-block:: console

    The entire cycle time is 500us. The gate entries for queues are set in the config XML as below
    Queue 2 - 125us
    Queue 1 - 125us
    Queue 0 - 250us

    Though the length argument passed to plget is 512bytes, it does not include the ethernet overhead such as preamble(7 bytes), SFD(1 byte), CRC(4 bytes).
    Also considering minimum interpacket gap of 12 bytes, the final frame size amounts to 536 bytes. At 1Gbps line rate, the frame transmission time is
    536 bytes * 8ns = 4.288us. The time gap between two frame is ~4.29us for about ~30 packets. This transmission duration corresponds to the time
    the gate/Queue-2 is open. Then there is a time jump of ~375us. This jump corresponds to the time where Queue-2 is closed (500 - 125 = 375us).

Sample XML based on EST YANG model
##################################

.. code-block:: console

 <bridges xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-bridge">
 	<bridge>
 		<name>br1</name>
 		<address>de-ad-be-ef-00-00</address>
 		<bridge-type>provider-bridge</bridge-type>
 	</bridge>
 </bridges>

 <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"
 	    xmlns:dot1q="urn:ieee:std:802.1Q:yang:ieee802-dot1q-bridge"
 	    xmlns:sched-bridge="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched-bridge"
 	    xmlns:sched="urn:ieee:std:802.1Q:yang:ieee802-dot1q-sched"
 	    xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
 	<interface>
 		<name>eth0</name>
 		<enabled>true</enabled>
 		<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
 		<dot1q:bridge-port>
 			<dot1q:bridge-name>br1</dot1q:bridge-name>
 			<sched-bridge:gate-parameter-table>
 				<sched-bridge:supported-interval-max>500000</sched-bridge:supported-interval-max>
 				<sched-bridge:supported-list-max>3</sched-bridge:supported-list-max>
 				<sched-bridge:supported-cycle-max>
 					<sched-bridge:numerator>1</sched-bridge:numerator>
 					<sched-bridge:denominator>1</sched-bridge:denominator>
 				</sched-bridge:supported-cycle-max>
 				<sched-bridge:gate-enabled>true</sched-bridge:gate-enabled>
 				<sched-bridge:admin-gate-states>255</sched-bridge:admin-gate-states>
 				<sched-bridge:config-change>true</sched-bridge:config-change>
 				<sched-bridge:admin-base-time>
 					<!-- Give past time -->
 					<sched-bridge:seconds>0</sched-bridge:seconds>
 					<sched-bridge:nanoseconds>0</sched-bridge:nanoseconds>
 				</sched-bridge:admin-base-time>
 				<sched-bridge:admin-cycle-time>
 					<sched-bridge:numerator>0</sched-bridge:numerator>
 					<sched-bridge:denominator>1</sched-bridge:denominator>
 				</sched-bridge:admin-cycle-time>
 				<sched-bridge:admin-control-list>
 					<sched-bridge:gate-control-entry>
 						<sched-bridge:index>0</sched-bridge:index>
 						<sched-bridge:operation-name>sched:set-gate-states</sched-bridge:operation-name>
 						<sched-bridge:gate-states-value>4</sched-bridge:gate-states-value>
 						<sched-bridge:time-interval-value>125000</sched-bridge:time-interval-value>
 					</sched-bridge:gate-control-entry>
                                         <sched-bridge:gate-control-entry>
                                                 <sched-bridge:index>1</sched-bridge:index>
                                                 <sched-bridge:operation-name>sched:set-gate-states</sched-bridge:operation-name>
                                                 <sched-bridge:gate-states-value>2</sched-bridge:gate-states-value>
                                                 <sched-bridge:time-interval-value>125000</sched-bridge:time-interval-value>
                                         </sched-bridge:gate-control-entry>
                                         <sched-bridge:gate-control-entry>
                                                 <sched-bridge:index>2</sched-bridge:index>
                                                 <sched-bridge:operation-name>sched:set-gate-states</sched-bridge:operation-name>
                                                 <sched-bridge:gate-states-value>1</sched-bridge:gate-states-value>
                                                 <sched-bridge:time-interval-value>250000</sched-bridge:time-interval-value>
                                         </sched-bridge:gate-control-entry>
 				</sched-bridge:admin-control-list>
 			</sched-bridge:gate-parameter-table>
 		</dot1q:bridge-port>
 	</interface>
 </interfaces>

