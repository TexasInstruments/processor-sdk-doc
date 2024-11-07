.. http://processors.wiki.ti.com/index.php/Processor_SDK_HSR_PRP


Duplicate algorithm and table
-----------------------------
Handling duplicate frames is one of the main tasks in HSR and PRP. The
LRE must not provide the duplicate of a frame to its upper layer in
order to offload the processor. The algorithm for discarding duplicates
is not specified in IEC 62439-3. However, the standard mandates that the
algorithm must be designed such that it never rejects a legitimate
frame, while occasional acceptance of a duplicate can be tolerated.

In HSR, additionally to discarding duplicates destined to the host, a
discard operation should also be used to prevent frames from looping in
the network. A looping frame is a frame that is never discarded in any
node of the network and therefore it keeps looping indefinitely.
Normally, such a frame should be dropped by its source node. The
function handles the case when a defective HSR device does not filter
correctly according to source/destination address. This operation is
less critical than the host duplicate discard. It is also specified that
any duplicate discard method shall be able to forget an entry identified
by the source MAC address and the sequence number after a time
EntryForgetTime (default 400ms).

A table holds entries representing frames that have been registered in
the LRE, each entry is represented bya frame signature. The signature
consists of the source MAC address and the 16 bit sequence number. The
sequence number value is incremented by 1 when a frame and its duplicate
are sent by a source in an HSR network. This signature allows
identifying a frame uniquely. When a frame is received, the list is
searched by comparing the frame signature with all entries in the table.
If such an entry is found, the frame is a duplicate and shall be
discarded. If no entry exists, the frame is the first one received and
needs to be forwarded to the application and/or – in case of HSR - to
the other port. With a successful forwarding process (frame received
with no error), a new entry with the signature of that frame is created
in the table.

A linear lookup process is too time consuming; thus Hash algorithms are
used to decrease the search time.

Port to Host Duplicate Table
----------------------------

It is used to prevent sending duplicate frames to the upper layers. This
table is common for both PRUs. Resource sharing implies that collision
(two PRUs accessing the same data) must be handled. Since the table is
common to both PRUs, the host duplicate rejection must be done after the
EOF is detected in order to avoid rejecting legitimate frames.

Port to Port Duplicate Table
----------------------------

A PRU forwards the frames received from one HSR port to the other HSR
port, unless the frame was sent already. Each PRU has its own port
duplicate table. A search operation can start before the EOF is detected
since the table is not shared between the PRU and is not subject to any
modification during the reception of a frame. In order to minimize the
load of the PRU after EOF reception, the search operation in the port
duplicate table is executed during frame reception. Moreover, this
allows to quickly detecting if the frame should be discarded early in
the reception process. An insertion in the table is still made only
after the EOF is detected, but the operation is much faster since the
result of the search operation can used.

Node Table
-----------

The node table is a central element of the HSR/PRP mechanism although
the standard declares node tables optional. This firmware implements
node tables for HSR and PRP. Node table handling is implemented in the
PRU and comprises of registering incoming supervision and
non-supervision-frames as well as ageing and deleting of old entries.
The standard requires updating the node table when a supervision frame
is received. Accessing the node table is thus not critical since
supervision frames are sent only every 2 seconds. For HSR, to maintain
statistics for each source node of the network and to facilitate
debugging, the implementation updates the node table for each frame
received by the host from a source that has previously sent a
supervision frame. A further advantage of this approach is having a
similar implementation for HSR and PRP. Indeed, the PRP Standard
requires updating the node table, if implemented, for all the incoming
frames in order to keep track of the traffic contented to each redundant
LAN. The node table is accessible by the host for management purposes.
Update- and register operations in the table should be done when the
frame is completely received in order to avoid registering erroneous
frames.

The node table search/update operation is very critical since it is
resource/time consuming (maximum NODE\_TABLE\_SIZE is 256 entries). In
the worst case scenario (node table full), a linear lookup operation in
the receiving task could load the PRU too much and in consequence could
cause Rx overflow or TX underflow. Moreover the node table is common to
both PRUs and since it is accessed often, the resource-sharing
management has additional impact on the latency. Optimized linear tables
were considered, but the timing remained too critical in the worst case
scenario. Hash tables are not considered because it is not allowed to
lose entries due to collisions. The implemented solution is a sorted
table with a two layer table structure. This allows to significantly
optimize the lookup time especially when the table has lots of valid
entries.

It is important to notice that in a normal HSR case scenario there are -
in average - significantly more successful lookup operations (MAC
address found in the table) than insertion and deletion operations.
Indeed, insertion operations are only made with a supervision frame.
This assumption cannot be made for PRP since all frames can create an
entry in the node table. The design is therefore optimized according to
this assumption.

Frame duplication from the host
-------------------------------

Frames sent by the host must be duplicated and should be sent to both
ports nearly at the same time for HSR and PRP. In a simple approach, the
host stores the frame in the queue of one PRU, the PRU then waits until
both ports are available and finally sends the frame at the same time
via both ports. However, this solution is not resource efficient and it
increases the latency of one PRU when waiting for the PORT to be ready.
Therefore, a solution that off-loads the PRU from the duplication task
is implemented: the host driver duplicates the frames and puts a copy to
each PRU queue.

The implementation is however not straightforward:

Since the frames are not “linked” to each other, there is no guarantee
that the frames are sent by both PRUs within a short interval. The host
could control the queue status and only push the frames in the highest
priority queue of both PRU when the queues are free. This would force
each PRU to send the frame and its duplicate next. Nevertheless, for HSR
this solution removes the prioritization of the frame circulating in the
HSR ring as a PRU could buffer a high priority frame from the ring due
to a lower priority frame sent by the host. Frames circulating in the
ring are to be treated with higher priority than frames sent by the
host. There is a compromise to be found.

The solution is the following: The host driver duplicates the frame and
puts the duplicates in the queues of each PRU. The queue is selected
based on the priority of the frame. Each PRU handles the frame
independently and we only have the assurance that each frame will be
sent out within an unknown interval. The drawback of this solution is
the lack of control on when each frame will be sent out. The interval
can be bigger than one maximum sized Ethernet frame in this case.

Supervision Frame
------------------

Incoming supervision frames are received and processed by the PRU. On
reception of a frame, the PRU updates the node table and the statistic
counters. For HSR, if the received supervision frame originates from the
receiver (i.e. it traversed the whole ring) it is discarded. Otherwise
it is sent to the next node in store and forward mode. The reason for
using store and forward mode is the following: A supervision frame might
trigger the creation of an entry in the node table and this task is time
consuming. By sending the frame in store and forward mode, more time is
available for this operation while receiving the frame. Each device in
an HSR/PRP network sends supervision frames at a constant time interval.
Outgoing supervision frames are composed and sent by the host CPU.

Cut-Through for HSR
--------------------

Cut through happens when switch firmware bypasses the transmit queues
and directly copies data from Rx FIFO to Tx FIFO. The concept is
explained here

The concept of forwarding frames from HSR port to HSR port when
operating in cut-through mode deserves more explanation since the
following boundary conditions require a carefully balanced
implementation: •Cut-through of a frame shall start as early as possible
in order to minimize the propagation delay in each node. The ICSS switch
supports starting the cut-through operation after a configurable amount
of bytes received. Theoretically, for HSR the minimum number of bytes
required is 22 (12 bytes Source-/Destination MAC, 4 bytes VLAN Tag, 6
bytes HSR Tag) in order to have all the necessary data to take the
routing decision. The receiving process is optimized to allow cut
through as soon as possible depending on the type of the frame ( see
start receiving process in 3.2.2 Micro Scheduler). •Duplicates shall not
be cut through (i.e. the detection of a duplicate shall be finished
before the next node in the ring starts processing the frame) •Detection
of duplicates (computing the hash index and scanning a bin in the hash
table) is time consuming

Waiting for the duplicate detection before taking the cut through
decision would delay the frame too much. Starting to cut-through a frame
without port duplicate rejection minimizes the delay and allows starting
the receiving process after 14 bytes. Once the cut through of a frame
has started, the port duplication rejection process starts. If the frame
is identified as duplicate or corrupted, the transmission of the frame
is aborted by asserting the TX\_RESET which will reset the transmit FIFO
and clear all its contents and therefore corrupt the frame being
cut-though.

.. _HSR_PRP_Firmware_Memory_Map_label:

HSR/PRP Memory Map
------------------

.. rubric:: Shared RAM Memory Map
   :name: shared-ram-memory-map

+--------------------+--------------------+--------------------+--------------------+
| Name of Offset     | Description        | Offset in Shared   | Size (in bytes)    |
|                    | Refer to           | RAM                |                    |
|                    | *hsr\_prp\_firmwar |                    |                    |
|                    | e.h*               |                    |                    |
+====================+====================+====================+====================+
| INDEX\_ARRAY       | Index entry for    | *0x1E0*            | 144                |
|                    | Node Table         |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| NODE\_TABLE        | Node Table for the | *0x1FCO*           | *4132*             |
|                    | DANH/DANP          |                    |                    |
+--------------------+--------------------+--------------------+--------------------+

Table:  **Shared RAM Memory Map**

+--------------------------+--------------------------+--------------------------+
| Name of Offset           | Description              | Offset in Shared RAM     |
|                          | Refer to                 | (base : 0x140)           |
|                          | *hsr\_prp\_firmware.h*   |                          |
+==========================+==========================+==========================+
| LRE\_CNT\_TX\_A          | Number of frames         | *4*                      |
|                          | successfully sent over   |                          |
|                          | port A that are HSR/PRP  |                          |
|                          | tagged                   |                          |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_TX\_B          | Same for Port B          | *8*                      |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_TX\_C          | Number of frames         | *12*                     |
|                          | successfully sent to     |                          |
|                          | Host that are HSR/PRP    |                          |
|                          | tagged                   |                          |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_ERRWRONGLAN\_A | number of frames with    | *16*                     |
|                          | the wrong LAN            |                          |
|                          | identifier received on   |                          |
|                          | LRE port A               |                          |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_ERRWRONGLAN\_B | Same for Port B          | *20*                     |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_ERRWRONGLAN\_C | Same for Host            | *24*                     |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_RX\_A          | number of frames         | *28*                     |
|                          | received successfully    |                          |
|                          | with HSR or PRP TAG on a |                          |
|                          | LRE port A               |                          |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_RX\_B          | Same for Port B          | *32*                     |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_RX\_C          | Same for Host            | *36*                     |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_ERRORS\_A      | number of frames with    | *40*                     |
|                          | errors                   |                          |
|                          | received on this LRE     |                          |
|                          | port A                   |                          |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_ERRORS\_B      | Same for Port B          | *44*                     |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_ERRORS\_C      | Same for Host            | *48*                     |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_NODES          | Number of active nodes   | *52*                     |
|                          | in the node table        |                          |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_PROXY\_NODES   | Number of active proxy   | *56*                     |
|                          | nodes in the node table  |                          |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_UNIQUE\_RX\_A  | Number of entries in the | *60*                     |
|                          | duplicate detection      |                          |
|                          | mechanism                |                          |
|                          | on port A for which no   |                          |
|                          | duplicate was received   |                          |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_UNIQUE\_RX\_B  | Same for Port B          | *64*                     |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_UNIQUE\_RX\_C  | Same for Host            | *68*                     |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_DUPLICATE\_RX\ | Number of entries in the | *72*                     |
| _A                       | duplicate detection      |                          |
|                          | mechanism on port A for  |                          |
|                          | which one single         |                          |
|                          | duplicate was received   |                          |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_DUPLICATE\_RX\ | Same for Port B          | *76*                     |
| _B                       |                          |                          |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_DUPLICATE\_RX\ | Same for Host            | *80*                     |
| _C                       |                          |                          |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_MULTIPLE\_RX\_ | Number of entries in the | *84*                     |
| A                        | duplicate detection      |                          |
|                          | mechanism on port A for  |                          |
|                          | which more than one      |                          |
|                          | duplicate was received   |                          |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_MULTIPLE\_RX\_ | Same for Port B          | *88*                     |
| B                        |                          |                          |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_MULTIPLE\_RX\_ | Same for Port C          | *92*                     |
| C                        |                          |                          |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_OWN\_RX\_A     | Number of entries on     | *96*                     |
|                          | port A received from     |                          |
|                          | device itself            |                          |
+--------------------------+--------------------------+--------------------------+
| LRE\_CNT\_OWN\_RX\_B     | Same for Port B          | *100*                    |
+--------------------------+--------------------------+--------------------------+
| LRE\_DUPLICATE\_DISCARD  | Number of frame retreive | *104*                    |
|                          | by the host              |                          |
+--------------------------+--------------------------+--------------------------+
| LRE\_TRANSPARENT\_RECEPT | Number of frame received | *108*                    |
| ION                      | without PRP RCT          |                          |
+--------------------------+--------------------------+--------------------------+
| LRE\_NODE\_TABLE\_LOOKUP | Number of instances      | *112*                    |
| \_ERROR\_A               | where node table look up |                          |
|                          | failed for Port A        |                          |
+--------------------------+--------------------------+--------------------------+
| LRE\_NODE\_TABLE\_LOOKUP | Same for Port B          | *116*                    |
| \_ERROR\_B               |                          |                          |
+--------------------------+--------------------------+--------------------------+
| LRE\_NODE\_TABLE\_FULL   | If Node Table is full,   | *120*                    |
|                          | this value is            |                          |
|                          | incremented              |                          |
+--------------------------+--------------------------+--------------------------+
| LRE\_MULTICAST\_DROPPED  | If the Multicast frame is| *124*                    |
|                          | dropped because of no    |                          |
|                          | hash value configured in |                          |
|                          | the filter table, this   |                          |
|                          | value is incremented     |                          |
+--------------------------+--------------------------+--------------------------+
| LRE\_VLAN\_DROPPED       | If the frame is dropped  | *128*                    |
|                          | because of no entry for  |                          |
|                          | the VID of the frame in  |                          |
|                          | the VLAN filter table,   |                          |
|                          | this value is incremented|                          |
+--------------------------+--------------------------+--------------------------+

Table:  **LRE Interface Stats**

+--------------------+--------------------+--------------------+--------------------+
| Name of Offset     | Description        | Offset in PRU0     | Size (in bytes)    |
|                    | Refer to           | DRAM               |                    |
|                    | *hsr\_prp\_firmwar |                    |                    |
|                    | e.h*               |                    |                    |
+====================+====================+====================+====================+
| DUPLICATE\_HOST\_T | Duplicate          | *0x200*            | *6136*             |
| ABLE               | detection table    |                    |                    |
|                    | for Host           |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| NEXT\_FREE\_ADDRES | Offset of the      | *0x1B00*           | *132*              |
| S\_NT\_QUEUE       | queue of the free  |                    |                    |
|                    | address            |                    |                    |
|                    | for the node table |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| POINTERS\_FREE\_AD | Offset of the read | *0x1B84*           | *4*                |
| DR\_NODETABLE      | and write pointer  |                    |                    |
|                    | of the             |                    |                    |
|                    | free address of    |                    |                    |
|                    | the node           |                    |                    |
|                    | table(read.w0,writ |                    |                    |
|                    | e.w2)              |                    |                    |
+--------------------+--------------------+--------------------+--------------------+

Table:  **PRU0 RAM Memory Map**

+--------------------+--------------------+--------------------+--------------------+
| Name of Offset     | Description        | Offset in PRU1     | Size (in bytes)    |
|                    | Refer to           | DRAM               |                    |
|                    | *hsr\_prp\_firmwar |                    |                    |
|                    | e.h*               |                    |                    |
+====================+====================+====================+====================+
| DUPLICATE\_PORT\_T | Offset of port     | *0x200*            | *3064*             |
| ABLE\_PRU0         | duplicate table    |                    |                    |
|                    | for PRU0 (HSR      |                    |                    |
|                    | Only)              |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| DUPLICATE\_PORT\_T | Offset of port     | *0xE00*            | *3064*             |
| ABLE\_PRU1         | duplicate table    |                    |                    |
|                    | for PRU1 (HSR      |                    |                    |
|                    | Only)              |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| NODE\_TABLE\_SIZE  | Size of the node   | *0x1C00*           | *4*                |
|                    | table [0..128]     |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| NODE\_TABLE\_ARBIT | Busy slave flag    | *0x1C04*           | *4*                |
| RATION             | and busy master    |                    |                    |
|                    | flag               |                    |                    |
|                    | for 3 lock used to |                    |                    |
|                    | protect the node   |                    |                    |
|                    | table              |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| DUPLICATE\_HOST\_T | Size and setup (N  | *0x1C08*           | *4*                |
| ABLE\_SIZE         | and M) of          |                    |                    |
|                    | duplicate host     |                    |                    |
|                    | table              |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| DUPLICATE\_PORT\_T | Size and setup (N  | *0x1C1C*           | *4*                |
| ABLE\_SIZE         | and M) of          |                    |                    |
|                    | duplicate port     |                    |                    |
|                    | table              |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| NODE\_FORGET\_TIME | Time after which a | *0x1C20*           | *4*                |
|                    | node entry is      |                    |                    |
|                    | cleared (10ms      |                    |                    |
|                    | resolution)        |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| DUPLI\_FORGET\_TIM | Time after which   | *0x1C24*           | *4*                |
| E                  | an entry is        |                    |                    |
|                    | removed from the   |                    |                    |
|                    | duplicate table    |                    |                    |
|                    | (10ms resolution)  |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| PATH\_BROKEN\_NB\_ | Supervision frame  | *0x1C28*           | *4*                |
| FRAM\_DIFF         | Counter minimum    |                    |                    |
|                    | difference to      |                    |                    |
|                    | detect a broken    |                    |                    |
|                    | path               |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| DUPLI\_PORT\_CHECK | Time interval to   | *0x1C2C*           | *4*                |
| \_RESO             | check the port     |                    |                    |
|                    | duplicate table    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| DUPLI\_HOST\_CHECK | Time interval to   | *0x1C30*           | *4*                |
| \_RESO             | check the host     |                    |                    |
|                    | duplicate table    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| NODETABLE\_CHECK\_ | Time interval to   | *0x1C34*           | *4*                |
| RESO               | check the node     |                    |                    |
|                    | duplicate table    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| HOST\_TIMER\_CHECK | Host \| Port       | *0x1C38*           | *4*                |
| \_FLAGS            |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| HOST\_DUPLICATE\_A | Arbitration flag   | *0x1C3C*           | *4*                |
| RBITRATION         | for the host       |                    |                    |
|                    | duplicate task     |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| ICSS\_FIRMWARE\_RE | Time counter to    | *0x1C40*           | *4*                |
| LEASE              | trigger the host   |                    |                    |
|                    | duplicate table    |                    |                    |
|                    | check task         |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| RED\_FIRMWARE\_REL | Time counter to    | *0x1C44*           | *4*                |
| EASE               | trigger the Node   |                    |                    |
|                    | Table check task   |                    |                    |
|                    | in firmware        |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| SUP\_ADDR          | Supervision        | *0x1C48*           | *4*                |
|                    | address in HSR     |                    |                    |
+--------------------+--------------------+--------------------+--------------------+

Table:  **PRU1 RAM Memory Map**

