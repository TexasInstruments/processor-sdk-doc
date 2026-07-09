.. _hsr-prp-ptp:

=======================
HSR and PRP PTP support
=======================

The `TI fork of linuxptp <https://git.ti.com/cgit/processor-sdk/linuxptp>`_
on the ``hsr_prp_ptp`` branch supports PTP (Precision Time Protocol)
synchronization over High-availability Seamless Redundancy (HSR) and Parallel Redundancy
Protocol (PRP) interfaces.

In the following commands, replace ``<proto>`` with ``hsr`` or ``prp`` as appropriate.

.. rubric:: Prerequisites

Complete the following steps on each node.

Clone linuxptp:

.. code-block:: console

   git clone --single-branch --branch hsr_prp_ptp https://git.ti.com/cgit/processor-sdk/linuxptp
   cd linuxptp

Build and install:

.. code-block:: console

   make && make install

.. rubric:: Running PTP

Set up the HSR or PRP interface as described in the respective offload documentation.
On the PTP primary node:

.. code-block:: console

   ./ptp4l -f configs/<proto>-master.cfg

On each PTP secondary node:

.. code-block:: console

   ./ptp4l -f configs/<proto>-slave.cfg

.. rubric:: Verifying PTP synchronization

Inspect the ``master offset`` values in the ptp4l log output to verify PTP synchronization.

Sample ptp4l output showing a synchronized secondary node:

.. code-block:: text

   ptp4l[xx.xxx]: master offset   -123 s2 freq  +4321 path delay   543
   ptp4l[xx.xxx]: master offset     45 s2 freq  +4290 path delay   541
   ptp4l[xx.xxx]: master offset    -78 s2 freq  +4310 path delay   544
