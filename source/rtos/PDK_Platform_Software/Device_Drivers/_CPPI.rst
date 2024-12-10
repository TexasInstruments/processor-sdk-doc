.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_CPPI

Overview
--------

Introduction
^^^^^^^^^^^^

CPPI offers developers a common way of handling different protocol
interfaces that may require multiple priorities and multiple channels on
a single port. CPPI defines the register set, data structures,
interrupts and buffer handling for all peripherals, regardless of
protocol.

CPPI is based on a buffer scatter/gather scheme, in which individual
packets are broken up and then stored into small buffers, from which
they are retrieved and reassembled (as opposed to using buffers that are
located contiguously in memory). When protocol translation is required,
a packet header can be appended in a small buffer, saving the CPU from
having to rewrite the entire packet and header by performing a copy from
one large buffer to another. The considerable savings in CPU cycles that
result make buffer scatter/gathering the most efficient scheme for
bridging and routing.

The LLD provides resource management for descriptors, receive/transmit
channels and receive flows.

User Interface
--------------

Driver Configuration
^^^^^^^^^^^^^^^^^^^^^

The driver configures the CPPI subsystem using cppiGblCfgParams(system
configuration) structure. The default global configuration per device is
present under cppi_device.c file provided per device.

For details about individual fields of this structure, see the Doxygen
help by opening
PDK_INSTALL_DIR\CPPIckages\ti\drv\CPPI\docs\doxygen\html\index.html.

APIs
^^^^^

API reference for application:

::

    #include <ti/drv/CPPI/CPPI_drv.h>

Application
------------

Examples
^^^^^^^^

+-----------------------+-----------------------+-----------------------+
| Name                  || Description          | Expected Results      |
+=======================+=======================+=======================+
| CPPI_Example          | | Example             | | User observes the   |
| application           |   demonstrating       |   output printed over |
|                       |   *sample test* use   |   the CCS console     |
|                       |   case. Reference     |                       |
|                       |   example for         |                       |
|                       |   developers          |                       |
+-----------------------+-----------------------+-----------------------+
| CPPI_UnitTestApplicat | | Unit Test           | | User observes the   |
| ion                   |   application to test |   output printed over |
|                       |   all APIs            |   the CCS console     |
+-----------------------+-----------------------+-----------------------+

.. rubric:: Sample Example output
   :name: sample-example-output

This came from k2k example:

::

    **************************************************
    *************** CPPI LLD usage example ***********
    **************************************************
    **************************************************
    *************** CPPI LLD usage example ***********
    **************************************************
    **************************************************
    **************************************************
    *************** CPPI LLD usage example ***********
    *************** CPPI LLD usage example ***********
    **************************************************
    **************************************************
    *******Test running on Core 1 *******************
    *******Test running on Core 0 *******************
    *******Test running on Core 2 *******************
    *******Test running on Core 3 *******************
    Core 0 : L1D cache size 4. L2 cache size 0.
    Core 2 : Starting BIOS...
    Core 3 : Starting BIOS...
    Core 0 : Starting BIOS...
    Core 1 : Starting BIOS...
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

    Core 0 : QMSS initialization done


    Core 3 : Opened Server's receive Q
    Core 1 : QMSS initialization done
    Core 2 : QMSS initialization done
    Core 3 : Waiting for QMSS to be initialized...


    Core 3 : QMSS initialization done


    Core 0 : QMSS CPDMA Opened
    Core 1 : QMSS CPDMA Opened


    Core 0 : Memory region 0 inserted
    Core 0 : Number of descriptors requested : 8. Number of descriptors allocated : 8
    Core 0 : Opened Rx channel : 0
    Core 0 : Opened Tx channel : 0
    Core 0 : Queue Number : 8192 opened
    Core 0 : Queue Number : 8193 opened
    Transmit Queue 8192 Entry Count : 1 Tx descriptor 0x@10853b20
    Receive Queue 8193 Entry Count : 1 Rx descriptor 0x@10853b20
    Transmit Queue 8192 Entry Count : 1 Tx descriptor 0x@10853b50
    Receive Queue 8193 Entry Count : 1 Rx descriptor 0x@10853b50
    Transmit Queue 8192 Entry Count : 1 Tx descriptor 0x@10853b80
    Receive Queue 8193 Entry Count : 1 Rx descriptor 0x@10853b80
    Transmit Queue 8192 Entry Count : 1 Tx descriptor 0x@10853bb0
    Receive Queue 8193 Entry Count : 1 Rx descriptor 0x@10853bb0
    Transmit Queue 8192 Entry Count : 1 Tx descriptor 0x@10853be0
    Receive Queue 8193 Entry Count : 1 Rx descriptor 0x@10853be0
    Transmit Queue 8192 Entry Count : 1 Tx descriptor 0x@10853c10
    Receive Queue 8193 Entry Count : 1 Rx descriptor 0x@10853c10
    Transmit Queue 8192 Entry Count : 1 Tx descriptor 0x@10853c40
    Receive Queue 8193 Entry Count : 1 Rx descriptor 0x@10853c40
    Transmit Queue 8192 Entry Count : 1 Tx descriptor 0x@10853c70
    Receive Queue 8193 Entry Count : 1 Rx descriptor 0x@10853c70
    Core 0 : Received host descriptor from Queue 897 Sucessfully
    Core 0 : Tx Channel closed successfully. Ref count :0
    Core 0 : Rx Channel closed successfully. Ref count :0
    Core 0 : Rx queue closed successfully. Ref count :0
    Core 0 : Tx queue closed successfully. Ref count :0
    Core 0 : Free queue closed successfully. Ref count :0
    Core 0 : Closing CPPI CPDMA Ref count : 3
    Core 0 : CPPI CPDMA closed successfully
    Core 1 : Memory region 1 inserted


    Core 1 : Number of descriptors requested : 8. Number of descriptors allocated : 8
    Core 2 : QMSS CPDMA Opened
    Core 3 : QMSS CPDMA Opened
    Core 1 : Opened Rx channel : 0


    Core 1 : Opened Tx channel : 0
    Core 2 : Memory region 2 inserted
    Core 3 : Memory region 3 inserted
    Core 1 : Queue Number : 0 opened
    Core 2 : Number of descriptors requested : 8. Number of descriptors allocated : 8
    Core 3 : Number of descriptors requested : 8. Number of descriptors allocated : 8
    Core 1 : Queue Number : 1 opened
    Core 2 : Opened Rx channel : 1
    Core 3 : Opened Rx channel : 2
    Transmit Queue 0 Entry Count : 1 Tx descriptor 0x@11853b20
    Core 2 : Opened Tx channel : 1
    Core 3 : Opened Tx channel : 2
    Receive Queue 1 Entry Count : 1 Rx descriptor 0x@11853b20
    Core 2 : Queue Number : 8192 opened
    Core 3 : Queue Number : 8193 opened
    Transmit Queue 0 Entry Count : 1 Tx descriptor 0x@11853b50
    Core 2 : Queue Number : 8194 opened
    Core 3 : Queue Number : 8195 opened
    Receive Queue 1 Entry Count : 1 Rx descriptor 0x@11853b50
    Transmit Queue 8192 Entry Count : 1 Tx descriptor 0x@12853b20
    Transmit Queue 8193 Entry Count : 1 Tx descriptor 0x@13853b20
    Transmit Queue 0 Entry Count : 1 Tx descriptor 0x@11853b80
    Receive Queue 8194 Entry Count : 1 Rx descriptor 0x@12853b20
    Receive Queue 8195 Entry Count : 1 Rx descriptor 0x@13853b20
    Receive Queue 1 Entry Count : 1 Rx descriptor 0x@11853b80
    Transmit Queue 8192 Entry Count : 1 Tx descriptor 0x@12853b50
    Transmit Queue 8193 Entry Count : 1 Tx descriptor 0x@13853b50
    Transmit Queue 0 Entry Count : 1 Tx descriptor 0x@11853bb0
    Receive Queue 8194 Entry Count : 1 Rx descriptor 0x@12853b50
    Receive Queue 8195 Entry Count : 1 Rx descriptor 0x@13853b50
    Receive Queue 1 Entry Count : 1 Rx descriptor 0x@11853bb0
    Transmit Queue 8192 Entry Count : 1 Tx descriptor 0x@12853b80
    Transmit Queue 8193 Entry Count : 1 Tx descriptor 0x@13853b80
    Transmit Queue 0 Entry Count : 1 Tx descriptor 0x@11853be0
    Receive Queue 8194 Entry Count : 1 Rx descriptor 0x@12853b80
    Receive Queue 8195 Entry Count : 1 Rx descriptor 0x@13853b80
    Receive Queue 1 Entry Count : 1 Rx descriptor 0x@11853be0
    Transmit Queue 8192 Entry Count : 1 Tx descriptor 0x@12853bb0
    Transmit Queue 8193 Entry Count : 1 Tx descriptor 0x@13853bb0
    Transmit Queue 0 Entry Count : 1 Tx descriptor 0x@11853c10
    Receive Queue 8194 Entry Count : 1 Rx descriptor 0x@12853bb0
    Receive Queue 8195 Entry Count : 1 Rx descriptor 0x@13853bb0
    Receive Queue 1 Entry Count : 1 Rx descriptor 0x@11853c10
    Transmit Queue 8192 Entry Count : 1 Tx descriptor 0x@12853be0
    Transmit Queue 8193 Entry Count : 1 Tx descriptor 0x@13853be0
    Transmit Queue 0 Entry Count : 1 Tx descriptor 0x@11853c40
    Receive Queue 8194 Entry Count : 1 Rx descriptor 0x@12853be0
    Receive Queue 8195 Entry Count : 1 Rx descriptor 0x@13853be0
    Receive Queue 1 Entry Count : 1 Rx descriptor 0x@11853c40
    Transmit Queue 8192 Entry Count : 1 Tx descriptor 0x@12853c10
    Transmit Queue 8193 Entry Count : 1 Tx descriptor 0x@13853c10
    Transmit Queue 0 Entry Count : 1 Tx descriptor 0x@11853c70
    Receive Queue 8194 Entry Count : 1 Rx descriptor 0x@12853c10
    Receive Queue 8195 Entry Count : 1 Rx descriptor 0x@13853c10
    Receive Queue 1 Entry Count : 1 Rx descriptor 0x@11853c70
    Transmit Queue 8192 Entry Count : 1 Tx descriptor 0x@12853c40
    Transmit Queue 8193 Entry Count : 1 Tx descriptor 0x@13853c40
    Core 1 : Received host descriptor from Queue 896 Sucessfully
    Receive Queue 8194 Entry Count : 1 Rx descriptor 0x@12853c40
    Receive Queue 8195 Entry Count : 1 Rx descriptor 0x@13853c40
    Core 1 : Tx Channel closed successfully. Ref count :0
    Transmit Queue 8192 Entry Count : 1 Tx descriptor 0x@12853c70
    Transmit Queue 8193 Entry Count : 1 Tx descriptor 0x@13853c70
    Core 1 : Rx Channel closed successfully. Ref count :0
    Receive Queue 8194 Entry Count : 1 Rx descriptor 0x@12853c70
    Receive Queue 8195 Entry Count : 1 Rx descriptor 0x@13853c70
    Core 1 : Rx queue closed successfully. Ref count :0
    Core 2 : Received host descriptor from Queue 9026 Sucessfully
    Core 3 : Received host descriptor from Queue 898 Sucessfully
    Core 1 : Tx queue closed successfully. Ref count :0
    Core 2 : Tx Channel closed successfully. Ref count :0
    Core 3 : Tx Channel closed successfully. Ref count :0
    Core 1 : Free queue closed successfully. Ref count :0
    Core 2 : Rx Channel closed successfully. Ref count :0
    Core 3 : Rx Channel closed successfully. Ref count :0
    Core 1 : Closing CPPI CPDMA Ref count : 2
    Core 2 : Rx queue closed successfully. Ref count :0
    Core 3 : Rx queue closed successfully. Ref count :0
    Core 1 : CPPI CPDMA closed successfully
    Core 2 : Tx queue closed successfully. Ref count :0
    Core 3 : Tx queue closed successfully. Ref count :0
    Core 2 : Free queue closed successfully. Ref count :0
    Core 3 : Free queue closed successfully. Ref count :0
    Core 2 : Closing CPPI CPDMA Ref count : 1
    Core 3 : CPPI CPDMA closed successfully
    Core 2 : CPPI CPDMA closed successfully
    Core 2 : CPPI exit successful
    *******************************************************
    *************** CPPI LLD usage example Done ***********
    *******************************************************
    Core 1 : CPPI exit successful
    Core 3 : CPPI exit successful
    *******************************************************
    *******************************************************
    *************** CPPI LLD usage example Done ***********
    *************** CPPI LLD usage example Done ***********
    *******************************************************
    *******************************************************
    Core 0 : CPPI exit successful
    Core 0: exit QMSS
    Instance name: RM_Server
    Handle: 0x00849ee8
    Type:   Server

    Resource Status:

    Core 0 : All resources freed successfully
    *******************************************************
    *************** CPPI LLD usage example Done ***********
    *******************************************************

.. rubric:: Debug FAQ
   :name: debug-faq

#. CPPI Lockup

   #. CPPI can lock up if any pointer or length, including hint bits,
      are wrong. Use the User Guide (TRM) referenced below to verify
      every pointer and length in the descriptor. Also verify the hint
      bits (low 4 bits of each descriptor) which represents size of
      descriptor (not data) in 16-byte units. When using CPPI it should
      be at least 1 (32 bytes) if no extensions are used, or 2 (48
      bytes) if some extensions are used. 0 (16 bytes) is likely to
      cause lock up!!

#. See `QMSS Debug FAQ <index_device_drv.html#qmss>`__ for more.

Additional References
---------------------

.. list-table::
   :header-rows: 1

   * - **Document**

     - **Location**

   * - API Reference Manual

     - ``$(TI_PDK_INSTALL_DIR)/packages/ti/drv/CPPI/docs/doxygen/html/index.html``

   * - Release Notes

     - ``$(TI_PDK_INSTALL_DIR)/packages/ti/drv/CPPI/docs/ReleaseNotes_CPPI_LLD.pdf``

   * - Hardware Userguide/TRM

     - `UG TRM PDF <http://www.ti.com/lit/sprugr9>`__

   * - QMSS LLD (Navigator/Queueing HW component)

     - `QMSS LLD`_

.. _QMSS LLD:  index_device_drv.html#qmss

