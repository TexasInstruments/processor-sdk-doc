.. rubric:: Bringing Up interface
   :name: k3-bringing-up-interfaces

The network interface can be configured automatically depending on root file system or configured manually. Manual configuration:

.. code-block:: console

   ip addr add 192.168.1.1/24 dev eth0
   ip link set dev eth0 up

   < or >

   ifconfig eth0 <ip> netmask <mask> up

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   .. note::

      The DP83869 PHY (associated with the eth1 CPSW interface for AM642-EVM) is not built into the kernel image. It is not available during early boot as a result, and must be brought up by adding a systemctl service as below:

   Assuming the root directory of the file system is ``/``.

   Create a service file named ``network_up.service`` in the directory ``/etc/systemd/system/`` and add the following into that file:

   .. code-block:: console

      [Unit]
      Description=Service to bring up network interfaces

      [Service]
      ExecStart=/bin/sh /usr/bin/network_up.sh

      [Install]
      WantedBy=default.target

   Create a shell script file named ``network_up.sh`` in the directory ``/usr/bin/`` and add the following into that file:

   .. code-block:: console

      #!/bin/sh
      ETH1_DIR=/sys/class/net/eth1
      while [ ! -d "$ETH1_DIR" ]
      do
         sleep 1;
      done
      if_state=$(ifconfig eth1 up |& grep ERROR)
      while [ -n $if_state ]
      do
         if_state=$(ifconfig eth1 up |& grep ERROR)
         sleep 1;
      done

   Now run the below command to enable the service, and from the next boot, interface will be UP automatically.

   .. code-block:: console

      systemctl enable network_up.service

.. rubric:: Get driver information
   :name: k3-ethtool-i-driver

The MCU_CPSW0 interface can be identified by using ``ethtool -i|--driver`` command.
It also provides some information about supported features.

.. code-block:: console

   # ethtool -i <dev>
   driver: am65-cpsw-nuss
   version: 0.1
   firmware-version:
   expansion-rom-version:
   bus-info: 46000000.ethernet
   supports-statistics: yes
   supports-test: no
   supports-eeprom-access: no
   supports-register-dump: yes
   supports-priv-flags: yes

.. rubric:: ethtool - Display standard information about device/link
   :name: k3-ethtool-display-standard-information-about-device

.. code-block:: console

   # ethtool eth0
   Supported ports: [ TP MII ]
   Supported link modes:   10baseT/Half 10baseT/Full
                           100baseT/Half 100baseT/Full
                           1000baseT/Half 1000baseT/Full
   Supported pause frame use: Symmetric Receive-only
   Supports auto-negotiation: Yes
   Supported FEC modes: Not reported
   Advertised link modes:  10baseT/Half 10baseT/Full
                           100baseT/Half 100baseT/Full
                           1000baseT/Half 1000baseT/Full
   Advertised pause frame use: No
   Advertised auto-negotiation: Yes
   Advertised FEC modes: Not reported
   Link partner advertised link modes:  10baseT/Half 10baseT/Full
                                        100baseT/Half 100baseT/Full
   Link partner advertised pause frame use: Symmetric
   Link partner advertised auto-negotiation: Yes
   Link partner advertised FEC modes: Not reported
   Speed: 100Mb/s
   Duplex: Full
   Port: MII
   PHYAD: 0
   Transceiver: internal
   Auto-negotiation: on
   Supports Wake-on: d
   Wake-on: d
   Current message level: 0x00000000 (0)

   Link detected: yes

.. rubric:: RX checksum offload
   :name: k3-rx-csum-offload

The Driver enables RX checksum offload by default. It can be disabled/enabled by using ``ethtool -K`` command:

.. code-block:: console

   # ethtool -k <dev>
   ....
   rx-checksumming: on

.. code-block:: console

   ethtool -K <dev> rx-checksum on|off

.. rubric:: TX checksum offload
   :name: k3-tx-csum-offload

The Driver enables TX checksum offload by default. It can be disabled/enabled by using ``ethtool -K`` command:

.. code-block:: console

   # ethtool -k <dev>
   ....
   tx-checksumming: on

.. code-block:: console

   ethtool -K <dev> tx-checksum on|off

A zero checksum is **not** inverted. It is possible to invert a zero checksum for all packets by
updating the :file:`am65-cpsw-nuss.c` driver with the following change:

.. code-block:: diff

   diff --git a/drivers/net/ethernet/ti/am65-cpsw-nuss.c b/drivers/net/ethernet/ti/am65-cpsw-nuss.c
   index 3d378920e65c..89329ddbb231 100644
   --- a/drivers/net/ethernet/ti/am65-cpsw-nuss.c
   +++ b/drivers/net/ethernet/ti/am65-cpsw-nuss.c
   @@ -1745,7 +1745,8 @@ static netdev_tx_t am65_cpsw_nuss_ndo_slave_xmit(struct sk_buff *skb,
                   cs_offset = cs_start + skb->csum_offset;
                   /* HW numerates bytes starting from 1 */
                   psdata[2] = ((cs_offset + 1) << 24) |
   -                           ((cs_start + 1) << 16) | (skb->len - cs_start);
   +                           ((cs_start + 1) << 16) | (skb->len - cs_start)
   +                           | BIT(15); // BIT(15) enables csum inversion for zero csum
                   dev_dbg(dev, "%s tx psdata:%#x\n", __func__, psdata[2]);

.. ifconfig:: CONFIG_part_variant in ('AM65X')

   .. note::

      TX checksum offload is implemented, but it is disabled by default
      on affected |__PART_FAMILY_DEVICE_NAMES__| SR1.0 due to errata i2027.

.. rubric:: **VLAN Config**
   :name: k3-vlan-config

VLAN can be added/deleted using ``ip`` or ``vconfig`` utility.


*VLAN Add*

.. code-block:: console

   ip link add link eth0 name eth0.5 type vlan id 5

   < or >

   vconfig add eth0 5

*VLAN del*

.. code-block:: console

   ip link del eth0.5

   < or >

   vconfig rem eth0 5

*VLAN IP assigning*

IP address can be assigned to the VLAN interface either via udhcpc
when a VLAN aware dhcp server is present or via static ip assigning
using ``ip`` or ``ifconfig``.

Once VLAN is added, it will create a new entry in Ethernet interfaces
like eth0.5, below is an example how it check the vlan interface

.. code-block:: console

   ip addr add 192.168.1.1/24 dev eth0.5

   < or >

   ifconfig eth0.5
   ....
   eth0.5    Link encap:Ethernet  HWaddr 20:CD:39:2B:C7:BE
             inet addr:192.168.10.5  Bcast:192.168.10.255  Mask:255.255.255.0
             UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
             RX packets:0 errors:0 dropped:0 overruns:0 frame:0
             TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
             collisions:0 txqueuelen:0
             RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

*VLAN Packet Send/Receive*

To Send or receive packets with the VLAN tag, bind the socket to the
proper Ethernet interface shown above and can send/receive via that
socket-fd.

|

.. rubric:: **Multicast Add/Delete**
   :name: k3-multicast-adddelete

Multicast MAC address can be added/deleted using *ip maddr* commands or Linux
socket ioctl SIOCADDMULTI/SIOCDELMULTI.

*Show muliticast address*

.. code-block:: console

   # ip maddr show dev <dev>
   2:      eth0
      link  01:00:5e:00:00:01
      link  01:80:c2:00:00:00
      link  01:80:c2:00:00:03
      link  01:80:c2:00:00:0e
      link  01:00:5e:00:00:fc
      inet  224.0.0.252
      inet  224.0.0.1

*Add muliticast address*

.. code-block:: console

   # ip maddr add 01:00:5e:00:00:05 dev eth0
   # ip maddr show dev eth0
   2:      eth0
      link  01:00:5e:00:00:01
      link  01:80:c2:00:00:00
      link  01:80:c2:00:00:03
      link  01:80:c2:00:00:0e
      link  01:00:5e:00:00:fc
      link  01:00:5e:00:00:05 static
      inet  224.0.0.252
      inet  224.0.0.1

*Delete muliticast address*

.. code-block:: console

   # ip maddr del 01:00:5e:00:00:05 dev eth0

|

.. rubric:: ``ethtool -P|--show-permaddr DEVNAME`` Show permanent hardware
   address
   :name: k3-ethtool-show-permaddr

.. code-block:: console

   # ethtool -P eth0
   Permanent address: a0:f6:fd:a6:46:6e"

.. rubric:: ``ethtool -s|--change DEVNAME`` Change generic options
   :name: k3-ethtool-change-generic-options

Below commands will be redirected to the phy driver:

.. code-block:: console

   # ethtool -s <dev>
   [ speed %d ]
   [ duplex half|full ]
   [ autoneg on|off ]
   [ wol p|u|m|b|a|g|s|d... ]
   [ sopass %x:%x:%x:%x:%x:%x ]

.. note::

    CPSW driver do not perform any kind of WOL specific actions or
    configurations.

.. code-block:: console

   #ethtool -s eth0 duplex half speed 100
   [ 3550.892112] cpsw 48484000.ethernet eth0: Link is Down
   [ 3556.088704] cpsw 48484000.ethernet eth0: Link is Up - 100Mbps/Half - flow control off

Sets the driver message type flags by name or number

.. code-block:: console

   [ msglvl %d | msglvl type on|off ... ]
   # ethtool -s eth0 msglvl drv off
   # ethtool -s eth0 msglvl ifdown off
   # ethtool -s eth0 msglvl ifup off
   # ethtool eth0
   Current message level: 0x00000031 (49)
      drv ifdown ifup

.. rubric:: ``ethtool -r|--negotiate DEVNAME`` Restart N-WAY negotiation
   :name: k3-ethtool-restart-n-way-negotiation

.. code-block:: console

   # ethtool -r eth0
   [ 4338.167685] cpsw 48484000.ethernet eth0: Link is Down
   [ 4341.288695] cpsw 48484000.ethernet eth0: Link is Up - 1Gbps/Full - flow control rx/tx"

.. rubric:: ``ethtool -a|--show-pause DEVNAME`` Show pause options
   :name: k3-ethtool-show-pause-options

.. code-block:: console

   # ethtool -a eth0
   Pause parameters for eth0:
   Autonegotiate:  off
   RX:             off
   TX:             off

.. rubric:: ``ethtool -A|--pause DEVNAME`` Set pause options
   :name: k3-ethtool-set-pause-options

.. code-block:: console

   # ethtool -A eth0 rx on tx on
   cpsw 48484000.ethernet eth0: Link is Up - 1Gbps/Full - flow control rx/tx
   # ethtool -a eth0
   Pause parameters for eth0:
   Autonegotiate:  off
   RX:             on
   TX:             on

.. rubric:: ``ethtool -g|--show-ring DEVNAME`` Query RX/TX ring parameters
   :name: k3-ethtool-query-rxtx-ring-parameters

.. code-block:: console

   # ethtool -g eth0
   Ring parameters for eth0:
   Pre-set maximums:
   RX:             0
   RX Mini:        0
   RX Jumbo:       0
   TX:             0
   Current hardware settings:
   RX:             500
   RX Mini:        0
   RX Jumbo:       0
   TX:             512

.. rubric:: ``ethtool-l|--show-channels DEVNAME`` Query Channels
   :name: k3-ethtool-query-channels

.. code-block:: console

   # ethtool -l eth0
   Channel parameters for eth0:
   Pre-set maximums:
   RX:             1
   TX:             8
   Other:          0
   Combined:       0
   Current hardware settings:
   RX:             1
   TX:             8
   Other:          0
   Combined:       0

.. rubric:: ``ethtool -L\|--set-channels DEVNAME`` Set Channels.
   :name: k3-ethtool--l--set-channels

Allows to control number of TX channels driver is allowed to work with at DMA level. The maximum number of TX channels is 8.
Supported options ``[ tx N ]``:

.. code-block:: console

   # ethtool -L eth0 tx 3


.. rubric:: ``ethtool --show-priv-flags/--set-priv-flags DEVNAME`` Show/Set private flags
   :name: k3-ethtool--priv-flags

Allows to control private flags supported by driver.

==================== ====================
 Flag
==================== ====================
p0-rx-ptype-rrobin   Controls TX DMA channels processing mode: round-robin or priority mode.
                     In case priority mode is enabled, the high number channel will have higher priority: TX 7 - prio 7 ... TX 0 - prio 0.
iet-frame-preemption Enables support for Interspersed Express Traffic (IET) IEEE 802.3br (frame preemption).
iet-mac-verify       Enables Interspersed Express Traffic (IET) MAC verification procedure on link up event.
==================== ====================

.. code-block:: console

   # ethtool --show-priv-flags eth0
   Private flags for eth0:
   p0-rx-ptype-rrobin  : on
   iet-frame-preemption: off
   iet-mac-verify      : off

   # ethtool --set-priv-flags eth0 p0-rx-ptype-rrobin off

.. note:: The network interface have to be down for private flags configuration.

.. rubric:: ``ethtool -S|--statistics DEVNAME`` Show adapter statistics
   :name: k3-ethtool-show-adapter-statistics

"ethtool -S" command displays statistic for both external Port 1 and Host port 0.
Host port 0 statistics prefixed with *p0_*.

.. code-block:: console

   # ethtool -S eth0
   NIC statistics:
      p0_rx_good_frames: 347
      p0_rx_broadcast_frames: 4
      p0_rx_multicast_frames: 264
      p0_rx_crc_errors: 0
      p0_rx_oversized_frames: 0
      p0_rx_undersized_frames: 0
      p0_ale_drop: 0
      p0_ale_overrun_drop: 0
      p0_rx_octets: 25756
      p0_tx_good_frames: 4816
      p0_tx_broadcast_frames: 3629
      p0_tx_multicast_frames: 1120
      p0_tx_octets: 878055
      p0_tx_64B_frames: 735
      p0_tx_65_to_127B_frames: 1023
      ...
      rx_good_frames: 4816
      rx_broadcast_frames: 3629
      rx_multicast_frames: 1120
      rx_pause_frames: 0
      rx_crc_errors: 0
      rx_align_code_errors: 0
      rx_oversized_frames: 0
      rx_jabber_frames: 0
      rx_undersized_frames: 0
      rx_fragments: 0
      ale_drop: 0
      ale_overrun_drop: 0
      rx_octets: 878055
      tx_good_frames: 347
      tx_broadcast_frames: 4
      tx_multicast_frames: 264
      tx_pause_frames: 0
      tx_deferred_frames: 0
      tx_collision_frames: 0
      tx_single_coll_frames: 0
      tx_mult_coll_frames: 0
      tx_excessive_collisions: 0
      tx_late_collisions: 0
      ...

.. rubric:: ``ethtool -T|--show-time-stamping DEVNAME`` Show time stamping
   capabilities.
   :name: k3-ethtool-show-time-stamping-capabilities.

Accessible when CPTS is enabled.

.. code-block:: console

   # ethtool -T eth0
   Time stamping parameters for eth0:
   Capabilities:
      hardware-transmit     (SOF_TIMESTAMPING_TX_HARDWARE)
      software-transmit     (SOF_TIMESTAMPING_TX_SOFTWARE)
      hardware-receive      (SOF_TIMESTAMPING_RX_HARDWARE)
      software-receive      (SOF_TIMESTAMPING_RX_SOFTWARE)
      software-system-clock (SOF_TIMESTAMPING_SOFTWARE)
      hardware-raw-clock    (SOF_TIMESTAMPING_RAW_HARDWARE)
   PTP Hardware Clock: 1
   Hardware Transmit Timestamp Modes:
      off                   (HWTSTAMP_TX_OFF)
      on                    (HWTSTAMP_TX_ON)
   Hardware Receive Filter Modes:
      none                  (HWTSTAMP_FILTER_NONE)
      all                   (HWTSTAMP_FILTER_ALL)

.. rubric:: ``ethtool --show-eee DEVNAME`` Show EEE settings
   :name: k3-ethtool-show-eee-settings

.. code-block:: console

   #ethtool --show-eee eth0
   EEE Settings for eth0:
      EEE status: not supported

.. rubric:: ``ethtool --set-eee DEVNAME`` Set EEE settings.
   :name: k3-ethtool-set-eee-settings.

.. note::

    Full EEE is not supported in driver, but it enables reading
    and writing of EEE advertising settings in Ethernet PHY. This way one
    can disable advertising EEE for certain speeds.

.. rubric:: ``ethtool -d|--register-dump DEVNAME`` Do a register dump
   :name: k3-ethtool-do-a-register-dump

This command dumps all CPSW MMIO regions in the below format.
The TI switch-config tool can be used for CPSW NUSS register dump parsing.

+------------------------------------------------------------------+
| MMIO region header (8 Bytes)                                     |
+====================+=============================================+
| module_id          | MMIO region id                              |
| (u32)              | NUSS = 1,                                   |
|                    | RGMII_STATUS = 2,                           |
|                    | MDIO = 3,                                   |
|                    | CPSW = 4,                                   |
|                    | CPSW_P0 = 5,                                |
|                    | CPSW_P1 = 6,                                |
|                    | CPSW_CPTS = 7,                              |
|                    | CPSW_ALE = 8,                               |
|                    | CPSW_ALE_TBL = 9                            |
+--------------------+---------------------------------------------+
| len (u32)          | MMIO region dump length, including header   |
+--------------------+---------------------------------------------+
| MMIO region registers dump (num_regs * 8 Bytes)                  |
+--------------------+---------------------------------------------+
| reg_offset (u32)   | register offset from the start              |
|                    | of MCU NAVSS MMIO space                     |
+--------------------+---------------------------------------------+
| reg_value (u32)    | MMIO region dump length, including header   |
+--------------------+---------------------------------------------+

Exception: ALE table dumped as raw array of ALE records (3 * u32 per record).

.. code-block:: console

   # ethtool -d eth0
   Offset          Values
   ------          ------
   0x0000:         01 00 00 00 48 00 00 00 00 00 00 00 00 71 a0 6b
   0x0010:         04 00 00 00 00 00 00 00 08 00 00 00 00 00 00 00
   0x0020:         0c 00 00 00 00 00 00 00 10 00 00 00 01 00 00 00
   0x0030:         14 00 00 00 00 00 00 00 18 00 00 00 00 00 00 00
   0x0040:         1c 00 00 00 00 00 00 00 02 00 00 00 48 00 00 00
   0x0050:         30 00 00 00 0b 00 00 00 34 00 00 00 00 00 00 00
   0x0060:         38 00 00 00 00 00 00 00 3c 00 00 00 00 00 00 00
   ...

################
Interrupt pacing
################

The Interrupt pacing (IRQ coalescing) based on hrtimers for RX/TX data path separately can be enabled by following ethtool commands (min value is 20us).

The RX data path - only one queue:

.. code-block:: console

   # ethtool -C ethX rx-usecs N

The TX data path - any of enabed TX queue (up to 8):

.. code-block:: console

   # by default enables coalesing for TX0
   # ethtool -C ethX tx-usecs N

   # configure TX0
   # ethtool -Q ethX queue_mask 1 --coalesce tx-usecs N

   #configure TX1
   # ethtool -Q ethX queue_mask 2 --coalesce tx-usecs N

   # configure TX0 and TX1
   # ethtool -Q ethX queue_mask 3 --coalesce tx-usecs N --coalesce tx-usecs N

The Interrupt pacing (IRQ coalescing) configuration can be retrieved by commands:

.. code-block:: console

   # show interrupt coalescing configuration:
   # ethtool -c ethX

   # show configuration for TX0 and TX1:
   # ethtool -Q eth0 queue_mask 3 --show-coalesce

It is also possible to use standard Linux Net core hard irqs deferral feature which can be enabled by configuring:

.. code-block:: console

   /sys/class/net/ethX/
   gro_flush_timeout (in ns)
   napi_defer_hard_irqs (number of retries)

Enabling of hard IRQ will be deferred napi_defer_hard_irqs times with gro_flush_timeout timeout.

The main difference of the hard irqs deferral feature from ethtool interrupt pacing (IRQ coalescing) is that it affects on both RX/TX data path and all TX/RX queues simultaneously.

.. rubric:: TI AM65x switch-config tool
   :name: k3-am65x-switch-config

The TI Processor SDK includes precompiled correct version of |__PART_FAMILY_NAME__| switch-config tool.

The TI |__PART_FAMILY_NAME__| switch-config tool sources for |__PART_FAMILY_DEVICE_NAMES__|  SoC can be found at

.. code-block:: text

   https://git.ti.com/cgit/switch-config/switch-config/

Branch:

.. code-block:: text

   origin/am65x-v1.0

Usage:

.. code-block:: console

   # switch-config -h
   Switch configuration commands.....
   switch-config -I,--ndev <dev> <command>

   commands:
   switch-config -d,--dump-ale :dump ALE table
   switch-config -D,--dump=<0..9> :dump registers (0 - all)
   switch-config -v,--version

   dump values:
    :1 - cpsw-nuss regs
    :2 - cpsw-nuss-rgmii-status regs
    :3 - cpsw-nuss-mdio regs
    :4 - cpsw-nu regs
    :5 - cpsw-nu-p0 regs
    :6 - cpsw-nu-p1 regs
    :7 - cpsw-nu-cpts regs
    :8 - cpsw-nu-ale regs
    :9 - cpsw-nu-ale-tbl regs

Example of ALE table dump:

.. code-block:: console

   # switch-config -d
   K3 cpsw dump version (1) len(6328)
   ALE table dump ents(64):
   0   : type: vlan , vid = 0, untag_force = 0x3, reg_mcast = 0x0, unreg_mcast = 0x0, member_list = 0x3
   1   : type: ucast, addr = f4:84:4c:eb:a0:00, ucast_type = persistant, port_num = 0x0, Secure
   2   : type: mcast, addr = ff:ff:ff:ff:ff:ff, mcast_state = f, no super, port_mask = 0x3
   3   : type: mcast, addr = 01:00:5e:00:00:01, mcast_state = f, no super, port_mask = 0x3
   4   : type: mcast, addr = 01:80:c2:00:00:00, mcast_state = f, no super, port_mask = 0x3
   5   : type: mcast, addr = 01:80:c2:00:00:03, mcast_state = f, no super, port_mask = 0x3
   6   : type: mcast, addr = 01:80:c2:00:00:0e, mcast_state = f, no super, port_mask = 0x3
   8   : type: mcast, addr = 01:00:5e:00:00:fc, mcast_state = f, no super, port_mask = 0x3
   9   : type: ucast, vid = 0, addr = 9c:b6:d0:89:0d:85, ucast_type = touched   , port_num = 0x1
   26  : type: ucast, vid = 0, addr = c4:71:54:a9:6e:b4, ucast_type = touched   , port_num = 0x1
   27  : type: ucast, vid = 0, addr = 00:25:22:a9:4c:b3, ucast_type = touched   , port_num = 0x1

Example of CPTS registers dump:

.. code-block:: console

   switch-config -D7
   K3 cpsw dump version (1) len(6328)
   cpsw-nu-cpts regdump: num_regs(38)
   0003d000:reg(4E8A2109)
   0003d004:reg(00000C21)
   0003d008:reg(00000000)
   0003d00c:reg(00000000)
   0003d010:reg(7EA3BA9B)
   0003d014:reg(00000000)
   0003d018:reg(00000000)
   0003d01c:reg(00000000)
   0003d020:reg(00000000)
   0003d024:reg(00000000)
   0003d028:reg(00000001)
   0003d02c:reg(00000000)
   0003d030:reg(00000000)
   0003d034:reg(C7298A99)
   0003d038:reg(03300000)
   0003d03c:reg(00000000)
   0003d040:reg(0000028E)
   0003d044:reg(00000000)
   0003d048:reg(00000000)

########################################################
Errata: i2329 MDIO interface corruption (CPSW and PRUSS)
########################################################

***********
Description
***********

It is possible that the MDIO interface of all instances of CPSW and PRUSS peripherals (if present) returns corrupt read data on MDIO reads (e.g. returning stale or previous data), or sends incorrect data on MDIO writes.  It is also possible that the MDIO interface becomes unavailable until the next peripheral reset (either by LPSC reset or global device reset with reset isolation disabled in case of CPSW).

Possible system level manifestations of this issue could be (1) erroneous ethernet PHY link down status (2) inability to properly configure an ethernet PHY over MDIO (3) incorrect PHY detection (e.g. wrong address) (4) read or write timeouts when attempting to configure PHY over MDIO.

The most common issue with Linux is observation of following prints in the kernel log

.. code-block:: console

   am65-cpsw-nuss 46000000.ethernet eth0: Link is Down
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Down
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Up - 100Mbps/Full - flow control off
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Down
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Up - 100Mbps/Full - flow control off
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Down
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Up - 100Mbps/Full - flow control off
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Down
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Up - 100Mbps/Full - flow control off
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Down
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Up - 100Mbps/Full - flow control off
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Down
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Up - 100Mbps/Full - flow control off
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Down
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Up - 100Mbps/Full - flow control off
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Down
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Up - 100Mbps/Full - flow control off
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Down
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Up - 100Mbps/Full - flow control off
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Down
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Up - 100Mbps/Full - flow control off
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Down
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Up - 100Mbps/Full - flow control off
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Down
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Up - 100Mbps/Full - flow control off
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Down
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Up - 100Mbps/Full - flow control off
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Down
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Up - 100Mbps/Full - flow control off
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Down
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Up - 100Mbps/Full - flow control off
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Down
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Up - 100Mbps/Full - flow control off
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Down
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Up - 100Mbps/Full - flow control off
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Down
   am65-cpsw-nuss 46000000.ethernet eth0: Link is Up - 100Mbps/Full - flow control off

***********************************
Workaround for TI SDK Version > 8.4
***********************************

MDIO protocol can be emulated by reading and writing to the appropriate bits within
the MDIO_MANUAL_IF_REG register of the MDIO peripheral to directly manipulate the
MDIO clock and data pins. Refer to TRM for full details of manual mode register
bits and their function.

In this case the device pin multiplexing should be configured to allow the IO to be
controlled by the CPSW or PRUSS peripherals (same as in normal intended operation),
but the MDIO state machine must be disabled by ensuring MDIO_CONTROL_REG.ENABLE bit
is 0 in the MDIO_CONTROL_REG and enable manual mode by setting
MDIO_POLL_REG.MANUALMODE bit to 1.

The implementation of the above workaround is available from Processor SDK v8.5.
