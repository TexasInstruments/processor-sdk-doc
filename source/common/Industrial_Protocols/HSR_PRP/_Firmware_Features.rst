.. http://processors.wiki.ti.com/index.php/PRU_ICSS_HSR_PRP_Release_Notes

A common firmware is used across TI RTOS and Linux implementations of
HSR/PRP. This section describes the firmware details.

Firmware Features Supported
----------------------------

-  **HSR/PRP**

   -  The implementation is as per IEC 62439-3 Ed 2.0
   -  Operates as a DAN (Dual Attached Node)

-  **HSR**

   -  Operates as a DANH
   -  As per clause 5 of the standard
   -  Support for modes – H, T, U and N as per standard
   -  Modes can be changed at run time

-  **PRP**

   -  Operates as a DANP
   -  As per clause 6 of the standard
   -  Two ports as per standard, Port A and Port B

-  **Support for Node Table**

   -  Total 128 entries on AMICx, AM335x, AM437x
   -  Total 256 entries on AM57xx & K2G
   -  Hash Table for faster lookup
   -  O(1) complexity
   -  Node Table statistics

-  **Support for Multicast Filtering**

   -  Supported on all SoCs
   -  Hash Table for faster lookup
   -  O(1) complexity

-  **Duplicate Discard Table**

   -  Duplicate discard on Port to Host path (HSR and PRP)
   -  Duplicate discard table on Port to Port path (HSR)
   -  Data integrity (CRC) check during port to port forwarding, except cut through (HSR)

-  **QoS scheme** : 3-bit VLAN PCP

   -  No of levels supported : 8
   -  Number of host queues : 2 \| 4 QoS levels per host queue
   -  Number of port queues : 4 \| 2 QoS levels per port queue
   -  Number of host queues are configurable

-  **Statistics**

   -  Supports all MIB statistics as per standard
   -  Node Table statistics for debugging

-  **PTP/1588**

   -  PTP Slave and Master mode
   -  Supports P2P clock.
   -  PTP over 802.3 (Annex F)
   -  Transparent Clock supported
   -  Ordinary Clock supported
   -  Single and Two step clock supported
   -  Peer delay Response is always sent as two-step

-  **Storm Prevention** : Yes. Configurable per port
