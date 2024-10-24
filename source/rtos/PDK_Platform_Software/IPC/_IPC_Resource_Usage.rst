
Overview
^^^^^^^^^

The main aim of this page is to capture details about the different
resources used in the IPC drivers.

.. note:: This page is under construction

Interrupt map usage
^^^^^^^^^^^^^^^^^^^^

AM57xx Interrupt resources
"""""""""""""""""""""""""""

The following table captures the interrupt resources used by IPC
associated with different cores for the AM57xx platform. If customer
wants to use any of the interrupt resources, it is better to make sure
any of the resources listed here are not used.

**A15 Interrupt Mapping**

+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| Index   | Addr         | Value   | Name                       | Source           | Description                        |
+=========+==============+=========+============================+==================+====================================+
| 134     | 0x4A002B44   | 127     | EVE1_IRQ_MBX0_USER3        | EVE1_MAILBOX0    | Eve1 Mailbox 0 user 3 interrupt    |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 135     | 0x4A002B44   | 128     | EVE2_IRQ_MBX0_USER3        | EVE2_MAILBOX0    | Eve2 Mailbox 0 user 3 interrupt    |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 136     | 0x4A002B48   | 129     | MAILBOX5_IRQ_USER2         | MAILBOX5         | Mailbox 5 user 2 interrupt         |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 137     | 0x4A002B48   | 130     | EVE3_IRQ_MBX0_USER3        | EVE3_MAILBOX0    | Eve 3 Mailbox 0 user 3 interrupt   |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 138     | 0x4A002B4C   | 131     | EVE4_IRQ_MBX0_USER3        | EVE4_MAILBOX0    | Eve4 Mailbox 0 user 3 interrupt    |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 141     | 0x4A002B50   | 134     | MAILBOX6_IRQ_USER2         | MAILBOX6         | Mailbox 6 user 2 interrupt         |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+

**DSP1 Interrupt Mapping**

+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| Index   | Addr         | Value   | Name                       | Source           | Description                        |
+=========+==============+=========+============================+==================+====================================+
| 55      | 0x4A002974   | 24      | EVE1_IRQ_MBX0_USER1        | EVE1_MAILBOX0    | Eve1 Mailbox 0 user 1 interrupt    |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 56      | 0x4A002978   | 25      | EVE2_IRQ_MBX0_USER1        | EVE2_MAILBOX0    | Eve2 Mailbox 0 user 1 interrupt    |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 57      | 0x4A002978   | 26      | MAILBOX5_IRQ_USER0         | MAILBOX5         | Mailbox 5 user 0 interrupt         |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 58      | 0x4A00297C   | 27      | EVE3_IRQ_MBX0_USER1        | EVE3_MAILBOX0    | Eve 3 Mailbox 0 user 1 interrupt   |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 59      | 0x4A00297C   | 28      | EVE4_IRQ_MBX0_USER1        | EVE4_MAILBOX0i   | Eve4 Mailbox 0 user 1 interrupt    |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 60      | 0x4A002980   | 29      | MAILBOX7_IRQ_USER0         | MAILBOX7         | Mailbox 7 user 0 interrupt         |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 61      | 0x4A002980   | 30      | MAILBOX8_IRQ_USER0         | MAILBOX8         | Mailbox 8 user 0 interrupt         |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+

**DSP2 Interrupt Mapping**

+---------+--------------+---------+-----------------------------+------------------+------------------------------------+
| Index   | Addr         | Value   | Name                        | Source           | Description                        |
+=========+==============+=========+=============================+==================+====================================+
| 55      | 0x4A0029F4   | 24      | EVE1_IRQ_MBX1_USER1         | EVE1_MAILBOX1    | Eve1 Mailbox 1 user 1 interrupt    |
+---------+--------------+---------+-----------------------------+------------------+------------------------------------+
| 56      | 0x4A0029F8   | 25      | EVE2_IRQ_MBX1_USER1         | EVE2_MAILBOX1    | Eve2 Mailbox 1 user 1 interrupt    |
+---------+--------------+---------+-----------------------------+------------------+------------------------------------+
| 57      | 0x4A0029F8   | 26      | MAILBOX6_IRQ_USER0          | MAILBOX6         | Mailbox 6 user 0 interrupt         |
+---------+--------------+---------+-----------------------------+------------------+------------------------------------+
| 58      | 0x4A0029FC   | 27      | EVE3_IRQ_MLBX1_USER1        | EVE3_MAILBOX1    | Eve 3 Mailbox 1 user 1 interrupt   |
+---------+--------------+---------+-----------------------------+------------------+------------------------------------+
| 59      | 0x4A0029FC   | 28      | EVE4_IRQ_MBX1_USER1         | EVE4_MAILBOX1    | Eve4 Mailbox 1 user 1 interrupt    |
+---------+--------------+---------+-----------------------------+------------------+------------------------------------+
| 60      | 0x4A002A00   | 29      | MAILBOX7_IRQ_USER1          | MAILBOX7         | Mailbox 7 user 1 interrupt         |
+---------+--------------+---------+-----------------------------+------------------+------------------------------------+
| 61      | 0x4A002A00   | 30      | MAILBOX8_IRQ_USER1          | MAILBOX8         | Mailbox 8 user 1 interrupt         |
+---------+--------------+---------+-----------------------------+------------------+------------------------------------+

**IPU1 Interrupt Mapping**

+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| Index   | Addr         | Value   | Name                       | Source           | Description                        |
+=========+==============+=========+============================+==================+====================================+
| 64      | 0x4A002830   | 42      | EVE1_IRQ_MBX0_USER2        | EVE1_MAILBOX0    | Eve1 Mailbox 0 user 2 interrupt    |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 65      | 0x4A002834   | 43      | EVE2_IRQ_MBX0_USER2        | EVE2_MAILBOX0    | Eve2 Mailbox 0 user 2 interrupt    |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 66      | 0x4A002834   | 44      | MAILBOX5_IRQ_USER1         | MAILBOX5         | Mailbox 5 user 1 interrupt         |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 67      | 0x4A002838   | 45      | EVE3_IRQ_MBX0_USER2        | EVE3_MAILBOX0    | Eve 3 Mailbox 0 user 2 interrupt   |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 68      | 0x4A002838   | 46      | EVE4_IRQ_MBX0_USER2        | EVE4_MAILBOX0    | Eve4 Mailbox 0 user 2 interrupt    |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 69      | 0x4A00283C   | 47      | MAILBOX7_IRQ_USER2         | MAILBOX7         | Mailbox 7 user 2 interrupt         |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 70      | 0x4A00283C   | 48      | MAILBOX8_IRQ_USER2         | MAILBOX8         | Mailbox 8 user 2 interrupt         |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 71      | 0x4A002840   | 49      | EVE1_IRQ_MBX1_USER3        | EVE1_MAILBOX1    | Eve1 Mailbox 1 user 3 interrupt    |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 72      | 0x4A002840   | 50      | EVE2_IRQ_MBX1_USER3        | EVE2_MAILBOX1    | Eve2 Mailbox 1 user 3 interrupt    |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 73      | 0x4A002844   | 51      | MAILBOX5_IRQ_USER3         | MAILBOX5         | Mailbox 5 user 3 interrupt         |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 74      | 0x4A002844   | 52      | EVE3_IRQ_MBX1_USER3        | EVE3_MAILBOX1    | Eve 3 Mailbox 1 user 3 interrupt   |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 75      | 0x4A002848   | 53      | EVE4_IRQ_MBX1_USER3        | EVE4_MAILBOX1    | Eve4 Mailbox 1 user 3 interrupt    |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 76      | 0x4A002848   | 54      | MAILBOX8_IRQ_USER2         | MAILBOX8         | Mailbox 8 user 2 interrupt         |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+

|

**IPU2 Interrupt Mapping**

+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| Index   | Addr         | Value   | Name                       | Source           | Description                        |
+=========+==============+=========+============================+==================+====================================+
| 64      | 0x4A0028A4   | 42      | EVE1_IRQ_MBX1_USER2        | EVE1_MAILBOX1    | Eve1 Mailbox 1 user 2 interrupt    |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 65      | 0x4A0028A8   | 43      | EVE2_IRQ_MBX1_USER2        | EVE2_MAILBOX1    | Eve2 Mailbox 1 user 2 interrupt    |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 66      | 0x4A0028A8   | 44      | MAILBOX6_IRQ_USER1         | MAILBOX6         | Mailbox 6 user 1 interrupt         |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 67      | 0x4A0028AC   | 45      | EVE3_IRQ_MBX1_USER2        | EVE3_MAILBOX1    | Eve 3 Mailbox 1 user 2 interrupt   |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 68      | 0x4A0028AC   | 46      | EVE4_IRQ_MBX1_USER2        | EVE4_MAILBOX1    | Eve4 Mailbox 1 user 2 interrupt    |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 69      | 0x4A0028B0   | 47      | MAILBOX7_IRQ_USER3         | MAILBOX7         | Mailbox 7 user 3 interrupt         |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 70      | 0x4A0028B0   | 48      | MAILBOX8_IRQ_USER3         | MAILBOX8         | Mailbox 8 user 3 interrupt         |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 71      | 0x4A0028B4   | 49      | EVE1_IRQ_MBX1_USER3        | EVE1_MAILBOX1    | Eve1 Mailbox 1 user 3 interrupt    |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 72      | 0x4A0028B4   | 50      | EVE2_IRQ_MBX1_USER3        | EVE2_MAILBOX1    | Eve2 Mailbox 1 user 3 interrupt    |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 73      | 0x4A0028B8   | 51      | MAILBOX6_IRQ_USER3         | MAILBOX6         | Mailbox 6 user 3 interrupt         |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 74      | 0x4A0028B8   | 52      | EVE3_IRQ_MBX1_USER3        | EVE3_MAILBOX1    | Eve 3 Mailbox 1 user 3 interrupt   |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 75      | 0x4A0028BC   | 53      | EVE4_IRQ_MBX1_USER3        | EVE4_MAILBOX1    | Eve4 Mailbox 1 user 3 interrupt    |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+
| 76      | 0x4A0028BC   | 54      | MAILBOX8_IRQ_USER3         | MAILBOX8         | Mailbox 8 user 3 interrupt         |
+---------+--------------+---------+----------------------------+------------------+------------------------------------+

