.. _industrial-protocols-hsr-prp:

**********************************
HSR_PRP
**********************************

Protocol Overview
=================================
.. include:: ../common/Industrial_Protocols/HSR_PRP/_Protocol_Overview.rst

Getting Started
===============

To try out HSR/PRP (assuming two supported platforms are set up already,
and PRU-ICSS ports are eth1/eth2):

1 ) Connect the PRU-ICSS ports between devices, eth1 to eth1 and eth2 to eth2.
(This acts as a 2 node ring for HSR, or a 2 node point-to-point for PRP)

2 ) Configure ports to have the same MAC address

::

    ifconfig eth1 0.0.0.0 down && ifconfig eth2 0.0.0.0 down
    ifconfig eth1 hw ether 70:FF:76:1C:0E:8C && ifconfig eth2 hw ether 70:FF:76:1C:0E:8C

3 ) Configure offload feature, and create HSR/PRP interface

(for HSR)

::

    ethtool -K eth1 hsr-rx-offload on && ethtool -K eth2 hsr-rx-offload on
    ifconfig eth1 up && ifconfig eth2 up
    ip link add name hsr0 type hsr slave1 eth1 slave2 eth2 supervision 45 version 1
    ifconfig hsr0 192.168.2.20

(for PRP)

::

    ethtool -K eth1 prp-rx-offload on && ethtool -K eth2 prp-rx-offload on
    ifconfig eth1 up && ifconfig eth2 up
    ip link add name prp0 type hsr slave1 eth1 slave2 eth2 supervision 45 proto 1
    ifconfig prp0 192.168.2.20

4 ) Attempt to ping from one device to the other, and try disconnecting a link.
The connection will continue without loss.


ICSS Firmware
=================================
.. Firmware features
.. include:: ../common/Industrial_Protocols/HSR_PRP/_Firmware_Features.rst

.. include:: ../common/Industrial_Protocols/HSR_PRP/_Firmware.rst

Linux Software
=================================
.. include:: Industrial_Protocols/HSR_PRP/_HSR_PRP_for_Linux.rst
