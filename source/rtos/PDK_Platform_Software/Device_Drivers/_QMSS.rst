.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_QMSS

Overview
--------

Introduction
^^^^^^^^^^^^

The Queue Manager Sub System (QMSS) low level driver provides the
interface to Queue Manager Subsystem hardware which is part of the
Multicore Navigator functional unit for a keystone device. QMSS provides
hardware assisted queue system and implements fundamental operations
such as en-queue and de-queue, descriptor management, accumulator
functionality and configuration of infrastructure DMA mode. The LLD
provides APIs to get full entitlement of supported hardware
functionality.

The LLD also includes accumulation and QoS (Quality of Service)
firmware. QoS enables restriction of data rates in bytes per second or
packets per second, weighted round robin queue selection, and selective
descriptor dropping for oversubscribed queues. Accumulation The APIs are
provided through the LLD. The API documentation for both QoS and
Accumulator is available in the API Reference manual below. The
capabilities of the QoS firmware are documented in their design
documents. The capabilities of the accumulator are documented in the
Hardware Peripheral User Guide.

.. rubric:: Modes of Operation
   :name: modes-of-operation

QMSS library (ti.drv.qm) supports below modes

**Joint Mode**: In this mode, only linkingRAM0Base, linkingRAM0Size, and
linkingRAM1Base are used to configure all QM groups simultaneously. For
all existing devices (K2H, K2K) this is only mode that should be used.
For the rest of the devices such as K2L, K2E, 6678 and 6657, this is the
only mode available.

**Split Mode**: This mode shouldn't be used as it doesn't support all
peripherals on the device.

User Interface
--------------

Driver Configuration
^^^^^^^^^^^^^^^^^^^^^

The driver configures the QMSSSS subsystem using
Qmss_GlobalConfigGroupRegs(system configuration) structure. The default
global configuration per device is present under qmss_device.c file
provided per device.

For details about individual fields of this structure, see the Doxygen
help by opening
PDK_INSTALL_DIR\QMSSckages\ti\drv\QMSS\docs\doxygen\html\index.html.

APIs
^^^^^

API header for application:

::

    #include <ti/drv/QMSS/QMSS_drv.h>

Please see the doxygen in "API Reference Manual" below for details.

|

Application
------------

Examples
^^^^^^^^

+-----------------------+-----------------------+-----------------------+
| Name                  || Description          | Expected Results      |
+=======================+=======================+=======================+
| QMSS_Example          | | Example             | | User observes the   |
| application           |   demonstrating       |   output printed over |
|                       |   *infra DMA,         |   the CCS console     |
|                       |   interrupt test* use |                       |
|                       |   case. Reference     |                       |
|                       |   example for         |                       |
|                       |   developers          |                       |
+-----------------------+-----------------------+-----------------------+
| QMSS_UnitTestApplicat | | Unit Test           | | User observes the   |
| ion                   |   application to test |   output printed over |
|                       |   all APIs            |   the CCS console     |
+-----------------------+-----------------------+-----------------------+

.. rubric:: Sample Example Output
   :name: sample-example-output

This came from K2K multicore example:

::

    **************************************************
    ************ QMSS Multicore Example **************
    **************************************************
    **************************************************
    ************ QMSS Multicore Example **************
    **************************************************
    **************************************************
    **************************************************
    ************ QMSS Multicore Example **************
    ************ QMSS Multicore Example **************
    **************************************************
    **************************************************
    Core 1 : Starting BIOS...
    Core 2 : Starting BIOS...
    Core 3 : Starting BIOS...
    Core 0 : Starting BIOS...
    Core 0 : Created RM packet heap
    Core 0 : Created IPC MessageQ heap
    Core 0 : Created receive Q for Client1
    Core 1 : Opened RM packet heap
    Core 2 : Opened RM packet heap
    Core 3 : Opened RM packet heap
    Core 1 : Opened IPC MessageQ heap
    Core 2 : Opened IPC MessageQ heap
    Core 3 : Opened IPC MessageQ heap
    Core 1 : Created receive Q for Server
    Core 2 : Created receive Q for Server
    Core 3 : Created receive Q for Server
    Core 1 : Opened Server's receive Q
    Core 1 : Waiting for QMSS to be initialized...

    Core 0 : Opened Client1's receive Q for Server
    Core 0 : Created receive Q for Client2
    Core 0 : Opened Client2's receive Q for Server
    Core 0 : Created receive Q for Client3
    Core 2 : Opened Server's receive Q
    Core 2 : Waiting for QMSS to be initialized...

    Core 0 : Opened Client3's receive Q for Server

    -----------------------Initializing---------------------------
    Core 0 : L1D cache size 4. L2 cache size 0.
    Core 0 : Memory region 0 inserted
    Core 0 : Memory region 1 inserted
    Core 0 : Tx Completion Queue Number     : 897 opened
    Core 0 : Number of Tx descriptors requested : 32. Number of descriptors allocated : 32
    Core 0 : Number of Rx descriptors requested : 32. Number of descriptors allocated : 32
    Core 0 : Number of Sync free descriptors requested : 32. Number of descriptors allocated : 32
    Core 0 : Sync Queue Number              : 9025 opened
    Core 0 : Sync Cfg Queue Number          : 9026 opened
    Core 0 : Sync Free Queue Number         : 898 opened
    Core 0 : Receive Free Queue Number      : 736 opened
    Core 0 : Transmit Free Queue Number     : 8928 opened
    Core 0 : System initialization completed: 8928
    Core 0 : Publishing RM nameserver names for shared queues

    --------------------Queue status CORE 0----------------------
                        After Initialization

    Tx Free Queue 8928 Entry Count            : 32
    Rx Free Queue 736 Entry Count            : 32
    Tx completion Queue 897 Entry Count     : 0
    Sync Queue 9025 Entry Count              : 0
    Sync free Queue 898 Entry Count         : 32
    Sync Cfg Queue 9026 Entry Count          : 0
    -------------------------------------------------------------

    Core 0 : Registering High Priority interrupt channel : 0 eventId : 48 queue Number : 704


    Core 3 : Opened Server's receive Q
    Core 1 : QMSS initialization done.
    Core 2 : QMSS initialization done.
    Core 3 : Waiting for QMSS to be initialized...




    Core 3 : QMSS initialization done.

    Core 1 : Rx Free Queue Number       : 736 opened
    Core 2 : Rx Free Queue Number       : 736 opened
    Core 3 : Rx Free Queue Number       : 736 opened
    Core 1 : Tx Free Queue Number       : 8928 opened
    Core 2 : Tx Free Queue Number       : 8928 opened
    Core 3 : Tx Free Queue Number       : 8928 opened
    Core 1 : Tx Completion Queue Number : 897 opened
    Core 2 : Tx Completion Queue Number : 897 opened
    Core 3 : Tx Completion Queue Number : 897 opened
    Core 1 : Sync Queue Number          : 9025 opened
    Core 2 : Sync Queue Number          : 9025 opened
    Core 3 : Sync Queue Number          : 9025 opened
    Core 1 : Sync Free Queue Number     : 898 opened
    Core 2 : Sync Free Queue Number     : 898 opened
    Core 3 : Sync Free Queue Number     : 898 opened
    Core 1 : Sync Cfg Queue Number      : 9026 opened
    Core 2 : Sync Cfg Queue Number      : 9026 opened
    Core 3 : Sync Cfg Queue Number      : 9026 opened
    Core 1 : Registering High Priority interrupt channel : 1 eventId : 48 queue Number : 705
    Core 2 : Registering High Priority interrupt channel : 2 eventId : 48 queue Number : 706
    Core 3 : Registering High Priority interrupt channel : 3 eventId : 48 queue Number : 707
    Core 1 : Waiting for sync signal
    Core 2 : Waiting for sync signal
    Core 3 : Waiting for sync signal
    Core 0 : Opened Tx channel      : 0
    Core 0 : Opened Rx channel      : 0
    Core 0 : Transmit Queue Number  : 800
    Core 0 : Receive Queue Number   : 704
    Core 0 : Opened Rx flow         : 0
    Core 0 : High priority accumulator programmed for channel : 0 queue : 704

    Core 0 : Transmitting 8 packets..........

    *************************************************************
    Core 0 : Opened Tx channel      : 0
    Core 0 : Opened Rx channel      : 0
    Core 0 : Transmit Queue Number  : 800
    Core 0 : Receive Queue Number   : 705
    Core 0 : Opened Rx flow         : 0
    Core 0 : High priority accumulator programmed for channel : 1 queue : 705

    Core 0 : Transmitting 8 packets..........

    *************************************************************
    Core 0 : Opened Tx channel      : 0
    Core 0 : Opened Rx channel      : 0
    Core 0 : Transmit Queue Number  : 800
    Core 0 : Receive Queue Number   : 706
    Core 0 : Opened Rx flow         : 0
    Core 0 : High priority accumulator programmed for channel : 2 queue : 706

    Core 0 : Transmitting 8 packets..........

    *************************************************************
    Core 0 : Opened Tx channel      : 0
    Core 0 : Opened Rx channel      : 0
    Core 0 : Transmit Queue Number  : 800
    Core 0 : Receive Queue Number   : 707
    Core 0 : Opened Rx flow         : 0
    Core 0 : High priority accumulator programmed for channel : 3 queue : 707

    Core 0 : Transmitting 8 packets..........

    *************************************************************
    Core 0 : Waiting for sync signal
    Core 0 : Got sync signal
    *************************************************************


    --------------------Queue status CORE 0----------------------
                        After packet processing

    Tx Free Queue 8928 Entry Count            : 0
    Rx Free Queue 736 Entry Count            : 32
    Tx completion Queue 897 Entry Count     : 32
    Sync Queue 9025 Entry Count              : 4
    Sync free Queue 898 Entry Count         : 27
    Sync Cfg Queue 9026 Entry Count          : 1
    -------------------------------------------------------------

    Core 0 : Waiting for other cores to ack sync signal
    Core 1 : Got sync signal
    Core 2 : Got sync signal
    Core 3 : Got sync signal
    *************************************************************
    *************************************************************
    *************************************************************



    Core 0 : acks found

    --------------------Deinitializing---------------------------

    --------------------Queue status CORE 0----------------------
                        Before exit

    Tx Free Queue 8928 Entry Count            : 0
    Rx Free Queue 736 Entry Count            : 32
    Tx completion Queue 897 Entry Count     : 32
    Sync Queue 9025 Entry Count              : 0
    Sync free Queue 898 Entry Count         : 28
    Sync Cfg Queue 9026 Entry Count          : 4
    -------------------------------------------------------------

    Core 0 : Receive free queue closed successfully. Ref count : 0
    Core 0 : Transmit completion queue closed successfully. Ref count : 3
    Core 0 : Transmit free queue closed successfully. Ref count : 3
    Core 0 : Sync queue closed successfully. Ref count : 3
    Core 0 : Sync free queue closed successfully. Ref count : 3
    Core 0 : Sync queue closed successfully. Ref count : 3
    Core 0 : CPPI CPDMA closed successfully
    Core 0 : CPPI exit successful
    Core 0: Cleaning regions
    Core 0: exit QMSS
    Core 1 : Receive free queue closed successfully. Ref count : 3
    Core 2 : Receive free queue closed successfully. Ref count : 2
    Core 3 : Receive free queue closed successfully. Ref count : 1
    Core 1 : Transmit completion queue closed successfully. Ref count : 2
    Core 2 : Transmit completion queue closed successfully. Ref count : 1
    Core 3 : Transmit completion queue closed successfully. Ref count : 0
    Core 1 : Transmit free queue closed successfully. Ref count : 2
    Core 2 : Transmit free queue closed successfully. Ref count : 1
    Core 3 : Transmit free queue closed successfully. Ref count : 0
    Core 1 : Sync queue closed successfully. Ref count : 2
    Core 2 : Sync queue closed successfully. Ref count : 1
    Core 3 : Sync queue closed successfully. Ref count : 0
    Core 1 : Sync free queue closed successfully. Ref count : 2
    Core 2 : Sync free queue closed successfully. Ref count : 1
    Core 3 : Sync free queue closed successfully. Ref count : 0
    Core 1 : Sync queue closed successfully. Ref count : 2
    Core 2 : Sync queue closed successfully. Ref count : 1
    Core 3 : Sync queue closed successfully. Ref count : 0
    *******************************************************
    *******************************************************
    *******************************************************
    ******** QMSS Multicore (1) Example Done (PASS) *******
    ******** QMSS Multicore (2) Example Done (PASS) *******
    ******** QMSS Multicore (3) Example Done (PASS) *******
    *******************************************************
    *******************************************************
    *******************************************************
    Core 0 : Deleting RM nameserver names for shared queues
    Instance name: RM_Server
    Handle: 0x00854578
    Type:   Server

    Resource Status:

    Core 0 : All resources freed successfully
    *******************************************************
    ******** QMSS Multicore (0) Example Done (PASS) *******
    *******************************************************

Debug FAQ
----------

#. Double Push - Some queue elements lost.

   #. Pushing the same pointer twice is illegal. In hardware it does
      something similar to double linking the same object into two
      places of a software linked list. It corrupts the list, such that
      some items will be orphaned/lost.

#. NULL Push - Entire queue lost

   #. Pushing NULL (0) clears the entire queue. This is intentionally
      done by Qmss_QueueEmpty(). However the various Qmss_QueuePush
      functions don't check for NULL (to save cycles). Don't push NULL
      (for example received when Qmss_QueuePop finds an empty queue).

#. Hint Bits (4 low LSBs of desc pointer)

   #. These are used to tell DMAs such as CPPI the size of the
      descriptor. Thus, when receiving descriptors from hardware, you
      must use QMSS_DESC_PTR() to discard them, else unaligned memory
      accesses that corrupt descriptors will be generated by software.

#. General lost descriptors

   #. Its not a bad idea to have code that can inventory all your
      descriptors as part of destructive debug. Iterate over all queues,
      and pop all descriptors. Set a bit in a large bitmap for each
      descriptor found. Bits that remain 0 indicate "lost" descriptors
      which could have happened due to double push or null push or
      software bugs that simply lost them. By examining the contents of
      descriptor(s) and buffer(s), can often determine who last used
      them therefore what part of code lost them.
   #. Its also good to have nondestructive debug code that can call
      Qmss_getQueueByteCount() and Qmss_getQueueEntryCount() for each
      queue. This should be able to find all but a few (~4) descriptors
      per hardware DMA that are in flight. If large amounts of
      descriptors are missing, it means there is a bug. For this
      debug/monitor purpose, its OK to make own Qmss_QueueHandle by
      casting the queue number (eg (Qmss_QueueHandle)queueNum) since its
      undesirable to generate accounting/management for purpose of
      nondestructive debug.

Additional References
---------------------

.. list-table::
   :header-rows: 1

   * - **Document**

     - **Location**

   * - API Reference Manual

     - ``$(TI_PDK_INSTALL_DIR)/packages/ti/drv/QMSS/docs/doxygen/html/index.html``

   * - Release Notes

     - ``$(TI_PDK_INSTALL_DIR)/packages/ti/drv/QMSS/docs/ReleaseNotes_QMSS_LLD.pdf``

   * - QoS (Weighted Round Robin and SP QoS tree)

     - ``$(TI_PDK_INSTALL_DIR)/packages/ti/drv/QMSS/docs/firmware/qos_sched,qos_sched_drop_sched,qos_sched_wide.pdf``

   * - QoS (Leaky bucket and SRIO TX Scheduler)

     - ``$(TI_PDK_INSTALL_DIR)/packages/ti/drv/QMSS/docs/firmware/qos.pdf``

   * - Hardware Userguide/TRM

     - `UG TRM PDF <http://www.ti.com/lit/sprugr9>`__

   * - CPPI LLD (Navigator/QMSS DMA component)

     - `CPPI LLD`_

.. _CPPI LLD: index_device_drv.html#cppi

|


