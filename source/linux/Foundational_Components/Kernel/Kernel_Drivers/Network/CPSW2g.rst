.. _cpsw2g:

CPSW2g Ethernet
---------------

.. contents:: :local:
   :depth: 3

Introduction
============

The TI |__PART_FAMILY_NAME__| SoC has integrated two-port Gigabit Ethernet Switch subsystem
with selectable RGMII and RMII interfaces and an internal Communications
Port Programming Interface (CPPI) port (Host port 0). Host Port 0 CPPI Packet
Streaming Interface interface supports 8 TX channels and one RX channel
operating by TI |__PART_FAMILY_NAME__| NAVSS Unified DMA Peripheral Root Complex (UDMA-P) controller.

The driver follows the standard Linux network interface architecture and
supports the following features:

#. 10/100/1000 Mbps mode of operation.
#. Auto negotiation.
#. Linux NAPI support
#. VLAN filtering
#. Ethertool
#. CPTS/PTP as per 802.1AS-2011 (TSN)
#. EST/TAS offload as per 802.1Q-2018 (TSN)
#. IET/preemption offload as per 802.1Q-2018 (TSN)
#. Forwarding and Queuing Enhancements for Time-Sensitive Streams (FQTSS) as per 802.1Q-2018 previously referred to as CBS or 802.1Qav

Supported platforms
"""""""""""""""""""

+-----------+-------------------------------+--------------------+
| SoC       | Number of external ports      | Instances - Domain |
+===========+===============================+====================+
| J721e     | 1 external port (CPSW2g)      | 1 - MCU            |
+-----------+-------------------------------+--------------------+
| J7200     | 1 external port (CPSW2g)      | 1 - MCU            |
+-----------+-------------------------------+--------------------+
| J721S2    | 1 external port (CPSW2g)      | 2 - MAIN, MCU      |
+-----------+-------------------------------+--------------------+
| J784S4    | 1 external port (CPSW2g)      | 2 - MAIN, MCU      |
+-----------+-------------------------------+--------------------+

Driver Configuration
====================

The TI Processor SDK has |__PART_FAMILY_NAME__| CPSW2g driver enabled by default.
In case of custom builds, please ensure following configs are enabled.

.. code:: Kconfig

   CONFIG_TI_DAVINCI_MDIO
   CONFIG_TI_K3_AM65_CPSW_NUSS
   CONFIG_TI_K3_AM65_CPTS
   CONFIG_TI_AM65_CPSW_TAS
   CONFIG_PHY_TI_GMII_SEL

For further details regarding the above configs, refer:
#. drivers/net/ethernet/ti/Kconfig
#. drivers/phy/ti/Kconfig

.. rubric:: **Module Build**
   :name: k3-module-build

Module build for the cpsw driver is supported. To do this, use option 'm' for above configs, where applicable.

Device tree bindings
====================

The DT bindings description can be found at:

|   `Documentation/devicetree/bindings/net/ti,k3-am654-cpsw-nuss.yaml <https://git.ti.com/ti-linux-kernel/ti-linux-kernel/blobs/ti-linux-6.6.y/Documentation/devicetree/bindings/net/ti,k3-am654-cpsw-nuss.yaml>`__

|   `Documentation/devicetree/bindings/net/ti,k3-am654-cpts.yaml <https://git.ti.com/ti-linux-kernel/ti-linux-kernel/blobs/ti-linux-6.6.y/Documentation/devicetree/bindings/net/ti,k3-am654-cpts.yaml>`__
|

MAC mode
========

.. include:: _K3-CPSW-common.rst
   :parser: rst
