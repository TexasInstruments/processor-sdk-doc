.. _tsn_with_cpsw:

==============
TSN with CPSW
==============

.. contents:: :local:
   :depth: 3

Introduction
============

TI Common Platform Ethernet Switch (CPSW) supports TSN features such as:

1. PTP (Precision Time Protocol) [IEEE-1588, IEEE-802.1AS]
2. EST (Enhancements for Scheduled Traffic) [IEEE-802.1Qbv]
3. FQTSS / CBS (Credit Based Shaper) [IEEE-802.1Qav]
4. IET (Interspersing Express Traffic) [IEEE-802.3br, IEEE-802.1Qbu]

.. note::
   All TSN features require CONFIG_TI_AM65_CPTS to be enabled.

.. note::
   Switch based TSN features are supported only with CPSWxg for x >= 3.

Documentation and Testing
=========================

The documentation for each of the TSN features along with the tests are
present at:

.. toctree::
   :maxdepth: 1

   CPSW-PTP
   CPSW-EST
   CPSW-CBS
   CPSW-IET

Testing Details
================

- The tests have been performed on TI's J7VCL with CPSW5G in QSGMII/SGMII modes and on TI's AM625-SK with CPSW3G in RGMII mode.

- TI's AM64-SK with CPSW3G in RGMII mode has been used to assist in the testing process.

- TSN testing has been done in MAC mode as well as SWITCH mode.

- The test setup and the scripts are documented in this page to help replicate the tests with appropriate changes if required.

- The outputs for each of the performed tests have also been documented.

- **For all the tests, CONFIG_TI_K3_AM65_CPTS has to be enabled in kernel config.**

- For tuning the TSN features in Switch Mode, refer :ref:`tsn_tuning`

.. toctree::
   :hidden:

   CPSW-TSN-Tuning
