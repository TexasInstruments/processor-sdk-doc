.. _cpswng:

CPSWng Ethernet
---------------

.. contents:: :local:
   :depth: 1

Introduction
""""""""""""

The TI |__PART_FAMILY_NAME__| family of devices have Multi Port
Gigabit Ethernet Switch Subsystem CPSWng. SoCs may have more than 4 external
ports with selectable RGMII, QSGMII and SGMII interfaces and an internal
Communications Port Programming Interface (CPPI) port (Host port 0).
Host Port 0 CPPI Packet Streaming Interface interface supports 8 TX
channels and one RX channel DMA channel.

Multi port Gigabit Ethernet Switch Subsystem CPSWng supports both independent
MAC mode of operation supporting multiple independent Ethernet
interfaces with complete isolation (no packet switching between external
ports), or can be configured in Switch mode with IEEE 802.1Q HW bridge
in managed or learning mode between each of the individual MAC ports.

Depending on the SoC, the value of n in CPSWng varies as follows:

.. ifconfig:: CONFIG_part_family in ('J7_family')

   +-----------+----------------+-----------------------------------+
   | SoC       | n in CPSWng    | Number of Ports                   |
   +===========+================+===================================+
   | J7200     | n = 5 (CPSW5g) | 5 (1 host port, 4 external ports) |
   +-----------+----------------+-----------------------------------+
   | J721e     | n = 9 (CPSW9g) | 9 (1 host port, 8 external ports) |
   +-----------+----------------+-----------------------------------+
   | J784S4    | n = 9 (CPSW9g) | 9 (1 host port, 8 external ports) |
   +-----------+----------------+-----------------------------------+

.. ifconfig:: CONFIG_part_family in ('AM62PX_family')

   +-----------+----------------+-----------------------------------+
   | SoC       | n in CPSWng    | Number of Ports                   |
   +===========+================+===================================+
   | AM62P     | n = 3 (CPSW3g) | 3 (1 host port, 2 external ports) |
   +-----------+----------------+-----------------------------------+

The SDK provides support to use the CPSWng ports in two different
configurations:

#. CPSW Proxy Client
#. CPSWng Native Ethernet Switch

.. Caution::
   The two configurations are mutually exclusive. Only one of the two
   can be enabled for a build.

.. ifconfig:: CONFIG_part_family in ('J7_family')

   .. note::

      | Enabling the CPSW Proxy Client configuration or the CPSWng Native Ethernet configuration
      | requires applying a Linux device-tree overlay at U-Boot using the **name_overlays** U-Boot environment variable.
      | For details regarding applying CPSW Proxy Client overlay, refer :ref:`cpsw_proxy_client_enable`.
      | For details regarding applying CPSWng Native Ethernet overlay, refer :ref:`cpswng_native_eth_overlays`.


.. ifconfig:: CONFIG_part_family in ('AM62PX_family')

   .. note::

      | Enabling the CPSW Proxy Client configuration requires applying a Linux device-tree overlay
      | at U-Boot using the **name_overlays** U-Boot environment variable.
      | For details regarding applying CPSW Proxy Client overlay, refer :ref:`cpsw_proxy_client_enable`.

CPSW Proxy Client
"""""""""""""""""

In this configuration, the EthSwitch firmware running on one of the R5F cores
controls access to the CPSWng subsystem. The other cores have thin client
drivers running on them to receive data from the EthSwitch firmware. On the
A core running Linux, the cpsw-proxy-client driver is responsible for the
interaction with the EthSwitch firmware.

This configuration allows multiple cores to share the CPSWng ethernet subsystem.

For further details, refer :ref:`cpsw_proxy_client`

CPSWng Native Ethernet Switch
"""""""""""""""""""""""""""""

In this configuration, the am65-cpsw-nuss driver in Linux, takes complete
control of the CPSWng subsystem, allowing Linux to utilize all the external
ports of the CPSWng subsystem. Linux does not share any of the network traffic
with other cores.

This configuration supports MAC mode, Switch mode and TSN features on Linux.

.. ifconfig:: CONFIG_part_family in ('J7_family')

   For further details, refer :ref:`cpswng_native_ethernet`

.. ifconfig:: CONFIG_part_family in ('AM62PX_family')

   For further details, refer :ref:`cpsw3g`

.. toctree::
   :hidden:

   CPSW-Proxy-Client
   CPSWng-Native-Ethernet
