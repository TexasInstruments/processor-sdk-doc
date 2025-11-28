.. _cpswng_native_ethernet:

CPSWng Native Ethernet
----------------------

.. contents:: :local:
   :depth: 2

Introduction
""""""""""""

The CPSWng ethernet subsystem can be controlled by the am65-cpsw-nuss driver in Linux to
provide standard ethernet features such as MAC mode, Switch mode, VLAN and TSN features.

.. note::
   By default, the native ethernet is configured to start in MAC mode. Switch mode can be
   enabled on demand. Refer to the "Switch Mode" section of this page for further details
   on switch mode configuration.

Driver Configuration
""""""""""""""""""""

Enable the following configs for Native Ethernet with CPSWng:

.. code:: Kconfig

   CONFIG_TI_K3_AM65_CPSW_NUSS
   CONFIG_TI_K3_AM65_CPSW_SWITCHDEV
   CONFIG_TI_K3_AM65_CPTS
   CONFIG_TI_DAVINCI_MDIO
   CONFIG_TI_AM65_CPSW_TAS
   CONFIG_PHY_TI_GMII_SEL
   CONFIG_PHY_J721E_WIZ
   CONFIG_PHY_TI_GMII_SEL
   CONFIG_PHY_CADENCE_TORRENT
   CONFIG_PHY_CADENCE_SIERRA

.. _cpswng_native_eth_overlays:

Enabling CPSWng Native Ethernet for Linux
"""""""""""""""""""""""""""""""""""""""""

Currently, the following modes are supported in the SDK with the native ethernet driver:

+-----------+-------------------------------+-------------------------------------------+
| SoC       | Supported Modes               |           Overlay file to use             |
+===========+===============================+===========================================+
| J7200     | QSGMII                        |    k3-j7200-evm-quad-port-eth-exp.dtbo    |
+-----------+-------------------------------+-------------------------------------------+
| J7200     | SGMII                         |    Overlay not part of SDK                |
+-----------+-------------------------------+-------------------------------------------+
| J721e     | RGMII                         |    k3-j721e-evm-gesi-exp-board.dtbo       |
+-----------+-------------------------------+-------------------------------------------+
| J721e     | QSGMII                        |    k3-j721e-evm-quad-port-eth-exp.dtbo    |
+-----------+-------------------------------+-------------------------------------------+
| J721e     | SGMII                         |    Overlay not part of SDK                |
+-----------+-------------------------------+-------------------------------------------+
| J721S2    | RGMII                         |    k3-j721s2-evm-gesi-exp-board.dtbo      |
+-----------+-------------------------------+-------------------------------------------+
| J784S4    | QSGMII                        |    k3-j784s4-evm-quad-port-eth1-exp.dtbo  |
+-----------+-------------------------------+-------------------------------------------+
| J784S4    | USXGMII                       |    k3-j784s4-evm-usxgmii-exp1-exp2.dtbo   |
+-----------+-------------------------------+-------------------------------------------+

.. note::
   | For enabling native ethernet, the am65-cpsw-nuss driver has to be included in the kernel build.
   | The native ethernet features are enabled by applying device-tree overlays at U-Boot.
   | To apply an overlay at U-Boot save the following command in the uEnv.txt file:
   |   **name_overlays="ti/<overlay-file-name>"**
   | where <overlay-file-name> is the corresponding overlay file from the table above.

For RGMII mode, the GESI expansion card's overlay may be used.
For QSGMII mode, the Quad Port Ethernet Expander daughter card's overlay may be used.
While SGMII mode has been verified in the SoCs which mention SGMII mode, no overlay is
provided with the SDK. USXGMII mode has been verified in a fixed-link configuration.

MAC Mode
""""""""

All the features documented within the "MAC mode" section of :ref:`cpsw2g` are applicable
to CPSWng Native Ethernet as well. The steps documented in that section can be followed
for utilizing the MAC mode features.

Switch Mode
"""""""""""

.. note::

   Switch mode functionality requires at least two external ethernet ports to work, it is
   independent of the MAC interface modes.

The Switch mode can be enabled by configuring devlink driver parameter
"switch_mode" to 1/true::

      devlink dev param set platform/c000000.ethernet \
      name switch_mode value true cmode runtime

Above setting can be done regardless of the state of Port's netdev
devices - UP/DOWN, but Port's netdev devices have to be in UP state
before joining the bridge. This is to avoid overwriting of bridge
configuration as CPSW switch driver completely reloads its configuration
when first port changes its state to UP.

When all the interfaces have joined the bridge - CPSW switch driver will
enable marking packets with offload_fwd_mark flag.

All configuration is implemented via switchdev API.

Bridge setup
''''''''''''

.. code:: console

   devlink dev param set platform/c000000.ethernet \
   name switch_mode value true cmode runtime

   ip link add name br0 type bridge
   ip link set dev br0 type bridge ageing_time 1000
   ip link set dev eth1 up
   ip link set dev eth2 up
   ip link set dev eth3 up
   ip link set dev eth4 up
   ip link set dev eth1 master br0
   ip link set dev eth2 master br0
   ip link set dev eth3 master br0
   ip link set dev eth4 master br0

   [*] ip link set dev br0 type bridge vlan_filtering 1
   [*] bridge vlan add dev br0 vid 1 self
   [*] bridge vlan add dev br0 vid 1 pvid untagged self

   Note: Steps [*] are mandatory.

.. Caution::

   Multicast flooding is on by default when Switch Mode is enabled.

Turn On/Off Spanning Tree Protocol (STP)
''''''''''''''''''''''''''''''''''''''''

.. code:: console

   ip link set dev br0 type bridge stp_state 1/0

VLAN configuration
''''''''''''''''''

.. code:: console

   bridge vlan add dev br0 vid 1 self <---- add VLAN as a Bridge Entry
   bridge vlan add dev br0 vid 1 pvid untagged self <---- add cpu port to VLAN 1

This step is mandatory for bridge/default_pvid.

Adding extra VLANs
''''''''''''''''''

1. Untagged

.. code:: console

   bridge vlan add dev eth1 vid 100 pvid untagged master
   bridge vlan add dev sw0p2 vid 100 pvid untagged master
   bridge vlan add dev br0 vid 100 self <---- add VLAN as a Bridge Entry
   bridge vlan add dev br0 vid 100 pvid untagged self <---- Add cpu port to VLAN100

2. Tagged

.. code:: console

   bridge vlan add dev eth1 vid 100 master
   bridge vlan add dev sw0p2 vid 100 master
   bridge vlan add dev br0 vid 100 self <---- add VLAN as a Bridge Entry
   bridge vlan add dev br0 vid 100 pvid tagged self <---- Add cpu port to VLAN100

Forwarding Data Bases (FDBs)
''''''''''''''''''''''''''''

Forwarding entries for MAC addresses are automatically added on the
appropriate switch port upon detection as default operation as an
unmanaged bridge. For managed bridge operation manually add FDB entries
as required.

Manually adding FDBs::

   bridge fdb add aa:bb:cc:dd:ee:ff dev eth1 master vlan 100
   bridge fdb add aa:bb:cc:dd:ee:fe dev sw0p2 master <---- Add on all VLANs

Multicast Data Bases (MDBs)
'''''''''''''''''''''''''''

Multicast entries are automatically added on the appropriate switch port
upon detection as default operation as an unmanaged bridge. For managed
bridge operation manually add MDB entries as required.

Manually adding MDBs::

   bridge mdb add dev br0 port eth1 grp 239.1.1.1 permanent vid 100
   bridge mdb add dev br0 port eth1 grp 239.1.1.1 permanent <---- Add on all VLANs

Multicast flooding
''''''''''''''''''

CPU port mcast_flooding is always on

Turning flooding on/off on switch ports::

   bridge link set dev eth1 mcast_flood on/off

TSN Features
""""""""""""

The TSN features supported by CPSWng Native Ethernet along with the testing details are documented
at :ref:`tsn_with_cpsw`. The steps documented in that page can be followed with appropriate
modifications.
