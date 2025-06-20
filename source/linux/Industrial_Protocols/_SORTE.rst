**********************************
SORTE
**********************************

.. _sorte-overview:

Overview
===========

The Simple Open Real-time Ethernet protocol (SORTE) is a
TI-developed industrial Ethernet protocol that
supports 4-µs cycle time. The SORTE protocol operates exclusively on
TI's PRU-ICSS (Programmable Real-Time Unit Subsystem and Industrial
Communication SubSystem), and therefore, the ARM Cortex-A8, A9 or A15 processors
(depending on the device family) are available for industrial applications.
The Linux user space SORTE example uses the same firmware and supports
the same features as in RTOS, but implements the memory access through
Linux Userspace I/O (UIO) driver.

|

.. _sorte-memory-access-through-uio:

Memory Access through UIO
==========================

While RTOS can directly access memory locations, e.g.,
HW\_RD\_REG32(0x4b220000), Linux needs memory mapping of memory regions
to user space, and this is done using the UIO driver with linux file-I/O
like API such as open(), close(), read(), write(), and etc. More details
can be found from `here <Industrial_Protocols_PRU-ICSS.html#memory-access-and-interrupt-handling-through-uio>`__.

|

.. _sorte-rebuild-sorte-in-linux-user-spac:

Rebuild SORTE in Linux User Space
==================================

Processor SDK Linux has packaged the pre-built binary for the SORTE example,
which can be found on filesystem under /usr/bin directory

* master: pruss\_app\_sorte_\master\_[platform].out
* slave: pruss\_app\_sorte_\slave\_[platform].out


The source code of the SORTE application and firmware can be found at
`apps/sorte <http://git.ti.com/keystone-rtos/pruss-lld/trees/master/example/apps/sorte>`__.
The changes specific to Linux user space can be found by looking for the define of
"\_\_LINUX\_USER\_SPACE". The files to implement the UIO based memory
access can be found from `test/src <http://git.ti.com/keystone-rtos/pruss-lld/trees/master/test/src/armv7/linux>`__.


When there is need to modify the source code of SORTE application and/or firmware,
the SORTE application (which links the firmware statically) can be rebuilt through Yocto
recipes. In order to do so, please refer to `Building the SDK <Overview_Building_the_SDK.html>`__
to set up the build environment, and `Processor SDK Yocto
Recipes <Overview_Building_the_SDK.html#building-the-sdk-recipes>`__
to bitbake the recipes and install the newly built packages.

For example, the command below is for rebuilding the SORTE application for AM57xx.
If there is change for the SORTE firmware, the firmware will be rebuilt also.

::

    MACHINE=am57xx-evm bitbake pruss-lld-apps

After the bitbake command above is successfully done, the rebuilt sorte application can be
found from ./build/arago-tmp-external-arm-toolchain/work/am57xx\_evm-linux-gnueabi/pruss-lld-apps/<ver\_number>/packages-split/pruss-lld-apps/usr/bin
directory

|


.. _sorte-supported-evms:

Supported EVMs
==================

The following is a list of EVMS supported and the PRU-ICSS ethernet
ports to be used:

+--------------+-----------------------+-----------+-----------+
| **EVM Name** | **PRU-ICSS Instance** | **Port0** | **Port1** |
+--------------+-----------------------+-----------+-----------+
| idkAM437x    | PRU-ICSS instance 2   | J6        | J9        |
+--------------+-----------------------+-----------+-----------+
| idkAM571x    | PRU-ICSS instance 2   | J6        | J8        |
+--------------+-----------------------+-----------+-----------+
| idkAM572x    | PRU-ICSS instance 2   | J6        | J8        |
+--------------+-----------------------+-----------+-----------+
| idkAM574x    | PRU-ICSS instance 2   | J6        | J8        |
+--------------+-----------------------+-----------+-----------+

|


.. _sorte-running-sorte-example-in-linux-user-space:

Running SORTE Example in Linux User Space
===============================================

In order to run the SORTE applications, you will require one EVM running
as master and at least two EVMs running as slave (slave1/slave2).
Prior to running the applications, connect master Port0 to slave1 Port0,
and slave1 Port1 to slave2 Port0.

On the filesystem under :file:`/boot/dtb/` directory, link
:file:`<platfrom>-pru-excl-uio.dtb` as the default dtb file, and then reboot the
EVM. For AM571x IDK, ensure that Jumper J51 is not placed. That selects between
LCD function (J51 placed) and ICSS1 Ethernet (J51 removed). This also indicates
that ICSS-EMAC unit test cannot run with LCD connected on the AM571x IDK board.

After the EVMs are rebooted with the PRU UIO dtb files, run slave2 first,
then slave1, and lastly master. Note that the master device will wait until
it discovers two slave devices in the network. Console on the master will
print the following message until two slave devices are detected:
::

  sorte master: waiting for at least 2 SLAVE devices connected

Once two slave devices are detected by the master, the following print
will be seen on console and master will continue with state machine
and protocol processing:
::

  sorte master: 2 SLAVE devices connected

The slave device will continuosly display the number of packets it has
received on the console during input output exchange state of the
protocol until pass criteria is reached, e.g.,
::

  sorte slave: test in progress: current receive packet count: 35000
  sorte slave: test in progress: current receive packet count: 40000

Once pass criteria number of packets have been received, the following
print will be displayed on console:
::

  All tests have passed

|

.. rubric:: Sample Logs from AM572x IDK
   :name: sorte-sample-log-from-am572x-idk

**Master**

::

  root@am57xx-evm:~# pruss_app_sorte_master_am572x.out

  TI SORTE Demo Application
  PHY0: 0, PHY1: 1
  sorte master: 2 SLAVE devices connected

**Slave**

::

  root@am57xx-evm:~# pruss_app_sorte_slave_am572x.out

  TI SORTE Demo Application
  PHY0: 0, PHY1: 1
  sorte slave: test in progress: current receive packet count: 0
  sorte slave: test in progress: current receive packet count: 0
  sorte slave: test in progress: current receive packet count: 0
  sorte slave: test in progress: current receive packet count: 0
  sorte slave: test in progress: current receive packet count: 0
  sorte slave: test in progress: current receive packet count: 0
  sorte slave: test in progress: current receive packet count: 0
  sorte slave: test in progress: current receive packet count: 32020
  sorte slave: test in progress: current receive packet count: 19913
  sorte slave: test in progress: current receive packet count: 7806
  sorte slave: receive packet count: 61234
  All tests have passed


|

.. _sorte-additional-reference:

Additional Reference
=======================

+-----------------------------------+-----------------------------------+
| **Document**                      | **Location**                      |
+-----------------------------------+-----------------------------------+
| SORTE Master with PRU-ICSS        | http://www.ti.com/tool/TIDEP-0085 |
| Reference Design                  |                                   |
+-----------------------------------+-----------------------------------+
| SORTE Slave Device with PRU-ICSS  | http://www.ti.com/tool/TIDEP-0086 |
| Reference Design                  |                                   |
+-----------------------------------+-----------------------------------+

|
