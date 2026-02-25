.. http://processors.wiki.ti.com/index.php/Linux_Core_DCAN_User%27s_Guide

DCAN
----

.. rubric:: **Introduction**
   :name: introduction-linux-dcan

The Controller Area Network is a serial communications protocol which
efficiently supports distributed real-time control with a high level of
security. The DCAN module supports bitrates up to 1 Mbit/s and is
compliant to the CAN 2.0B protocol specification. The core IP within
DCAN is provided by Bosch.

This wiki page provides usage information of DCAN Linux driver.

.. rubric:: **Acronyms & definitions**
   :name: acronyms-definitions

+-----------+---------------------------+
| Acronym   | Definition                |
+===========+===========================+
| CAN       | Controller Area Network   |
+-----------+---------------------------+
| BTL       | Bit timing logic          |
+-----------+---------------------------+
| DLC       | Data Length Code          |
+-----------+---------------------------+
| MO        | Message Object            |
+-----------+---------------------------+
| LEC       | Last Error Code           |
+-----------+---------------------------+
| FSM       | Finite State Machine      |
+-----------+---------------------------+
| CRC       | Cyclic Redundancy Check   |
+-----------+---------------------------+

Table:  **DCAN Driver: Acronyms**

.. rubric:: **Setup Details**
   :name: setup-details

.. rubric:: **EVM List**
   :name: evm-list

+-----------+------------------------------+-----------------------+-------------------+----------------------+
| SoC       | EVM                          | Number of Instances   | Connection Type   | Enabled by default   |
+===========+==============================+=======================+===================+======================+
| AM335x    | General Purpose EVM          | 1                     | DB9               | No                   |
+-----------+------------------------------+-----------------------+-------------------+----------------------+
| AM437x    | General Purpose EVM          | 2                     | DB9               | Yes                  |
+-----------+------------------------------+-----------------------+-------------------+----------------------+
| 66AK2Gx   | General Purpose EVM          | 2                     | DB9               | Yes                  |
+-----------+------------------------------+-----------------------+-------------------+----------------------+
| AM571x    | Industrial Development Kit   | 1                     | Header            | Yes                  |
+-----------+------------------------------+-----------------------+-------------------+----------------------+
| DRA74x    | Evaluation Module            | 1                     | Header            | Yes                  |
+-----------+------------------------------+-----------------------+-------------------+----------------------+
| DRA72x    | Evaluation Module            | 1                     | Header            | Yes                  |
+-----------+------------------------------+-----------------------+-------------------+----------------------+

Table:  EVMs DCAN Driver is Validated on

.. note::

   On AM335x GP EVM CAN does not work by default. The evm must have its
   "Profile Switch" set to 1 to enable CAN support.

.. rubric:: **Hardware/Software Changes to Enable CAN Support**
   :name: hardwaresoftware-changes-to-enable-can-support

.. rubric:: **AM335x General Purpose EVM**
   :name: am335x-general-purpose-evm

Most TI boards by default will allow the user to use CAN without any
changes. The boards that do require modifications to be enabled for CAN
to work will be listed below.

+-------------------------------------------------------------+---------------------------------------------+
| .. Image:: /images/Am335x-profile-selection.png             | .. Image:: /images/Dcan_node.png            |
+-------------------------------------------------------------+---------------------------------------------+
| enable)                                                     | disabled to okay                            |
+-------------------------------------------------------------+---------------------------------------------+

Table:  AM335x Hardware and Software modifications


By default the CAN signals on the AM335x GP EVM isn't routed to the CAN
connector. To do so you must configure the EVM to profile 1 instead of
profile 0 which is the default. The profile switch can be found in front
of the LCD screen next to the brown ribbon cable. Pictures of the EVM
using profile 1 is shown above.

Since CAN from a hardware perspective isn't enabled on the EVM by
default it is kept disabled by default. Luckily to re-enable it is
relatively simple. The user must edit the am335x-evm.dts (device tree
file used for this specific evm). Edit the dcan1 node by changing the
node's status from "disabled" to "okay". Example of this change can be
seen above.

.. rubric:: **Connection Configuration**
   :name: connection-configuration

+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| .. Image:: /images/Dcan.png            | .. Image:: /images/Dcan-header.png            | .. Image:: /images/Dcan_header_to_db9.png            |
+----------------------------------------+-----------------------------------------------+------------------------------------------------------+
| DB9 to DB9                             | Header to Header                              | Header to DB9                                        |
+----------------------------------------+-----------------------------------------------+------------------------------------------------------+

Table:  Various DCAN EVM Connection Configuration

.. rubric:: **Equipment**
   :name: equipment

.. rubric:: **Female DB9 Cable**
   :name: female-db9-cable

A male DB9 connector is used on select evms. Therefore, a female
DB9/Serial Port/RS 232 cable must be used to connect with the evm.
Wheather the other end of the cable is female or male will depend on if
the other CAN device the user will be connecting to.

.. Image:: /images/DB9_cable.jpg
   :scale: 50%
   :align: center


.. rubric:: **Jumper Wires**
   :name: jumper-wires

.. Image:: /images/Female_to_female_jumper.png
   :scale: 20%
   :align: center


For evms whose DCAN pins are broken out via a header then a female
jumper wire would be best to use to connect to the various DCAN pins on
the evm. Note some evms have CAN H (typically header pin 1), GND
(typically middle header) and CAN L (typically the third header). Its
important to always connect the CAN's GND pin to what other device your
connecting to. Only exception are the evms that don't include the CAN
GND pin.

+--------------------------------------------------------------------------+
| .. Image:: /images/Dcan_j6eco.png                                        |
+--------------------------------------------------------------------------+
| Example of DCAN header on DRA72 EVM                                      |
+--------------------------------------------------------------------------+

.. note::

   Its important for the user to verify which header pin is associated with
   the various CAN signals. Unless there are already silk screens the user
   may need to double check the evm's schematic.

|

.. rubric:: **Custom DB9 to Header Cable**
   :name: custom-db9-to-header-cable

Typically CAN devices use a DB9 connection therefore for evms whose CAN
pins are broken out via a header it is helpful to create a header to DB9
connector cable. This custom cable is simple to make. Either a male or
female DB9 connector (not cable) must be purchased along with three
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

|

.. rubric:: **CAN Utilities**
   :name: can-utilities

There may be other userspace applications that can be used to interact
with the CAN bus but the SDK supports using Canutils which is already
included in the sdk filesystem.

.. note::

   These instructions are for main_dcan1 which is the 1st instance of CAN in the main domain.
   If the board has multiple CAN instances enabled, then they can be referenced as
   main_dcan\ ``X``\  where X is the CAN instance number just like main_dcan1 here.
   For example, 2nd instance of CAN in the main domain will be visible as main_dcan2
   to the users.

.. rubric:: **Quick Steps**
   :name: quick-steps

.. rubric:: **Initialize CAN Bus**
   :name: initialize-can-bus

-  Set bit-timing

Set the bit-rate to 50Kbits/sec using the following command:

.. code-block:: console

   $ ip link set main_dcan1 type can bitrate 50000

-  Set bit-timing (loopback mode)

Set the bit-rate to 50Kbits/sec in the loopback mode using the following
command

.. code-block:: console

   $ ip link set main_dcan1 type can bitrate 50000 loopback on

.. rubric:: **Start CAN Bus**
   :name: start-can-bus

-  Device bring up

Bring up the device using the command:

.. code-block:: console

   $ ip link set main_dcan1 up

.. note::

   The default state when starting a previously powered off CAN device is
   called "Error-Active". So don't worry when you see this command when you
   first start the CAN instance.

.. rubric:: **Send or Receive Packets**
   :name: send-or-receive-packets

-  Transfer packets

Packet transmission can be achieve by using cansend and cansequence
utilities.

Transmit 4 bytes with standard packet id number as 0x123

.. code-block:: console

   $ cansend main_dcan1 123#F00DCAFE


Transmit a sequence of can frames with random IDs and random data.

.. code-block:: console

   $ cangen main_dcan1

-  Receive packets

Packet reception can be achieve by using candump utility

.. code-block:: console

   $ candump main_dcan1


.. rubric:: **Stop CAN Bus**
   :name: stop-can-bus

.. code-block:: console

   $ ip link set main_dcan1 down

|

.. rubric:: **Advanced Usage**
   :name: advanced-usage

The following are some examples exploring the capabilties of can-utils. See can-utils documentation for a comprehensive set of options.

Transmit fixed CAN ID and length with an incrementing data

.. code-block:: console

   $ cangen main_dcan1 -g 4 -I 42A -L 1 -D i -v -v

Log only error frames but no data frames

.. code-block:: console

   $ candump -l any,0~0,#FFFFFFFF

.. rubric:: **Statistics of CAN**
   :name: statistics-of-can

Statistics of CAN device can be seen from these commands

.. code-block:: console

   $ ip -d -s link show main_dcan1

Below command also used to know the details

.. code-block:: console

   $ cat /proc/net/can/stats

.. rubric:: **Error frame details**
   :name: error-frame-details

.. rubric:: *DCAN IP Error details*
   :name: dcan-ip-error-details

If the CAN bus is not properly connected or some hardware issues DCAN
has the intelligence to generate an Error interrupt and corresponding
error details on hardware registers.

In CAN terminology errors are divided into three categories

-  Error warning state, this state is reached if the error count of
   transmit or receive is more than 96.
-  Error passive state, this state is reached if the core still
   detecting more errors and error counter reaches 127 then bus will
   enter into
-  Bus off state, still seeing the problems then it will go to Bus off
   mode.

.. rubric:: *DCAN driver provides*
   :name: dcan-driver-provides

For the above error state, driver will send the error frames to inform
that there is error encountered. Frame details with respect to different
states are listed here:

-  Error warning frame

.. code-block:: text

   <0x004> [8] 00 08 00 00 00 00 60 00

ID for error warning is 0x004 [8] represents 8 bytes have received 0x08
at 2nd byte represents type of error warning. 0x08 for transmission
error warning, 0x04 for receive error warning frame 0x60 at 7th byte
represent tx error count.

-  Error passive frame

.. code-block:: text

   <0x004> [8] 00 10 00 00 00 00 00 64

ID for error passive frame is 0x004 [8] represents 8 bytes have received
0x10 at 2nd byte represents type of error passive. 0x10 for receive
error passive, 0x20 for transmission error passive 0x64 at 8th byte
represent rx error count.

-  Bus off state

.. code-block:: text

   <0x040> [8] 00 00 00 00 00 00 00 00

ID for bus-off state is 0x040

.. rubric:: *Error frames display with candump*
   :name: error-frames-display-with-candump

candump has the capability to display the error frames along with data
frames on the console. Some of the error frames details are mentioned in
the previous section

.. code-block:: console

   $ candump main_dcan1 -e

.. note::

   The earlier CAN naming convention had can0 referring to  the first probed CAN instance
   and can1, can2.. and so on, to the other CAN instances in the order in which
   they are probed. For example, 2 CAN instances will have names as can0 and can1
   assigned to them in the linux kernel, based on the order in which they are probed and
   irrespective of their CAN instance number. If the earlier CAN naming convention is needed,
   you can revert `cfc97aeb022ddc03f252deebc9021aff449b24c8 <https://git.ti.com/cgit/arago-project/meta-arago
   /commit/?h=kirkstone&id=cfc97aeb022ddc03f252deebc9021aff449b24c8>`_ commit in meta-arago repository.

|

.. rubric:: **Linux Driver Configuration**
   :name: linux-driver-configuration

-  DCAN device driver in Linux is provided as a networking driver that
   confirms to the socketCAN interface
-  The driver is currently build-into the kernel with the right
   configuration items enabled (details below)

.. rubric:: Detailed Kernel Configuration
   :name: detailed-kernel-configuration

The SoC specific kernel configuration included in the SDK by default
enables full support for the DCAN driver. Therefore, manually enabling
these options are not required if your using the provided kernel config
(defconfig).

The below CAN specific drivers are the bare minimum needed to enable
DCAN driver:

-  CAN bus subsystem support
-  Bosch C\_CAN/D\_CAN devices
-  CAN\_C\_CAN\_PLATFORM

Four additional drivers are required to utilize all the CAN features:

-  Raw CAN Protocol (raw access with CAN-ID filtering)
-  Broadcast Manager CAN Protocol (with content filtering)
-  CAN Gateway/Router (with netlink configuration)
-  CAN bit-timing calculation

.. code-block:: text

   [*] Networking support ->
       <*|M> CAN bus subsystem support ->
          <*|M> Raw CAN Protocol (raw access with CAN-ID filtering)
          <*|M> Broadcast Manager CAN Protocol (with content filtering)
          <*|M> CAN Gateway/Router (with netlink configuration)
             CAN Device Drivers ->
                <*|M>   Platform CAN drivers with Netlink support
                [*]     CAN bit-timing calculation
                <*|M>   Bosch C_CAN/D_CAN devices ->
                   <M> Generic Platform Bus based C_CAN/D_CAN driver

.. note::

   \*\|M means can be either be built into the kernel or enabled as a
   kernel module.

|

.. rubric:: **DCAN driver Architecture**
   :name: dcan-driver-architecture

DCAN driver architecture shown in the figure below, is mainly divided
into three layers Viz user space, kernel space and hardware.

.. Image:: /images/Dcan_driver_architecture.png

.. rubric:: **User Space**

CAN utils are used as the application binaries for transfer/receive
frames. These utils are very useful for debugging the driver.

.. rubric:: **Kernel Space**
   :name: kernel-space

This layer mainly consists of the socketcan interface, network layer and
DCAN driver.

Socketcan interface provides a socket interface to user space
applications and which builds upon the Linux network layer. DCAN device
driver for CAN controller hardware registers itself with the Linux
network layer as a network device. So that CAN frames from the
controller can be passed up to the network layer and on to the CAN
protocol family module and vice-versa.

The protocol family module provides an API for transport protocol
modules to register, so that any number of transport protocols can be
loaded or unloaded dynamically.

In fact, the can core module alone does not provide any protocol and
cannot be used without loading at least one additional protocol module.
Multiple sockets can be opened at the same time, on different or the
same protocol module and they can listen/send frames on different or the
same CAN IDs.

Several sockets listening on the same interface for frames with the same
CAN ID are all passed the same received matching CAN frames. An
application wishing to communicate using a specific transport protocol,
e.g. ISO-TP, just selects that protocol when opening the socket. Then
can read and write application data byte streams, without having to deal
with CAN-IDs, frames, etc.

.. rubric:: **Hardware**

This layer mainly consisting of DCAN core and DCAN IO pins for packet
Transmission or reception.

.. rubric:: **Driver Location**
   :name: driver-location

+--------+---------------------------------------------+--------------------------------+
| S.No   | Location                                    | Description                    |
+========+=============================================+================================+
| 1      | drivers/net/can/c\_can/c\_can.c             | DCAN driver core file          |
+--------+---------------------------------------------+--------------------------------+
| 2      | drivers/net/can/c\_can/c\_can\_platform.c   | Platform/SoC DCAN bus driver   |
+--------+---------------------------------------------+--------------------------------+

