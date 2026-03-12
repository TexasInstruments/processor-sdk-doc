.. http://processors.wiki.ti.com/index.php/Linux_Core_MCAN_User%27s_Guide

.. _mcan:

MCAN
----

.. rubric:: **Introduction**
   :name: introduction

The Controller Area Network is a serial communications protocol which
efficiently supports distributed real-time control with a high level of
security. The MCAN module supports bitrates up to 5 Mbit/s and is
compliant to the ISO 11898-1:2015. The core IP within M\_CAN is provided
by Bosch.

This wiki page provides usage information of M\_CAN Linux driver.

.. rubric:: **Setup Details**
   :name: setup-details

.. rubric:: **TI board List**
   :name: ti-board-list

+----------+---------+-----------------------+-------------------+----------------------+
| SoC      | Board   | Number of Instances   | Connection Type   | Enabled by default   |
+==========+=========+=======================+===================+======================+
| Dra76x   | EVM     | 1                     | Header            | Yes                  |
+----------+---------+-----------------------+-------------------+----------------------+
| AM654x   | IDK     | 2                     | DB9               | Yes                  |
+----------+---------+-----------------------+-------------------+----------------------+
| AM64x    | EVM     | 2                     | Header            | Yes                  |
+----------+---------+-----------------------+-------------------+----------------------+
| AM62x    | SK      | 3                     | Header            | No                   |
+----------+---------+-----------------------+-------------------+----------------------+
| AM68     | SK      | 4                     | Header            | Yes                  |
+----------+---------+-----------------------+-------------------+----------------------+
| AM69     | SK      | 4                     | Header            | Yes                  |
+----------+---------+-----------------------+-------------------+----------------------+
| J721E    | SK      | 4                     | Header            | Yes                  |
+----------+---------+-----------------------+-------------------+----------------------+
| J721E    | EVM     | 4                     | Header            | Yes                  |
+----------+---------+-----------------------+-------------------+----------------------+
| J7200    | EVM     | 4                     | Header            | Yes                  |
+----------+---------+-----------------------+-------------------+----------------------+
| J721S2   | EVM     | 5                     | Header            | Yes                  |
+----------+---------+-----------------------+-------------------+----------------------+
| J784S4   | EVM     | 6                     | Header            | Yes                  |
+----------+---------+-----------------------+-------------------+----------------------+
| J722S    | EVM     | 3                     | Header            | Yes                  |
+----------+---------+-----------------------+-------------------+----------------------+

Table:  Boards M\_CAN Driver is Validated on

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   **Notice for AM62x:**

   The AM62x SK does not carry a transciever to experiment with. The SoC does support CAN-FD, but it is required to connect a CAN external
   transceiver to the AM62x SK to test the full CAN functionality. Go to the following guide: :ref:`mcan-on-am62x` for an example
   for connecting a CAN external transceiver to the AM62x SK.

.. ifconfig:: CONFIG_part_variant not in ('AM62X')

   .. rubric:: **Connection Configuration**
      :name: connection-configuration

   +------------------------------------------------+------------------------------------------------------+
   | .. Image:: /images/mcan-diagram-evm-to-evm.png | .. Image:: /images/Dcan_header_to_db9.png            |
   +------------------------------------------------+------------------------------------------------------+
   | Header to Header                               | Header to DB9                                        |
   +------------------------------------------------+------------------------------------------------------+


   Table:  Various MCAN EVM Connection Configuration

   .. rubric:: **Equipment**
      :name: equipment

   .. rubric:: **Female DB9 Cable**
      :name: female-db9-cable

   For boards exposing M\_CAN using male DB9 connectors, a female connector
   is required. The other side can be male or female depending on the other
   CAN device the user connects to.

   .. Image:: /images/DB9_cable.jpg
      :scale: 50%
      :align: center


   .. rubric:: **Jumper Wires**
      :name: jumper-wires

   For boards where the CAN pins are broken out via a header, female jumper
   cables will be ideal for connection. The CAN pins will be CAN H
   (typically pin 1 of the header), GND (middle pin of the header) and CAN
   L (lowest pin on the header). The pinout in the header might vary across
   different boards and users must consult the board's schematic to verify
   this.

   .. Image:: /images/Female_to_female_jumper.png
      :scale: 20%
      :align: center


   .. rubric:: **Custom DB9 to Header Cable**
      :name: custom-db9-to-header-cable

   Typically CAN devices use a DB9 connection therefore for boards whose
   CAN pins are broken out via a header it is helpful to create a header to
   DB9 connector cable. This custom cable is simple to make. Either a male
   or female DB9 connector (not cable) must be obtained along with three
   female jumper wires.

   Snip one end of each of the jumper wires and expose some of the wiring.
   Now solder each of the exposed wires to pin 7 (CAN H), pin 2 (CAN L) and
   pin 3 (GND). Make sure your soldering on the side of the DB9 that has
   the metal lip meant to push some of the exposed wire into and soldering
   to the correct pins correctly. Use the below diagram as a reference.

   +-------------------------------------------------------------+------------------------------------------------+
   | .. Image:: /images/DCAN_custom_cable_diagram.png            | .. Image:: /images/Custom_cable.png            |
   +-------------------------------------------------------------+------------------------------------------------+
   | Wiring Diagram                                              | Example of completed cable.                    |
   +-------------------------------------------------------------+------------------------------------------------+

.. rubric:: **CAN Utilities**
   :name: can-utilities

There may be other userspace applications that can be used to interact
with the CAN bus but the SDK supports using Canutils which is already
included in the sdk filesystem.

.. note::

   These instructions are for mcu_mcan0. If the board has multiple CAN instances
   enabled then they can be referenced by their CAN dts node names just like
   mcu_mcan0 here. For example, 2nd instance of CAN in the main domain ( ie
   main_mcan2 as referenced in the dts ) will be visible as main_mcan2 to the
   users.

.. rubric:: **Quick Steps**
   :name: quick-steps

.. rubric:: **Initialize CAN Bus**
   :name: initialize-can-bus

-  Set bitrate

.. code-block:: console

   $ ip link set mcu_mcan0 type can bitrate 1000000

-  CAN-FD mode with bitrate switching

.. code-block:: console

   $ ip link set mcu_mcan0 type can bitrate 1000000 dbitrate 4000000 fd on

.. rubric:: **Start CAN Bus**
   :name: start-can-bus

-  Device bring up

Bring up the device using the command:

.. code-block:: console

   $ ip link set mcu_mcan0 up

|

.. rubric:: **Transfer Packets**
   :name: transfer-packets

.. rubric:: **Cansend**
   :name: cansend

Used to generate a specific can frame. The syntax for cansend is as
follows:

.. code-block:: text

   <can_id>#{R|data}          for CAN 2.0 frames
   <can_id>##<flags>{data}    for CAN FD frames

Some examples:

a. Send CAN 2.0 frame

.. code-block:: console

   $ cansend mcu_mcan0 123#F00DCAFE

b. Send CAN FD frame

.. code-block:: console

   $ cansend mcu_mcan0 113##2AAAAAAAA

c. Send CAN FD frame with BRS

.. code-block:: console

   $ cansend mcu_mcan0 143##1AAAAAAAAA

.. rubric:: **Cangen**
   :name: cangen

Used to generate frames at equal intervals. The syntax for cangen is as
follows:

.. code-block:: text

   cangen [options] <CAN interface>

Some examples:

a. Full load test with polling, 10 ms timeout

.. code-block:: console

   $ cangen mcu_mcan0 -g 0 -p 10 -x

b. fixed CAN ID and length, inc. data, canfd frames with bitrate
switching

.. code-block:: console

   $ cangen mcu_mcan0 -g 4 -I 42A -L 1 -D i -v -v -f -b

.. rubric:: **Candump**
   :name: candump

Candump is used to display received frames.

.. code-block:: console

   candump [options] <CAN interface>

Example:

.. code-block:: console

   $ candump mcu_mcan0

Note: Use Ctrl-C to terminate candump

Further options for all canutils commands are available at
https://git.pengutronix.de/cgit/tools/canutils

.. rubric:: **Stop CAN Bus**
   :name: stop-can-bus

Stop the can bus by:

.. code-block:: console

   $ ip link set mcu_mcan0 down

.. note::

   The earlier CAN naming convention had can0 referring to  the first probed CAN instance
   and can1, can2.. and so on, to the other CAN instances in the order in which
   they are probed. For example, 2 CAN instances will have names as can0 and can1
   assigned to them in the linux kernel, based on the order in which they are probed and
   irrespective of their CAN instance number. If the earlier CAN naming convention is needed,
   you can revert `2d2df9f8058a3aa323daa01a64fcef59176500e3 <https://git.ti.com/cgit/arago-project/meta-arago
   /commit/?h=scarthgap&id=2d2df9f8058a3aa323daa01a64fcef59176500e3>`_ commit in meta-arago repository.
