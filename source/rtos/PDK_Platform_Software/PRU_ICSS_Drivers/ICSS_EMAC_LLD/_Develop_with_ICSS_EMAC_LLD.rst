.. http://processors.wiki.ti.com/index.php/ICSS_EMAC_LLD_developers_guide

Terms and Glossary
^^^^^^^^^^^^^^^^^^^

.. table::  **Glossary**

   +-----------------+-----------------+-----------------+-----------------+
   | Abbreviation    | Meaning         | Abbreviation    | Meaning         |
   +=================+=================+=================+=================+
   | ICSS            | Industrial      | SDK             | Industrial      |
   |                 | Communicatin    |                 | Software        |
   |                 | Sub-System      |                 | Development Kit |
   +-----------------+-----------------+-----------------+-----------------+
   | PRU             | Programmable    | INTC            | Interrupt       |
   |                 | Real Time Unit  |                 | Controller      |
   +-----------------+-----------------+-----------------+-----------------+
   | LLD             | Low Level       | SoC             | System On Chip. |
   |                 | Driver          |                 | Platforms like  |
   |                 |                 |                 | AM335x/AM437x   |
   |                 |                 |                 | etc             |
   +-----------------+-----------------+-----------------+-----------------+
   | EMAC            | Ethernet MAC    | RTOS            | Real Time       |
   |                 |                 |                 | Operating       |
   |                 |                 |                 | System          |
   +-----------------+-----------------+-----------------+-----------------+
   | TRM             | Technical       | DLR             | Device Level    |
   |                 | Reference       |                 | Ring - a        |
   |                 | Manual for an   |                 | redundancy      |
   |                 | SoC. Such as    |                 | protocol for    |
   |                 | `this <http://w |                 | EtherNet/IP.    |
   |                 | ww.ti.com/lit/u |                 |                 |
   |                 | g/spruh73l/spru |                 |                 |
   |                 | h73l.pdf>`__.   |                 |                 |
   +-----------------+-----------------+-----------------+-----------------+
   | Rx/Tx           | Packet          | Host/CPU/Cortex | Used            |
   |                 | Receive/Packet  |                 | interchangeably |
   |                 | Transmit        |                 | and refers to   |
   |                 |                 |                 | the Application |
   |                 |                 |                 | Processor       |
   +-----------------+-----------------+-----------------+-----------------+

|

-  **Bold** typeface refers to name of function/API/variable/structure.
-  Code snippets are shown as below

::

    Sample code snippet

Document Revision Table
^^^^^^^^^^^^^^^^^^^^^^^^

.. table::  Document Revision

   +--------------+----------+-----------------------------------+
   | Date         | Revision | Comments                          |
   +==============+==========+===================================+
   | 02-Oct-2015  | v.1.0    | Initial Release                   |
   +--------------+----------+-----------------------------------+
   | 04-Oct-2015  | v.1.1    | Fixed links and images            |
   +--------------+----------+-----------------------------------+
   | 04-July-2016 | v.1.2    | Added Time Triggered Send details |
   +--------------+----------+-----------------------------------+

Introduction
^^^^^^^^^^^^^^

The `Industrial SDK <http://www.ti.com/tool/sysbiossdk-ind-sitara>`__
release from Texas Instruments enables the use of the PRU-ICSS for
ethernet packet processing. This is used to implement several Industrial
Ethernet based protocols including Profinet, EtherNet/IP, EtherCAT etc.,
The SDK contains one example for each protocol. These are available
under *SDK/public/examples*. For more information on protocols,
examples, folder structure and information on how to use the SDK, please
refer to the `Getting Started
Guide <http://processors.wiki.ti.com/index.php/AM335x_SYSBIOS_Industrial_SDK_Getting_Started_Guide>`__.

In addition to these, the SDK comes with an Ethernet MAC example. This
example uses two PRU's to implement two independent MAC's with two
different MAC addresses and two different IP addresses. To provide an
analogy, this is somewhat similar to a two port Ethernet PCIe NIC card
on a PC, only here, the Ethernet interface is available along with the
Host processor on a single SoC.

Since all the Industrial protocols and Ethernet MAC share the same basic
software architecture a discussion of Ethernet MAC goes a long way in
understanding the implementation of other protocols. This is a
recommended reading for anyone trying to develop or use other Ethernet
based protocols provided in the SDK.

Assumption
"""""""""""""

The guide is geared towards helping developers with starting to build
applications using the Ethernet MAC and as such does not contain
extensive architectural and design information. Readers are expected to
be well versed with PRU-ICSS hardware architecture and peripherals. A
description of the PRU-ICSS can be found
`here <http://processors.wiki.ti.com/index.php/PRU-ICSS>`__.

This guide also assumes general familiarity with the SDK structure and
Industrial EVM's. If you are not familiar with this then please go
through the Getting Started Guide mentioned previously.

Current SDK release
`2.1.0.1 <http://downloads.ti.com/sitara_indus/esd/SYSBIOSSDK-IND-SITARA/latest/index_FDS.html>`__
covers both AM335x and AM437x platforms, please refer to the TRM's for
details on the SoC. The TRM's can be found here.
`AM335x <http://www.ti.com/lit/ug/spruh73l/spruh73l.pdf>`__/`AM437x <http://www.ti.com/lit/ug/spruhl7d/spruhl7d.pdf>`__.

Scope of the Document
""""""""""""""""""""""

This document:

-  Enables a developer to build simple applications using the Ethernet
   Driver and the sample Ethernet MAC application
-  Explains the components, software organization and architecture of
   the Ethernet driver briefly. This is only to enable developers to use
   and debug the modules. A detailed discussion of the architecture is
   beyond the scope of this document.
-  Explains usage and simple tasks through use cases and examples
-  Helps port another TCP/IP Stack or RTOS for the Ethernet MAC example

The document follows a hands on approach and different aspects are
explained through examples and code snippets, these in turn are derived
from questions on the forum and field.

To prevent the guide from becoming too big and to limit it's scope a
separate `debugging
guide <index_device_drv.html#debug-with-icss-emac-driver>`__
has been written which covers various other aspects such as Q&A's and
Debug examples with screenshots. The two documents must be used in
conjunction to utilize them fully.

.. note::
   The code snippets in this guide are only informative, they may or may
   not compile if taken as it is. Developers are requested to consult the
   API guide and other relevant user guides for exact coding details.

Software Architecture
^^^^^^^^^^^^^^^^^^^^^^

The ICSS EMAC consists of driver + firmware implementation. Firmware
refers to the code running on the two PRU's which are part of ICSS while
driver refers to that portion of code running on host which is directly
associated with the firmware. The two PRU's are responsible for
reception of packets while Host runs higher level tasks.

Logically the software on host can be partitioned into

-  Ethernet Driver - Copying packet data and providing to upper layers.
   Managing PRU/ICSS.
-  TCP/IP and other network stack. NDK in this case.
-  RTOS code. SYS/BIOS in this case.
-  Peripheral initialization and management.

Out of these the first three are relevant to this discussion. Only the
driver is discussed in depth while NDK and SYS/BIOS are mentioned in
passing whenever relevant.

File Organization
""""""""""""""""""

SDK Folder structure is covered in the SDK User Guide
`here <http://processors.wiki.ti.com/index.php/SYSBIOS_Industrial_SDK_02.01.00.01_User_Guide#SDK_Directory_Structure>`__.
This guide only covers the contents of the folder referred to as
*os_drivers* in the user guide.

The contents of the folder *os_drivers* are discussed briefly:

-  ***lld*** - Refers to Link Layer Driver. This contains the core of
   the driver which implements the following:

   -  Rx - Copying the packet received from the firmware and providing
      it to the TCP/IP stack
   -  Tx - Providing packet from TCP/IP stack to the firmware
   -  Learning/Forwarding Data Base - refer `here <index_device_drv.html#learning-fdb>`__
   -  Storm Prevention implementation - refer `here <index_device_drv.html#storm-control>`__
   -  Host Statistics implementation - refer `here <index_device_drv.html#statistics>`__

-  ***pruss*** - Refers to the software which manages the PRU. It
   performs the following tasks

   -  Initializing the PRU memory
   -  Populating memory offsets, MAC addresses in PRU memory
   -  Managing PRU Interrupt Controller

-  ***ICSS*** - Contains software related to the NDK (TCP/IP) Interface.

   -  TCP/IP stack related initialization
   -  Configuring IP address
   -  ARM interrupt management

EMAC and Switch
"""""""""""""""""

It is important to differentiate between the two different types of
implementations in SDK context because this keeps coming up while
discussing SDK and it's components. An EMAC example implements two
independent Ethernet MAC's using PRU 0/1, they have two different MAC,
IP addresses and two different instances of the TCP/IP stack while a
Switch presents a single IP and MAC address for any external entity.
Another important difference which is obvious from the name is that an
EMAC does not forward a packet from one port to another like a Switch.

SDK only provides a separate EMAC example, right now there is no example
in the SDK for a standalone Switch on the lines of EMAC. The example
that comes close to it is the EtherNetIP adapter which is a standalone
Ethernet Switch running a EtherNet/IP protocol stack. Instructions on
how to remove the EtherNet/IP part of it are given
`here <http://processors.wiki.ti.com/index.php/SYSBIOS_ISDK_Steps_for_creating_stand_alone_switch_example>`__.

There are some important differences between an EMAC and Switch

|

.. table::  Differences between EMAC and Switch

   +-----------------------------------+-----------------------------------+
   | EMAC                              | Ethernet Switch                   |
   |                                   | (Profinet and EtherNet/IP)        |
   +===================================+===================================+
   | Two interface MAC addresses       | Single interface MAC address      |
   +-----------------------------------+-----------------------------------+
   | PRU0 transmits on Port0 and PRU1  | PRU0 transmits on Port1 and PRU1  |
   | on Port1                          | on Port0                          |
   +-----------------------------------+-----------------------------------+
   | Two TCP/IP instances and two IP   | One TCP/IP instance and one IP    |
   | addresses                         | address                           |
   +-----------------------------------+-----------------------------------+
   | Two Rx interrupts, semaphores and | Single Rx interrupt, semaphore    |
   | tasks for two ports               | and task                          |
   +-----------------------------------+-----------------------------------+
   | Two ICSS EMAC Handles             | Single ICSS EMAC Handle           |
   +-----------------------------------+-----------------------------------+
   | No collision handling             | Collision buffer with Collision   |
   | (independent MAC's)               | Handling                          |
   |                                   | Collision refers to Queue         |
   |                                   | Contention                        |
   +-----------------------------------+-----------------------------------+
   | No forwarding of packets          | Packets forwarded depending on    |
   |                                   | forwarding rules                  |
   +-----------------------------------+-----------------------------------+

Ports in Driver context
""""""""""""""""""""""""""

Before beginning it’s important to explain the conventions used in this
document, although there are two physical ports for every ICSS for the
sake of convenience the Host is considered as a third port. In fact for
some protocols this is the logical partitioning used. The convention
used here is two physical ports and one host port.

The ports are referred to as

-  Host Port - *ICSS_EMAC_PORT_0*
-  Physical Port 0 - *ICSS_EMAC_PORT_1*
-  Physical Port 1 - *ICSS_EMAC_PORT_2*

This convention is followed throughout the document as well as inside
the driver and firmware.

Driver Architecture and Memory Map
"""""""""""""""""""""""""""""""""""

A detailed discussion of the architecture is beyond the scope of this
document. A brief summary is provided below to explain where the data is
copied to, how and why.

While discussing the ICSS Switch we are mainly concerned with 4 types of
memories.

DDR
'''''

This is the memory from where ARM core operates. It's not on the SoC and
hence has a lower performance. This is cached.

This contains

-  TCP/IP Buffers.
-  Learning/FDB tables.
-  Host Statistics.
-  Control structures and variables.

L3 OCMC RAM
''''''''''''

This is where the actual packet buffers or queues are located. There are
15 queues (Switch) or 12 queues (EMAC) in total. 4 queues for each port
(including host) and 1 additional queue for each port to handle
collision. This is covered later in QoS section. Developer needs to know
that firmware copies the packet data here after receiving them and this
is where the driver writes the packet data meant for transmission using
the firmware. So this acts as a place holder for packet data before it
received or transmitted. This memory resides inside the SoC (but outside
ICSS) and is faster than DDR. It's buffered but non-cached. Size varies
from SoC to SoC, please refer to the TRM for more details. The L3 OCMC
RAM contains:

-  Host receive queues
-  Port transmit queues
-  Collision queues (not in EMAC mode)

.. note::
   This memory map is applicable only for EMAC application. Other
   applications might have their own map.


Shared Data RAM
'''''''''''''''''

This is specific to the PRU subsystem although access is possible from
Host albeit slowly. Data common to both PRU's such as Host queue
descriptors are stored here. A lot of the memory is available for
protocol or application specific usage, for more details refer to the
memory map. Size varies from SoC to SoC, please refer to the TRM for
more details. The Shared Data RAM contains

-  Host queue descriptors
-  Buffer descriptors for all 12 queues
-  Host Rx Context for 4 Host receive queues

.. note::
   This memory map is applicable only for EMAC application. Other
   applications might have their own map.


PRU0 Data RAM
'''''''''''''''

This is similar to Shared Data RAM though meant for use only by PRU0.
Access from PRU1 is also possible, so the separation is only logical,
not in hardware. Size varies from SoC to SoC, please refer to the TRM
for more details. The PRU0 Data RAM contains:

-  Port 0 Time Triggered Send variables
-  Port 0 Queue descriptors for 4 Tx queues
-  Port 0 Tx Context for 4 Port Tx queues
-  Port 0 Statistics
-  Port 0 MAC ID
-  Port 0 Port, Speed and Duplex information

.. note::
   This memory map is applicable only for EMAC application. Other
   applications might have their own map.

PRU1 Data RAM
''''''''''''''

Similar to PRU0 Data RAM but for PRU1.

Quality of Service and Queues
""""""""""""""""""""""""""""""

Quality of Service is very important for an Ethernet Switch/EMAC as it
allows high priority packets to be processed separately from regular
packets. This provides reliability for real time traffic. In EMAC this
is done using queues which are mapped to 8 VLAN based priority levels.
Each queue is a block of memory on L3 used to store the packet data.
Queue sizes may vary and are build time configurable from
*icss_emacSwitch.h*, for example host queue sizes used for default EMAC
application are given below, the sizes are denoted by blocks. Each block
is 32 bytes in size. The sizes are limited by L3 size which are dictated
by SoC. For in depth information on how to re-build the icss-emac LLD
PDK component in case your use case requires re-sizing the Queue sizes,
refer to
`[1] <How_to_Guides.html#rebuild-drivers-from-pdk-directory>`__.

::

    #define HOST_QUEUE_1_SIZE      194
    #define HOST_QUEUE_2_SIZE       194
    #define HOST_QUEUE_3_SIZE       194
    #define HOST_QUEUE_4_SIZE       194

The transmit queues sizes are denoted separately

::

    #define QUEUE_1_SIZE       97
    #define QUEUE_2_SIZE        97
    #define QUEUE_3_SIZE        97
    #define QUEUE_4_SIZE        97

So in total there are 15 queues (12 queues in EMAC), 4 receive queues
for Host and 4 transmit queues for each of the two physical ports. In
addition to these there is 1 collision queue each for Host and 2 ports
which can hold one packet irrespective of packet size.

.. note::
   There are no collision queues in EMAC.


The figure below is illustrative to remember this

How QoS Works
''''''''''''''

Switch QoS
~~~~~~~~~~~~

When a packet is received in firmware, the 3 bit PCP field of the VLAN
tag is read and the packet is copied to the appropriate queue based on
fixed mapping which maps 2 levels(out of 8) of QoS to one queue. So 7 &
6 map to Queue 4, 5 & 4 to Queue 3 and so on. On the driver this queue
number then translates to the priority value and is used to decide how
to process the packet. If a packet is missing VLAN tag then the lowest
priority queue Queue 4 is chosen.

EMAC QoS
~~~~~~~~~

PCP to queue mapping is different for EMAC. In EMAC, the 4 Host receive
queues are split into two groups. Queue 1 and Queue 2 are used for
storing packets received at PRU0/Port1 and Queue 3 and Queue 4 are used
for storing packets received at PRU1/Port2. So, the low priority queues
are Queue 2 and Queue 4 for Port 1 and Port 2 respectively. Queue 1 and
Queue 3 are high priority queues for Port 1 and Port 2 respectively.

-  All the non-VLAN tagged frames are stored in the lowest priority
   queue (Queue 2 for Port 1 and Queue 4 for Port 2).
-  VLAN tagged frames with “Priority Code Point (PCP)” value of 4, 5, 6
   and 7 are stored in highest priority queue (Queue 1 for Port 1 and
   Queue 3 for Port 2).
-  VLAN tagged frames with “Priority Code Point (PCP)” value of 0, 1, 2,
   and 3 are stored in low priority queue (Queue 2 for Port 1 and Queue
   4 for Port 2).

More on this in the next section where driver side Rx processing is
discussed in detail.

.. note::
   -  When a queue overflows, packets are **not** automatically copied to
      the next free queue. So overflow can occur.
   -  Contention/Collision queue can only handle a single packet
      irrespective of size, anything above is dropped.
   -  On Tx side, there is no special handling with regards to QoS. Data is
      copied to one of the four queues based on the **queuePriority** field
      **ICSS_EmacTxArgument** structure passed to the **ICSS_EmacTxPacket**
      API.
   -  At the moment driver/firmware doesn't support DSCP.


Data Path
"""""""""""

Data path refers to the control flow which is executed on the driver and
firmware to send or receive a packet. A basic understanding of it goes a
long way in explaining the software architecture and if a developer is
only trying to use the Rx and Tx capabilities of EMAC or Switch a
knowledge of this is sufficient to build an application.

Rx Data Path
''''''''''''''

Packets are received in the ICSS from where they are copied by the PRU's
to L3 memory. The PRU's then assert an interrupt to tell the Host about
the presence of a packet. PRU avoids corruption and does not write over
the memory till the packet is copied by the Host.

The flowchart shown above shows the sequence in very broad strokes. A
detailed description is given below.

#. PRU Posts an Rx interrupt to the ARM interrupt controller. For EMAC
   each PRU has a separate Rx interrupt, the configuration for which is
   done in the application (details in Interrupts).
#. The interrupt triggers the ISR **ICSS_EmacRxInterruptHandler** which
   in turn posts a semaphore rxSemaphoreHandle to signal **RxTask** to
   empty the Rx queues.
#. The **RxTask** function goes through all the queues, extracts the
   port/queue number and provides it to an API which copies data from L3
   to DDR. The code excerpt is shown below with explanations.

.. code-block:: c

    /*Read till all queues are empty*/
    while(allQueuesEempty != 1 && numPacketsInLoop <= ((((ICSSEMAC_Object*)icssEmacHandle->object)->emacInitcfg)->pacingThreshold))
    {
         /*This API reads the queues and gets the queue and port number for each packet*/
         pLength = ICSS_EmacRxPktInfo(icssEmacHandle, &port_number, &queue_number);
         if(pLength > 0)
         {
              if(queue_number >= ((ICSSEMAC_Object*)(icssEmacHandle->object))->emacInitcfg->ethPrioQueue)
              {
                   /*Based on queue priority settings decide if the packet is to be sent to the TCP/IP stack*/
                   /*This API is hooked to NDK*/
                   icssEmacHwIntRx(&queue_number,icssEmacHandle);
              }
              else
              {
                   /*Protocol specific callback*/
                   if(((((ICSSEMAC_Object*)icssEmacHandle->object)->callBackHandle)->rxRTCallBack)->callBack != NULL)
                   {
                        ((((ICSSEMAC_Object*)icssEmacHandle->object)->callBackHandle)->rxRTCallBack)->callBack(&queue_number,
                        ((((ICSSEMAC_Object*)icssEmacHandle->object)->callBackHandle)->rxRTCallBack)->userArg);
                   }
                   else
                   {
                        /* just dump the packet here so we do no stall the queues*/
                        ICSS_EmacRxPktGet(icssEmacHandle,(uint32_t)dest_address, queue_number, &port_number, &more);
                   }
              }
              ...
              ...
    }

In the code snippet above, function **ICSS_EmacRxPktInfo** goes through
each queue one at a time, extracts the port & queue number information
for every packet and provides it to functions below. Based on the
priority of the packet which is decided by the queue number (refer to
`discussion <index_device_drv.html#how-qos-works>`__
on QoS and queues) driver decides to either forward it to NDK, done by
**icssEmacHwIntRx** or give it to the callback function.

The threshold for this decision is decided by the user settable
parameter shown in the code above.

.. code-block:: c

    ((ICSSEMAC_Object*)(icssEmacHandle->object))->emacInitcfg->ethPrioQueue)

Anything lower than this configured value goes to the callback function.
If a callback is not registered then the queue is just emptied to
prevent queues from overflowing. This is done by the function
**ICSS_EmacRxPktGet** which takes a single packet and copies it into
**dest_address** provided as a parameter. This is not a dummy API but a
basic Rx API which performs the task of copying data from L3 to DDR,
even the NDK API **icssEmacHwIntRx** internally calls
**ICSS_EmacRxPktGet** to fetch the packet data.

If a developer is building a custom API to process packets then he/she
needs to call the API **ICSS_EmacRxPktGet** in their respective
function, this is explained with an example below.

***Doing customized packet processing:***

This example is taken from EtherNet/IP adapter application where some
DLR packets are processed different from other packets using a callback.
For this example the value of **ethPrioQueue** is set to 4 or
*ICSS_EMAC_QUEUEPRIO4* and in this case these DLR frames have a the
highest priority so they go to the callback function, developers need to
set an appropriate value for **ethPrioQueue** based on their
requirements. The callback is configured in **main** like this (taken
from *icss_eip_driver.c*)

.. code-block:: c

    /*Packet processing callback*/
    ((((ICSSEMAC_Object*)icssEmacHandle->object)->callBackHandle)->rxRTCallBack)->callBack = (ICSS_EmacCallBack)processProtocolFrames;
    ((((ICSSEMAC_Object*)icssEmacHandle->object)->callBackHandle)->rxRTCallBack)->userArg = icssEmacHandle;

Where **icssEmacHandle** is the main driver handle and
**processProtocolFrames** is the callback function whose outline is
given below

.. code-block:: c

    void processProtocolFrames(uint32_t* queue_number, void* userArg) {
    ...
    ...
    uint8_t *dstMacId = tempFrame;
    ICSSEMAC_Handle eipIcssEmacHandle = (ICSSEMAC_Handle)userArg;
    /*Fetch the packet*/
    size = ICSS_EmacRxPktGet(eipIcssEmacHandle,(uint32_t)tempFrame, *queue_number, &port, &more);
    ...
    /*Compare Destination MAC ID and determine if this is a DLR packet*/
    if(COMPARE_MAC(dstMacId, dlrMAC)) {
      processDLRFrame(eipIcssEmacHandle, tempFrame, port-1, size);
    ...
    ...
    }

As can be seen **processProtocolFrames** function calls
**ICSS_EmacRxPktGet** internally and passes the data to
**processDLRFrame** for further processing.

Tx Data Path
'''''''''''''''

The Transmit path on host is simpler than the Rx path. As far as the
developer is concerned the main API call is **ICSS_EmacTxPacket**. This
API implements the Learning/FDB functionality. **ICSS_EmacTxPacket** in
turn calls another API **ICSS_EmacTxPacketEnqueue** which performs the
actual task of copying data from DDR to L3 and signals the PRU to
transmit the data. **ICSS_EmacTxPacket** when called with the parameter
*ICSS_EMAC_PORT_0* in **portNumber** field enables learning/FDB and
calls the **ICSS_EmacTxPacketEnqueue** with the correct port number and
when called with parameter *ICSS_EMAC_PORT_1* or *ICSS_EMAC_PORT_1* the
API directly calls the underlying API. To avoid confusion developers
must always call the API **ICSS_EmacTxPacket** (NOT
[STRIKEOUT:**ICSS_EmacTxPacketEnqueue**]) with **portNumber** as

-  *ICSS_EMAC_PORT_0* : If they do not know the port number on which to
   transmit.
-  *ICSS_EMAC_PORT_1* or *ICSS_EMAC_PORT_2* : If they know the port
   number

.. note::
   Firmware automatically appends CRC to the packet on Transmit path.


Usage
'''''''

For simple and/or non time critical applications, it makes more sense to
use the NDK socket API's to perform Receive and Transmit operations. An
example using NDK sockets which performs both Rx and Tx is given below.
For in depth information on how to use sockets please consult `NDK
User's guide <http://www.ti.com/lit/ug/spru523i/spru523i.pdf>`__ and
`NDK API Reference
guide <http://www.ti.com/lit/ug/spru524i/spru524i.pdf>`__.

.. code-block:: c

    /*Transmit to System with IP Address*/
    #define DST_IP "192.168.1.64"
    #define DST_PORT 7
    /*Open file session*/
    fdOpenSession( (HANDLE)Task_self() );
    SOCKET s = INVALID_SOCKET;
    struct sockaddr_in sin1;
    struct timeval timeout;
    /*Create UDP socket*/
    s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    /*Prepare address for connect*/
    IPN IPAddr;
    IPAddr = inet_addr(DST_IP);
    bzero( &sin1, sizeof(struct sockaddr_in) );
    sin1.sin_family = AF_INET;
    sin1.sin_addr.s_addr = IPAddr;
    sin1.sin_port = htons(DST_PORT);
     /*Configure our Tx and Rx timeout*/
    timeout.tv_sec = 0;
    timeout.tv_usec = 1;
    setsockopt( s, SOL_SOCKET, SO_SNDTIMEO, &timeout, sizeof( timeout ) );
    setsockopt( s, SOL_SOCKET, SO_RCVTIMEO, &timeout, sizeof( timeout ) );
    /*Transmit packet*/
    sendto( s, pBuf, testsize, 0, (PSA)&sin1, sizeof(sin1) );
    /*Receive packet*/
    recv(s, pBuf, MAX_UDP_SIZE, 0);

For time critical applications with low latency requirements directly
calling the API's is recommended. For Transmit this can be done by
populating the packet directly(or through a stack) in a memory buffer
and calling **ICSS_EmacTxPacket** with the buffer in a task in
**main()**. Shown below is an example of a periodic transmit being done
in main function.

.. code-block:: c

    /**A dummy packet*/
    uint8_t dummyPkt[ETHERNET_FRAME_SIZE_60] = {0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0x00,0x00,0x00,0x00,0x00,0x00,0x08,0x00,
    0x45,0x00,0x00,0x2E,0x00,0x00,0x40,0x00,0x40,0x00,0x3A,0xD1};
    Void taskSendPacket(UArg a0, UArg a1) {
      /*wait for system to initialize*/
      /*Send packet in a loop every 500ms*/
      Task_sleep(5000);
      while(1) {
        /*Send packet on PORT 1*. Size is known previously/
        ICSS_EmacTxPacket(emachandle,dummyPkt, ICSS_EMAC_PORT_1, 1, ETHERNET_FRAME_SIZE_60);
        Task_sleep(500);
      }
    }

For receive the application/stack can receive the packet data directly
in **(uint32_t)dest_address** from **ICSS_EmacRxPktGet** inside
**RxTask**. Modify the **ethPrioQueue** value as per requirement.
(Explained above)

Forwarding Rules
'''''''''''''''''

Forwarding Rules specify how packets are forwarded between ports and
from the port to the Host. There are three basic types of forwarding
scenarios. The image below shows all modes when receiving on first port.
**HW Port** represents the physical port. These modes are not exclusive
to each other and multiple modes are also allowed.

Please note that EMAC can only forward to the Host, other modes only
apply to switch.

-  **Cut Through** - In this mode the firmware copies the data from Rx
   FIFO to Tx FIFO through the registers. No data is copied to the
   queues, this is the fastest mode of transmit from one port to
   another. Advantage is low latency, disadvantage is that CRC is not
   checked before transmit since it lies at the end of the packet.
-  **Store & Forward** - In this mode the firmware copies the received
   data to the transmit queues on opposite port, no data is sent to the
   Host (Rx interrupt on Host is not asserted). CRC is checked before
   transmit. Many protocols like PTP use this mode.
-  **Forward to Host** - Data is received in the Host receive queues and
   an Rx interrupt is asserted to copy the data. This is the only mode
   available for an EMAC.

|

.. table::  **Forwarding Rules**

   +-----------------------------------+-----------------------------------+
   | Packet Type                       | Forwarding Mode                   |
   +===================================+===================================+
   | Broadcast                         | Cut through & Forward to Host     |
   +-----------------------------------+-----------------------------------+
   | Multicast                         | Cut through & Forward to Host     |
   |                                   | Multicast frames like PTP/DLR are |
   |                                   | handled based on protocol         |
   +-----------------------------------+-----------------------------------+
   | Unicast (not to Host)             | Cut through                       |
   +-----------------------------------+-----------------------------------+
   | Unicast (to Host)                 | Forward to Host                   |
   +-----------------------------------+-----------------------------------+

|

Interrupts and Tasks
""""""""""""""""""""""

This section deals with Interrupts and Tasks required to implement an
EMAC LLD application. Since they are tied to the RTOS used, they are
exported via the driver handle to the application as well as through the
OSAL layer. Developers must take care to maintain correct priorities and
order so as not to alter the behavior of the driver. All the interrupts
and tasks enabled in an application can be checked using the SYSBIOS
ROV. For more details on this tool refer to the
`SYSBIOS <index_device_drv.html#sys-bios>`__ section of EMAC LLD Debug Guide.

Interrupts
'''''''''''

There are six interrupts (eight if time triggered send is enabled) in an
EMAC LLD coming from PRU. Other implementations like EtherNet/IP, PTP,
Profinet etc may use their own interrupts. Please note that there are
individual interrupts for each port because this is a dual MAC
implementation, for an Ethernet switch like EtherNet/IP there are only
two interrupts (no time triggered send in Switch mode).

The eight interrupts are:

#. Rx interrupt x 2 : One for each port, both mapping to same ISR. These
   are used by PRU to tell ARM about the presence of a packet. For Port
   0 this is interrupt number (ARM) 20 on AM335x and for Port 1 it is
   21. In the mapping these are indicated by **PRU_ARM_EVENT0** and
   **PRU_ARM_EVENT1** respectively. For ethernet switch it's just
   **PRU_ARM_EVENT0**.
#. Link interrupt x 2: One for each port, both mapping to same ISR.
   These are used to indicate PHY state change to Host. For Port 0
   interrupt number (ARM) is 26 and for Port 1 27. In mapping these are
   indicated by **MII_LINK0_EVENT** and **MII_LINK1_EVENT** which map to
   **CHANNEL7** and **CHANNEL8** respectively. For ethernet switch both
   link events map to a single channel **CHANNEL7**.
#. Tx Completion Interrupt x 2: One for each port, mapping to different
   ISRs. These are used by PRU to tell ARM about the completion of
   transmission of a packet. For Port 0 this is interrupt number (ARM)
   22 on AM335x and for Port 1 it is 23. In the mapping these are
   indicated by **PRU_ARM_EVENT2** and **PRU_ARM_EVENT3** respectively.
#. TTS Insert Cyclic Frame Interrupt x 2: One for each port, mapping to
   different ISRs. These are used by PRU to tell ARM that its time to
   insert cyclic frame. For Port 0 this is interrupt number (ARM) 22 on
   AM335x and for Port 1 it is 23. In the mapping these are indicated by
   **PRU_ARM_EVENT4** and **PRU_ARM_EVENT5** respectively. These are
   only applicable when TTS is enabled and initialized by the
   application.

.. note::
   Tx Completion Interrupts and TTS Cyclic Frame Interrupts are different
   PRU events, i.e., total 4 PRU events. But these map to the same
   interrupt and ISR per port i.e., Tx Completion Interrupt and TTS Cyclic
   Frame Interrupt share one ARM interrupt number and ISR for Port 1 and
   share one ARM interrupt number and ISR for Port 2.

There are two types of interrupts:

-  ***ICSS Interrupts*** : These are interrupts that are routed through
   the ICSS Interrupt controller to the Host (Refer to section 4.4.2 of
   `AM335x TRM <http://www.ti.com/lit/ug/spruh73l/spruh73l.pdf>`__). It
   consists of interrupts asserted by the PRU as well as interrupts
   asserted by the peripherals (MDIO, ECAP etc) attached to the ICSS
   Interrupt controller.

The Host Interrupt controller has 8 usable interrupts mapped to the ICSS
interrupt controller. This mapping is programmable and varies from
example to example. Every example has a *x_pruss_intc_mapping.h* file in
the *sdk/examples* folder where x stands for the example name. For EMAC
this file is called *tiemac_pruss_intc_mapping.h*.

***Mapping Explanation***

The interrupt mapping consists of 3 parts:

#. 8 PRU user interrupts (can be set in the firmware by writing to R31)
   - represented by *PRU_ARM_EVENT0* to *PRU_ARM_EVENT7*. These are part
   of the 64 system interrupts (out of which 32 are usable). This
   includes the two link interrupts for two ports *MII_LINK0_EVENT* and
   *MII_LINK1_EVENT*.
#. 10 ICSS Host channels *CHANNEL0* to *CHANNEL9* out of which the first
   two *CHANNEL0* and *CHANNEL1* are used internally.
#. 8 ARM PRU interrupts represented by *PRU_EVTOUT0* to *PRU_EVTOUT7*.
   These can also be seen in the ARM INTC in SoC TRM. Provided below is
   a screenshot from AM335x TRM showing the 8 interrupts mapped to the
   PRU.

|

|
| The complete mapping follows the pattern

::

    PRU user interrupts --> Host Channels --> ARM PRU Interrupts

To take an example of Rx interrupt for Port 0 (EMAC only). For switch
this is the Rx interrupt for both ports.

The following line maps PRU user interrupt 0 to Host channel 2.

::

    {PRU_ARM_EVENT0,CHANNEL2, SYS_EVT_POLARITY_HIGH ,SYS_EVT_TYPE_PULSE}

Host channel *CHANNEL2* in turn maps to the first ARM interrupt
*PRU_ICSS_EVTOUT_0* through this line.

::

    {CHANNEL2, PRU_EVTOUT0}

As seen from the screenshot the interrupt number for *PRU_ICSS_EVTOUT_0*
on AM335x is *20*, so the interrupt number that must be configured for
this in application should be 20 if the platform is AM335x. This is done
in the following line (defined in *main.c*)

::

    switchEmacCfg->rxIntNum = 20;

This mapping alone determines which ARM interrupt number will be
associated with a particular PRU user interrupt. For example the line
above where PRU user interrupt 0 maps to Host channel 2 can be modified
to

::

    {PRU_ARM_EVENT0,CHANNEL2, SYS_EVT_POLARITY_HIGH ,SYS_EVT_TYPE_PULSE} ---> {PRU_ARM_EVENT0,CHANNEL4, SYS_EVT_POLARITY_HIGH ,SYS_EVT_TYPE_PULSE}

and the Channel to ARM interrupt map can be configured as, and the
interrupt number on ARM would still remain the same i.e. 20

::

    {CHANNEL2, PRU_EVTOUT0} --->  {CHANNEL4, PRU_EVTOUT0}

A question arises in this case as to the usefulness of *CHANNELx*. The
answer is that channels allow us to map multiple PRU User interrupts and
system interrupts to a single channel and in turn to a single ARM
interrupt. For example take a look at the link interrupt mapping

::

    {MII_LINK0_EVENT, CHANNEL7, SYS_EVT_POLARITY_HIGH ,SYS_EVT_TYPE_PULSE},    \
    {MII_LINK1_EVENT, CHANNEL7, SYS_EVT_POLARITY_HIGH ,SYS_EVT_TYPE_PULSE}, \

and

::

    {CHANNEL7, PRU_EVTOUT6}

This configuration maps both Port 0 and Port 1 interrupts to a single
channel and in turn to a single ARM interrupt *PRU_ICSS_EVTOUT6*, which
is interrupt number 26 (shown by the line below in *main.c*)

::

    switchEmacCfg->linkIntNum=26;

The link interrupt binds to a single ISR **ICSS_EmacLinkISR** on Host.
Inside the ISR an ICSS register **HW_ICSS_INTC_SECR1**\ is checked to
find out which link event *MII_LINK0_EVENT* or *MII_LINK1_EVENT*
asserted the interrupt. The advantage of such an approach is that both
interrupts are serviced even if they are raised at the same time.

These interrupt numbers can change from SoC to SoC so please consult TRM
before making any modifications to the interrupt map. This is also one
of the reasons for exporting these configurations to application so that
a single driver can handle multiple SoC's others being ease of use,
porting other operating systems etc.

|

.. table::  PRU Interrupt Mapping in EMAC

   +-----------------+-----------------+-----------------+-----------------+
   | PRU Interrupt   | Channel Number  | Host Interrupt  | ISR             |
   | Number          |                 | Number          |                 |
   +=================+=================+=================+=================+
   | PRU_ARM_EVENT0  | CHANNEL2        | 20              | *ICSS_EmacRxInt |
   | Port 0 RX       |                 |                 | erruptHandler*  |
   | Interrupt       |                 |                 |                 |
   +-----------------+-----------------+-----------------+-----------------+
   | PRU_ARM_EVENT1  | CHANNEL3        | 21              | *ICSS_EmacRxInt |
   | Port 1 RX       |                 |                 | erruptHandler*  |
   | Interrupt       |                 |                 |                 |
   +-----------------+-----------------+-----------------+-----------------+
   | PRU_ARM_EVENT2  | CHANNEL4        | 22              | *ICSS_EmacTxInt |
   | Port 0 TX       |                 |                 | erruptHandlerPo |
   | Completion      |                 |                 | rt1*            |
   | Interrupt       |                 |                 |                 |
   +-----------------+-----------------+-----------------+-----------------+
   | PRU_ARM_EVENT3  | CHANNEL5        | 23              | *ICSS_EmacTxInt |
   | Port 1 TX       |                 |                 | erruptHandlerPo |
   | Completion      |                 |                 | rt2*            |
   | Interrupt       |                 |                 |                 |
   +-----------------+-----------------+-----------------+-----------------+
   | PRU_ARM_EVENT4  | CHANNEL4        | 22              | *ICSS_EmacTxInt |
   | Port 0 TTS      |                 |                 | erruptHandlerPo |
   | Insert Cyclic   |                 |                 | rt1*            |
   | Frame Interrupt |                 |                 |                 |
   +-----------------+-----------------+-----------------+-----------------+
   | PRU_ARM_EVENT5  | CHANNEL5        | 23              | *ICSS_EmacTxInt |
   | Port 1 TTS      |                 |                 | erruptHandlerPo |
   | Insert Cyclic   |                 |                 | rt2*            |
   | Frame Interrupt |                 |                 |                 |
   +-----------------+-----------------+-----------------+-----------------+
   | MII_LINK0_EVENT | CHANNEL7        | 26              | *ICSS_EmacLinkI |
   | Port 0 Link     |                 |                 | SR*             |
   | Interrupt       |                 |                 |                 |
   +-----------------+-----------------+-----------------+-----------------+
   | MII_LINK1_EVENT | CHANNEL8        | 27              | *ICSS_EmacLinkI |
   | Port 1 Link     |                 |                 | SR*             |
   | Interrupt       |                 |                 |                 |
   +-----------------+-----------------+-----------------+-----------------+

|

-  ***Host Interrupts*** : Host interrupts are interrupts that are not
   coming via ICSS Interrupt controller. These include peripherals,
   EDMA, timers etc. A full list is present inside the Interrupt section
   of any TRM. On AM335x a total of 128 interrupts are available through
   this (including 8 PRU ICSS interrupts). Discussion of Host interrupts
   is beyond the scope of this guide as we only deal with the EMAC LLD
   driver here.

Some examples of Host interrupts used in the driver are DMTimer
interrupts and EDMA interrupts which are available through the OSAL
layer *osdrv_edma.c* and *osdrv_osal.c*

Interrupt Pacing
'''''''''''''''''

When packets are sent to the Host at a very high rate (this happens more
often with small frames) it's possible that ARM is interrupted
frequently by the PRU's, this results in packets getting dropped as the
host is unable to empty the queues in time because of context switching.
Interrupt pacing is a scheme used to cope with this situation. In this
scheme interrupts are disabled when the first Rx interrupt is received
(The PRU still keeps receiving the frames and putting them on the
queues), after a certain number of packets have been processed on the
Host, the interrupts are enabled once more. Since interrupts on PRU have
not been disabled any pending packets will assert the interrupt again,
this ensures that no packets are missed. The advantage of pacing is that
a greater throughput is achieved while disadvantage is that if any
critical packets need to be serviced immediately, it's possible that
some delay may occur. Pacing is enabled in the driver using the variable
**intrPacingMode**. There are two pacing modes in driver.

-  **INTR_PACING_MODE1** : This is entirely ARM based, i.e. interrupts
   are disabled only on the Host. This does not require any firmware
   support. This is the scheme supported with Ethernet MAC and Ethernet
   IP Adapter.
-  **INTR_PACING_MODE1** : In this scheme interrupts are disabled on the
   PRU. This requires firmware support. Only supported in Profinet right
   now.

Tasks
''''''

Tasks are the Linux equivalent of processes in SysBIOS. A simple example
to create a task from EMAC application is given below

.. code-block:: c

     Task_Params_init(&taskParams);
     taskParams.priority = 15;
     taskParams.instance->name = "SwitchTask";
     Task_create(taskPruss, &taskParams, &eb);

Here **taskPruss** is given the job of initializing the PRU's and
loading the firmware onto them. The task itself is a simple function
with two arguments

::

    /*
     *  ---task to initialize PRU---
     */
    Void taskPruss(UArg a0, UArg a1)
    {
      ...
      ...
      ...
    }

They can be used for simple tasks like sending or receiving a packet. To
get an idea `refer <index_device_drv.html#usage>`__
to the example usage for sending a packet through a call to transmit API
**ICSS_EmacTxPacket** in a loop. If calling the task in an endless while
loop developers must add a small delay inside the loop using
*Task_sleep(time in milliseconds)* to let other tasks get some time as
well, failure to do so is a common mistake that developers make.

Learning/FDB
"""""""""""""

Learning/FDB where FDB stands for Forwarding Data Base is a module that
learns source MAC addresses of packets addressed to the Host and thus
maintains a list of which devices reside on which port. While
transmitting a packet when provided with the destination MAC address the
module returns the port number on which the device resides. This avoids
duplication of traffic on both ports. This module is applicable only in
Switch mode, in EMAC mode this module is disabled since there is only
one port.

Design
''''''''

Learning table is currently implemented as a Hash table. There is one
table for each physical port. Each table has 256 buckets where a bucket
has a size of 4. The bucket size and number of buckets are in turn
dictated by the choice of Hashing algorithm. A detailed discussion on
this topic is beyond the scope of this document, suffice to say that
theoretically a hash table is capable of learning 256 \* 4 = 1024
entries. The actual capacity may be lower owing to collisions.

A single bucket has

-  Four entries - For storing four MAC Id's
-  Four ageing counters - One associated with each entry
-  Number of Entries - A value which tells how many entries are there in
   the bucket.

A single table has

-  256 buckets
-  Total number of entries - Sum of entries in all the buckets
-  Port State - A table has three states

   -  Learning - This is the default state. All actions are permitted
   -  Not Learning - No new addresses are learnt. Deletions possible.
   -  Locked - No additions/deletions allowed

Collisions are handled using ageing counters, one ageing counter is
associated with each of the 4 entries inside a bucket. It tells the
module which entries are old and which ones are new.

API Guide & Data Structures
'''''''''''''''''''''''''''''

A learning table has the following structure

.. code-block:: c

    typedef struct HashTable_t{

     uint32_t totalNumEntries;        /**Total number of entries in the hash table*/
     portState state;             /**State of the hash table, see enum portState above*/
     HashBucket_t  entries[NUMBUCKETS];  /**Number of bucket entries*/

    } HashTable_t;

The individual bucket which makes up the learning table has the
following structure

.. code-block:: c

    typedef struct {

     MAC mac[MAX_NUM_ENTRIES];            /**Four MAC Id per bucket*/
     uint8_t timerCount[MAX_NUM_ENTRIES]; /**Timer count used for ageing and conflict resolution*/
     uint8_t numEntries;                  /**Number of MAC entries in the bucket, 4 means it is full*/

    } HashBucket_t;

The default values are

-  NUMBUCKETS 256
-  MAX_NUM_ENTRIES 4

The algorithm assumes these values and they cannot be changed at
present.

API descriptions are only for information, developers are requested to
use corresponding `IOCTL <index_device_drv.html#ioctl>`__
calls. The IOCTL command for Learning/FDB modules is
***ICSS_EMAC_IOCTL_LEARNING_CTRL***

***Adding A MAC address*** : The corresponding API for this is

::

    void updateHashTable(uint8_t* macId, uint8_t portNum, HashTable_t *tablePtr,ICSSEMAC_CallBackConfig* exceptionCallBack)

The API is integrated inside **ICSS_EmacRxPktGet** so developer need not
call it separately, if at all it is required please use the IOCTL call
for this. IOCTL Param value is *ICSS_EMAC_LEARN_CTRL_UPDATE_TABLE*

***Looking up an Entry*** : The corresponding API for this is

::

    uint8_t findMAC(const uint8_t * macId, HashTable_t *tablePtr)

Integrated with driver inside **ICSS_EmacTxPacket**, use IOCTL Param
value *ICSS_EMAC_LEARN_CTRL_FIND_MAC*

***Removing a MAC address*** : The corresponding API for this is

::

    uint8_t removeMAC(uint8_t * macId, HashTable_t *tablePtr)

Entries are removed automatically upon ageing, if forced removal is
required use IOCTL Param value *ICSS_EMAC_LEARN_CTRL_REMOVE_MAC*

***Ageing an Entry*** : The driver already implements this inside the
periodic task which is called every 100 NDK Ticks ***\_HwPktPoll()***
but users can call it as well. IOCTL Param value
*ICSS_EMAC_LEARN_CTRL_INC_COUNTER*

The corresponding API for this is

::

    void incrementCounter(HashTable_t *tablePtr)

***Removing an Aged Entry*** : The corresponding API for this is

::

    void ageingRoutine(uint8_t portNum, HashTable_t *tablePtr)

Integrated with driver. IOCTL Param value *ICSS_EMAC_LEARN_CTRL_AGEING*

***Changing Port State*** : Change the port state to appropriate value.
This is useful in the implementation of requirements specified by IEEE
802.1D.

The corresponding API for this is

::

    void changePortState(portState state, HashTable_t *tablePtr)

As part of changing port state the module implements locking of a port
(where addition/deletion of entries is not possible), ageing (age the
entries to simulate passage of time). Not integrated with driver,
application must do it. IOCTL Param value
*ICSS_EMAC_LEARN_CTRL_SET_PORTSTATE*

***Flushing/Clearing the entire Table*** : The corresponding API for
this is

::

    void purgeTable(uint8_t portNum, HashTable_t *tablePtr)

Not integrated with driver, call separately using IOCTL Param value
*ICSS_EMAC_LEARN_CTRL_CLR_TABLE*

Usage
'''''''

The module is integrated with the driver so a developer need not bother
about calling the API's separately in the application unless there is a
specific need to

-  Add a MAC ID
-  Remove a MAC ID
-  Lock the Port or change it's state

The ageing module is called inside **\_HwPktPoll** (which is a periodic
NDK task, more info in the porting guide) via an IOCTL call, to age
faster please call the routine separately in another task. Changing the
time period of **\_HwPktPoll** is not recommended as many other tasks
are performed in this.

Storm Control
"""""""""""""""

Strom control or Storm prevention is a feature that limits the number of
broadcast and multicast packets going to the host and/or cutting through
to the other port. Since broadcast and multicast packets are sent over
all the ports of a switch they have the potential to create a storm
which drowns all other traffic on the network, in this regard this is a
very important feature for the switch.

Design
'''''''

Storm prevention is implemented on the two PRU's as a credit based
scheme. When the feature is enabled, every time a multicast or broadcast
packet is received a counter referred to as storm prevention credits is
decremented and the packet is sent to the host as well as cut through.
If the counter value is 0 then the packet is dropped. The counter is
stored on respective PRU DMEM's and is reset after a fixed period by the
Host. The combination of this period and credit value decides the rate
of acceptance/rejection.

The mechanism is shown below in the diagram

.. Image:: /images/Storm_Prevention_architecture_Industrial.jpeg

The Storm prevention implementation is similar in both PRU's but
implemented separately, so it's possible to turn it off selectively for
each port. As of now the multicast and broadcast storm prevention
functionalities are clubbed together but it is proposed to have them
separate in the future.

API Guide & Data Structures
''''''''''''''''''''''''''''

The main parent structure for Storm Prevention is

.. code-block:: c

    typedef struct {

     uint8_t suppressionEnabled;   /** enable/disable storm prevention*/
     uint16_t credits;             /** Number of packets allowed in a time interval*/

    } stormPrevention_t;

There is an instance of this structure for each port

API descriptions are only for information, developers are requested to
use corresponding `IOCTL <index_device_drv.html#ioctl>`__
calls. The IOCTL command for Learning/FDB modules is
***ICSS_EMAC_IOCTL_STORM_PREV_CTRL***

***Enabling Storm Prevention***  : The corresponding API for this is

.. code-block:: c

    void ICSS_EmacEnableStormPrevention(uint8_t portnum, ICSSEMAC_Handle icssEmacHandle)

Corresponding IOCTL Param value is *ICSS_EMAC_STORM_PREV_CTRL_ENABLE*

***Disabling Storm Prevention*** : Similar to enablement, variable set
to False. The corresponding API for this is

::

    void ICSS_EmacDisableStormPrevention(uint8_t portnum, ICSSEMAC_Handle icssEmacHandle)

IOCTL Param value is *ICSS_EMAC_STORM_PREV_CTRL_DISABLE*

***Resetting the counters*** : This is called inside **\_HwPktPoll**
which is the NDK tick function. The time period of this tick function
(default 100ms) in combination with **credits** value decides the rate
at which Storm Prevention works. This is called by default inside the
driver.

The corresponding API for this is

::

    void ICSS_EmacResetStormPreventionCounter(ICSSEMAC_Handle icssEmacHandle)

IOCTL Param value is *ICSS_EMAC_STORM_PREV_CTRL_RESET*

***Changing the rate*** : To change how many packets are accepted or
rejected change the value in the structure. At every iteration these
values are written to the data RAM by the
**ICSS_EmacResetStormPreventionCounter** API. The scheme through which
this occurs is explained in the design description above

The corresponding API for this is

::

    void setCreditValue(uint16_t creditValue, stormPrevention_t* stormPrevPtr)

IOCTL Param value is *ICSS_EMAC_STORM_PREV_CTRL_SET_CREDITS*

Usage
''''''

Most often Storm Prevention is the main reason for users not being able
to receive a packet, esp if the rate is configured incorrectly. So first
verify if it is enabled for that port. This can be done by

-  Checking structure variable : See the value of **suppressionEnabled**
   variable in the structure.
-  Checking memory : See the memory offset STORM_PREVENTION_OFFSET in
   the corresponding data RAM. The first bit of the byte location tells
   you whether the logic is enabled on the port.
-  Disabling Storm Prevention : This is the easiest and preferable for
   someone not using an emulator. Use the corresponding IOCTL call.

To quickly verify if the logic is indeed dropping packets, try sending
some broadcast packets at line rate to the device and check the value of
PRU statistics variable **stormPrevCounter**. See statistics section on
how to read this variable.

Statistics
""""""""""""

Statistics on ICSS Switch provide a great deal of information on what's
going on with the switch. They are enabled by default and provide
provide port specific statistics. They are also a great debugging tool
and should be the first thing a developer should look at if they suspect
any issue with Rx or Tx.

Design
''''''''

The Statistics are divided into

-  ***Statistics on PRU*** : Since the LLD functionality is implemented
   on the PRU's the majority of statistics are implemented on them. The
   count for each port is stored on the respective Data RAM's starting
   at the offset STATISTICS_OFFSET. The map is shown below
-  ***Statistics on Host*** : The packets coming to the Host are counted
   once again, this is useful for debugging purposes and to measure
   throughput (from the PRU to Host) if required. Some statistics like
   "Unknown protocol type" are only implemented on the Host.

Functionally the statistics are classified into

-  ***Rx/Tx related statistics*** : This includes count of broadcast,
   multicast and unicast packets and their derivatives. Only valid
   packets are part of this which means that an Rx packet which has been
   dropped because of storm prevention will not be counted.
-  ***Error Counters*** : This includes statistics such as Dropped
   frames, Rx/Tx errors etc.
-  ***Other statistics*** : Includes statistics related to 802.1
   CSMA/CD, number of link breaks etc.

A description of PRU statistics along with corresponding memory map is
given below.

align="center"
***PRU Statistics Description & Memory Map***
Name of Variable

Description

Name of Offset

Refer to *icss_emacSwitch.h*

Offset in PRU DRAM 0/1

**txBcast**

Number of broadcast packets sent

*TX_BC_FRAMES_OFFSET*

*0x1F00*

**txMcast**

Number of multicast packets sent

*TX_MC_FRAMES_OFFSET*

*0x1F04*

**txUcast**

Number of unicast packets sent

*TX_UC_FRAMES_OFFSET*

*0x1F08*

**txOctets**

Total number of octets sent, includes all packets

*TX_BYTE_CNT_OFFSET*

*0x1F0C*

**rxBcast**

Number of broadcast packets received

*RX_BC_FRAMES_OFFSET*

*0x1F10*

**rxMcast**

Number of multicast packets received

*RX_MC_FRAMES_OFFSET*

*0x1F14*

**rxUcast**

Number of unicast packets received

*RX_UC_FRAMES_OFFSET*

*0x1F18*

**rxOctets**

Total number of octets received, includes all packets

*RX_BYTE_CNT_OFFSET*

*0x1F1C*

**lateColl**

Number of packets that suffered collisions late into Tx

*LATE_COLLISION_OFFSET*

*0x1F20*

**singleColl**

Number of packets that suffered collision only once

*SINGLE_COLLISION_OFFSET*

*0x1F24*

**multiColl**

Number of packets that suffered collisions more than once

*MULTIPLE_COLLISION_OFFSET*

*0x1F28*

**excessColl**

Number of packets that suffered collisions more than 15 times

*EXCESS_COLLISION_OFFSET*

*0x1F2C*

**txOverFlow**

Number of times Tx queue overflowed

(This is not supported right now)

*TX_OVERFLOW_OFFSET*

*0x1F30*

**rxMisAlignmentFrames**

Number of frames with uneven number of bytes in an octet

(This is not tested)

*RX_MISALIGNMENT_COUNT_OFFSET*

*0x1F34*

**stormPrevCounter**

Number of packets dropped due to storm prevention

*STORM_PREVENTION_COUNTER*

*0x1F38*

**macRxError**

Number of packets with Rx MAC Error

*RX_ERROR_OFFSET*

*0x1F3C*

**SFDError**

Number of packets with incorrect SFD

*SFD_ERROR_OFFSET*

*0x1F40*

**defTx**

Number of packets deferred at least once due to CS high signal

*TX_DEFERRED_OFFSET*

*0x1F44*

**macTxError**

Number of packets facing Tx MAC Error

*TX_ERROR_OFFSET*

*0x1F48*

**rxOverSizedFrames**

Number of packets >1518 bytes

*RX_OVERSIZED_FRAME_OFFSET*

*0x1F4C*

**rxUnderSizedFrames**

Number of packets < 60 bytes

*RX_UNDERSIZED_FRAME_OFFSET*

*0x1F50*

**rxCRCFrames**

Frames with CRC/FCS Error

*RX_CRC_COUNT_OFFSET*

*0x1F54*

**droppedPackets**

Number of Received packets that were not transmitted because of link
loss

*RX_DROPPED_FRAMES_OFFSET*

*0x1F5C*

**tx64byte**

Transmitted frames with size <= 64 bytes

*TX_64_BYTE_FRAME_OFFSET*

*0x1F60*

**tx65_127byte**

Transmitted frames with size >= 65 bytes and <= 127 bytes

*TX_65_127_BYTE_FRAME_OFFSET*

*0x1F64*

**tx128_255byte**

Transmitted frames with size >= 128 bytes and <= 255 bytes

*TX_128_255_BYTE_FRAME_OFFSET*

*0x1F6C*

**tx256_511byte**

Transmitted frames with size >= 256 bytes and <= 511 bytes

*TX_256_511_BYTE_FRAME_OFFSET*

*0x1F70*

**tx512_1023byte**

Transmitted frames with size >= 512 bytes and <= 1023 bytes

*TX_512_1023_BYTE_FRAME_OFFSET*

*0x1F74*

**rx64byte**

Received frames with size <= 64 bytes

*RX_64_BYTE_FRAME_OFFSET*

*0x1F78*

**rx65_127byte**

Received frames with size >= 65 bytes and <= 127 bytes

*RX_65_127_BYTE_FRAME_OFFSET*

*0x1F7C*

**rx128_255byte**

Received frames with size >= 128 bytes and <= 255 bytes

*RX_128_255_BYTE_FRAME_OFFSET*

*0x1F80*

**rx256_511byte**

Received frames with size >= 256 bytes and <= 511 bytes

*RX_256_511_BYTE_FRAME_OFFSET*

*0x1F84*

**rx512_1023byte**

Received frames with size >= 512 bytes and <= 1023 bytes

*RX_512_1023_BYTE_FRAME_OFFSET*

*0x1F88*

API Guide & Data Structures
''''''''''''''''''''''''''''

As discussed above there are two data structures for Statistics.

#. PRU based
#. On Host

Shown below are the members of Host Statistics. The members of PRU
statistics are listed in the memory map.

.. code-block:: c

    typedef struct {

     volatile uint32_t txUcast;         /**Number of unicast packets sent*/
     volatile uint32_t txBcast;         /**Number of broadcast packets sent*/
     volatile uint32_t txMcast;         /**Number of multicast packets sent*/
     volatile uint32_t txOctets;            /**Number of bytes sent*/
     volatile uint32_t rxUcast;         /**Number of unicast packets rcvd*/
     volatile uint32_t rxBcast;         /**Number of broadcast packets rcvd*/
     volatile uint32_t rxMcast;         /**Number of multicast packets rcvd*/
     volatile uint32_t rxOctets;            /**Number of Rx packets*/
     volatile uint32_t rxUnknownProtocol;           /**Number of packets with unknown protocol*/
     volatile uint32_t linkBreak;           /**Number of link breaks*/

    }hostStatistics_t;

As one can see most of the members are identical to that of PRU
statistics (they are a subset) and if all packets are sent to the Host
then these member values for PRU and Host statistics should match.

API descriptions are only for information, developers are requested to
use corresponding `IOCTL <index_device_drv.html#ioctl>`__
calls. The IOCTL command for Statistics module is
***ICSS_EMAC_IOCTL_STATS_CTRL***

***Reading PRU Statistics***  : To fetch PRU statistics an M2M copy is
done from the PRU Data RAM to the PRU statistics structure on DDR. To
get the values correctly the memory layout on both sides should be
identical. Developers should not modify the member order in
**pruStatistics_t. Doing so can give incorrect results**

Host statistics are updated on the fly in the structure as packets are
received (ICSS_EmacUpdateRxStats) or transmitted
(ICSS_EmacUpdateTxStats) so there is no separate API to collate
them.

The corresponding API for this is

::

    void ICSS_EmacReadStats(uint8_t portNum, ICSSEMAC_Handle icssEmacHandle)

IOCTL Param value is *ICSS_EMAC_IOCTL_STAT_CTRL_GET*

***Clearing PRU and Host Statistics***  : To clear the values do memory
write to the structure memory, PRU data RAM and initialize to 0.

The corresponding API for this is

::

    void PurgeStats(uint8_t portNum, ICSSEMAC_Handle icssEmacHandle)

IOCTL Param value is *ICSS_EMAC_IOCTL_STAT_CTRL_CLEAR*

Usage
''''''''

Statistics are a great tool to debug issues on the switch. To get them
in the application use the IOCTL calls to get and clear statistics

While IOCTL calls provide access to statistics in the application. If
someone is using CCS then another quick way to see if there is any
activity on the Ports is to directly go to the PRU data RAM offset
*STATISTICS_OFFSET* and see the values directly in memory Refer Debug
guide on how to see data RAM values directly in CCS.

Memory Map
^^^^^^^^^^^

The memory map here refers to the Shared Data RAM memory map in ICSS. L3
map is not of much use to the developer while DDR map is dynamic and is
part of the application. The goal of providing this is to help the
developer in debugging. Based on the memory map one can directly look at
the memory in a CCS + Emulator environment and verify if driver/firmware
is working correctly.

The memory map can be found in *icss_emacSwitch.h* under
*os_drivers/lld/emac* and is common to firmware and driver builds

.. table::  ***ICSS Shared Memory Map***

   +-----------+-----------+-----------+-----------+-----------+-----------+
   | Shared    | Value     | PRU0 Data | Value     | PRU1 Data | Value     |
   | Memory    |           | RAM       |           | RAM       |           |
   | Offset    |           |           |           |           |           |
   +===========+===========+===========+===========+===========+===========+
   | 0x0000 -  | Buffer    | 0x0000 -  | Reserved  | 0x0000 -  | Reserved  |
   | 0x1C10    | Descripto | 0x0400    | for       | 0x0400    | for       |
   |           | r         |           | Future    |           | Future    |
   |           | Offsets   |           | Use       |           | Use       |
   |           | For Host  |           |           |           |           |
   |           | Queues    |           |           |           |           |
   +-----------+-----------+-----------+-----------+-----------+-----------+
   | 0x1C10-0x | Multicast | 0x0400-0x | Available | 0x0400-0x | Available |
   | 2010      | Filtering | 1EC0      | for       | 1EC0      | for       |
   |           | Table     |           | Protocol/ |           | Protocol/ |
   |           | (Disabled |           | Applicati |           | Applicati |
   |           | for EMAC) |           | on        |           | on        |
   +-----------+-----------+-----------+-----------+-----------+-----------+
   | 0x2010-0x | Reserved  | 0x1EC0-0x | Port      | 0x1EC0-0x | Port      |
   | 2400      | for       | 1F00      | Queue     | 1F00      | Queue     |
   |           | Future    |           | Offsets   |           | Offsets   |
   |           | Use       |           |           |           |           |
   +-----------+-----------+-----------+-----------+-----------+-----------+
   | 0x2400-0x | Available | 0x1F00-0x | Port0     | 0x1F00-0x | Port1     |
   | 3000      | for       | 1F8C      | Statistic | 1F8C      | Statistic |
   |           | Protocol/ |           | s         |           | s         |
   |           | Applicati |           | (Map      |           | (Map      |
   |           | on        |           | provided  |           | provided  |
   |           |           |           | `above <h |           | `above <h |
   |           |           |           | ttp://pro |           | ttp://pro |
   |           |           |           | cessors.w |           | cessors.w |
   |           |           |           | iki.ti.co |           | iki.ti.co |
   |           |           |           | m/index.p |           | m/index.p |
   |           |           |           | hp/ICSS_E |           | hp/ICSS_E |
   |           |           |           | MAC_LLD_d |           | MAC_LLD_d |
   |           |           |           | evelopers |           | evelopers |
   |           |           |           | _guide#De |           | _guide#De |
   |           |           |           | sign_3>`_ |           | sign_3>`_ |
   |           |           |           | _)        |           | _)        |
   +-----------+-----------+-----------+-----------+-----------+-----------+
   |           |           | 0x1F8C    | Port0     | 0x1F8C    | Port1     |
   |           |           |           | Storm     |           | Storm     |
   |           |           |           | Preventio |           | Preventio |
   |           |           |           | n         |           | n         |
   |           |           |           | Control   |           | Control   |
   |           |           |           | Variable  |           | Variable  |
   +-----------+-----------+-----------+-----------+-----------+-----------+
   |           |           | 0x1F90    | Port0     | 0x1F90    | Port1     |
   |           |           |           | Link      |           | Link      |
   |           |           |           | Speed     |           | Speed     |
   |           |           |           | 0x64 -    |           | Same as   |
   |           |           |           | 100Mbps   |           | Port0     |
   |           |           |           |           |           |           |
   |           |           |           | 0xA -     |           | Any other |
   |           |           |           | 10Mbps    |           | value is  |
   |           |           |           |           |           | illegal   |
   +-----------+-----------+-----------+-----------+-----------+-----------+
   |           |           | 0x1F94    | Port0     | 0x1F94    | Port1     |
   |           |           |           | Link      |           | Link      |
   |           |           |           | Status    |           | Status    |
   |           |           |           | 0x1 -     |           | Same as   |
   |           |           |           | Link Up   |           | Port0     |
   |           |           |           |           |           |           |
   |           |           |           | 0x0 -     |           |           |
   |           |           |           | Link Down |           |           |
   +-----------+-----------+-----------+-----------+-----------+-----------+
   |           |           | 0x1F9A    | Port0     | 0x1F9A    | Port1     |
   |           |           |           | Control   |           | Control   |
   |           |           |           | 0x1 - Rx  |           | Same as   |
   |           |           |           | Disabled  |           | Port0     |
   |           |           |           |           |           |           |
   |           |           |           | 0x0 - Rx  |           |           |
   |           |           |           | Enabled   |           |           |
   +-----------+-----------+-----------+-----------+-----------+-----------+
   |           |           | 0x1FA0    | Port0 MAC | 0x1FA0    | Port1 MAC |
   |           |           |           | ID        |           | ID        |
   |           |           |           | 6 bytes   |           | 6 bytes   |
   +-----------+-----------+-----------+-----------+-----------+-----------+


OS and TCP/IP
^^^^^^^^^^^^^^^

RTOS
"""""

The SDK uses
`SYS/BIOS <http://processors.wiki.ti.com/index.php/Category:SYSBIOS>`__
as it's RTOS. Configuration for the RTOS is done through RTSC tool chain
integrated with CCS. SYS/BIOS is provided free of cost and is a very
capable RTOS for typical use cases with minimal latency.

The driver is written in a manner such that there is very little
dependency on the Operating System. All dependence on SYS/BIOS is
abstracted to OSAL (Operating System Abstraction Layer) and developers
are integrate their own operating systems.

OSAL consists of

#. Interrupt management
#. Task and Semaphore management, Mailbox
#. Management of peripherals like DMTimer, BIOS Timers

The *osdrv* layer deals with RTOS and other OS related tasks in general,
within this layer the relevant files which deal with OSAL layer are
***osdrv_osal.c*** and ***osdrv_osal.h***. Developers are requested to
port the API's within these two files to their own Operating System.


TCP/IP
""""""""

The Industrial SDK uses `NDK <http://www.ti.com/tool/NDKTCPIP>`__ as
it's TCP/IP stack. API reference guide
`here <http://www.ti.com/lit/ug/spru524i/spru524i.pdf>`__. Like SYS/BIOS
the module is imported externally through RTSC (refer Debug Guide) and
managed through the application configuration file (***am335x_app.cfg***
and ***am437x_app.cfg***)

NDK recommends it's own abstraction layer which is called NIMU (Network
Interface Management Unit). This layer is implemented in the driver.
Relevant source files are

-  *icss_ethdriver.c*
-  *icss_nimu_eth.c*
-  *icss_switch_emac.c*

Understanding the NIMU layer helps in porting another TCP/IP stack to
the example. The NIMU layer is explained in this
`guide <http://www.ti.com/lit/ug/sprufp2a/sprufp2a.pdf>`__

`Porting
guide <http://processors.wiki.ti.com/index.php/ICSS_EMAC_LLD_developers_guide#Porting_ICSS_EMAC_LLD>`__
covers all aspects of using a custom TCP/IP stack to the EMAC LLD
example.

PRUSS & EMAC Handle
^^^^^^^^^^^^^^^^^^^^

The ICSS EMAC Handle is a main driver handle which provides access to
all members, variables, registers and addresses in the SoC.

It is the application's task to allocate memory for the handle and pass
it to the driver initialization API. The handle is also required as a
parameter for most of the external API's and all IOCTL calls in the
driver so it's important to understand it's members.

The members of the EMAC Handle are discussed in detail
`here <http://processors.wiki.ti.com/index.php?title=SYSBIOS_Industrial_SDK_Migration_guide_from_1.1_to_2.1#ICSS_EMAC_LLD>`__

The sample code for Handle allocation and initialization (from the
example application) is shown below

.. code-block:: c

    /*Declare the EMAC Handle*/
    ICSSEMAC_Handle emachandle;
    /*Declare the PRUSS Handle*/
    PRUICSS_Handle handle;
    /*Allocate memory for EMAC and PRUSS Handle*/
    handle = (PRUICSS_Handle)malloc(sizeof(PRUICSS_Config));
    handle->object = (PRUICSS_V1_Object*)malloc(sizeof(PRUICSS_V1_Object));
    handle->hwAttrs = (PRUICSS_HwAttrs*)malloc(sizeof(PRUICSS_HwAttrs));
    emachandle = (ICSSEMAC_Handle)malloc(sizeof(ICSSEMAC_Config));
    /*Initialize the EMAC*/
    ICSSEmacDRVInit(emachandle, 0);
    /*Initialize PRUSS*/
    PRUSSDRVInit(handle); /* ICSS_M instance 0 */
    /*Assign PRU handle to EMAC handle making it the parent structure*/
    ((ICSSEMAC_Object*)emachandle->object)->pruIcssHandle = handle;
    ((ICSSEMAC_Object*)emachandle->object)->emacInitcfg = switchEmacCfg;

IOCTL
^^^^^^^

IOCTL implementation for the switch drivers is identical to the
Unix/Linux based IOCTL calls. They provide the application a convenient
method to access driver/kernel space parameters or modify them.

Developers are expected to familiarize themselves with the full list of
IOCTL calls so that they can utilize all the features provided. This is
even more important when working in an Application/OS kind of
environment where access to an emulator is not available.

Design
"""""""

The primary IOCTL call is through the API **ICSS_EmacIoctl** which is
implemented in the file icss_emacFwInit.c An IOCTL call uses two
parameters to find out which driver API to call

#. **ioctlCommand** : Is used to locate the module (Statistics/ Port
   control etc) which should be called.
#. **ioctlParams** : Is used to give module specific instructions

***ioctlParams*** consists of

-  **command** : Indicates which specific API to execute
-  **ioctlVal** : Sometimes the API may require specific input, this is
   used to provide that.

For example to disable receive functionality on a port the following
code is used. This code is part of Link interrupt functionality where
receive is disabled when PHY detects a link down.

.. code-block:: c

    ioctlvalue = ICSS_EMAC_IOCTL_PORT_CTRL_DISABLE;
    ioctlParams.ioctlVal = &ioctlvalue;
    ICSS_EmacIoctl(icssEmacHandle, ICSS_EMAC_IOCTL_PORT_CTRL, ICSS_EMAC_PORT_1, (void*)&ioctlParams);

Here *ICSS_EMAC_IOCTL_PORT_CTRL* refers to the ***ioctlCommand*** while
*ICSS_EMAC_IOCTL_PORT_CTRL_DISABLE* is the ***command*** part of
**ioctlParams** which tells which action to perform, in this case
disabling the port. Port selected is *ICSS_EMAC_PORT_1* which refers to
Port 1.

A complete list of commands and actions is given below.

API Guide & Data Structures
"""""""""""""""""""""""""""""

IOCTL Command structure

.. code-block:: c

     typedef struct ICSSEMAC_IoctlCmd {
       uint8_t command;
       uint8_t* ioctlVal;
     }ICSSEMAC_IoctlCmd;

There is only one API for IOCTL. It's defined below

.. code-block:: c

    uint8_t ICSS_EmacIoctl(ICSSEMAC_Handle icssEmacHandle, uint32_t ioctlCommand, uint8_t portNo, void *ioctlParams)

The possible values for ***ioctlCommand*** are

-  *ICSS_EMAC_IOCTL_PORT_CTRL* : Select Port Control Operations.
   Enable/Disable Rx for the specified port.
-  *ICSS_EMAC_IOCTL_LEARNING_CTRL* : Select Learning/FDB module.
-  *ICSS_EMAC_IOCTL_STORM_PREV_CTRL* : Select Storm Prevention module.
-  *ICSS_EMAC_IOCTL_STATS_CTRL* : Select Statistics module.
-  *ICSS_EMAC_IOCTL_TTS_CTRL* : Select Time Triggered Send Configuration
   module. Enable/Disable TTS for the specified port.
-  *ICSS_EMAC_IOCTL_TTS_STATUS_CTRL* : Select Time Triggered Send Query
   module. Get TTS status and other details for the specified port from
   PRU firmware.

Possible values for ***ioctlParams*** are

-  **ICSS_EMAC_IOCTL_LEARNING_CTRL** : Refer to Learning/FDB API's

   -  *ICSS_EMAC_LEARN_CTRL_UPDATE_TABLE* : Add an entry to the Hash
      table.
   -  *ICSS_EMAC_LEARN_CTRL_CLR_TABLE* : Clear the Learning Table for
      the specified port.
   -  *ICSS_EMAC_LEARN_CTRL_AGEING* : Age out old entries from the
      table.
   -  *ICSS_EMAC_LEARN_CTRL_FIND_MAC* : Find the port number given a MAC
      ID.
   -  *ICSS_EMAC_LEARN_CTRL_REMOVE_MAC* : Remove a MAC ID from the
      Learning Table
   -  *ICSS_EMAC_LEARN_CTRL_INC_COUNTER* : Age the entries with time by
      calling this periodically
   -  *ICSS_EMAC_LEARN_CTRL_INIT_TABLE* : Initialize the learning table
   -  *ICSS_EMAC_LEARN_CTRL_SET_PORTSTATE* : Set the Port state to value
      defined by the enum type **portState**

-  **ICSS_EMAC_IOCTL_STATS_CTRL** : Refer to Statistics API's

   -  *ICSS_EMAC_IOCTL_STAT_CTRL_GET* : Get the statistics
   -  *ICSS_EMAC_IOCTL_STAT_CTRL_CLEAR* : Clear all stat counters

-  **ICSS_EMAC_IOCTL_STORM_PREV_CTRL** : Refer to Storm prevention API's

   -  *ICSS_EMAC_STORM_PREV_CTRL_ENABLE* : Enable Storm Prevention
   -  *ICSS_EMAC_STORM_PREV_CTRL_DISABLE* : Disable Storm Prevention
   -  *ICSS_EMAC_STORM_PREV_CTRL_SET_CREDITS* : Set how many BC/MC
      packets are allowed in a period of 100 NDK Ticks (Time period of
      **\_HwPktPoll()**)
   -  *ICSS_EMAC_STORM_PREV_CTRL_INIT* : Initialize Storm Prevention
   -  *ICSS_EMAC_STORM_PREV_CTRL_RESET* : Renew the storm prevention
      counters, this allows more packets to come through once existing
      credits have expired. This must be called periodically in
      **\_HwPktPoll()**

-  **ICSS_EMAC_IOCTL_PORT_CTRL** : For Rx Enable/Disable operations.
   There are no sub-commands here. Whether to enable or disable is
   decided by the value of ***ioctlVal***


Usage
"""""""

Using IOCTL to debug the issues is encouraged. This is easier than
trying to connect an emulator and reading the values at run time. There
are numerous instances of it's usage. A quick search for the API
**ICSS_EmacIoctl** throughout the code reveals numerous examples. One of
them pertaining to Storm Control module is shown below.

In this example the storm prevention counters are reset in PRU Data RAM
using IOCTL. The **if/else** refers to Switch or EMAC mode, rest of the
code is self-explanatory

.. code-block:: c

     ioctlParams.command = ICSS_EMAC_STORM_PREV_CTRL_RESET;
     /*Reset the credit values used for Storm prevention*/
     if(ICSS_EMAC_MODE_SWITCH == ((ICSSEMAC_Object*)(pi->nimuDrvHandle)->object)->emacInitcfg->portMask)
     {
       strmPreventionEnable1 = (stormPrevention_t*)(((ICSSEMAC_Object*)(pi->nimuDrvHandle)->object)->stormPrevPtr);
       strmPreventionEnable2 = (stormPrevention_t*)(((ICSSEMAC_Object*)(pi->nimuDrvHandle)->object)->stormPrevPtr +1);
       if(strmPreventionEnable1->suppressionEnabled ||   strmPreventionEnable2->suppressionEnabled)
        ICSS_EmacIoctl(pi->nimuDrvHandle, ICSS_EMAC_IOCTL_STORM_PREV_CTRL, NULL, (void*)&ioctlParams);
     }
     else
     {
       strmPreventionEnable1 = (stormPrevention_t*)(((ICSSEMAC_Object*)(pi->nimuDrvHandle)->object)->stormPrevPtr);
       if(strmPreventionEnable1->suppressionEnabled)
        ICSS_EmacIoctl(pi->nimuDrvHandle, ICSS_EMAC_IOCTL_STORM_PREV_CTRL, NULL, (void*)&ioctlParams);
     }

Time Triggered Send
^^^^^^^^^^^^^^^^^^^^^

The EMAC Time Triggered Send (TTS) is used to expand classical Ethernet
to meet deterministic, time-critical or safety-relevant conditions. TTS
reduces the transmission jitter from 10us range to 40ns. TTS can be
dynamically enabled and disabled by the Host. We have two well defined
TTS APIs which control all TTS related EMAC aspects. Developers are
advised to access these APIs using the EMAC IOCTL implementation as
explained in the `IOCTL <index_device_drv.html#ioctl>`__ section
previously.

TTS Design Overview
"""""""""""""""""""""

TTS is designed to facilitate transmission of packets at pre-defined
cyclic instants/triggers. The `TTS API Details and Data
Structures <index_device_drv.html#tts-api-details-and-data-structures>`__
are explained below but in a broad sense we can say that while
initializing TTS, the application must provide the first cyclic trigger
and the cycle period. The PRU firmware then sets cyclic triggers
repeatedly and shall send the packets cyclically provided that they are
queued before the trigger. The following timing diagram explains the use
of TTS.

Each cycle shall have a configuration time (as shown in the figure
above) before each trigger. This configuration time is used to setup the
start trigger and end trigger of current cycle in the PRU firmware. If
the application does not set a suitable (long enough) configuration
time, the PRU and perhaps even the EMAC Driver TTS API may not get
enough time to setup and initialize TTS. This might result in improper
functionality. The configuration time shall also be provided during
initialization and shall be application specific. For example, if a
response packet is to be received for the cyclic packet sent at trigger
T1 and based on that response packet the next cyclic packet shall be
generated, then the developer can increase/decrease configuration time
accordingly to ensure that the next cyclic packet is ready before
trigger T2 which shall in-turn be based on when the response packet is
received.

Queue 0 (high priority queue) is reserved as the real-time queue. All
packets in queue 0 are cyclic packets. On the other hand, packets from
other queues are acyclic packets. Cyclic packets are sent at triggered
instances, whereas acyclic packets are sent based on time availability,
as shown in the figure below.

The time availability check for cyclic packets means to basically check
whether the acyclic packet can be transmitted such that its transmission
does not overlap the next cyclic trigger, considering the size of the
acyclic packet. Such a situation is represented as “Undesired Behaviour”
in the above figure and PRU firmware ensures that this never happens.
Only one cyclic packet will be sent out in each cycle irrespective of
the number of cyclic packets available in Queue 0. There is no
restriction on the number of acyclic packets sent out in each cycle but
it is contingent on time availability. Cyclic packets must be queued in
Queue 0 before the trigger instant else two erroneous situations are
possible:

#. If the firmware finds a packet in any other low priority queue, it
   will send the acyclic packet. Once an acyclic packet has been
   transmitted in a given cycle, no cyclic packet will be transmitted in
   that cycle. So, if the cyclic packet is not queued on time, it will
   miss the cycle and will be transmitted in the next cycle.
#. If all the queues are empty and a cyclic packet is inserted late, it
   will result in increased jitter.

The above two situations are demonstrated in the figure below.

In the above figure, the PRU firmware ensures that the first two
situations never occur but the application needs to take care of the
third situation, i.e., by queueing the cyclic packet on time.

The PRU firmware makes the following assumptions regarding TTS:

#. The cycle period is long enough to be able to transmit any cyclic
   packet in queue 0. Failure to ensure this will cause the cyclic
   packet with size greater than the allowed size (as per the period),
   and any cyclic packets following it, to remain in the queue.
#. The configuration time provided (using ICSS EMAC IOCTL) is sufficient
   for the PRU to configure the next cycle. PRU should typically need a
   maximum of 10us to configure the next cycle.
#. If the host keeps queuing packets irrespective of the fact whether
   the packet has been transmitted by the firmware (in accordance with
   the preset triggered intervals), the packets might get dropped at the
   driver level if the queue is full. It is assumed that this is taken
   care of at the host level.

TTS API Details and Data Structures
"""""""""""""""""""""""""""""""""""""

TTS has the following APIs, which are accessed using EMAC IOCTL
implementation as explained in the IOCTL section previously.

.. code-block:: c

    int8_t ICSS_EmacTTS(const ICSS_EmacTTSConfig* ttsConfig)

This API is used to enable/disable time triggered send for Queue 0
frames.

.. code-block:: c

    int8_t ICSS_EmacTTSGetStatus(ICSS_EmacTTSQuery* ttsQuery)

This API is used to query time triggered send details, status and TTS
parameter values from PRU firmware.

The TTS parameter structure is explained below:

.. code-block:: c

    typedef struct ICSS_EmacTTSConfig_s {
      ICSSEMAC_Handle icssEmacHandle;
      uint8_t portNumber;
      uint64_t cycleStartTime;
      uint32_t cyclePeriod;
      uint32_t configTime;
      uint8_t statusTTS;
      uint8_t cycTxSOFStatus;
    } ICSS_EmacTTSConfig;

-  *icssEmacHandle*: EMAC handle for concerned EMAC instance and port.
-  *portNumber*: Port number for which TTS needs to be enabled/disabled.
-  *cycleStartTime*: A future IEP counter value at which the first
   cyclic packet will be transmitted.
-  *cyclePeriod*: TTS cycle period.
-  *configTime*: Configuration time for PRU to setup upcoming TTS cycle.
-  *statusTTS*: Enable/Disable TTS. Enable = 1, Disable = 0.
-  *cycTxSOFStatus*: Enable/Disable storing transmit start-of-frame
   timestamp for cyclic packets in memory. Enable = 1, Disable = 0.

The TTS query structure is as explained below:

.. code-block:: c

    typedef struct ICSS_EmacTTSQuery_s {
      ICSSEMAC_Handle icssEmacHandle;
      uint8_t portNumber;
      uint8_t statusTTS;
      uint8_t missedCycle;
      uint8_t insertCycFrameNotification;
      uint8_t cycTxSOFStatus;
      uint32_t missedCycleCounter;
      uint64_t cycTxSOF;
    } ICSS_EmacTTSQuery;

-  *icssEmacHandle*: EMAC handle for concerned EMAC instance and port.
-  *portNumber*: Port number for which TTS query needs to be performed.
-  *statusTTS*: Whether TTS is enabled/disabled for given port. Enabled
   = 1, Disabled = 0.
-  *missedCycle*: Whether any cyclic packet missed a cycle. Missed = 1,
   Did not miss = 0.
-  *insertCycFrameNotification*: Notification to state that it’s time to
   insert cyclic packet. If it’s time = 1, else = 0.
-  *cycTxSOFStatus*: Whether storing transmit start-of-frame timestamp
   for cyclic packets in memory is enabled/disabled. Enabled = 1,
   Disabled = 0.
-  *missedCycleCounter*: Number of cycles missed by cyclic packets.

The application shall update the elements of the ICSS_EmacTTSConfig
structure and pass its pointer to EMAC IOCTL with appropriate command to
enable/disable TTS. On the other hand, the application shall only update
the icssEmacHandle and portNumber elements of the ICSS_EmacTTSQuery
structure and pass its pointer to EMAC IOCTL with appropriate command to
retrieve the details from PRU firmware. The driver TTS API
(ICSS_EmacTTSGetStatus) shall then update the elements of the structure
with appropriate values.

TTS can be enabled/disabled using EMAC IOCTL as follows:

For Enable:

.. code-block:: c

    ICSSEMAC_IoctlCmd ioctlParams;
    ICSS_EmacTTSConfig ttsConfig;
    uint32_t iepRegsBase;
    int8_t ret;

    ioctlParams.command = 0;
    ioctlParams.ioctlVal = (void *)(&ttsConfig);

    ttsConfig.icssEmacHandle = icssEmacHandle;
    ttsConfig.cycTxSOFStatus = ICSS_EMAC_TTS_CYC_TXSOF_ENABLE;
    ttsConfig.portNumber = portNumber;
    ttsConfig.configTime = ICSS_EMAC_TTS_CONFIG_TIME;
    ttsConfig.cyclePeriod = cyclePeriod;
    ttsConfig.statusTTS = ICSS_EMAC_TTS_ENABLE;

    iepRegsBase = (((ICSS_EmacHwAttrs*)icssEmacHandle->hwAttrs)->emacBaseAddrCfg)->prussIepRegs;

    /*  Reading IEP Counter Value.  */
    iepCounterVal = (*((uint64_t*)(iepRegsBase + CSL_ICSSIEP_COUNT_REG0)));

    /*  Calculating cycle start value by adding 100us to counter value. */
    ttsConfig.cycleStartTime = (uint64_t)(iepCounterVal + 100000);

    /*  Enabling time triggered send.   */
    ret = ICSS_EmacIoctl(icssEmacHandle, ICSS_EMAC_IOCTL_TTS_CTRL, portNumber, &ioctlParams);
    assert(ret == 0);

For Disable:

.. code-block:: c

    ICSSEMAC_IoctlCmd ioctlParams2;
    ICSS_EmacTTSConfig ttsConfig;
    int8_t ret;

    /*  Setting tts status to disable (Port 1)  */
    ttsConfig.icssEmacHandle = icssEmacHandle;
    ttsConfig.statusTTS = ICSS_EMAC_TTS_DISABLE;
    ttsConfig.cyclePeriod = 0;
    ttsConfig.configTime = 0;
    ttsConfig.cycleStartTime = 0;
    ttsConfig.cycTxSOFStatus = ICSS_EMAC_TTS_CYC_TXSOF_DISABLE;
    ttsConfig.portNumber = portNumber;

    ioctlParams2.command = 0;
    ioctlParams2.ioctlVal = (void *)(&ttsConfig);

    /*  Disabling time triggered send on PORT 1 (PRU0). */
    ret = ICSS_EmacIoctl(icssEmacHandle, ICSS_EMAC_IOCTL_TTS_CTRL, portNumber, &ioctlParams2);
    assert(ret == 0);

TTS Cyclic Frame Notification
"""""""""""""""""""""""""""""""

The PRU firmware has been designed to notify the Host when it’s time to
insert the cyclic packet. This helps the Host to queue the cyclic packet
well before trigger time and avoid any unnecessary jitter or any other
erroneous situations as mentioned previously. The firmware does this in
two ways:

Polling Mode
''''''''''''''

-  In this mode the firmware sets a status bit when it’s time to insert
   the cyclic frame and this bit cleared when the time to insert the
   cyclic frame is over or the firmware has found a cyclic frame in
   Queue 0.
-  This status bit can be queried using the EMAC IOCTL and is reflected
   in insertCycFrameNotification element of the ICSS_EmacTTSQuery
   structure.
-  If it’s time, insertCycFrameNotification = 1, else
   insertCycFrameNotification = 0.
-  The application must then continuously poll for this status by
   repeating EMAC IOCLT calls and querying TTS status.
-  Once insertCycFrameNotification = 1, the application must queue the
   cyclic frame in Queue 0.

Interrupt Mode
''''''''''''''''

-  In this mode, in addition to setting the status bit as in polling
   mode, the firmware has the capability to give an interrupt to the
   Host when it’s time to insert a cyclic frame.
-  The interrupt feature should be first enabled as follows during EMAC
   Driver Initilization.

::

    ICSS_EmacInitConfig* switchEmacCfg;
    switchEmacCfg = (ICSS_EmacInitConfig*)malloc(sizeof(ICSS_EmacInitConfig));
    switchEmacCfg->ICSS_EmacTTSEnableCycPktInterrupt = ICSS_EMAC_TTS_CYC_INTERRUPT_ENABLE;

-  Also, proper interrupt mapping should be done as explained earlier in
   this guide.
-  Interrupt callback functions should also be registered for all
   concerned EMAC handles using the following API:

::

    ICSS_EmacRegisterHwIntTTSCyc(emachandle, (ICSS_EmacCallBack)ttsCycPort1Callback);

-  Interrupts should also be enabled. Please refer to example ICSS EMAC
   applications from Processor SDK RTOS for further details.
-  Once the PRU firmware throws an interrupt, the registered callback
   function is called and this is where the application shall queue the
   cyclic packet to Queue 0.

ICSS EMAC LLD Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ICSS EMAC LLD is dependent on the Application/Transport layer for its
proper functioning. These dependencies have been consolidated and
exported to the application layer (example) to make it easy for
developer to integrate the LLD with their own RTOS and TCP/IP stack.

Interrupt Configuration
""""""""""""""""""""""""

ICSS EMAC LLD expects the Interrupt configuration to come from
Application/Transport layer. The interrupt configuration is explained in
detail in the interrupts `section <index_device_drv.html#id58>`__.
Please refer to it for more details.

The LLD makes use of two interrupts for copying packets from the queues
to the TCP/IP stack.

Rx Interrupt
''''''''''''''

The ICSS EMAC LLD depends on the Rx interrupt for receiving packets.The
application should do the interrupt creation and should use the API
**ICSS_EmacRxInterruptHandler** as the ISR.This will enable the ICSS
EMAC LLD to receive packets. The user should make sure the arm interrupt
(Rx) is mapped to correct PRUSS Event. The PRUSS Event that is used for
Rx will be determined by the firmware which will be used along with the
ICSS EMAC LLD

Link Interrupt
'''''''''''''''

Link Interrupt informs the ICSS EMAC LLD of any Link state change. This
is where the LLD informs the firmware about the Link status and the Phy
configuration.The LLD expects single interrupt for both Ports. In case
the Interrupt mechanism is not available, the application should call
**ICSS_EmacLinkISR** whenever there is a link change.

Learning module Increment counter implementation
"""""""""""""""""""""""""""""""""""""""""""""""""

This is required for Switch implementation only. The application needs
to call the IOCTL periodically, this is already done by the NDK. Refer
to the API `section <index_device_drv.html#api-guide-data-structures>`__
of Learning for more details.

MDIO Configurations
"""""""""""""""""""""

ICSS EMAC LLD does not do any of the MDIO configurations. It expects the
application to do following MDIO operations

-  MDIO Initialization -
-  MDIO Link Interrupt enable if MDIO Link interrupt is used

NOTE: Please refer to ti/drv/icss_emac/test/src/test_mdio.c for details
of how to initialize the MDIO sub-system and how to enable MDIO link
interrupts. This file contains a set of MDIO test APIs which are used by
the icss emac loopback unit tests.

EMAC Configuration and How To
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Network related
""""""""""""""""""

How to configure IP address and other IPv4 parameters
'''''''''''''''''''''''''''''''''''''''''''''''''''''''

IP address, network mask and other params can be set through the NDK
configuration file. See
`here <http://processors.wiki.ti.com/index.php/SYSBIOS_Industrial_SDK_02.01.00.01_User_Guide#Ethernet_MAC>`__

.. rubric:: How to configure MAC address
   :name: How-to-configure-MAC-address

MAC address is variable macId in the configuration ICSSEMAC_InitConfig. It can
be set as per the application requirements. The following excerpt from
ethernet_mac example shows how to do this

::

    /*Get MAC address from eFUSE*/
    SOCCtrlGetPortMacAddr(1,lclMac);
    /*Assign MAC ID for that particular port*/
    switchEmacCfg->macId = lclMac;

