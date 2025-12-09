SERDES
######

.. contents:: :local:
   :depth: 3

Introduction
************

SERDES converts device (SoC) parallel data into serialized data that can be
output over a high-speed electrical interface. In the opposite direction,
SerDes converts high-speed serial data into parallel data that can be
processed by the device.

SERDES is used for transmitting/receiving data for PCIe, USB3, CPSW
(QSGMII, SGMII, USXGMII, XFI), eDP in K3 SoC.

.. Note::

   The following documentation describes the different PHY types (data rates)
   supported by the SERDES. While the SERDES might support a given protocol,
   it does not imply that the peripheral is capable of utilizing it. Please
   refer to the Technical Reference Manual for verifying hardware support for
   the peripheral. Refer to the peripheral driver documentation for verifying
   software support for the peripheral.

Types of SERDES
***************

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   The TI |__PART_FAMILY_NAME__| SoC has a 1 Lane SERDES.

   .. rubric:: *1 Lane Serdes*

   .. code-block:: text

                        ┌───────────────────┐
                        │                   │
                        │                   │
      <-> Peripheral IP1│                   │   <-> RX0/TX0
      ──────────────────┤     1L SERDES     ├────────────────
                        │                   │
                        │                   │
                        └───────────────────┘

.. ifconfig:: CONFIG_part_variant in ('J721E')

   There are two types of SERDES present in J721E:
      1) 2 Lane SERDES
      2) 4 Lane SERDES

   .. rubric:: *2 Lane Serdes*

   .. code-block:: text

                        ┌───────────────────┐
                        │                   │
                        │                   │
      <-> Peripheral IP1│                   │   <-> RX0/TX0
      ──────────────────┤                   ├────────────────
                        │                   │
                        │                   │
                        │                   │
                        │    2L SERDES      │
                        │                   │
                        │                   │
                        │                   │
      <-> Peripheral IP2│                   │   <-> RX1/TX1
      ──────────────────┤                   ├────────────────
                        │                   │
                        │                   │
                        │                   │
                        └───────────────────┘

.. ifconfig:: CONFIG_part_variant in ('J7200','J721S2','J784S4','J742S2')

   The TI |__PART_FAMILY_NAME__| SoC has a 4 Lane SERDES.

.. ifconfig:: CONFIG_part_variant in ('J721E','J7200','J721S2','J784S4','J742S2')

   .. rubric:: *4 Lane Serdes*

   .. code-block:: text

                        ┌───────────────────┐
      <-> Peripheral IP1│                   │   <-> RX0/TX0
      ──────────────────┤                   ├────────────────
                        │                   │
                        │                   │
      <-> Peripheral IP2│                   │   <-> RX1/TX1
      ──────────────────┤                   ├────────────────
                        │                   │
                        │    4L SERDES      │
      <-> Peripheral IP3│                   │   <-> RX2/TX2
      ──────────────────┤                   ├────────────────
                        │                   │
                        │                   │
      <-> Peripheral IP4│                   │   <-> RX3/TX3
      ──────────────────┤                   ├────────────────
                        │                   │
                        │                   │
                        └───────────────────┘

SERDES Configurations
*********************

This section lists the set of PHY types (data rates) that the SERDES can be
configured in, from the perspective of the SERDES driver and SERDES hardware
support. To enable the desired configuration, the SoC device-tree has to be
modified based on the instructions mentioned in the SERDES Muxing section.

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   .. rubric:: *Supported 1 Lane Serdes Configurations*

   The 1 Lane SERDES in AM64 SoC is configured by the Torrent Serdes kernel driver:

   .. code-block:: text

      drivers/phy/cadence/phy-cadence-torrent.c

   The possible Peripheral IP configurations that can be configured on the 1 Lane SERDES are:

   * EDP
   * PCIe
   * QSGMII
   * SGMII
   * USB
   * USXGMII

.. ifconfig:: CONFIG_part_variant in ('J721E','J7200','J721S2','J784S4','J742S2')

   A single SERDES can support either one protocol (connects to one Peripheral IP)
   or two protocols (connects to multiple Peripheral IP) at the same time.

   If a SERDES supports one protocol, it's called a single link PHY and
   if a SERDES supports two protocols, it's called multi-link PHY.
   Note that a single link PHY can comprise multiple lanes. For a
   multi-link PHY, the lanes can be split up in different ways but the
   only constraint is that the SERDES can support up to two protocols
   simultaneously.

   It's also not always necessary to use all the lanes of a SERDES and
   some lanes can be left unused.

.. ifconfig:: CONFIG_part_variant in ('J721E')

   .. rubric:: *Supported 2 Lane Serdes Configurations*

   The 2 Lane SERDES instances in J721E SoC are configured by the Sierra Serdes kernel driver:

   .. code-block:: text

      drivers/phy/cadence/phy-cadence-sierra.c

   The possible Peripheral IP configurations that can be configured on the 2 Lane SERDES are:

   Single Protocol Configurations:

   * PCIe
   * SGMII
   * USB

   Multi Protocol Configurations:

   * PCIe + QSGMII
   * PCIe + SGMII

.. ifconfig:: CONFIG_part_variant in ('J721E','J7200','J721S2','J784S4','J742S2')

   .. rubric:: *Supported 4 Lane Serdes Configurations*

   The 4 Lane SERDES instances in |__PART_FAMILY_NAME__| SoC are configured by the
   Torrent Serdes kernel driver:

   .. code-block:: text

      drivers/phy/cadence/phy-cadence-torrent.c

   The possible Peripheral IP configurations that can be configured on the 4 Lane SERDES are:

   Single Protocol Configurations:

   * EDP
   * PCIe
   * QSGMII
   * SGMII
   * USB
   * USXGMII

   Multi Protocol Configurations:

   * EDP + PCIe
   * EDP + USB
   * PCIe + QSGMII
   * PCIe + SGMII
   * PCIe + USB
   * PCIe + USXGMII
   * QSGMII + USB
   * QSGMII + USXGMII
   * SGMII + USB
   * SGMII + USXGMII

SERDES Instances
****************

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   AM64 SoC has a single instance of the 1 Lane Serdes.

.. ifconfig:: CONFIG_part_variant in ('J721E')

   J721E SoC has four instances of the 2 Lane SERDES and one instance of the 4 Lane Serdes.

.. ifconfig:: CONFIG_part_variant in ('J7200')

   J7200 SoC has a single instance of the 4 Lane Serdes.

.. ifconfig:: CONFIG_part_variant in ('J721S2')

   J721S2 SoC has a single instance of the 4 Lane Serdes.

.. ifconfig:: CONFIG_part_variant in ('J784S4')

   J784S4 SoC has four instances of the 4 Lane Serdes.

.. ifconfig:: CONFIG_part_variant in ('J742S2')

   J742S2 SoC has three instances of the 4 Lane Serdes.

SERDES Muxing
*************

SERDES Muxing refers to the process of selecting the mapping between the Peripheral
Lanes and the SERDES Lanes. A valid mapping refers to the process of selecting a
valid combination of Peripheral Lane and SERDES Lane based on the physical connections
available to choose from. Listed below is the valid set of combinations for the
SERDES instances.

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   .. rubric:: *SERDES 0*

   .. code-block:: text

                           ┌───────────────────┐
               PCIE0_LANE0/|                   │
                    USBSS0 │     1L SERDES     │   <-> RX0/TX0
         ──────────────────┤                   ├────────────────
                           │                   │
                           └───────────────────┘

.. ifconfig:: CONFIG_part_variant in ('J721E')

   .. rubric:: *SERDES 0*

   .. code-block:: text

                           ┌───────────────────┐
       CPSW0_Q/SGMII_LANE1/│                   │
               PCIE0_LANE0/│                   │
               USB3_0_SWAP │                   │   <-> RX0/TX0
         ──────────────────┤                   ├────────────────
                           │                   │
                           │    2L SERDES      │
       CPSW0_Q/SGMII_LANE2/│                   │
               PCIE0_LANE1/│                   │
                    USB3_0 │                   │   <-> RX1/TX1
         ──────────────────┤                   ├────────────────
                           │                   │
                           │                   │
                           └───────────────────┘

   .. rubric:: *SERDES 1*

   .. code-block:: text

                           ┌───────────────────┐
       CPSW0_Q/SGMII_LANE3/│                   │
               PCIE1_LANE0/│                   │
               USB3_1_SWAP/│                   │
        ICSSG1_SGMII_LANE0 │                   │   <-> RX0/TX0
         ──────────────────┤                   ├────────────────
                           │                   │
                           │    2L SERDES      │
       CPSW0_Q/SGMII_LANE4/│                   │
               PCIE1_LANE1/│                   │
                    USB3_1/│                   │
        ICSSG1_SGMII_LANE1 │                   │   <-> RX1/TX1
         ──────────────────┤                   ├────────────────
                           │                   │
                           │                   │
                           └───────────────────┘

   .. rubric:: *SERDES 2*

   .. code-block:: text

                           ┌───────────────────┐
               PCIE2_LANE0/│                   │
               USB3_1_SWAP/│                   │
        ICSSG1_SGMII_LANE0 │                   │   <-> RX0/TX0
         ──────────────────┤                   ├────────────────
                           │                   │
                           │    2L SERDES      │
               PCIE2_LANE1/│                   │
                    USB3_1/│                   │
        ICSSG1_SGMII_LANE1 │                   │   <-> RX1/TX1
         ──────────────────┤                   ├────────────────
                           │                   │
                           │                   │
                           └───────────────────┘

   .. rubric:: *SERDES 3*

   .. code-block:: text

                           ┌───────────────────┐
               PCIE3_LANE0/│                   │
               USB3_0_SWAP │                   │   <-> RX0/TX0
         ──────────────────┤                   ├────────────────
                           │                   │
                           │    2L SERDES      │
               PCIE3_LANE1/│                   │
                    USB3_0 │                   │   <-> RX1/TX1
         ──────────────────┤                   ├────────────────
                           │                   │
                           │                   │
                           └───────────────────┘

   .. rubric:: *SERDES 4*

   .. code-block:: text

                           ┌───────────────────┐
                 EDP_LANE0/│                   │
       CPSW0_Q/SGMII_LANE5 │                   │   <-> RX0/TX0
         ──────────────────┤                   ├────────────────
                           │                   │
                           │                   │
                 EDP_LANE1/│                   │
       CPSW0_Q/SGMII_LANE6 │                   │   <-> RX1/TX1
         ──────────────────┤                   ├────────────────
                           │                   │
                           │    4L SERDES      │
                 EDP_LANE2/│                   │
       CPSW0_Q/SGMII_LANE7 │                   │   <-> RX2/TX2
         ──────────────────┤                   ├────────────────
                           │                   │
                           │                   │
                 EDP_LANE3/│                   │
       CPSW0_Q/SGMII_LANE8 │                   │   <-> RX3/TX3
         ──────────────────┤                   ├────────────────
                           │                   │
                           └───────────────────┘

.. ifconfig:: CONFIG_part_variant in ('J7200')

   .. rubric:: *SERDES 0*

   .. code-block:: text

                           ┌───────────────────┐
       CPSW0_Q/SGMII_LANE3/|                   │
               PCIE1_LANE0 │                   │   <-> RX0/TX0
         ──────────────────┤                   ├────────────────
                           │                   │
                           │                   │
       CPSW0_Q/SGMII_LANE4/│                   │
               PCIE1_LANE1/│                   │
                      USB0 │                   │   <-> RX1/TX1
         ──────────────────┤                   ├────────────────
                           │                   │
                           │    4L SERDES      │
       CPSW0_Q/SGMII_LANE1/│                   │
               PCIE1_LANE2 │                   │   <-> RX2/TX2
         ──────────────────┤                   ├────────────────
                           │                   │
                           │                   │
       CPSW0_Q/SGMII_LANE2/│                   │
               PCIE1_LANE3/│                   │
                      USB0 │                   │   <-> RX3/TX3
         ──────────────────┤                   ├────────────────
                           │                   │
                           └───────────────────┘

.. ifconfig:: CONFIG_part_variant in ('J721S2')

   .. rubric:: *SERDES 0*

   .. code-block:: text

                           ┌───────────────────┐
                EDP0_LANE0/|                   │
               PCIE1_LANE0/|                   │
           HYPERLINK_LANE0 │                   │   <-> RX0/TX0
         ──────────────────┤                   ├────────────────
                           │                   │
                           │                   │
                EDP0_LANE1/|                   │
               PCIE1_LANE1/│                   │
                    USB3_0/│                   │
           HYPERLINK_LANE1 │                   │   <-> RX1/TX1
         ──────────────────┤                   ├────────────────
                           │                   │
                           │    4L SERDES      │
     EDP0_LANE2/EDP0_LANE0/|                   │
               PCIE1_LANE2/│                   │
           HYPERLINK_LANE2 │                   │   <-> RX2/TX2
         ──────────────────┤                   ├────────────────
                           │                   │
                           │                   │
     EDP0_LANE3/EDP0_LANE1/|                   │
               PCIE1_LANE3/│                   │
                    USB3_0/│                   │
           HYPERLINK_LANE3 │                   │   <-> RX3/TX3
         ──────────────────┤                   ├────────────────
                           │                   │
                           └───────────────────┘

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

   .. rubric:: *SERDES 0*

   .. code-block:: text

                           ┌───────────────────┐
                           |                   │
               PCIE1_LANE0/|                   │
           HYPERLINK_LANE0 │                   │   <-> RX0/TX0
         ──────────────────┤                   ├────────────────
                           │                   │
                           │                   │
               PCIE1_LANE1/|                   │
           HYPERLINK_LANE1 │                   │   <-> RX1/TX1
         ──────────────────┤                   ├────────────────
                           │                   │
                           │    4L SERDES      │
               PCIE3_LANE0/|                   │
               PCIE1_LANE2/│                   │
           HYPERLINK_LANE2 │                   │   <-> RX2/TX2
         ──────────────────┤                   ├────────────────
                           │                   │
                           │                   │
               PCIE3_LANE1/|                   │
               PCIE1_LANE3/│                   │
                    USB3_0/│                   │
           HYPERLINK_LANE3 │                   │   <-> RX3/TX3
         ──────────────────┤                   ├────────────────
                           │                   │
                           └───────────────────┘

   .. rubric:: *SERDES 1*

   .. code-block:: text

                           ┌───────────────────┐
                           |                   │
       CPSW0_Q/SGMII_LANE3/|                   │
               PCIE0_LANE0 │                   │   <-> RX0/TX0
         ──────────────────┤                   ├────────────────
                           │                   │
                           │                   │
       CPSW0_Q/SGMII_LANE4/|                   │
               PCIE0_LANE1 │                   │   <-> RX1/TX1
         ──────────────────┤                   ├────────────────
                           │                   │
                           │    4L SERDES      │
       CPSW0_Q/SGMII_LANE1/│                   │
               PCIE0_LANE2/|                   │
               PCIE2_LANE0 │                   │   <-> RX2/TX2
         ──────────────────┤                   ├────────────────
                           │                   │
                           │                   │
       CPSW0_Q/SGMII_LANE2/│                   │
               PCIE0_LANE3/|                   │
               PCIE2_LANE1 │                   │   <-> RX3/TX3
         ──────────────────┤                   ├────────────────
                           │                   │
                           └───────────────────┘

   .. ifconfig:: CONFIG_part_variant in ('J784S4')

      .. rubric:: *SERDES 2*

      .. code-block:: text

                              ┌───────────────────┐
                              |                   │
          CPSW0_Q/SGMII_LANE5 │                   │   <-> RX0/TX0
            ──────────────────┤                   ├────────────────
                              │                   │
                              │                   │
          CPSW0_Q/SGMII_LANE6 │                   │   <-> RX1/TX1
            ──────────────────┤                   ├────────────────
                              │                   │
                              │    4L SERDES      │
          CPSW0_Q/SGMII_LANE7/|                   │
          CPSW0_Q/SGMII_LANE1 │                   │   <-> RX2/TX2
            ──────────────────┤                   ├────────────────
                              │                   │
                              │                   │
          CPSW0_Q/SGMII_LANE8/│                   │
          CPSW0_Q/SGMII_LANE2 │                   │   <-> RX3/TX3
            ──────────────────┤                   ├────────────────
                              │                   │
                              └───────────────────┘

   .. rubric:: *SERDES 4*

   .. code-block:: text

                           ┌───────────────────┐
                EDP1_LANE0/|                   │
       CPSW0_Q/SGMII_LANE5/|                   │
           HYPERLINK_LANE0 │                   │   <-> RX0/TX0
         ──────────────────┤                   ├────────────────
                           │                   │
                EDP1_LANE1/|                   │
       CPSW0_Q/SGMII_LANE6/|                   │
           HYPERLINK_LANE1 │                   │   <-> RX1/TX1
         ──────────────────┤                   ├────────────────
                           │    4L SERDES      │
                EDP1_LANE2/|                   │
       CPSW0_Q/SGMII_LANE7/|                   │
           HYPERLINK_LANE2 │                   │   <-> RX2/TX2
         ──────────────────┤                   ├────────────────
                           │                   │
                EDP1_LANE3/|                   │
       CPSW0_Q/SGMII_LANE8/|                   │
                    USB3_0/|                   │
           HYPERLINK_LANE0 │                   │   <-> RX3/TX3
         ──────────────────┤                   ├────────────────
                           │                   │
                           └───────────────────┘

The Muxing configuration for each of the SERDES lanes can be described using
device tree. The device tree node labelled serdes_ln_ctrl corresponds to the
mux used to configure each of the SERDES lanes. The property "idle-states"
inside the serdes_ln_ctrl mux is used to specify the mapping between the
SERDES lane and the IP lane.

A valid mapping can be determined by referring to the SERDES muxing section
above. To select a mapping, the following format has to be used:

.. code-block:: text

   <SoC_SERDESw_LANEx_IPa_LANEb>

where:

* SoC is the name of the SoC,
* 'w' specifies the SERDES instance: SERDES0 for example,
* 'x' specifies the SERDES Lane: LANE0 for example,
* IP specifies the peripheral IP: PCIE for example,
* 'a' specifies the instance of that peripheral IP: PCIE0 for example,
* 'b' specifies the peripheral IP's Lane: LANE0 for example.

The mapping is interpret as follows:

*For the SoC named: SoC, SERDESw LANEx should be mapped to IPa LANEb.*

For unused Serdes lanes, indicate them using:

.. code-block:: text

   <SoC_SERDESw_LANEx_IPa_UNUSED>

.. rubric:: **Serdes Muxing Example**

Consider an SoC named SoCX with one 1L SERDES, one 2L SERDES and one 4L SERDES, with the
instances being SERDES0, SERDES1 and SERDES2. Additionally, let the SoC have PCIe instance
PCIE1, EDP instance EDP0 and a CPSW instance using QSGMII.

Then, to configure:

* SERDES0 Lane0 for PCIE1 Lane0
* SERDES1 Lane0 for EDP0 Lane2
* SERDES1 Lane1 for EDP0 Lane3
* SERDES2 Lane0 for QSGMII Lane3
* SERDES2 Lane1 for QSGMII Lane4
* SERDES2 Lane2 for QSGMII Lane1
* SERDES2 Lane3 for QSGMII Lane2

the device tree serdes_ln_ctrl node has to be defined as follows:

.. code-block:: text

   &serdes_ln_ctrl {
       idle-states = <SoCX_SERDES0_LANE0_PCIE1_LANE0>, <SoCX_SERDES1_LANE0_EDP0_LANE2>,
                     <SoCX_SERDES1_LANE1_EDP0_LANE3>, <SoCX_SERDES2_LANE0_QSGMII_LANE3>,
                     <SoCX_SERDES2_LANE1_QSGMII_LANE4>, <SoCX_SERDES2_LANE2_QSGMII_LANE1>
                     <SoCX_SERDES2_LANE3_QSGMII_LANE2>;
   };

.. rubric:: **Default Device Tree Muxing**

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   The AM642 board file k3-am642-evm.dts contains the following Serdes Muxing by default:

   .. code-block:: text

      &serdes_ln_ctrl {
          idle-states = <AM64_SERDES0_LANE0_PCIE0>;
      };

.. ifconfig:: CONFIG_part_variant in ('J721E')

   The J721E common processor board file k3-j721e-common-proc-board.dts contains the
   following Serdes Muxing by default:

   .. code-block:: text

      &serdes_ln_ctrl {
          idle-states = <J721E_SERDES0_LANE0_PCIE0_LANE0>, <J721E_SERDES0_LANE1_QSGMII_LANE2>,
                        <J721E_SERDES1_LANE0_PCIE1_LANE0>, <J721E_SERDES1_LANE1_PCIE1_LANE1>,
                        <J721E_SERDES2_LANE0_PCIE2_LANE0>, <J721E_SERDES2_LANE1_PCIE2_LANE1>,
                        <J721E_SERDES3_LANE0_USB3_0_SWAP>, <J721E_SERDES3_LANE1_USB3_0>,
                        <J721E_SERDES4_LANE0_EDP_LANE0>, <J721E_SERDES4_LANE1_EDP_LANE1>,
                        <J721E_SERDES4_LANE2_EDP_LANE2>, <J721E_SERDES4_LANE3_EDP_LANE3>;
      };

.. ifconfig:: CONFIG_part_variant in ('J7200')

   The J7200 common processor board file k3-j7200-common-proc-board.dts contains the
   following Serdes Muxing by default:

   .. code-block:: text

      &serdes_ln_ctrl {
          idle-states = <J7200_SERDES0_LANE0_PCIE1_LANE0>, <J7200_SERDES0_LANE1_PCIE1_LANE1>,
                        <J7200_SERDES0_LANE2_QSGMII_LANE1>, <J7200_SERDES0_LANE3_IP4_UNUSED>;
      };

.. ifconfig:: CONFIG_part_variant in ('J721S2')

   The J721S2 common processor board file k3-j721s2-common-proc-board.dts contains the
   following Serdes Muxing by default:

   .. code-block:: text

      &serdes_ln_ctrl {
          idle-states = <J721S2_SERDES0_LANE0_PCIE1_LANE0>, <J721S2_SERDES0_LANE1_USB>,
                        <J721S2_SERDES0_LANE2_EDP_LANE2>, <J721S2_SERDES0_LANE3_EDP_LANE3>;
      };

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

   .. ifconfig:: CONFIG_part_variant in ('J742S2')

      J742S2 is subset device of J784S4 and hence includes devicetree from j784s4, after which SERDES2 instance is removed.

   The J784S4 board file k3-j784s4-evm.dts contains the following Serdes Muxing by default:

   .. code-block:: text

      &serdes_ln_ctrl {
          idle-states = <J784S4_SERDES0_LANE0_PCIE1_LANE0>, <J784S4_SERDES0_LANE1_PCIE1_LANE1>,
                        <J784S4_SERDES0_LANE2_IP3_UNUSED>, <J784S4_SERDES0_LANE3_USB>,
                        <J784S4_SERDES1_LANE0_PCIE0_LANE0>, <J784S4_SERDES1_LANE1_PCIE0_LANE1>,
                        <J784S4_SERDES1_LANE2_PCIE0_LANE2>, <J784S4_SERDES1_LANE3_PCIE0_LANE3>,
                        <J784S4_SERDES2_LANE2_QSGMII_LANE1>, <J784S4_SERDES2_LANE3_QSGMII_LANE2>;
      };

The exact mux values to be programmed can be obtained from the dt-bindings include directory
of the kernel repository:

.. code-block:: text

   include/dt-bindings/mux/ti-serdes.h

The serdes_ln_ctrl based configuration uses the mux framework of Linux. More information can
be found in the Documentation of the kernel repository:

.. code-block:: text

   Documentation/devicetree/bindings/mux/mux-controller.yaml

SERDES Clocking Options
***********************

Each SERDES has PLLs inside it which have to be programmed to operate at different frequencies,
based on the data rate required by the Peripheral IP connected to the SERDES.

For example, based on the specification, the data rates for some of the Peripheral IPs are:

#. 8Gbps for PCIe GEN3
#. 5Gbps for PCIe GEN2
#. 2.5Gbps for PCIe GEN1
#. 5Gbps for USB3 SS
#. 5Gbps for QSGMII [CPSW Ethernet]

The input reference clocks connected to each SERDES are used to program the PLLs inside the SERDES.
The details regarding the PLL frequencies and programming is abstracted from the user. The user
only has to provide the reference clocks to be used by the SERDES for programming the PLLs, based
on the data rates required by the Peripheral IPs being used.

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   .. rubric:: *1L SERDES Clocking Options*

   The following illustration shows the clocking options for the 1L SERDES.

   .. code-block:: text

                                                   /|HFOSC0_CLKOUT
        ┌───────────────────────┐                 / ┌◄───────────────
        │                       │                 │ │
        │                       │                 │ │HFOSC1_CLKOUT
        │      ┌─────────┐      │ core_refclk     │ ├◄───────────────
        │      │  PLL0   │      │◄────────────────┤ │
        │      │         │      │                 │ │MAIN_PLL0_HSDIV8_CLKOUT (100/125 MHz)
        │      └─────────┘      │                 │ ├◄───────────────
        │                       │                 │ │
        │      ┌─────────┐      │                 │ │MAIN_PLL2_HSDIV4_CLKOUT (100 MHz)
        │      │  PLL1   │      │                 \ ├◄───────────────
        │      │         │      │                  \│
        │      └─────────┘      │ cmn_refclk
        │                       │◄─────────────────
        │                       │
        │      1L SERDES        │
        │                       │
        │                       │ ref_der_out_clock /
        │                       │ refclk_out
        │                       │─────────────────►
        └───────────────────────┘

   As seen in the figure above, 1L SERDES IP supports 2 clock inputs (core_refclk and cmn_refclk).
   core_refclk is the internal reference clock while the cmn_refclk is the external reference clock.

   For the clock IDs corresponding to the 1 Lane SERDES instances, refer:

   `1 Lane SERDES0 Clock IDs for AM64 <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/am64x/clocks.html#clocks-for-serdes-10g0-device>`_

.. ifconfig:: CONFIG_part_variant in ('J721E')

   .. rubric:: *2L SERDES Clocking Options*

   The following illustration shows the clocking options for the 2L SERDES.

   .. code-block:: text

                                                   /|HFOSC0_CLKOUT
        ┌───────────────────────┐                 / ┌◄───────────────
        │                       │                 │ │
        │                       │ core_refclk /   │ │HFOSC1_CLKOUT
        │      ┌─────────┐      │ core_refclk1    │ ├◄───────────────
        │      │  PLL0   │      │◄────────────────┤ │
        │      │         │      │                 │ │MAIN_PLL3_HSDIV4_CLKOUT (100/125/156.25 MHz)
        │      └─────────┘      │                 │ ├◄───────────────
        │                       │                 │ │
        │                       │                 │ │MAIN_PLL2_HSDIV4_CLKOUT (100 MHz)
        │                       │                 \ ├◄───────────────
        │      ┌─────────┐      │                  \│
        │      │  PLL1   │      │
        │      │         │      │ cmn_refclk
        │      └─────────┘      │◄─────────────────X Not Connected
        │                       │
        │                       │
        │                       │
        │                       │ cmn_refclk1
        │                       │◄───────────────── External Source (CLKGEN or Remote CLK)
        │      2L SERDES        │
        │                       │
        │                       │ ref_der_out_clock /
        │                       │ refclk1_out       ┌─────────┐
        │                       │─────────────────► │ ACSPCIE │
        └───────────────────────┘                   └─────────┘

   As seen in the figure above, 2L SERDES IP supports 4 clock inputs (core_refclk, core_refclk1,
   cmn_refclk, cmn_refclk1), of which cmn_refclk is not brought out of SoC). Thus, core_refclk
   and core_refclk1 should be used for internal reference clock while cmn_refclk1 can be used for external
   reference clock.

   For the clock IDs corresponding to the 2 Lane SERDES instances, refer:

   * `2 Lane SERDES0 Clock IDs for J721E <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/j721e/clocks.html#clocks-for-serdes-16g0-device>`_
   * `2 Lane SERDES1 Clock IDs for J721E <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/j721e/clocks.html#clocks-for-serdes-16g1-device>`_
   * `2 Lane SERDES2 Clock IDs for J721E <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/j721e/clocks.html#clocks-for-serdes-16g2-device>`_
   * `2 Lane SERDES3 Clock IDs for J721E <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/j721e/clocks.html#clocks-for-serdes-16g3-device>`_

.. ifconfig:: CONFIG_part_variant in ('J721E','J7200','J721S2','J784S4','J742S2')

   .. rubric:: *4L SERDES Clocking Options*

   The following illustration shows the clocking options for the 4L SERDES.

   .. code-block:: text

                                                   /|HFOSC0_CLKOUT
        ┌───────────────────────┐                 / ┌◄───────────────
        │                       │                 │ │
        │                       │                 │ │HFOSC1_CLKOUT
        │      ┌─────────┐      │ core_refclk     │ ├◄───────────────
        │      │  PLL0   │      │◄────────────────┤ │
        │      │         │      │                 │ │MAIN_PLL3_HSDIV4_CLKOUT (100/125/156.25 MHz)
        │      └─────────┘      │                 │ ├◄───────────────
        │                       │                 │ │
        │                       │                 │ │MAIN_PLL2_HSDIV4_CLKOUT (100 MHz)
        │                       │                 \ ├◄───────────────
        │      ┌─────────┐      │                  \│
        │      │  PLL1   │      │
        │      │         │      │ cmn_refclk
        │      └─────────┘      │◄─────────────────
        │                       │
        │                       │
        │      4L SERDES        │ refclk_out
        │                       │─────────────────►X Not Used
        │                       │
        │                       │
        └───────────────────────┘

   As seen in the figure above, 4L SERDES IP supports 2 clock inputs (core_refclk and cmn_refclk).
   The clock core_refclk is the internal reference clock while the clock cmn_refclk is the external
   reference clock. It also has an output reference clock which is not used (refclk_out).

   For the clock IDs corresponding to the 4 Lane SERDES instances, refer:

.. ifconfig:: CONFIG_part_variant in ('J721E')

   `4 Lane SERDES4 Clock IDs for J721E <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/j721e/clocks.html#clocks-for-serdes-10g0-device>`_

.. ifconfig:: CONFIG_part_variant in ('J7200')

   `4 Lane SERDES0 Clock IDs for J7200 <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/j7200/clocks.html#clocks-for-serdes-10g1-device>`_

.. ifconfig:: CONFIG_part_variant in ('J721S2')

   `4 Lane SERDES0 Clock IDs for J721S2 <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/j721s2/clocks.html#clocks-for-serdes-10g0-device>`_

.. ifconfig:: CONFIG_part_variant in ('J784S4')

   * `4 Lane SERDES0 Clock IDs for J784S4 <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/j784s4/clocks.html#clocks-for-serdes-10g0-device>`_
   * `4 Lane SERDES1 Clock IDs for J784S4 <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/j784s4/clocks.html#clocks-for-serdes-10g1-device>`_
   * `4 Lane SERDES2 Clock IDs for J784S4 <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/j784s4/clocks.html#clocks-for-serdes-10g2-device>`_
   * `4 Lane SERDES4 Clock IDs for J784S4 <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/j784s4/clocks.html#clocks-for-serdes-10g4-device>`_

.. ifconfig:: CONFIG_part_variant in ('J742S2')

   * `4 Lane SERDES0 Clock IDs for J742S2 <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/j784s4/clocks.html#clocks-for-serdes-10g0-device>`_
   * `4 Lane SERDES1 Clock IDs for J742S2 <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/j784s4/clocks.html#clocks-for-serdes-10g1-device>`_
   * `4 Lane SERDES4 Clock IDs for J742S2 <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/j784s4/clocks.html#clocks-for-serdes-10g4-device>`_

Internal Reference Clock
========================

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   In order to use internal reference clock, core_refclk input to 1L SERDES should be used.
   core_refclk can use one of the four inputs provided to the input-muxed clock.

   The WIZ wrapper allows selecting the input clock to be used for core_refclk.
   In the device-tree, within the WIZ parent node of the 1 Lane SERDES node, the following
   device-tree properties are used to configure the clocks:

   * "assigned-clocks" property is used to indicate the input-muxed clock corresponding to the
   core_refclk internal reference clock.
   * "assigned-clock-parents" property is used to indicate which of the 4 clock inputs to the
   input-muxed clock is to be selected and used for core_refclk.

   .. code-block:: text

      serdes_wiz0: wiz@f000000 {
               compatible = "ti,am64-wiz-16g";
               .
               .
               assigned-clocks = <&k3_clks 162 1>;
               assigned-clock-parents = <&k3_clks 162 5>;
               .
               .
      };

   In the above example, the WIZ node corresponding to the 1 Lane SERDES0 instance is shown.
   Within the WIZ node, using the "assigned-clocks" property, we are indicating that
   core_refclk receives its input from the clock identified by:

   .. code-block:: text

      <k3_clks 162 1>

   which is the input-muxed clock corresponding to core_refclk. The value 162 corresponds to
   the AM64X_DEV_SERDES_10G0 device, while the value 1 corresponds to DEV_SERDES_10G0_CORE_REF_CLK
   which is the input-muxed clock.

   The value of the "assigned-clock-parents" property corresponding to core_refclk is:

   .. code-block:: text

      <&k3_clks 162 5>

   which indicates that the clock with clock ID 5 (DEV_SERDES_10G0_CORE_REF_CLK_PARENT_HSDIV4_16FFT_MAIN_2_HSDIVOUT4_CLK)
   which is the MAIN_PLL2_HSDIV4_CLKOUT clock, is used as the core_refclk, via the input-muxed clock.

.. ifconfig:: CONFIG_part_variant in ('J721E')

   .. rubric:: *Internal Reference Clock (2 Lane Serdes)*

   In order to use internal reference clock, core_refclk and core_refclk1 inputs to 2L SERDES
   should be used. core_refclk and core_refclk1 can each use one of the four inputs provided
   to the input-muxed clock.

   The WIZ wrapper allows selecting the input clock to be used for core_refclk and core_refclk1.
   In the device-tree, within the WIZ parent node of the 2 Lane SERDES node, the following
   device-tree properties are used to configure the clocks:

   * "assigned-clocks" property is used to indicate the input-muxed clock corresponding to the
   core_refclk and core_refclk1 internal reference clocks.
   * "assigned-clock-parents" property is used to indicate which of the 4 clock inputs to the
   input-muxed clock is to be selected and used for core_refclk and core_refclk1.

   .. code-block:: text

      serdes_wiz0: wiz@5000000 {
               compatible = "ti,j721e-wiz-16g";
               .
               .
               assigned-clocks = <&k3_clks 292 11>, <&k3_clks 292 0>;
               assigned-clock-parents = <&k3_clks 292 15>, <&k3_clks 292 4>;
               .
               .
      };

   In the above example, the WIZ node corresponding to the 2 Lane SERDES0 instance is shown.
   Within the WIZ node, using the "assigned-clocks" property, we are indicating that
   core_refclk receives its input from the clock identified by:

   .. code-block:: text

      <k3_clks 292 11>

   which is the input-muxed clock corresponding to core_refclk. The value 292 corresponds to
   the J721E_DEV_SERDES_16G0 device, while the value 11 corresponds to DEV_SERDES_16G0_CORE_REF_CLK
   which is the input-muxed clock.

   Similarly, core_refclk1 is mapped to:

   .. code-block:: text

      <&k3_clks 292 0>

   with a similar pattern as core_refclk.

   The value of the "assigned-clock-parents" property corresponding to core_refclk is:

   .. code-block:: text

      <&k3_clks 292 15>

   which indicates that the clock with clock ID 15 (DEV_SERDES_16G0_CORE_REF_CLK_PARENT_HSDIV4_16FFT_MAIN_2_HSDIVOUT4_CLK)
   which is the MAIN_PLL2_HSDIV4_CLKOUT clock, is used as the core_refclk, via the input-muxed clock.
   Similar pattern is followed for core_refclk1's "assigned-clock-parents" property value.

.. ifconfig:: CONFIG_part_variant in ('J721E')

   .. rubric:: *Internal Reference Clock (4 Lane Serdes)*

.. ifconfig:: CONFIG_part_variant in ('J721E','J7200','J721S2','J784S4','J742S2')

   In order to use internal reference clock, core_refclk input to the 4L SERDES should be used.
   core_refclk can use one of the four inputs provided to the input-muxed clock.

   The WIZ wrapper allows selecting the input clock to be used for core_refclk.
   In the device-tree, within the WIZ parent node of the 4 Lane SERDES node, the following
   device-tree properties are used to configure the clocks:

   * "assigned-clocks" property is used to indicate the input-muxed clock corresponding to the
   core_refclk internal reference clock.
   * "assigned-clock-parents" property is used to indicate which of the 4 clock inputs to the
   input-muxed clock is to be selected and used for core_refclk.

.. ifconfig:: CONFIG_part_variant in ('J721E')

   .. code-block:: text

      serdes_wiz4: wiz@5050000 {
               compatible = "ti,j721e-wiz-10g";
               .
               .
               assigned-clocks = <&k3_clks 297 9>;
               assigned-clock-parents = <&k3_clks 297 10>;
               .
               .
      };

   In the above example, the WIZ node corresponding to the 4 Lane SERDES4 instance is shown.
   Within the WIZ node, using the "assigned-clocks" property, we are indicating that
   core_refclk receives its input from the clock identified by:

   .. code-block:: text

      <k3_clks 297 9>

   which is the input-muxed clock corresponding to core_refclk. The value 297 corresponds to
   the J721E_DEV_SERDES_10G0 device, while the value 9 corresponds to DEV_SERDES_10G0_CORE_REF_CLK
   which is the input-muxed clock.

   The value of the "assigned-clock-parents" property corresponding to core_refclk is:

   .. code-block:: text

      <&k3_clks 297 10>

   which indicates that the clock with clock ID 10 (DEV_SERDES_10G0_CORE_REF_CLK_PARENT_GLUELOGIC_HFOSC0_CLKOUT)
   which is the HFOSC0_CLKOUT clock has to be used as the core_refclk, via the input-muxed clock.

.. ifconfig:: CONFIG_part_variant in ('J7200')

   .. code-block:: text

      serdes_wiz0: wiz@5060000 {
               compatible = "ti,j7200-wiz-10g";
               .
               .
               assigned-clocks = <&k3_clks 292 85>;
               assigned-clock-parents = <&k3_clks 292 89>;
               .
               .
      };

   In the above example, the WIZ node corresponding to the 4 Lane SERDES0 instance is shown.
   Within the WIZ node, using the "assigned-clocks" property, we are indicating that
   core_refclk receives its input from the clock identified by:

   .. code-block:: text

      <k3_clks 292 85>

   which is the input-muxed clock corresponding to core_refclk. The value 292 corresponds to
   the J7200_DEV_SERDES_10G1 device, while the value 85 corresponds to DEV_SERDES_10G1_CORE_REF_CLK
   which is the input-muxed clock.

   The value of the "assigned-clock-parents" property corresponding to core_refclk is:

   .. code-block:: text

      <&k3_clks 292 89>

   which indicates that the clock with clock ID 89 (DEV_SERDES_10G1_CORE_REF_CLK_PARENT_HSDIV4_16FFT_MAIN_2_HSDIVOUT4_CLK)
   which is the MAIN_PLL2_HSDIV4_CLKOUT clock has to be used as the core_refclk, via the input-muxed clock.

.. ifconfig:: CONFIG_part_variant in ('J721S2')

   .. code-block:: text

      serdes_wiz0: wiz@5060000 {
               compatible = "ti,j721e-wiz-10g";
               .
               .
               assigned-clocks = <&k3_clks 365 3>;
               assigned-clock-parents = <&k3_clks 365 7>;
               .
               .
      };

   In the above example, the WIZ node corresponding to the 4 Lane SERDES0 instance is shown.
   Within the WIZ node, using the "assigned-clocks" property, we are indicating that
   core_refclk receives its input from the clock identified by:

   .. code-block:: text

      <k3_clks 365 3>

   which is the input-muxed clock corresponding to core_refclk. The value 365 corresponds to
   the J721S2_DEV_SERDES_10G0 device, while the value 3 corresponds to DEV_SERDES_10G0_CORE_REF_CLK
   which is the input-muxed clock.

   The value of the "assigned-clock-parents" property corresponding to core_refclk is:

   .. code-block:: text

      <&k3_clks 365 7>

   which indicates that the clock with clock ID 7 (DEV_SERDES_10G0_CORE_REF_CLK_PARENT_HSDIV4_16FFT_MAIN_2_HSDIVOUT4_CLK)
   which is the MAIN_PLL2_HSDIV4_CLKOUT clock has to be used as the core_refclk, via the input-muxed clock.

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

   .. code-block:: text

      serdes_wiz0: wiz@5060000 {
               compatible = "ti,j784s4-wiz-10g";
               .
               .
               assigned-clocks = <&k3_clks 404 6>;
               assigned-clock-parents = <&k3_clks 404 10>;
               .
               .
      };

   In the above example, the WIZ node corresponding to the 4 Lane SERDES0 instance is shown.
   Within the WIZ node, using the "assigned-clocks" property, we are indicating that
   core_refclk receives its input from the clock identified by:

   .. code-block:: text

      <k3_clks 404 6>

   which is the input-muxed clock corresponding to core_refclk. The value 404 corresponds to
   the J784S4_DEV_SERDES_10G0 device, while the value 6 corresponds to DEV_SERDES_10G0_CORE_REF_CLK
   which is the input-muxed clock.

   The value of the "assigned-clock-parents" property corresponding to core_refclk is:

   .. code-block:: text

      <&k3_clks 404 10>

   which indicates that the clock with clock ID 10 (DEV_SERDES_10G0_CORE_REF_CLK_PARENT_HSDIV4_16FFT_MAIN_2_HSDIVOUT4_CLK)
   which is the MAIN_PLL2_HSDIV4_CLKOUT clock has to be used as the core_refclk, via the input-muxed clock.

External Reference Clock
========================

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   The 1L SERDES IP supports one external reference clock input cmn_refclk (named as serdes_refclk
   in the device-tree).

   The external reference clock input is represented in the SoC device-tree file (k3-am64-main.dtsi)
   as shown below:

   .. code-block:: text

      / {
          serdes_refclk: serdes-refclk {
                  #clock-cells = <0>;
                  compatible = "fixed-clock";
                  clock-frequency = <0>;
          };
          .
          .
          .
      };

   Note that "clock-frequency = <0>;" is set to "0" since the external clocks need not always
   be connected, based on the board design.

.. ifconfig:: CONFIG_part_variant in ('J721E')

   .. rubric:: *External Reference Clock (2 Lane Serdes)*

   The 2L SERDES IP supports two external reference clock inputs. However the J721E SoC has only
   one external reference clock input connected (cmn_refclk1).

   The two external reference clock inputs are represented in the SoC device-tree file
   (k3-j721e-main.dtsi) as shown below:

   .. code-block:: text

      / {
          cmn_refclk: clock-cmnrefclk {
                  #clock-cells = <0>;
                  compatible = "fixed-clock";
                  clock-frequency = <0>;
          };

          cmn_refclk1: clock-cmnrefclk1 {
                  #clock-cells = <0>;
                  compatible = "fixed-clock";
                  clock-frequency = <0>;
          };
      };

   Note the "clock-frequency = <0>;" is set to "0" since the external clocks need not always
   be connected and is based on the board design. In the case of J721E CPB, CLKGEN provides
   100MHz clocks to these inputs. So the frequency is actually set in
   the board device-tree file (k3-j721e-common-proc-board.dts) as shown below:

   .. code-block:: text

      &cmn_refclk1 {
         clock-frequency = <100000000>;
      };

   .. rubric:: *External Reference Clock (4 Lane Serdes)*

   The 4L SERDES IP supports one external reference clock input (cmn_refclk).

   The external reference clock input is represented in the SoC device-tree file (k3-j721e-main.dtsi)
   as shown below:

   .. code-block:: text

      / {
          cmn_refclk: clock-cmnrefclk {
                  #clock-cells = <0>;
                  compatible = "fixed-clock";
                  clock-frequency = <0>;
          };
          .
          .
          .
      };

   Note that "clock-frequency = <0>;" is set to "0" since the external clocks need not always
   be connected, based on the board design.

.. ifconfig:: CONFIG_part_variant in ('J7200')

   The 4L SERDES IP supports one external reference clock input cmn_refclk (named as serdes_refclk
   in the device-tree).

   The external reference clock input is represented in the SoC device-tree file (k3-j7200-main.dtsi)
   as shown below:

   .. code-block:: text

      / {
          serdes_refclk: serdes-refclk {
                  #clock-cells = <0>;
                  compatible = "fixed-clock";
          };
          .
          .
          .
      };

.. ifconfig:: CONFIG_part_variant in ('J721S2')

   The 4L SERDES IP supports one external reference clock input cmn_refclk (named as serdes_refclk
   in the device-tree).

   The external reference clock input is represented in the SoC device-tree file (k3-j721s2-main.dtsi)
   as shown below:

   .. code-block:: text

      / {
          serdes_refclk: serdes-refclk {
                  #clock-cells = <0>;
                  compatible = "fixed-clock";
          };
          .
          .
          .
      };

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

   The 4L SERDES IP supports one external reference clock input cmn_refclk (named as serdes_refclk
   in the device-tree).

   The external reference clock input is represented in the SoC device-tree file (k3-j784s4-main.dtsi)
   as shown below:

   .. code-block:: text

      / {
          serdes_refclk: serdes-refclk {
                  #clock-cells = <0>;
                  compatible = "fixed-clock";
          };
          .
          .
          .
      };

Selecting Between Internal and External Reference Clock
=======================================================

The WIZ wrapper allows selecting between the internal and external clock to be used as the
input to PLL0 and PLL1 of the SERDES. Additionally, the reference clock to be used as input
for the digital logic of the SERDES PHY and PMA can also be selected.

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   It is possible to choose between the internal and external reference clocks for PLL0, PLL1
   and the digital reference clock. By default they are configured to use the internal
   reference clock in the k3-am64-main.dtsi SoC device-tree file:

   .. code-block:: text

           serdes0: serdes@f000000 {
               compatible = "ti,j721e-serdes-10g";
               .
               .
               .
               assigned-clocks = <&serdes_wiz0 TI_WIZ_PLL0_REFCLK>,
                                 <&serdes_wiz0 TI_WIZ_PLL1_REFCLK>,
                                 <&serdes_wiz0 TI_WIZ_REFCLK_DIG>;
               assigned-clock-parents = <&k3_clks 162 1>,
                                        <&k3_clks 162 1>,
                                        <&k3_clks 162 1>;
               .
               .
               .
           };

   For the example above corresponding to SERDES0 instance, the "assigned-clocks" property is
   used to indicate the clocks for PLL0, PLL1 and the digital reference clock respectively.

   The "assigned-clock-parents" property is used to indicate which of the clocks shall be used
   for each of PLL0, PLL1 and digital reference clocks as the input. Each of them have two
   reference clock inputs to choose from: internal clock (k3_clks) and external clock
   (serdes_refclk).

   The "assigned-clock-parents" by default sets the clock to internal clocks.

   For using the external reference clock, the "assigned-clock-parents" property has to be
   set to <&serdes_refclk>.

.. ifconfig:: CONFIG_part_variant in ('J721E')

   .. rubric:: *Selecting Between Internal and External Reference Clock (2 Lane Serdes)*

   Configuring the wizX_pll0_refclk, wizX_pll1_refclk and wizX_refclk_dig device-tree nodes for
   the SERDES instance SERDESX, it is possible to choose between the internal and external
   reference clocks for PLL0, PLL1 and the digital reference clock respecitvely. By default they
   are configured to use the internal reference clock in the k3-j721e-main.dtsi SoC device-tree
   file:

   .. code-block:: text

                wiz0_pll0_refclk: pll0-refclk {
                        clocks = <&k3_clks 292 11>, <&cmn_refclk>;
                        #clock-cells = <0>;
                        assigned-clocks = <&wiz0_pll0_refclk>;
                        assigned-clock-parents = <&k3_clks 292 11>;
                };

                wiz0_pll1_refclk: pll1-refclk {
                        clocks = <&k3_clks 292 0>, <&cmn_refclk1>;
                        #clock-cells = <0>;
                        assigned-clocks = <&wiz0_pll1_refclk>;
                        assigned-clock-parents = <&k3_clks 292 0>;
                };

                wiz0_refclk_dig: refclk-dig {
                        clocks = <&k3_clks 292 11>, <&k3_clks 292 0>, <&cmn_refclk>, <&cmn_refclk1>;
                        #clock-cells = <0>;
                        assigned-clocks = <&wiz0_refclk_dig>;
                        assigned-clock-parents = <&k3_clks 292 11>;
                };

   For the example above corresponding to SERDES0 instance, each of wiz0_pll0_refclk, wiz0_pll1_refclk
   and wiz0_refclk_dig have two reference clock inputs to choose from: internal clock (k3_clks) and
   external clock (cmn_refclk).

   The "assigned-clock-parents" by default sets the clock to internal clocks.

   However since in J721E Common Processor Board, there is an external clock generator which feeds
   both to the SERDES input and to the PCIe connector, in order to use common reference clock in
   PCIe RC mode, the inputs are configured to use external reference clock.

   For using the external reference clock, the below device-tree modifications are done in
   k3-j721e-common-proc-board.dts Board device-tree file:

   .. code-block:: text

        &wiz0_pll1_refclk {
            assigned-clocks = <&wiz0_pll1_refclk>;
            assigned-clock-parents = <&cmn_refclk1>;
        };

        &wiz0_refclk_dig {
            assigned-clocks = <&wiz0_refclk_dig>;
            assigned-clock-parents = <&cmn_refclk1>;
        };

        &serdes0 {
            assigned-clocks = <&serdes0 CDNS_SIERRA_PLL_CMNLC>, <&serdes0 CDNS_SIERRA_PLL_CMNLC1>;
            assigned-clock-parents = <&wiz0_pll1_refclk>, <&wiz0_pll1_refclk>;
        };

   Here "wiz0_pll1_refclk" is configured to use external reference clock "cmn_refclk1" and
   "wiz0_refclk_dig" is configured to use external reference clock "&cmn_refclk1"

   CDNS_SIERRA_PLL_CMNLC represents the PLL0 within SERDES and CDNS_SIERRA_PLL_CMNLC1 represents
   the PLL1 within SERDES. Since external clock is NOT connected to cmn_refclk (cmn_refclk is
   input to wiz0_pll0_refclk), PLL0 within SERDES cannot use wiz0_pll0_refclk. Hence both
   CDNS_SIERRA_PLL_CMNLC and CDNS_SIERRA_PLL_CMNLC1 are configured to use &wiz0_pll1_refclk.

   .. rubric:: *Selecting Between Internal and External Reference Clock (4 Lane Serdes)*

   Configuring the wiz4_pll0_refclk, wiz4_pll1_refclk and wiz4_refclk_dig device-tree nodes for
   the SERDES instance SERDES4, it is possible to choose between the internal and external
   reference clocks for PLL0, PLL1 and digital reference clock respectively. By default they are
   configured to use the internal reference clock in the k3-j721e-main.dtsi SoC device-tree file:

   .. code-block:: text

        wiz4_pll0_refclk: pll0-refclk {
                clocks = <&k3_clks 297 9>, <&cmn_refclk>;
                clock-output-names = "wiz4_pll0_refclk";
                #clock-cells = <0>;
                assigned-clocks = <&wiz4_pll0_refclk>;
                assigned-clock-parents = <&k3_clks 297 9>;
        };

        wiz4_pll1_refclk: pll1-refclk {
                clocks = <&k3_clks 297 9>, <&cmn_refclk>;
                clock-output-names = "wiz4_pll1_refclk";
                #clock-cells = <0>;
                assigned-clocks = <&wiz4_pll1_refclk>;
                assigned-clock-parents = <&k3_clks 297 9>;
        };

        wiz4_refclk_dig: refclk-dig {
                clocks = <&k3_clks 297 9>, <&cmn_refclk>;
                clock-output-names = "wiz4_refclk_dig";
                #clock-cells = <0>;
                assigned-clocks = <&wiz4_refclk_dig>;
                assigned-clock-parents = <&k3_clks 297 9>;
        };

   For the example above corresponding to SERDES4 instance, each of wiz4_pll0_refclk, wiz4_pll1_refclk
   and wiz4_refclk_dig have two reference clock inputs to choose from: internal clock (k3_clks) and
   external clock (cmn_refclk).

   The "assigned-clock-parents" by default sets the clock to internal clocks.

   For using the external reference clock, the "assigned-clock-parents" property has to be
   set to <&cmn_refclk>.

.. ifconfig:: CONFIG_part_variant in ('J7200')

   It is possible to choose between the internal and external reference clocks for PLL0, PLL1 and
   the digital reference clock. By default they are configured to use the internal reference clock in the k3-j7200-main.dtsi SoC device-tree file:

   .. code-block:: text

            serdes0: serdes@5060000 {
                compatible = "ti,j7200-serdes-10g";
                .
                .
                .
                assigned-clocks = <&serdes_wiz0 TI_WIZ_PLL0_REFCLK>,
                                  <&serdes_wiz0 TI_WIZ_PLL1_REFCLK>,
                                  <&serdes_wiz0 TI_WIZ_REFCLK_DIG>;
                assigned-clock-parents = <&k3_clks 292 85>,
                                         <&k3_clks 292 85>,
                                         <&k3_clks 292 85>;
                .
                .
                .
            };

   For the example above corresponding to SERDES0 instance, the "assigned-clocks" property is
   used to indicate the clocks for PLL0, PLL1 and the digital reference clock respectively.

   The "assigned-clock-parents" property is used to indicate which of the clocks shall be used
   for each of PLL0, PLL1 and digital reference clocks as the input. Each of them have two
   reference clock inputs to choose from: internal clock (k3_clks) and external clock
   (serdes_refclk).

   The "assigned-clock-parents" by default sets the clock to internal clocks.

   For using the external reference clock, the "assigned-clock-parents" property has to be
   set to <&serdes_refclk>.

.. ifconfig:: CONFIG_part_variant in ('J721S2')

   Configuring the wiz0_pll0_refclk, wiz0_pll1_refclk and wiz0_refclk_dig device-tree nodes for
   the SERDES instance SERDES0, it is possible to choose between the internal and external
   reference clocks for PLL0, PLL1 and digital reference clock respectively. By default they are
   configured to use the internal reference clock in the k3-j721s2-main.dtsi SoC device-tree file:

   .. code-block:: text

        wiz0_pll0_refclk: pll0-refclk {
                clocks = <&k3_clks 365 3>, <&serdes_refclk>;
                clock-output-names = "wiz0_pll0_refclk";
                #clock-cells = <0>;
                assigned-clocks = <&wiz0_pll0_refclk>;
                assigned-clock-parents = <&k3_clks 365 3>;
        };

        wiz0_pll1_refclk: pll1-refclk {
                clocks = <&k3_clks 365 3>, <&serdes_refclk>;
                clock-output-names = "wiz0_pll1_refclk";
                #clock-cells = <0>;
                assigned-clocks = <&wiz0_pll1_refclk>;
                assigned-clock-parents = <&k3_clks 365 3>;
        };

        wiz0_refclk_dig: refclk-dig {
                clocks = <&k3_clks 365 3>, <&serdes_refclk>;
                clock-output-names = "wiz0_refclk_dig";
                #clock-cells = <0>;
                assigned-clocks = <&wiz0_refclk_dig>;
                assigned-clock-parents = <&k3_clks 365 3>;
        };

   For the example above corresponding to SERDES0 instance, each of wiz0_pll0_refclk, wiz0_pll1_refclk
   and wiz0_refclk_dig have two reference clock inputs to choose from: internal clock (k3_clks) and
   external clock (serdes_refclk).

   The "assigned-clock-parents" by default sets the clock to internal clocks.

   For using the external reference clock, the "assigned-clock-parents" property has to be
   set to <&serdes_refclk>.

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

   It is possible to choose between the internal and external reference clocks for PLL0, PLL1 and
   the digital reference clock. By default they are configured to use the internal reference clock
   in the k3-j7200-main.dtsi SoC device-tree file:

   .. code-block:: text

            serdes0: serdes@5060000 {
                compatible = "ti,j7200-serdes-10g";
                .
                .
                .
                assigned-clocks = <&serdes_wiz0 TI_WIZ_PLL0_REFCLK>,
                                  <&serdes_wiz0 TI_WIZ_PLL1_REFCLK>,
                                  <&serdes_wiz0 TI_WIZ_REFCLK_DIG>;
                assigned-clock-parents = <&k3_clks 404 6>,
                                         <&k3_clks 404 6>,
                                         <&k3_clks 404 6>;
                .
                .
                .
            };

   For the example above corresponding to SERDES0 instance, the "assigned-clocks" property is
   used to indicate the clocks for PLL0, PLL1 and the digital reference clock respectively.

   The "assigned-clock-parents" property is used to indicate which of the clocks shall be used
   for each of PLL0, PLL1 and digital reference clocks as the input. Each of them have two
   reference clock inputs to choose from: internal clock (k3_clks) and external clock
   (serdes_refclk).

   The "assigned-clock-parents" by default sets the clock to internal clocks.

   For using the external reference clock, the "assigned-clock-parents" property has to be
   set to <&serdes_refclk>.

.. ifconfig:: CONFIG_part_variant in ('J721E')

   .. rubric:: **Special Case CPSW9G (PCIe + QSGMII)**

   In the J721E Common Processor Board (for J721E SoC), the 1st SERDES instance is shared between
   PCIe and CPSW9G (1L for PCIe and 1L for CPSW). Since CPSW is configured and used by Ethernet
   Firmware and PCIe is configured and used by Linux, SERDES configuration for this instance
   has to be done before loading ethernet firmware and Linux. Hence the shared SERDES
   configuration is done in u-boot. Since by default firmwares are not loaded in u-boot and
   there is no way to configure only the external PHY in Linux, the QSGMII PHY (VSC8514) in
   Quad Port Add-On Ethernet Card has to be brought out of reset in u-boot.

   The following command should be used to bring the external PHY out of reset

   .. code-block:: text

      setenv dorprocboot 1

   .. rubric:: **Driving Clock Out**

   Support for driving clock out via ACSPCIE using ref_der_out_clock/refclk1_out is not present
   in SDK.

.. ifconfig:: CONFIG_part_variant in ('J721S2')

   .. rubric:: *EDP Muxing Configuration*

   The following shows the default SERDES configuration for
   the J721S2 common processor board.

   .. code-block:: text

        &serdes_ln_ctrl {
            idle-states = <J721S2_SERDES0_LANE0_PCIE1_LANE0>, <J721S2_SERDES0_LANE1_USB>,
                      <J721S2_SERDES0_LANE2_EDP_LANE2>, <J721S2_SERDES0_LANE3_EDP_LANE3>;
        };

        &edp_serdes_mux {
            idle-states = <1>; /* EDP0 to SERDES lane 2/3 /
        };

   Additional edp mux configuration as shown above, is required to use serdes lane 2 and 3 for edp

   .. rubric:: *Serdes limitation in J721S2*

   - Only 2 IPs can share serdes at a time, below are the possible option

      - USB + PCIe
      - EDP + PCIe (Default SDK combination)
      - EDP + USB (https://git.ti.com/cgit/ti-linux-kernel/ti-upstream-tools/tree/arch/arm64/boot/dts/ti/k3-j721s2-usb3.dtso?h=ti-linux-5.10.y)

   By default EDP + PCIe is enabled for J721S2 common processor board, USB
   is enabled in high speed mode which does not use serdes

   - Serdes can not be shared between RTOS and linux (SW limitation). Currently all
     configuration for serdes sharing is done in linux driver, if serdes is
     used in RTOS running in mcu cores it can not be used in linux
