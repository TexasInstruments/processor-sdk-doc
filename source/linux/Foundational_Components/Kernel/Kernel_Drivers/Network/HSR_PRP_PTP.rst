.. _hsr-prp-ptp:

=======================
HSR and PRP PTP support
=======================

The `linuxptp-hsr <https://git.kernel.org/pub/scm/linux/kernel/git/bigeasy/linuxptp-hsr.git>`_
implementation on the ``hsr_prp_v2_plus`` branch supports PTP (Precision Time Protocol)
synchronization over High-availability Seamless Redundancy (HSR) and Parallel Redundancy
Protocol (PRP) interfaces.

In the following commands, replace ``<proto>`` with ``hsr`` or ``prp`` as appropriate.

.. rubric:: Prerequisites

Complete the following steps on each node.

Clone linuxptp-hsr:

.. code-block:: console

   git clone https://git.kernel.org/pub/scm/linux/kernel/git/bigeasy/linuxptp-hsr.git
   cd linuxptp-hsr
   git checkout hsr_prp_v2_plus

Patch the config files with the actual interface names and the P2P destination MAC
address. The config files use INI-style sections where ``[eth1]`` and ``[eth2]``
denote the two physical interfaces. The first command appends the ``p2p_dst_mac``
key (destination MAC for P2P delay-request messages) into the ``[global]``
section just after the ``delay_mechanism`` key. The second command replaces the
``[eth1]`` and ``[eth2]`` section headers with the actual interface names:

.. code-block:: console

   sed -i '/^delay_mechanism/a p2p_dst_mac 01:1B:19:00:00:01' configs/<proto>-master.cfg configs/<proto>-slave.cfg
   sed -i 's/^\[eth1\]/[<INTF_A>]/; s/^\[eth2\]/[<INTF_B>]/' configs/<proto>-master.cfg configs/<proto>-slave.cfg

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
