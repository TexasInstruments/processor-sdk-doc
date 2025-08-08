CPSW Ethernet
-------------

.. contents:: :local:
   :depth: 1

Introduction
""""""""""""

The CPSW Ethernet Subsystem is capable of supporting MAC mode, Switch mode, VLAN and the
standard TSN features such as PTP, EST, CBS and IET.

.. note::

   To operate in switch mode, at least two external ports are required.

Instances of the CPSW Subsystem
""""""""""""""""""""""""""""""""

The TI |__PART_FAMILY_DEVICE_NAMES__| family of devices contain the following instances
of the CPSW Ethernet Subsystem:

.. ifconfig:: CONFIG_part_family in ('J7_family')

   1. CPSW2g

.. ifconfig:: CONFIG_part_variant in ('J721E','J7200','J784S4','J742S2')

   2. CPSWng

.. ifconfig:: CONFIG_part_family in ('J7_family')

   The CPSW2g instance is controlled by the am65-cpsw-nuss driver in Linux.
   For further details regarding the CPSW2g instance, refer :ref:`cpsw2g`

.. ifconfig:: CONFIG_part_variant in ('J721E','J7200','J784S4','J742S2')

   The CPSWng instance can be configured to operate in two ways:
      #. CPSWng Virtual Client
      #. CPSWng Native Ethernet

   For further details regarding the CPSWng instance, refer :ref:`cpswng`

.. ifconfig:: CONFIG_part_family in ('AM62X_family','AM62AX_family','AM62DX_family','AM64X_family','AM62LX_family')

   CPSW3g

   The CPSW3g instance is a part of the Main domain and is controlled by the am65-cpsw-nuss
   driver in Linux.
   For further details regarding the CPSW3g instance, refer :ref:`cpsw3g`

.. ifconfig:: CONFIG_part_family in ('AM62PX_family')

   CPSW3g

   The CPSW3g instance can be configured to operate in two ways:
      #. CPSW3g Virtual Client
      #. CPSW3g Native Ethernet

   To generalize, CPSW3g instance can be referred to as CPSWng with 'n' being '3'.
   For further details regarding the CPSW3g instance, refer :ref:`cpswng`

TSN Documentation and Testing
""""""""""""""""""""""""""""""

The CPSW Ethernet Subsystem supports TSN features in the following configurations:

.. ifconfig:: CONFIG_part_family in ('J7_family')

   1. The CPSW2g instance supports MAC mode TSN features.

.. ifconfig:: CONFIG_part_variant in ('J721E','J7200','J784S4','J742S2')

   2. The CPSWng Native Ethernet configuration of the CPSWng instance supports both MAC mode
      and Switch mode TSN features with Linux.

.. ifconfig:: CONFIG_part_family in ('AM62X_family','AM62AX_family','AM62DX_family','AM64X_family','AM62PX_family','AM62LX_family')

   The CPSW3g instance supports MAC mode and Switch mode TSN features with Linux.

For further details regarding the TSN features and testing, refer :ref:`tsn_with_cpsw`

.. toctree::
   :hidden:

   CPSW2g
   CPSW3g
   CPSWng
   CPSW-TSN
