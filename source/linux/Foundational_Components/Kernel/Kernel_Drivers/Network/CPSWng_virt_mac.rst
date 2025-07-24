.. _cpswng_virt_mac:

CPSWng virtual MAC (remoteproc)
-------------------------------

.. contents:: :local:
    :depth: 3

Introduction
============

The TI |__PART_FAMILY_NAME__| SoC has integrated nine-port Gigabit Ethernet Switch subsystem
into device MAIN domain named CPSW0 and has 5 or 8 external Ethernet ports.

The |__SDK_FULL_NAME__| on the |__PART_FAMILY_NAME__| family of SoC's does not allow direct access to CPSW0 from Linux and
the CPSW0 is placed under exclusive control of the EthSwitch firmware running on one of the R5F cores (main_r5fss0_core0 by default).

Only the EthSwitch firmware has full control over |__PART_FAMILY_NAME__| CPSW0 and allows segregate
Ethernet traffic for each attached Remote CPU by using programable ALE classifiers and
exclusive UDMA TX channels and RX flows. The EthSwitch firmware supports the rpmsg-kdrv protocol and presents itself
as a number of rpmsg-kdrv devices, which provide CPSW0 resource management and debugging services for each attached Remote CPU.

The |__SDK_FULL_NAME__| on the |__PART_FAMILY_NAME__| family of SoC's contains a solution to allow sending/receiving Ethernet traffic
directed to/from CPU Core running Linux using a standard Linux network device.
The provided solution is implemented by two drivers:
- drivers/rpmsg-kdrv/rpmsg_kdrv_switch.c
- drivers/net/ethernet/ti/j721e-cpsw-virt-mac.c

This solution is illustrated below.

.. note::

   Overall TI remoteproc/virtio/rpmsg/rpmsg-kdrv description is out of scope of this section.

.. code:: text

 User space           +------+
 +--------------------+ethX  +----------------------------------------+
                      +--^---+
                        |
                        |
                +-------v-----+
                |Net core     |
                +-----^-------+
                      |
       +--------------v--------------------+ rpmsg_remotedev/
       | main_r5fss_cpswng_virt_macX       | rpmsg_remotedev_eth_switch_ops API
       | ethernet/ti/j721e-cpsw-virt-mac.c <--------+
       +-----------------------------------+        |
                                                    |
                           +------------------------v------+
                           | mpu_1_0_ethswitch-device-0 or |
                           | mpu_1_0_ethmac-device-1       |
                           | rpmsg-kdrv/rpmsg_kdrv_switch.c|
                           +-------------^-----------------+
        rpmsg_kdr Bus                    |
      +---------------------^--------+--------------------------+
                            |
                       +----+--------+
                       | rpmsg-kdrv  |
                       |             |
                       +----^--------+
        RPMSG Bus           |
      +---------------------+-----------------^-----------------+
                                              |
                                     +--------+--------------+
                                     |   virtio_rpmsg_bus    |
                                     |                       |
                                     +--------^--------------+
                                              |
                                              |
                                     +--------v--------------+
                                     | remoteproc            |
                                     | ti_k3_r5_remoteproc   |
                                     +--------+--------------+
 Kernel                                       |
 +--------------------------------------------|------------------------+
            +---------------------------------v------------+
            |SoC                                           |
            |  +------------+        +------------------+  |
            |  |            |        |main_r5fss0_core0 |  |
            |  |  CPSWnG    <--------+                  |  |
            |  +------------+        +------------------+  |
            |                                              |
            +----------------------------------------------+

Depending on ethSwitch firmware configuration two types of rpmsg-kdrv devices are registered:

**mpu_1_0_ethswitch-device-0** - virtual MAC interface which operates as part of the switch represented by number of CPSWng external ports, so called *virtual MAC switch mode*.
Only one rpmsg-kdrv device of this type is supported.

**mpu_1_0_ethmac-device-X** - virtual MAC interface which operated with dedicated CPSWng external port, so called *virtual MAC only mode*

The separate standard Linux network interfaces are created for every registered rpmsg-kdrv devices.

The |__SDK_FULL_NAME__| on the |__PART_FAMILY_NAME__| family of SoC contains ethSwitch firmware which is configured to instantiate one mpu_1_0_ethswitch-device-0 and one mpu_1_0_ethmac-device-1.

.. note::

   The EthSwitch FW configuration description is out of scope of this section.

Virtual MAC switch mode
"""""""""""""""""""""""

In virtual MAC switch mode (mpu_1_0_ethswitch-device-0) the j721e-cpsw-virt-mac driver operates as part of the switch represented by number of CPSWng external ports.

It can receive only traffic segregated to it by ethSwitch firmware which are:

 - unicast packets to assigned MAC address
 - multicast (MC) packets from registered MC addresses (exclusive, see :ref:`Multicast (MC) filtering<cpswng_virt_mac_mc_filtering>`)

It can send any kind of packets, but how they are forwarded inside CPSWng switch HW is defined by learning process and ethSwitch firmware configuration.

.. note::

   The EthSwitch FW configuration description is out of scope of this section.

Virtual MAC only mode
"""""""""""""""""""""

In virtual MAC only mode (mpu_1_0_ethmac-device-1) the j721e-cpsw-virt-mac driver operates with dedicated CPSWng external port X.

It can receive all non-VLAN tagged traffic from dedicated CPSWng external port X including unicast (to assigned MAC address) and multicats packets by default.

It should not receive packets from CPSWng external ports operated as switch.

It can send any kind of packets to dedicated CPSWng external port X and those packets expected to egress only through this external port X and not be forwarded to any CPSWng external ports operated as switch.

The Linux network interface (netdev) in this mode operates in ALLMULTI mode which can't be disabled, and also supports promisc mode, which enables reception of VLAN tagged packets.

|

Drivers initialization
""""""""""""""""""""""

The Linux TI remoteproc core ensures proper R5F core initialization, loads and starts the EthSwitch firmware,
and creates the default virtio devices for interacting with this firmware.
The virtio_rpmsg_bus driver performs discovery of the RPMSG devices and creates an rpmsg-kdrv device,
which, in turn, will trigger the rpmsg-kdrv core to discover "mpu_1_0_ethswitch-device-0" or "mpu_1_0_ethmac-device-1" and probe the rpmsg_kdrv_switch driver

The j721e-cpsw-virt-mac driver is started separately by the Linux core once the corresponding main_r5fss_cpswng_virt_macX device has been created by the Linux DT parsing code.
Once started, the j721e-cpsw-virt-mac driver will wait for rpmsg_kdrv_switch driver to be probed.

.. note::

   The EthSwitch FW may also be loaded by the bootloader, and, in this case, the remoteproc components will be started in "IPC-only" mode.

Drivers initialization Linux kernel log example for Virtual MAC switch mode:

.. code:: text

 rpmsg-kdrv-eth-switch rpmsg-kdrv-1-mpu_1_0_ethswitch-device-0: Device info: permissions: 0FFFFFFF uart_id: 2
 rpmsg-kdrv-eth-switch rpmsg-kdrv-1-mpu_1_0_ethswitch-device-0: FW ver 0.2 (rev 0)  3/Oct/2021 SHA:31ed829b
 j721e-cpsw-virt-mac main_r5fss_cpsw9g_virt_mac0: rpmsg attach_ext - rx_mtu:1522 features:00000003 tx_mtu[0]:2024 flow_idx:172 tx_cpsw_psil_dst_id:51712 mac_addr:70:ff:76:1d:92:c1 mac-only:0
 j721e-cpsw-virt-mac main_r5fss_cpsw9g_virt_mac0: virt_cpsw_nuss mac loaded
 j721e-cpsw-virt-mac main_r5fss_cpsw9g_virt_mac0: rdev_features:00000003 rdev_mtu:1522 flow_id:172 tx_psil_dst_id:4A00 mac_only:0
 j721e-cpsw-virt-mac main_r5fss_cpsw9g_virt_mac0: local_mac_addr:00:00:00:00:00:00 rdev_mac_addr:70:ff:76:1d:92:c1

Drivers initialization Linux kernel log example for Virtual MAC only mode:

.. code:: text

 rpmsg-kdrv-eth-switch rpmsg-kdrv-3-mpu_1_0_ethmac-device-1: Device info: permissions: 0FFFFFFF uart_id: 2
 rpmsg-kdrv-eth-switch rpmsg-kdrv-3-mpu_1_0_ethmac-device-1: FW ver 0.2 (rev 0)  3/Oct/2021 SHA:31ed829b
 j721e-cpsw-virt-mac main-r5fss-cpsw9g-virt-mac1: rpmsg attach_ext - rx_mtu:1522 features:00000007 tx_mtu[0]:2024 flow_idx:173 tx_cpsw_psil_dst_id:51713 mac_addr:70:ff:76:1d:92:c2 mac-only:1
 j721e-cpsw-virt-mac main-r5fss-cpsw9g-virt-mac1: virt_cpsw_nuss mac loaded
 j721e-cpsw-virt-mac main-r5fss-cpsw9g-virt-mac1: rdev_features:00000007 rdev_mtu:1522 flow_id:173 tx_psil_dst_id:4A01 mac_only:1
 j721e-cpsw-virt-mac main-r5fss-cpsw9g-virt-mac1: local_mac_addr:00:00:00:00:00:00 rdev_mac_addr:70:ff:76:1d:92:c2

rpmsg_kdrv_switch driver
""""""""""""""""""""""""

The rpmsg_kdrv_switch driver (drivers/rpmsg-kdrv/rpmsg_kdrv_switch.c) does not perform any functions by iteslf,
except checking for the supported EthSwitch FW version. It's intended to provide the RPMSG-KDRV rpmsg_remotedev API interface to be used by the j721e-cpsw-virt-mac driver.
Features controlled by the RPMSG-KDRV rpmsgi_remotedev API include:
- DMA resources allocation: TX UDMA channel and RX Flow
- MAC addresses assignment
- ARP helper for ARP requests processing from remote Net Hosts
- dbg: IPC ping
- dbg: CPSW0 register access
- dbg: statistic print request on R5F console (ioctl)

j721e-cpsw-virt-mac driver
""""""""""""""""""""""""""

The j721e-cpsw-virt-mac driver (drivers/net/ethernet/ti/j721e-cpsw-virt-mac.c) follows the standard Linux network interface architecture and supports the following features:

   - Network device up/down
   - Automatic (or manual) MAC address assignment
   - IP address assignment
   - Basic Ethertool functions
   - RX/TX csum offload (if enabled by EthSwitch FW)
   - SW Interrupt Pacing using timers.

*Virtual MAC switch mode*

   - Multicast (MC) packet filtering

*Virtual MAC only mode*

   - ALLMULTI mode - always on
   - promisc mode

*Not supported*:

- HW Interrupt Pacing is not supported.

Network data flow
"""""""""""""""""

The EthSwitch FW is responsible for UDMA resource management and allocation between attached remote cores.
The j721e-cpsw-virt-mac driver requests the EthSwitch FW for available UDMA resources during initialization by performing an attach operation: TX channel and RX flow through the Control path (rpmsg_remotedev API).
In the current design, the EthSwitch FW allocates dedicated (not shared) TX UDMA channel for each attached core,
but the EthSwitch FW controls RX UDMA channel and only provides dedicated UDMA RX flow to attached cores.

Hence, after allocation, the j721e-cpsw-virt-mac driver is responsible for the full TX UDMA channel initialization (including TX and TX completion ring initialization).
The j721e-cpsw-virt-mac driver also starts/stops the TX UDMA channel.
For RX side, the j721e-cpsw-virt-mac driver only performs UDMA RX flow initialization (including RX free descriptor and RX ring initialization).


.. code:: text

        User space          +------+
       +--------------------+ethX  +----------------------------------------+
                            +--^---+
                               |
                               |
                       +-------v-----+
                       |Net core     |
                       +-----^-------+
                             |
              +--------------v-------+
              | j721e-cpsw-virt-mac  |   Control Path
              |                      <----------+
              +----+---^-------------+          |
                   |   |                        |
                   |   |                        |
                   |   |              +---------v---------+
       TX channel  |   |RX flow       | rpmsg_kdrv_switch |
                   |   |              |                   |
                   |   |              +---------^---------+
                   |   |                        |
                Data Path                       |
              +----+---+-------------------------------------+
              |    |   |                        |      SoC   |
              |  +-v---+------+                 |            |
              |  |            |                 |            |
              |  |  UDMA      |                 |            |
              |  +---+--------+                 |            |
              |      |                          |            |
              |  +---v--------+        +--------v---------+  |
              |  |            |        |main_r5fss0_core0 |  |
              |  |  CPSWnG    <--------+                  |  |
              |  +------------+        +------------------+  |
              |                                              |
              +----------------------------------------------+

TThe EthSwitch FW needs to know which traffic to segregate to the Linux Host; therefore, the j721e-cpsw-virt-mac driver
registers the MAC address assigned to the virt_mac Network device within EthSwitch FW using Control path.

Once configured, the network data can be passed between the Linux virt_mac Network device and the CPSW0 without interaction with EthSwitch FW.

.. _cpswng_virt_mac_u_boot:

Enabling CPSWng Virtual Client for Linux
========================================

The CPSWng Virtual Client functionality is enabled by applying
the corresponding Linux device-tree overlay at U-Boot prompt.

To enable Linux CPSWng Virtual Client functionality at U-Boot, save the following command in uEnv.txt:

.. ifconfig:: CONFIG_part_variant in ('J721E')

    .. code-block:: text

        name_overlays="ti/k3-j721e-evm-virt-mac-client.dtbo"

.. ifconfig:: CONFIG_part_variant in ('J7200')

    .. code-block:: text

        name_overlays="ti/k3-j7200-evm-virt-mac-client.dtbo"

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

    .. code-block:: text

        name_overlays="ti/k3-j784s4-evm-virt-mac-client.dtbo"

Driver Configuration
====================

The |__SDK_FULL_NAME__| package has a |__PART_FAMILY_NAME__| rpmsg_kdrv_switch and j721e-cpsw-virt-mac drivers enabled by default and built as modules.
In case of custom builds, please ensure following configs are enabled.

.. code:: text

   CONFIG_RPMSG_KDRV
   CONFIG_RPMSG_KDRV_ETH_SWITCH
   CONFIG_TI_RDEV_ETH_SWITCH_VIRT_EMAC

User guide
==========

Starting the interface
""""""""""""""""""""""

Eth0 can be started by default or configured manually:

*DHCP*

.. code:: console

      udhcpc -i ethX
      ip link set dev ethX up

*Manual IP address configuration*

.. code:: console

    ip addr add <ip>/24 dev ethX
    ip link set dev ethX up

    < or >

    ifconfig ethX <ip> netmask <mask> up

Set MAC address
"""""""""""""""

The j721e-cpsw-virt-mac supports changing the HW MAC address, but this operation can be performed only when the network device is inactive (down).

.. code:: console

   ip link set dev ethX down
   ip link set dev ethX address <MAC-addr>
   ip link set dev ethX up

ethtool interface
"""""""""""""""""

Get driver information
^^^^^^^^^^^^^^^^^^^^^^

The CPSW0 interface can be identified by using ``ethtool -i|--driver`` command.
It also provides some information about supported features.

.. code:: console

    # ethtool -i <dev>
    ...

Display standard information about device/link
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: console

   # ethtool eth0

.. note::
   This command is supported, but not very useful, as the link is always up and no PHY.

Show permanent hardware address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: console

           # ethtool -P eth0
           Permanent address: a0:f6:fd:a6:46:6e"

RX/TX checksum offload
^^^^^^^^^^^^^^^^^^^^^^

The driver enables RX checksum offload by default. The current status can be obtained by using "ethtool -k" command:

.. code:: console

    # ethtool -k <dev>
    ....
    rx-checksumming: on
    tx-checksumming: off
        tx-checksum-ipv4: off [fixed]
        tx-checksum-ip-generic: off

It can be disabled/enabled by using "ethtool -K" command:

.. code:: console

    ethtool -K <dev> rx-checksum on|off
    ethtool -K <dev> tx-checksum-ip-generic on|off

.. note::

    TX checksum offload enablement is controlled by EthSwitch FW and current status provided to j721e-cpsw-virt-mac driver.

Driver testing
^^^^^^^^^^^^^^

.. code:: console

   # ethtool -t|--test <dev>
   ...
   RPMSG Ping test
   RPMSG Read reg
   RPMSG Dump stat

The j721e-cpsw-virt-mac can run several types of tests (if enabled by EthSwitch FW):
   - RPMSG Ping test: sends ping command to EthSwitch FW and checks if the same data returned back
   - RPMSG Read reg: sends CPSW0 CPSW_SS_CPSW_NUSS_IDVER_REG (0x0C000000) read register command to EthSwitch FW
   - RPMSG Dump stat: sends command to EthSwitch FW to dump current status and statistics

Interrupt pacing
""""""""""""""""

The Interrupt pacing (IRQ coalescing) based on hrtimers for RX/TX data path separately can be enabled by ethtool commands (min value is 20us):

::

  #  ethtool -C ethX tx-usecs N
  #  ethtool -C ethX rx-usecs N

The Interrupt pacing (IRQ coalescing) configuration can be retrieved by commands:

.. code:: console

  #  ethtool -c ethX

It is also possible to use standard Linux Net core hard irqs deferral feature which can be enabled by configuring:

.. code:: console

 /sys/class/net/ethX/
  gro_flush_timeout (in ns)
  napi_defer_hard_irqs (number of retries)

Enabling of hard IRQ will be deferred napi_defer_hard_irqs times with gro_flush_timeout timeout.

The main difference of the hard irqs deferral feature from ethtool interrupt pacing (IRQ coalescing) is that it affects on both RX/TX data path simultaneously.

.. _cpswng_virt_mac_mc_filtering:

Multicast (MC) filtering
""""""""""""""""""""""""

The EthFW supports MC filtering which allows to offload MC addresses list to EthFW and so enables MC traffic to be forwarded to Linux.

The EthFW supports two logical types of MC addresses:

  - *exclusive MC addresses* : such MC addresses will be exclusively directed to the Linux only through j721e-cpsw-virt-mac driver netdev.

  - *shared MC addresses* : such MC addresses belongs to statically configurable by EthFW MC addresses range. In this case MC packets will be delivered to Linux host by other means (i.e. shared memory based TAP interface) and not through j721e-cpsw-virt-mac driver netdev.
    Shared MC addresses intended to be used when it's required to deliver MC packets to more then one CPU cores present on |__PART_FAMILY_NAME__| SoC.

  - *reserved MC addresses* : such MC addresses belongs to reserved, statically configurable by EthFW MC addresses range.
    Reserved MC addresses intended to be consumed by EthFW itself only.


  The j721e-cpsw-virt-mac driver doesn't distinguish between exclusive, shared and reserved MC addresses and offloads all requested MC addresses, but if MC address is shared or reserved - the offload operation become NOP from the j721e-cpsw-virt-mac driver point of view.

.. note::

   The EthSwitch FW configuration description and shared MC addresses processing is out of scope of this section.


MC MAC addresses can be added/deleted using *ip maddr* command:

.. code:: console

    # Add MC address 239.255.1.4
    ip maddr add 01:00:5e:7f:01:04 dev ethX
    ip maddr show dev ethX
    2:      ethX
        ...
        link  01:00:5e:00:00:fb users 2
        link  01:00:5e:00:00:fc users 2
        link  01:00:5e:7f:01:03 users 2
        link  01:00:5e:7f:01:04 users 2 static
        ^^^^

    # Del MC address 239.255.1.4
    ip maddr del 01:00:5e:7f:01:04 dev eth0

or by using Linux socket IOCTL SIOCADDMULTI/SIOCDELMULTI:

.. code:: console

    ip route add 239.255.1.3 dev eth1
    iperf -s -B 239.255.1.3 -u&
    ip maddr show dev ethX
    2:      ethX
        ...
        link  01:00:5e:7f:01:03 users 2
        inet  239.255.1.3
        ^^^^
