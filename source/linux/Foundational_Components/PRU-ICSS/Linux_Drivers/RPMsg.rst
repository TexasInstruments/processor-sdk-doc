.. _pru_rpmsg:

RPMsg
-----

Introduction
^^^^^^^^^^^^

RPMsg is a method of passing messages and data between the PRU cores and
the ARM core running Linux. RPMsg is
enabled by a combination of remoteproc and the virtio framework.

Supported Devices
"""""""""""""""""

Linux ARM to PRU RPMsg communication is supported on these processors:

 * AM335x

 * AM437x

 * AM572x

 * AM65x

 * AM64x

 * AM62x

.. rubric:: RPMsg
   :name: rpmsg

RPMsg is a message passing mechanism that requests resources through
remoteproc and builds on top of the virtio framework. Shared buffers are
requested through the resource_table and provided by the remoteproc
module during PRU firmware loading (as shown in the remoteproc procedure
above). The shared buffers are contained inside a vring data structure
in DDR memory. There are two vrings provided per PRU core, one vring is
used for messages passed to the ARM and the other vring is used for
messages received from the ARM. System level mailboxes are used to
notify cores (ARM or PRU) when new messages are waiting in the shared
buffers.

There are two RPMsg software implementations provided in the Linux
Processor SDK. On the ARM Linux side, RPMsg communication is received in
kernel space. An interface module is provided (rpmsg_pru) that creates
a character device in user space so that users can write/read to/from a
character device in the file system to send/receive messages to/from the
PRUs. On the PRU side, an RPMsg library is provided in the PRU Software
Support Package that aims to abstract the communication to a point where
a user's code can just call the pru_rpmsg_receive and pru_rpmsg_send
functions in order to communicate with the ARM core. Source code for the
PRU RPMsg library is provided in the support package along with the
ability to rebuild the library if changes are desired.

.. Image:: /images/Rpmsg_diagram_2_0_2_11.PNG

--------------

.. rubric:: ARM to PRU
   :name: arm-to-pru

.. Image:: /images/Arm-to-pru.PNG

The diagram to the right shows the process that occurs when the ARM
sends a message to the PRU. These steps are shown for illustrative
purposes as the provided software in the SDK hides them in an
abstraction layer.

-  ARM Host Steps

   -  Step 1a: Allocate a new buffer
      -or-
   -  Step 1b: Get a Used buffer from the slave Vring
   -  Step 2: Copy data to be transferred into the buffer from Step 1
   -  Step 3: Add the newly filled buffer to the Available list in the
      slave Vring
   -  Step 4: Kick the slave Vring by writing its index (1) into a
      message in Mailbox 2

-  PRU Steps

   -  Step 5: A Kick is discovered in Mailbox 2 with the index of the
      Kicked Vring (1). This indicates to the PRU that data is available
      for receive
   -  Step 6: Get the Available buffer from the slave Vring
   -  Step 7: Copy data to be received out of the buffer from Step 2
   -  Step 8: Add the now empty buffer to the Used list in the slave
      Vring
   -  Step 9: Kick the slave Vring by writing its index (1) into a
      message in Mailbox 3

|

.. rubric:: PRU to ARM
   :name: pru-to-arm

.. Image:: /images/Pru-to-arm.PNG

The diagram to the right shows the process that occurs when the PRU
sends a message to the ARM. These steps are shown for illustrative
purposes as the provided software in the SDK hides them in an
abstraction layer.

-  PRU Steps

   -  Step 1: Get an Available buffer from the host Vring
   -  Step 2: Copy data to be transferred into the buffer from Step 1
   -  Step 3: Add the newly filled buffer to the Used list in the host
      Vring
   -  Step 4: Kick the host Vring by writing its index (0) into a
      message in Mailbox 3

-  ARM Host Steps

   -  Step 5: An interrupt signals that Mailbox 3 was kicked with the
      index of Vring (0). This indicates to the ARM Host that data is
      available for receive
   -  Step 6: Get the Used buffer from the host Vring
   -  Step 7: Copy data to be received out of the buffer from Step 2
   -  Step 8: Add the now empty buffer to the Available list in the host
      Vring
   -  Step 9: Kick the host Vring by writing its index (0) into a
      message in Mailbox 2

|

.. rubric:: RPMsg PRU Code Example
   :name: rpmsg-pru-code-example

| The RPMsg library provided for the PRU cores attempts to abstract the
  underlying implementation (Vring transport layer, mailboxes, etc.) to
  make programming as simple as possible. See the code below for an
  example PRU firmware the that can receive, and then echo back,
  messages from the ARM core. This code is provided as an example in the
  PRU Software Support Package that is include in the Linux Processor
  SDK.

.. Image:: /images/Rpmsg_code.PNG

.. rubric:: Next Steps
   :name: next-steps

To get started quickly with remoteproc and RPMsg you can use the
:ref:`rpmsg_quick_start_guide`.

For Hands-on Labs that work with the BeagleBone Black and a PRU Cape take a look
at :ref:`pru_hands_on_labs`.

