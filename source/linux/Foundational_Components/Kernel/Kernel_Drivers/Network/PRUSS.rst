.. http://processors.wiki.ti.com/index.php/Linux_Core_PRUSS_Ethernet_User%27s_Guide

PRUSS
---------------------------------

.. rubric:: **Introduction**
   :name: introduction-linux-pruss-ethernet-ug

All the Industrial Development Kit (IDK) boards can support 2 Ethernet
ports per PRUSS (Programmable Real-time Unit Subsystem). Although it is
meant to support real-time Industrial Ethernet protocols this wiki page
will only describe how to get standard Ethernet working using the
Kernel's PRU Ethernet driver.

.. rubric:: **Acronyms & definitions**

+-----------+-------------------------------+
| Acronym   | Definition                    |
+===========+===============================+
| IDK       | Industrial Development Kit    |
+-----------+-------------------------------+
| PRU       | Programmable Real-time Unit   |
+-----------+-------------------------------+

Table:  **PRU Ethernet Driver: Acronyms**

.. rubric:: **PRU Ethernet Driver Architecture**
   :name: pru-ethernet-driver-architecture

Below figure shows the PRU Ethernet Driver architecture.

.. Image:: /images/PRU_ethernet_architecture.png

.. rubric:: **Overview**
   :name: overview-kernel-core-pruss

Each PRUSS instance contains 2 PRU cores and 2 Ethernet PHY interfaces.
This means that each PRU core can fully own one Ethernet port allowing
us to create a dual Ethernet solution. The firmware running on each PRU
implements the Ethernet MAC application. It uses the System OCMC RAM to
exchange network packets between firmware and PRU Ethernet kernel
driver.

Before the PRU Ethernet kernel driver can start transferring packets,
the following things have to be done:

-  Initialize the PRU cores and load the correct formware. This is taken
   care by the Remoteproc core via the PRU Remoteproc driver
   (pru\_rproc.c).
-  Initialize the PRUSS Interrupt Controller (INTC) and configure the
   interrupt mapping as per firmware requirement. This is done by the
   PRUSS INTC driver (pruss\_intc.c).
-  Initialize the Ethernet PHYs over the MDIO interface. This is done by
   the PHY MDIO driver (davinci\_mdio.c).

Once all initialization is done the PRU Ethernet driver (prueth.c) takes
over and interfaces with the firmware using PRUSS internal RAM (DRAM &
SRAM) and the System OCMC RAM. It also interfaces to the Linux
Networking stack to provide the standard networking interface to user
space.

.. rubric:: **Files**
   :name: files

+--------+-------------------------------------------+-------------------------+
| S.No   | Location                                  | Description             |
+========+===========================================+=========================+
| 1      | drivers/net/ethernet/ti/icssm             | PRU Ethernet driver     |
+--------+-------------------------------------------+-------------------------+
| 2      | drivers/remoteproc/pruss.c                | PRUSS core driver       |
+--------+-------------------------------------------+-------------------------+
| 3      | drivers/remoteproc/pruss\_intc.c          | PRUSS INTC driver       |
+--------+-------------------------------------------+-------------------------+
| 4      | drivers/remoteproc/pru\_rproc.c           | PRU Remoteproc driver   |
+--------+-------------------------------------------+-------------------------+
| 5      | drivers/net/ethernet/ti/davinci\_mdio.c   | PHY MDIO driver         |
+--------+-------------------------------------------+-------------------------+
| 6      | lib/firmware/ti-pruss/                    | Firmware                |
+--------+-------------------------------------------+-------------------------+

.. rubric:: **Board specific Setup Details**
   :name: board-specific-setup-details

.. ifconfig:: CONFIG_part_variant in ('AM335X')

   This board has only 2 Ethernet ports that can be used either as CPSW
   Ethernet or PRUSS Ethernet. For PRUSS Ethernet configration place
   jumpers J18 and J19 at MII position before powering up the board.

.. ifconfig:: CONFIG_part_variant in ('AM437X')

   This board as one Gigabit (CPSW) Ethernert port and 2 PRUSS Ethernet
   ports. No special board configuration is needed to use all ports.

.. ifconfig:: CONFIG_part_variant in ('AM57X')

   .. rubric:: AM571x-IDK
      :name: am571x-idk

   This board has 2 Gigabit (CPSW) Ethernet ports and 4 PRUSS Ethernet
   ports. Due to pinmux limitations it can support either of the following
   configurations

   -  Jumper J51 placed. LCD + 2 Gigabit (CPSW) + 2 PRUSS Ethernet ports
      (PRU2\_ETH0 and PRU2\_ETH1)

   **OR**

   -  Jumper J51 removed. No LCD, 2 Gigabit (CPSW) + 4 PRUSS Ethernet
      ports.

   NOTE: Jumper must be configured before powering up the board.

   .. rubric:: AM572x-IDK
      :name: am572x-idk

   This board has 2 Gigabit (CPSW) Ethernet ports and 4 PRUSS Ethernet
   ports. However, only 2 Gigabit + 2 PRUSS Ethernet ports (PRU2\_ETH0 and
   PRU2\_ETH1) are supported due to pinmux limitations.

   NOTE: Only ES2.0 silicon (Board Rev1.3 or later) is supported as older
   Silicon uses a older version of PRUSS core that is not compatible with
   the supplied firmware.

.. rubric:: Kernel configuration
   :name: kernel-configuration

To enable/disable PRU Ethernet driver support, start the Linux Kernel Configuration tool:

::

    $ make menuconfig ARCH=arm

Make sure Remoteproc and PRUSS core driver is enabled.

Select Device drivers from the main menu.

::

        ...
        [*] Networking support --->
        Device Drivers -->
        File systems --->
        ...

Select Remoteproc drivers.

::

        ...
        [*] IOMMU Hardware Support  --->
        Remoteproc drivers  --->
        Rpmsg drivers  --->
        ...

Enable the below drivers.

::

        ...
        <M> Support for Remote Processor subsystem
        <M>   TI PRUSS remoteproc support
        <M>   Keystone Remoteproc support
        ...

Go back to the Device drivers menu Network device support.

::

        ...
        IEEE 1394 (FireWire) support  --->
        [*] Network device support  --->
        [ ] Open-Channel SSD target support  ----
        ...

Select Ethernet driver support.

::

        ...
        Distributed Switch Architecture drivers  ----
        [*]   Ethernet driver support  --->
        < >   FDDI driver support
        ...

Select TI PRU Ethernet driver.

::

        ...
        < >     TI ThunderLAN support
        <M>     TI PRU Ethernet EMAC/Switch driver
        [ ]   VIA devices
        ...

.. rubric:: **Driver Usage & Testing**
   :name: driver-usage-testing

You can use standard Linux networking tools to test the networking
interface (e.g. ifconfig, ping, iperf, scp, ethtool, etc)

