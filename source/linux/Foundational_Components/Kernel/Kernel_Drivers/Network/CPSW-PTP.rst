PTP
===

.. contents:: :local:
    :depth: 3

Introduction
------------

The Common Platform Time Sync (CPTS) module is used to facilitate host
control of time sync operations. It enables compliance with the IEEE
1588-2008 standard for a precision clock synchronization protocol.

The support for CPTS module can be enabled by Kconfig option
CONFIG_TI_AM65_CPTS or through menuconfig tool.

When CPTS module is enabled it will exports a kernel interface for
specific clock drivers and a PTP clock API user space interface and
enable support for SIOCSHWTSTAMP and SIOCGHWTSTAMP socket ioctls. The
PTP exposes the PHC as a character device with standardized ioctls which
usually can be found at path:

.. code:: text

   /dev/ptpN

Supported PTP hardware clock functionality:

.. code:: text

   Basic clock operations
      - Set time
      - Get time
      - Shift the clock by a given offset atomically
      - Adjust clock frequency

.. code:: text

   Ancillary clock features
      - Time stamp external events
      - Periodic output signals configurable from user space
      - Synchronization of the Linux system time via the PPS subsystem

Supported parameters for SIOCSHWTSTAMP and SIOCGHWTSTAMP:

.. code:: text

   SIOCSHWTSTAMP
      hwtstamp_config.flags = 0
      hwtstamp_config.tx_type
         HWTSTAMP_TX_ON - enables hardware time stamping for outgoing packets
         HWTSTAMP_TX_OFF - no outgoing packet will need hardware time stamping
      hwtstamp_config.rx_filter
         HWTSTAMP_FILTER_NONE - time stamp no incoming packet at all
         HWTSTAMP_FILTER_ALL - time stamp any incoming packet

CPTS PTP packet timestamping default configuration when enabled
(SIOCSHWTSTAMP):


.. code:: text

   CPSW_PN_TS_CTL_REG
      TS_MSG_TYPE_EN = 0xF (Sync, Delay_Req, Pdelay_Req, and Pdelay_Resp.)
      TS_TX_ANNEX_F_EN = 1
      TS_TX_ANNEX_E_EN = 1
      TS_TX_ANNEX_D_EN = 1
      TS_TX_VLAN_LTYPE1_E = 1

.. code:: text

   CPSW_PN_TS_CTL_LTYPE2_REG
      TS_TTL_NONZERO = 1
      TS_320 = 1
      TS_319 = 1
      TS_132 = 1
      TS_131 = 1
      TS_130 = 1
      TS_129 = 1
      TS_107 = 1
      TS_LTYPE1 = 0x88F7 (ETH_P_1588)

.. code:: text

   CPSW_PN_TS_SEQ_LTYPE_REG
      TS_SEQ_ID_OFFSET = 0x1e
      TS_LTYPE1 = 0x88F7 (ETH_P_1588)

.. code:: text

   CPSW_PN_TS_VLAN_LTYPE_REG
      TS_VLAN_LTYPE1 =  0x8100 (ETH_P_8021Q)

For more information about PTP clock API and Network timestamping see
Linux kernel documentation

| `Documentation/driver-api/ptp.rst  <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/Documentation/driver-api/ptp.rst>`__
| `include/uapi/linux/ptp\_clock.h <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/include/uapi/linux/ptp_clock.h>`__
| `Documentation/ABI/testing/sysfs-ptp <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/Documentation/ABI/testing/sysfs-ptp>`__
| `Documentation/networking/timestamping.rst <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/Documentation/networking/timestamping.rst>`__
| `Documentation/driver-api/pps.rst <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/Documentation/driver-api/pps.rst>`__
|
| Code examples and tools:
| `tools/testing/selftests/ptp/testptp.c <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/tools/testing/selftests/ptp/testptp.c>`__
| `tools/testing/selftests/net/timestamping.c <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/tools/testing/selftests/net/timestamping.c>`__
|
| `Open Source Project linuxptp <http://linuxptp.sourceforge.net/>`__
| `Linux PPS tools <https://github.com/redlab-i/pps-tools>`__
|

To check the ptp clock adjustment with PTP protocol, a PTP slave
(client) and a PTP master (server) applications are needed to run on
separate devices (EVM or PC). Open source application package linuxptp
can be used as slave and as well as master. Hence TX timestamp
generation can be delayed (especially with low speed links) the ptp4l
"tx_timestamp_timeout" parameter needs to be set for ptp4l to work.

- create file ptp.cfg with content as below:

.. code:: text

   [global]
   tx_timestamp_timeout     400

- pass configuration file to ptp4l using "-f" option:

.. code:: console

   ptp4l -E -2 -H -i eth0  -l 6 -m -q -p /dev/ptpN -f ptp.cfg

-  Slave Side Examples

The following command can be used to run a ptp-over-L4 client on the evm
in slave mode

.. code:: console

   ./ptp4l -E -4 -H -i eth0 -s -l 7 -m -q -p /dev/ptpN

For ptp-over-L2 client, use the command

.. code:: console

   ./ptp4l -E -2 -H -i eth0 -s -l 7 -m -q -p /dev/ptpN

-  Master Side Examples

ptp4l can also be run in master mode. For example, the following command
starts a ptp4l-over-L2 master on an EVM using hardware timestamping,

.. code:: console

   ./ptp4l -E -2 -H -i eth0 -l 7 -m -q -p /dev/ptpN

On a Linux PC which does not support hardware timestamping, the
following command starts a ptp4l-over-L2 master using software
timestamping.

.. code:: console

   ./ptp4l -E -2 -S -i eth0 -l 7 -m -q

.. rubric:: Testing using testptp tool from Linux kernel
   :name: k3-testing-using-testptp-tool-from-linux-kernel

-  get the ptp clock time

.. code:: console

   # testptp -d /dev/ptpN -g
   clock time: 1493255613.608918429 or Thu Apr 27 01:13:33 2017

-  query the ptp clock's capabilities

.. code:: console

   # testptp -d /dev/ptpN -c
   capabilities:
   10000000 maximum frequency adjustment (ppb)
   0 programmable alarms
   4 external time stamp channels
   2 programmable periodic signals
   1 pulse per second
   0 programmable pins
   0 cross timestamping

-  Sanity testing of cpts ref frequency

Time difference between to testptp -g calls should be equal sleep time

.. code:: console

   # testptp -g -d /dev/ptpN && sleep 5 && testptp -g -d /dev/ptpN
   clock time: 1493255884.565859901 or Thu Apr 27 01:18:04 2017
   clock time: 1493255889.611065421 or Thu Apr 27 01:18:09 2017

-  shift the ptp clock time by 'val' seconds

.. code:: console

   # testptp -g -d /dev/ptpN && testptp -t 100 && testptp -g -d /dev/ptpN
   clock time: 1493256107.640649117 or Thu Apr 27 01:21:47 2017
   time shift okay
   clock time: 1493256207.678819093 or Thu Apr 27 01:23:27 2017

-  set the ptp clock time to 'val' seconds

.. code:: console

   # testptp -g -d /dev/ptpN && testptp -T 1000000 && testptp -g -d /dev/ptpN
   clock time: 1493256277.568238925 or Thu Apr 27 01:24:37 2017
   set time okay
   clock time: 100.018944504 or Thu Jan  1 00:01:40 1970

-  adjust the ptp clock frequency by 'val' ppb

.. code:: console

   # testptp -g -d /dev/ptpN && testptp -f 1000000 && testptp -g -d /dev/ptpN
   clock time: 151.347795184 or Thu Jan  1 00:02:31 1970
   frequency adjustment okay
   clock time: 151.386187454 or Thu Jan  1 00:02:31 1970

.. rubric:: Time stamping external events
   :name: k3-example-of-using-time-stamp-external-events

External events can be timestamped by the CPTS module. The CPTS module loads a hardware timestamp
event to the Event FIFO, whenever the HWx_TS_PUSH inputs are set. Thus, it is possible to
timestamp events by using the HWx_TS_PUSH inputs to the CPTS module.

The following example illustrates the process of timestamping an external event. The external
event in the example corresponds to the rising edge of GENF0 (Timestamp Generator Function).
This involves using the output of CPSWxG CPTS GENF0 as an input to one of the HWx_TS_PUSH inputs.

The process of routing the CPSWxG CPTS GENF0 output to any of the HWx_TS_PUSH inputs is achieved
through the Time Sync Router. The procedure to route the CPSWxG CPTS GENF0 output to HW4_TS_PUSH
input for example, involves modifying the device-tree node of the Time Sync Router, to map the
CPWSxG CPTS GENF0 output to HW4_TS_PUSH input.

The following block shows the Time Sync Router device-tree node with the mapping from CPSWxG CPTS
GENF0 to HW4_TS_PUSH added.

.. ifconfig:: CONFIG_part_variant in ('AM62AX','AM62X')

   .. code:: dts

      #define TS_OFFSET(pa, val)     (0x4+(pa)*4) (0x10000 | val)
      &timesync_router {
         pinctrl-names = "default";
         pinctrl-0 = <&cpsw_cpts>;

            /* Example of the timesync routing */
               cpsw_cpts: cpsw-cpts {
                        pinctrl-single,pins = <
                                 /* pps [cpsw cpts genf0] in16 -> out13 [cpsw cpts hw4_push] */
                                 TS_OFFSET(13, 16)
                        >;
               };
      };

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   .. code:: dts

      #define TS_OFFSET(pa, val)     (0x4+(pa)*4) (0x10000 | val)

      &timesync_router {
         pinctrl-names = "default";
         pinctrl-0 = <&cpsw_cpts>;

            /* Example of the timesync routing */
               cpsw_cpts: cpsw-cpts {
                        pinctrl-single,pins = <
                                 /* pps [cpsw cpts genf0] in21 -> out33 [cpsw cpts hw4_push] */
                                 TS_OFFSET(33, 21)
                        >;
               };
      };

.. ifconfig:: CONFIG_part_variant in ('J721E','J7200','J721S2','J784S4','J742S2')

    .. code:: dts

      #define TS_OFFSET(pa, val)     (0x4+(pa)*4) (0x10000 | val)

      &timesync_router {
         pinctrl-names = "default";
         pinctrl-0 = <&cpsw_cpts>;

            /* Example of the timesync routing */
               cpsw_cpts: cpsw-cpts {
                        pinctrl-single,pins = <
                                 /* pps [cpsw cpts genf0] in16 -> out25 [cpsw cpts hw4_push] */
                                 TS_OFFSET(25, 16)
                        >;
               };
      };

Similar approach can be used for routing the outputs of other timestamp generator functions (GENFy)
as inputs to other Hardware Timestamping push inputs (HWx_TS_PUSH).

The Input Sources and their indices, along with the Output Destinations and their indices for the
Time Sync Router are obtained from the documentation as mentioned below.

The Input Sources for the Time Sync Router are documented at:

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

   `Time Sync Router Input Sources for AM62AX <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/am62ax/interrupt_cfg.html#timesync-event-router0-interrupt-router-input-sources>`_

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   `Time Sync Router Input Sources for AM62X <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/am62x/interrupt_cfg.html#timesync-event-router0-interrupt-router-input-sources>`_

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   `Time Sync Router Input Sources for AM64X <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/am64x/interrupt_cfg.html#timesync-event-introuter0-interrupt-router-input-sources>`_

.. ifconfig:: CONFIG_part_variant in ('J721E')

   `Time Sync Router Input Sources for J721E <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/j721e/interrupt_cfg.html#timesync-intrtr0-interrupt-router-input-sources>`_

.. ifconfig:: CONFIG_part_variant in ('J7200')

   `Time Sync Router Input Sources for J7200 <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/j7200/interrupt_cfg.html#timesync-intrtr0-interrupt-router-input-sources>`_

.. ifconfig:: CONFIG_part_variant in ('J721S2')

   `Time Sync Router Input Sources for J721S2 <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/j721s2/interrupt_cfg.html#timesync-intrtr0-interrupt-router-input-sources>`_

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

   `Time Sync Router Input Sources for J784S4 <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/j784s4/interrupt_cfg.html#timesync-intrtr0-interrupt-router-input-sources>`_

The Output Destinations for the Time Sync Router are documented at:

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

   `Time Sync Router Output Destinations for AM62AX <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/am62ax/interrupt_cfg.html#cmp-event-introuter0-interrupt-router-output-destinations>`_

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   `Time Sync Router Output Destinations for AM62X <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/am62x/interrupt_cfg.html#cmp-event-introuter0-interrupt-router-output-destinations>`_

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   `Time Sync Router Output Destinations for AM64X <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/am64x/interrupt_cfg.html#timesync-event-introuter0-interrupt-router-output-destinations>`_

.. ifconfig:: CONFIG_part_variant in ('J721E')

   `Time Sync Router Output Destinations for J721E <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/j721e/interrupt_cfg.html#timesync-intrtr0-interrupt-router-output-destinations>`_

.. ifconfig:: CONFIG_part_variant in ('J7200')

   `Time Sync Router Output Destinations for J7200 <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/j7200/interrupt_cfg.html#timesync-intrtr0-interrupt-router-output-destinations>`_

.. ifconfig:: CONFIG_part_variant in ('J721S2')

   `Time Sync Router Output Destinations for J721S2 <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/j721s2/interrupt_cfg.html#timesync-intrtr0-interrupt-router-output-destinations>`_

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

   `Time Sync Router Output Destinations for J784S4 <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/j784s4/interrupt_cfg.html#timesync-intrtr0-interrupt-router-output-destinations>`_

To test that the timestamping feature works with the above changes, execute the following

.. code:: console

   # testptp -d /dev/ptpN -p 500000000 -i 0
   # testptp -d /dev/ptpN -e 5 -i 3
   event index 2 at 384.250000025
   event index 2 at 384.750000025
   event index 2 at 385.250000025
   event index 2 at 385.750000025
   event index 2 at 386.250000025

The first command is used to specify that /dev/ptpN has to be used as the clock, with the output
period ('p') being 500000000 nanoseconds (500 milliseconds) and the event index 'i' being 0
(corresponding to GENF0).

The second command is used to specify that /dev/ptpN has to be used as the clock, with the first
5 events to be output ('e') , corresponding to the event index 3 ('i'). Event index starts from
0, due to which, the 3 here corresponds to HW4_TS_PUSH.

.. rubric:: PPS Pulse Per Second support
   :name: k3-cpts-pps-support

The PPS support for |__PART_FAMILY_NAME__| can be enabled with the following steps:

1. Route the output of the CPSWxG CPTS timestamp generator function (GENFy) to one of the
   CPSWxG CPTS timestamp generator inputs (HWx_TS_PUSH) using the Time Sync Router, by
   modifying the device-tree node corresponding to the Time Sync Router:

For example, route CPSWxG CPTS GENF1 output to HW3_TS_PUSH input

.. ifconfig:: CONFIG_part_variant in ('AM62AX','AM62X')

    .. code:: dts

      #define TS_OFFSET(pa, val)     (0x4+(pa)*4) (0x10000 | val)

      &timesync_router {
            pinctrl-names = "default";
            pinctrl-0 = <&cpsw_cpts>;

            /* Example of timesync routing */
            cpsw_cpts: cpsw-cpts {
                  pinctrl-single,pins = <
                           /* pps [cpsw cpts genf1] in17 -> out12 [cpsw cpts hw3_push] */
                           TS_OFFSET(12, 17)
                  >;
            };
      };

.. ifconfig:: CONFIG_part_variant in ('AM64X')

    .. code:: dts

      #define TS_OFFSET(pa, val)     (0x4+(pa)*4) (0x10000 | val)
      &timesync_router {
            pinctrl-names = "default";
            pinctrl-0 = <&cpsw_cpts>;

            /* Example of timesync routing */
            cpsw_cpts: cpsw-cpts {
                  pinctrl-single,pins = <
                           /* pps [cpsw cpts genf1] in22 -> out32 [cpsw cpts hw3_push] */
                           TS_OFFSET(32, 22)
                  >;
            };
      };

.. ifconfig:: CONFIG_part_variant in ('J721E','J7200','J721S2','J784S4','J742S2')

    .. code:: dts

      #define TS_OFFSET(pa, val)     (0x4+(pa)*4) (0x10000 | val)

      &timesync_router {
            pinctrl-names = "default";
            pinctrl-0 = <&cpsw_cpts>;

            /* Example of timesync routing */
            cpsw_cpts: cpsw-cpts {
                  pinctrl-single,pins = <
                           /* pps [cpsw cpts genf1] in17 -> out24 [cpsw cpts hw3_push] */
                           TS_OFFSET(24, 17)
                  >;
            };
      };

2. Inform the mapping to the CPSWxG driver, by using the "ti,pps" device-tree property
   in the cpts device-tree node present within the CPSWxG device-tree node:

.. code:: dts

   &cpswx {
      cpts@3d000 {
               ti,pps = <2 1>;
      };
   };

The property "ti,pps" is of the form <x-1 y>, where x and y correspond to the choice of
HWx_TS_PUSH and GENFy.

PPS can now be tested using testptp and ppstest tools::

      # ./testptp -d /dev/ptpX -P 1
      pps for system time request okay
      # ./ppstest /dev/pps0
      trying PPS source "/dev/pps0"
      found PPS source "/dev/pps0"
      ok, found 1 source(s), now start fetching data...
      source 0 - assert 198.000000700, sequence: 7 - clear  0.000000000, sequence: 0
      source 0 - assert 199.000000700, sequence: 8 - clear  0.000000000, sequence: 0

.. note::

   When using PPS signal along with PTP, the ptp4l application has to be
   rerun **before** enabling the PPS signal. This is required in order to
   ensure that the PPS signal remains in sync with the PHC which in turn
   is synchronized with the PTP master clock via the ptp4l application.
   If the ptp4l application is run **after** enabling the PPS signal, then
   the PPS signal will **not** be in sync with the PHC. Additionally, if the
   ptp4l application is stopped and rerun at any point in time, then the
   command to generate the PPS signal also has to be rerurn accordingly.

Setup
------

1. In both J7VCL and AM625-SK, create a config file named **ptp.cfg** whose
contents are as follows:

.. code:: text

   [global]
   tx_timestamp_timeout 400

2. Install **ptp4l** if it is not already present on the boards.

PTP with Ordinary Clock (MAC mode)
-----------------------------------

J7VCL as master clock and AM625-SK as slave clock
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Assuming that eth1 is the interface on J7VCL that is connected to eth0
on AM625-SK, the following commands have to be run. The commands can be
modified for different interface connections.

**Steps:**


1. Run the following on J7VCL:

.. code:: console

   ptp4l -E -2 -H -i eth1 -l 6 -m -q -f ptp.cfg

2. Run the following on AM625-SK:

.. code:: console

   ptp4l -E -2 -H -i eth0 -s -l 6 -m -q -f ptp.cfg

**Observed Outputs:**

On J7VCL:

.. code:: console

   root@j7200-evm:~/TSN-PTP4L# ptp4l -E -2 -H -i eth1 -l 6 -m -q -f ptp.cfg
   ptp4l[1827.484]: selected /dev/ptp2 as PTP clock
   ptp4l[1827.561]: port 1 (eth1): INITIALIZING to LISTENING on INIT_COMPLETE
   ptp4l[1827.561]: port 0 (/var/run/ptp4l): INITIALIZING to LISTENING on INIT_COMPLETE
   ptp4l[1834.569]: port 1: announce timeout
   ptp4l[1834.569]: port 1 (eth1): LISTENING to MASTER on ANNOUNCE_RECEIPT_TIMEOUT_EXPIRES
   ptp4l[1834.569]: selected best master clock 70ff76.fffe.1d8c08
   ptp4l[1834.569]: selected local clock 70ff76.fffe.1d8c08 as best master
   ptp4l[1834.569]: port 1: assuming the grand master role

On AM625-SK:

.. code:: console

   root@am62xx-evm:~# ptp4l -E -2 -H -i eth0 -s -l 6 -m -q -f ptp.cfg
   ptp4l[1874.715]: selected /dev/ptp0 as PTP clock
   ptp4l[1874.763]: port 1 (eth0): INITIALIZING to LISTENING on INIT_COMPLETE
   ptp4l[1874.763]: port 0 (/var/run/ptp4l): INITIALIZING to LISTENING on INIT_COMPLETE
   ptp4l[1875.717]: port 1: new foreign master 70ff76.fffe.1d8c08-1
   ptp4l[1879.717]: selected best master clock 70ff76.fffe.1d8c08 on port 1
   ptp4l[1879.717]: selected best master clock 70ff76.fffe.1d8c08
   ptp4l[1879.717]: port 1 (eth0): LISTENING to UNCALIBRATED on RS_SLAVE
   ptp4l[1881.717]: master offset 1146408914 s0 freq      +0 path delay     -1582
   ptp4l[1882.717]: master offset 1146420591 s1 freq  +11677 path delay     -2965
   ptp4l[1883.717]: master offset      -4307 s2 freq   +7370 path delay     -2965
   ptp4l[1883.717]: port 1 (eth0): UNCALIBRATED to SLAVE on MASTER_CLOCK_SELECTED
   ptp4l[1884.717]: master offset      -1385 s2 freq   +9000 path delay     -2965
   ptp4l[1885.717]: master offset      -1480 s2 freq   +8489 path delay     -1582
   ptp4l[1886.717]: master offset       -405 s2 freq   +9120 path delay      -851
   ptp4l[1887.717]: master offset         48 s2 freq   +9452 path delay      -121
   ptp4l[1888.717]: master offset        888 s2 freq  +10306 path delay      -121
   ptp4l[1889.717]: master offset        758 s2 freq  +10442 path delay         3
   ptp4l[1890.718]: master offset        614 s2 freq  +10526 path delay         3
   ptp4l[1891.717]: master offset        -96 s2 freq  +10000 path delay       479
   ptp4l[1892.718]: master offset        199 s2 freq  +10266 path delay       479
   ptp4l[1893.718]: master offset        221 s2 freq  +10348 path delay       497
   ptp4l[1894.718]: master offset        145 s2 freq  +10338 path delay       519
   ptp4l[1895.718]: master offset        103 s2 freq  +10340 path delay       519
   ptp4l[1896.718]: master offset         43 s2 freq  +10311 path delay       529
   ptp4l[1897.718]: master offset         17 s2 freq  +10297 path delay       529
   ptp4l[1898.718]: master offset         12 s2 freq  +10298 path delay       529
   ptp4l[1899.718]: master offset          3 s2 freq  +10292 path delay       529
   ptp4l[1900.718]: master offset         -3 s2 freq  +10287 path delay       529
   ptp4l[1901.718]: master offset          2 s2 freq  +10291 path delay       529
   ptp4l[1902.718]: master offset         -7 s2 freq  +10283 path delay       529
   ptp4l[1903.718]: master offset          0 s2 freq  +10288 path delay       528
   ptp4l[1904.718]: master offset         -3 s2 freq  +10285 path delay       528
   ptp4l[1905.718]: master offset         -9 s2 freq  +10278 path delay       526
   ptp4l[1906.718]: master offset          0 s2 freq  +10284 path delay       525
   ptp4l[1907.718]: master offset          8 s2 freq  +10292 path delay       524
   ptp4l[1908.718]: master offset          2 s2 freq  +10288 path delay       524
   ptp4l[1909.718]: master offset          6 s2 freq  +10293 path delay       524
   ptp4l[1910.718]: master offset         -6 s2 freq  +10283 path delay       524
   ptp4l[1911.718]: master offset          3 s2 freq  +10290 path delay       523
   ptp4l[1912.718]: master offset          3 s2 freq  +10291 path delay       523
   ptp4l[1913.718]: master offset          4 s2 freq  +10293 path delay       523
   ptp4l[1914.719]: master offset         -3 s2 freq  +10287 path delay       523
   ptp4l[1915.719]: master offset          9 s2 freq  +10298 path delay       522
   ptp4l[1916.718]: master offset          1 s2 freq  +10293 path delay       523
   ptp4l[1917.719]: master offset          2 s2 freq  +10294 path delay       523
   ptp4l[1918.719]: master offset        -12 s2 freq  +10281 path delay       523

AM625-SK as master clock and J7VCL as slave clock
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Assuming that eth1 is the interface on J7VCL that is connected to eth0
on AM625-SK, the following commands have to be run. The commands can be
modified for different interface connections.

**Steps:**

1. Run the following on AM625-SK:

.. code:: console

   ptp4l -E -2 -H -i eth0 -l 6 -m -q -f ptp.cfg

2. Run the following on J7VCL:

.. code:: console

   ptp4l -E -2 -H -i eth1 -s -l 6 -m -q -f ptp.cfg

**Observed Outputs:**

On AM625-SK:

.. code:: console

   root@am62xx-evm:~# ptp4l -E -2 -H -i eth0 -l 6 -m -q -f ptp.cfg
   ptp4l[2647.841]: selected /dev/ptp0 as PTP clock
   ptp4l[2647.895]: port 1 (eth0): INITIALIZING to LISTENING on INIT_COMPLETE
   ptp4l[2647.895]: port 0 (/var/run/ptp4l): INITIALIZING to LISTENING on INIT_COMPLETE
   ptp4l[2655.009]: port 1: announce timeout
   ptp4l[2655.010]: port 1 (eth0): LISTENING to MASTER on ANNOUNCE_RECEIPT_TIMEOUT_EXPIRES
   ptp4l[2655.010]: selected best master clock f4844c.fffe.fc1151
   ptp4l[2655.010]: selected local clock f4844c.fffe.fc1151 as best master
   ptp4l[2655.010]: port 1: assuming the grand master role

On J7VCL:

.. code:: console

   root@j7200-evm:~/TSN-PTP4L# ptp4l -E -2 -H -i eth1 -s -l 6 -m -q -f ptp.cfg
   ptp4l[2215.575]: selected /dev/ptp2 as PTP clock
   ptp4l[2215.657]: port 1 (eth1): INITIALIZING to LISTENING on INIT_COMPLETE
   ptp4l[2215.657]: port 0 (/var/run/ptp4l): INITIALIZING to LISTENING on INIT_COMPLETE
   ptp4l[2215.787]: port 1: new foreign master f4844c.fffe.fc1151-1
   ptp4l[2219.787]: selected best master clock f4844c.fffe.fc1151 on port 1
   ptp4l[2219.787]: selected best master clock f4844c.fffe.fc1151
   ptp4l[2219.787]: port 1 (eth1): LISTENING to UNCALIBRATED on RS_SLAVE
   ptp4l[2221.786]: master offset      15033 s0 freq      +0 path delay       -38
   ptp4l[2222.787]: master offset      16404 s2 freq   +1371 path delay       -38
   ptp4l[2222.787]: port 1 (eth1): UNCALIBRATED to SLAVE on MASTER_CLOCK_SELECTED
   ptp4l[2223.787]: master offset      15861 s2 freq  +17232 path delay       523
   ptp4l[2224.786]: master offset         27 s2 freq   +6156 path delay       523
   ptp4l[2225.787]: master offset      -4768 s2 freq   +1369 path delay       523
   ptp4l[2226.787]: master offset      -4758 s2 freq     -51 path delay       523
   ptp4l[2227.787]: master offset      -3322 s2 freq     -43 path delay       520
   ptp4l[2228.787]: master offset      -1895 s2 freq    +388 path delay       520
   ptp4l[2229.787]: master offset       -725 s2 freq    +989 path delay       344
   ptp4l[2230.787]: master offset       -334 s2 freq   +1163 path delay       344
   ptp4l[2231.787]: master offset       -253 s2 freq   +1144 path delay       482
   ptp4l[2232.787]: master offset        -11 s2 freq   +1310 path delay       477
   ptp4l[2233.787]: master offset         39 s2 freq   +1356 path delay       490
   ptp4l[2234.787]: master offset         43 s2 freq   +1372 path delay       490
   ptp4l[2235.787]: master offset         39 s2 freq   +1381 path delay       490
   ptp4l[2236.787]: master offset         31 s2 freq   +1385 path delay       490
   ptp4l[2237.787]: master offset         13 s2 freq   +1376 path delay       490
   ptp4l[2238.787]: master offset         -3 s2 freq   +1364 path delay       490
   ptp4l[2239.787]: master offset         -3 s2 freq   +1363 path delay       490
   ptp4l[2240.787]: master offset        -10 s2 freq   +1355 path delay       500
   ptp4l[2241.787]: master offset        -26 s2 freq   +1336 path delay       521
   ptp4l[2242.787]: master offset        -14 s2 freq   +1340 path delay       521
   ptp4l[2243.788]: master offset         18 s2 freq   +1368 path delay       521
   ptp4l[2244.788]: master offset         13 s2 freq   +1369 path delay       524
   ptp4l[2245.788]: master offset         17 s2 freq   +1376 path delay       524
   ptp4l[2246.788]: master offset         -6 s2 freq   +1359 path delay       524
   ptp4l[2247.788]: master offset        -19 s2 freq   +1344 path delay       524
   ptp4l[2248.788]: master offset         -6 s2 freq   +1351 path delay       524

PTP with Transparent Clock (Switch mode)
----------------------------------------

Use the following ptp config file on the device that acts as the transparent clock:

**tc-ptp.cfg**

.. code:: text

   [global]
   tx_timestamp_timeout 400
   clock_type           E2E_TC

On other devices, the existing ptp.cfg file can be used.

J7VCL as transparent clock, PC as master clock and AM625-SK as slave clock
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Switch mode is enabled on J7VCL, with the CPSW5G ports in QSGMII mode acting
as switch ports. A PC (Personal Computer) with Software Timestamping
capability is used (PC with Hardware Timestamping capability or another
board is preferred) as the master clock. The setup is as follows:

PC is connected to eth1 of J7VCL's CPSW5G ports while AM625-SK's eth0 is
connected to J7VCL's eth2.

.. note::

   Since the PC uses Software Timestamping, the offset is relatively
   large when compared to the previous section where only boards with
   Hardware Timestamping capabilities were used.

**Steps:**

1. Enable switch mode on J7VCL by running the following commands:

.. code:: console

   devlink dev param set platform/c000000.ethernet name switch_mode value true cmode runtime
   ip link add name br0 type bridge
   ip link set dev br0 type bridge ageing_time 1000
   ip link set dev eth1 up
   ip link set dev eth2 up
   ip link set dev eth1 master br0
   ip link set dev eth2 master br0
   ip link set dev br0 up
   ip link set dev br0 type bridge vlan_filtering 1
   bridge vlan add dev br0 vid 1 self
   bridge vlan add dev br0 vid 1 pvid untagged self
   # Ensure that multicast flooding is off
   bridge link set dev eth1 mcast_flood off
   bridge link set dev eth2 mcast_flood off

2. On the PC, create the same ptp.cfg file mentioned earlier and run:

.. code:: console

   sudo ptp4l -E -2 -S -i enp2s0 -l 6 -m -q -f ptp.cfg

enp2s0 is assumed to be the ethernet interface.
Replace -S with -H if PC supports Hardware Timestamping.

3. On J7VCL, run:

.. code:: console

   ptp4l -E -2 -H -i eth1 -i eth2 -s -f tc-ptp.cfg --step_threshold=1 -m -q

4. On AM625-SK, run:

.. code:: console

   ptp4l -E -2 -H -i eth0 -s -l 6 -m -q -f ptp.cfg

**Observed Outputs:**

On PC:

.. code:: console

   user@pc:~/TSN-PTP4L$ sudo ptp4l -E -2 -S -i enp2s0 -l 6 -m -q -f p.cfg
   ptp4l[16750.478]: port 1: INITIALIZING to LISTENING on INITIALIZE
   ptp4l[16750.478]: port 0: INITIALIZING to LISTENING on INITIALIZE
   ptp4l[16750.478]: port 1: link up
   ptp4l[16757.189]: port 1: LISTENING to MASTER on ANNOUNCE_RECEIPT_TIMEOUT_EXPIRES
   ptp4l[16757.189]: selected best master clock b0227a.fffe.d8b7e3
   ptp4l[16757.189]: assuming the grand master role

On J7VCL:

.. code:: console

   root@j7200-evm:~/PTP# ptp4l -E -2 -H -i eth1 -i eth2 -s -f ptp.cfg --step_threshold=1 -q -m
   ptp4l[602.896]: selected /dev/ptp2 as PTP clock
   ptp4l[602.936]: port 1 (eth1): INITIALIZING to LISTENING on INIT_COMPLETE
   ptp4l[602.968]: port 2 (eth2): INITIALIZING to LISTENING on INIT_COMPLETE
   ptp4l[602.968]: port 0 (/var/run/ptp4l): INITIALIZING to LISTENING on INIT_COMPLETE
   ptp4l[604.014]: port 1: new foreign master b0227a.fffe.d8b7e3-1
   ptp4l[608.014]: selected best master clock b0227a.fffe.d8b7e3 on port 1
   ptp4l[608.014]: selected best master clock b0227a.fffe.d8b7e3
   ptp4l[608.014]: foreign master not using PTP timescale
   ptp4l[608.014]: running in a temporal vortex
   ptp4l[608.014]: port 1 (eth1): LISTENING to UNCALIBRATED on RS_SLAVE
   ptp4l[609.182]: selected best master clock b0227a.fffe.d8b7e3 on port 1
   ptp4l[609.182]: selected best master clock b0227a.fffe.d8b7e3
   ptp4l[609.182]: foreign master not using PTP timescale
   ptp4l[609.182]: running in a temporal vortex
   ptp4l[610.015]: master offset    4240878 s0 freq  -29261 path delay    411528
   ptp4l[611.015]: master offset    4420049 s1 freq +149852 path delay    411528
   ptp4l[612.015]: master offset    -217741 s2 freq  -67889 path delay    411528
   ptp4l[612.015]: port 1 (eth1): UNCALIBRATED to SLAVE on MASTER_CLOCK_SELECTED
   ptp4l[613.015]: master offset      19010 s2 freq +103540 path delay    411528
   ptp4l[614.015]: master offset    -169233 s2 freq  -79000 path delay    432761
   ptp4l[615.015]: master offset      74375 s2 freq +113838 path delay    432761
   ptp4l[615.965]: selected best master clock b0227a.fffe.d8b7e3 on port 1
   ptp4l[615.965]: selected best master clock b0227a.fffe.d8b7e3
   ptp4l[615.965]: foreign master not using PTP timescale
   ptp4l[615.965]: running in a temporal vortex
   ptp4l[616.015]: master offset    -249811 s2 freq -188035 path delay    447928
   ptp4l[617.016]: master offset     255527 s2 freq +195312 path delay    429728
   ptp4l[618.016]: master offset     -92188 s2 freq -105356 path delay    447928
   ptp4l[619.016]: master offset     279496 s2 freq +195312 path delay    429728
   ptp4l[620.016]: master offset     -53619 s2 freq  -94443 path delay    447928
   ptp4l[621.016]: master offset     258016 s2 freq +195312 path delay    447928
   ptp4l[622.016]: master offset    -143222 s2 freq -195312 path delay    453994
   ptp4l[623.016]: master offset     355710 s2 freq +195312 path delay    453994
   ptp4l[623.037]: selected best master clock b0227a.fffe.d8b7e3 on port 1
   ptp4l[623.037]: selected best master clock b0227a.fffe.d8b7e3
   ptp4l[623.037]: foreign master not using PTP timescale
   ptp4l[623.037]: running in a temporal vortex
   ptp4l[624.016]: master offset     -81029 s2 freq -137939 path delay    456066
   ptp4l[625.017]: master offset     399612 s2 freq +195312 path delay    456066
   ptp4l[626.017]: master offset     -59174 s2 freq -140392 path delay    456066
   ptp4l[627.017]: master offset     535534 s2 freq +195312 path delay    372817
   ptp4l[628.017]: master offset      68957 s2 freq  -30014 path delay    372817
   ptp4l[629.017]: master offset     469268 s2 freq +195312 path delay    372817
   ptp4l[630.017]: master offset     227264 s2 freq +148980 path delay    465639
   ptp4l[630.879]: selected best master clock b0227a.fffe.d8b7e3 on port 1
   ptp4l[630.879]: selected best master clock b0227a.fffe.d8b7e3
   ptp4l[630.879]: foreign master not using PTP timescale
   ptp4l[630.879]: running in a temporal vortex
   ptp4l[631.018]: master offset     188501 s2 freq +178397 path delay    416485
   ptp4l[632.017]: master offset    -292192 s2 freq -195312 path delay    416485
   ptp4l[633.018]: master offset     392634 s2 freq +195312 path delay    322010
   ptp4l[634.017]: master offset     -61040 s2 freq  -14594 path delay    322010
   ptp4l[635.018]: master offset     318688 s2 freq +195312 path delay    322010
   ptp4l[636.018]: master offset    -177868 s2 freq -149734 path delay    322010
   ptp4l[637.018]: master offset     371574 s2 freq +195312 path delay    320475
   ptp4l[637.827]: selected best master clock b0227a.fffe.d8b7e3 on port 1
   ptp4l[637.827]: selected best master clock b0227a.fffe.d8b7e3
   ptp4l[637.827]: foreign master not using PTP timescale
   ptp4l[637.827]: running in a temporal vortex
   ptp4l[638.018]: master offset     129834 s2 freq +104608 path delay    420138
   ptp4l[639.018]: master offset      71472 s2 freq  +85196 path delay    420138
   ptp4l[640.019]: master offset      45549 s2 freq  +80714 path delay    411496
   ptp4l[641.019]: master offset      15511 s2 freq  +64341 path delay    411496
   ptp4l[642.019]: master offset     -41550 s2 freq  +11933 path delay    451793
   ptp4l[643.019]: master offset       3387 s2 freq  +44405 path delay    441161
   ptp4l[644.019]: master offset       6207 s2 freq  +48241 path delay    441161
   ptp4l[644.259]: selected best master clock b0227a.fffe.d8b7e3 on port 1
   ptp4l[644.259]: selected best master clock b0227a.fffe.d8b7e3
   ptp4l[644.259]: foreign master not using PTP timescale
   ptp4l[644.259]: running in a temporal vortex
   ptp4l[645.019]: master offset      11684 s2 freq  +55581 path delay    437299
   ptp4l[646.019]: master offset       1653 s2 freq  +49055 path delay    443743
   ptp4l[647.019]: master offset      -6190 s2 freq  +41708 path delay    447606
   ptp4l[648.019]: master offset       3011 s2 freq  +49052 path delay    444569
   ptp4l[649.020]: master offset       3506 s2 freq  +50450 path delay    447606
   ptp4l[650.020]: master offset      -6195 s2 freq  +41801 path delay    447606
   ptp4l[650.630]: selected best master clock b0227a.fffe.d8b7e3 on port 1
   ptp4l[650.630]: selected best master clock b0227a.fffe.d8b7e3
   ptp4l[650.630]: foreign master not using PTP timescale
   ptp4l[650.630]: running in a temporal vortex
   ptp4l[651.020]: master offset       3461 s2 freq  +49598 path delay    442913
   ptp4l[652.020]: master offset       2104 s2 freq  +49280 path delay    442913

On AM625-SK:

.. code:: console

   root@am62xx-evm:~# ptp4l -E -2 -H -i eth0 -s -l 6 -m -q -f ptp.cfg
   ptp4l[618.874]: selected /dev/ptp0 as PTP clock
   ptp4l[618.927]: port 1 (eth0): INITIALIZING to LISTENING on INIT_COMPLETE
   ptp4l[618.927]: port 0 (/var/run/ptp4l): INITIALIZING to LISTENING on INIT_COMPLETE
   ptp4l[619.431]: port 1: new foreign master b0227a.fffe.d8b7e3-1
   ptp4l[623.431]: selected best master clock b0227a.fffe.d8b7e3 on port 1
   ptp4l[623.431]: selected best master clock b0227a.fffe.d8b7e3
   ptp4l[623.431]: foreign master not using PTP timescale
   ptp4l[623.431]: running in a temporal vortex
   ptp4l[623.431]: port 1 (eth0): LISTENING to UNCALIBRATED on RS_SLAVE
   ptp4l[625.432]: master offset    4167996 s0 freq  -15185 path delay    414520
   ptp4l[626.432]: master offset    4365478 s1 freq +182227 path delay    414520
   ptp4l[627.432]: master offset    -235340 s2 freq  -53113 path delay    414520
   ptp4l[627.432]: port 1 (eth0): UNCALIBRATED to SLAVE on MASTER_CLOCK_SELECTED
   ptp4l[628.432]: master offset      33747 s2 freq +145372 path delay    376516
   ptp4l[629.432]: master offset    -293346 s2 freq -171597 path delay    376516
   ptp4l[630.432]: master offset     228692 s2 freq +262438 path delay    338513
   ptp4l[631.432]: master offset    -192552 s2 freq  -90199 path delay    376516
   ptp4l[632.433]: master offset     159142 s2 freq +203730 path delay    376516
   ptp4l[633.433]: master offset    -188770 s2 freq  -96440 path delay    414520
   ptp4l[634.433]: master offset     176253 s2 freq +211952 path delay    376516
   ptp4l[635.433]: master offset    -222145 s2 freq -133570 path delay    376516
   ptp4l[636.433]: master offset     306349 s2 freq +328281 path delay    298604
   ptp4l[637.433]: master offset    -247846 s2 freq -134010 path delay    298604
   ptp4l[638.433]: master offset     242133 s2 freq +281616 path delay    298604
   ptp4l[639.433]: master offset    -289587 s2 freq -177465 path delay    298604
   ptp4l[640.434]: master offset     291214 s2 freq +316460 path delay    279683
   ptp4l[641.434]: master offset    -283245 s2 freq -170634 path delay    279683
   ptp4l[642.434]: master offset     294661 s2 freq +322298 path delay    256129
   ptp4l[643.434]: master offset      31931 s2 freq +147966 path delay    256129
   ptp4l[644.434]: master offset     -41547 s2 freq  +84068 path delay    256129
   ptp4l[645.434]: master offset    -414538 s2 freq -301387 path delay    256129
   ptp4l[646.435]: master offset     299758 s2 freq +288547 path delay    251884
   ptp4l[647.434]: master offset    -233796 s2 freq -155079 path delay    251884
   ptp4l[648.435]: master offset     282743 s2 freq +291321 path delay    268964
   ptp4l[649.435]: master offset    -296428 s2 freq -203027 path delay    268964
   ptp4l[650.435]: master offset     318129 s2 freq +322601 path delay    268964
   ptp4l[651.435]: master offset      54329 s2 freq +154240 path delay    276656
   ptp4l[652.436]: master offset     -40272 s2 freq  +75938 path delay    276656
   ptp4l[653.436]: master offset     -52185 s2 freq  +51943 path delay    276656
   ptp4l[654.436]: master offset    -124449 s2 freq  -35976 path delay    361074
   ptp4l[655.436]: master offset     -90327 s2 freq  -39189 path delay    423913
   ptp4l[656.436]: master offset       8536 s2 freq  +32576 path delay    423913
   ptp4l[657.436]: master offset      37342 s2 freq  +63943 path delay    423175
   ptp4l[658.436]: master offset      15742 s2 freq  +53545 path delay    444110
   ptp4l[659.436]: master offset      27596 s2 freq  +70122 path delay    444110
   ptp4l[660.436]: master offset      13826 s2 freq  +64631 path delay    446241
   ptp4l[661.437]: master offset      10467 s2 freq  +65419 path delay    446241
   ptp4l[662.437]: master offset      11032 s2 freq  +69124 path delay    446241
   ptp4l[663.437]: master offset      -3933 s2 freq  +57469 path delay    446241
   ptp4l[664.437]: master offset        735 s2 freq  +60957 path delay    444278

AM625-SK as transparent clock, PC as master clock and J7VCL as slave clock
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Switch mode is enabled on AM625-SK, with the CPSW3G ports in RGMII mode acting
as switch ports. A PC (Personal Computer) with Software Timestamping
capability is used (PC with Hardware Timestamping capability or another
board is preferred) as the master clock. The setup is as follows:

PC is connected to eth0 of AM625-SK's CPSW3G ports while J7VCL's eth1 is
connected to AM625-SK's eth1.

**Steps:**

1. Enable switch mode on AM625-SK by running the following commands:

.. code:: console

   devlink dev param set platform/8000000.ethernet name switch_mode value true cmode runtime
   ip link add name br0 type bridge
   ip link set dev br0 type bridge ageing_time 1000
   ip link set dev eth0 up
   ip link set dev eth1 up
   ip link set dev eth0 master br0
   ip link set dev eth1 master br0
   ip link set dev br0 up
   ip link set dev br0 type bridge vlan_filtering 1
   bridge vlan add dev br0 vid 1 self
   bridge vlan add dev br0 vid 1 pvid untagged self
   # Ensure that multicast flooding is off
   bridge link set dev eth0 mcast_flood off
   bridge link set dev eth1 mcast_flood off

2. On the PC, create the same ptp.cfg file mentioned earlier and run:

.. code:: console

   sudo ptp4l -E -2 -S -i enp2s0 -l 6 -m -q -f ptp.cfg

enp2s0 is assumed to be the ethernet interface.
Replace -S with -H if PC supports Hardware Timestamping.

3. On AM625-SK, run:

.. code:: console

   ptp4l -E -2 -H -i eth0 -i eth1 -s -f tc-ptp.cfg --step_threshold=1 -m -q

4. On J7VCL, run:

.. code:: console

   ptp4l -E -2 -H -i eth1 -s -l 6 -m -q -f ptp.cfg

**Observed Outputs:**

On PC:

.. code:: console

   user@pc:~/TSN-PTP4L$ sudo ptp4l -E -2 -S -i enp2s0 -l 6 -m -q -f ptp.cfg
   ptp4l[18640.121]: port 1: INITIALIZING to LISTENING on INITIALIZE
   ptp4l[18640.121]: port 0: INITIALIZING to LISTENING on INITIALIZE
   ptp4l[18640.122]: port 1: link up
   ptp4l[18647.795]: port 1: LISTENING to MASTER on ANNOUNCE_RECEIPT_TIMEOUT_EXPIRES
   ptp4l[18647.795]: selected best master clock b0227a.fffe.d8b7e3
   ptp4l[18647.796]: assuming the grand master role

On AM625-SK:

.. code:: console

   root@am62xx-evm:~# ptp4l -E -2 -H -i eth0 -i eth1 -s -f ptp.cfg --step_threshold=1 -m -q
   ptp4l[508.734]: selected /dev/ptp0 as PTP clock
   ptp4l[508.768]: port 1 (eth0): INITIALIZING to LISTENING on INIT_COMPLETE
   ptp4l[508.808]: port 2 (eth1): INITIALIZING to LISTENING on INIT_COMPLETE
   ptp4l[508.808]: port 0 (/var/run/ptp4l): INITIALIZING to LISTENING on INIT_COMPLETE
   ptp4l[510.134]: port 1: new foreign master b0227a.fffe.d8b7e3-1
   ptp4l[514.135]: selected best master clock b0227a.fffe.d8b7e3 on port 1
   ptp4l[514.135]: selected best master clock b0227a.fffe.d8b7e3
   ptp4l[514.135]: foreign master not using PTP timescale
   ptp4l[514.135]: port 1 (eth0): LISTENING to UNCALIBRATED on RS_SLAVE
   ptp4l[515.135]: master offset -1660108720858304691 s0 freq      +0 path delay    145597
   ptp4l[515.404]: selected best master clock b0227a.fffe.d8b7e3 on port 1
   ptp4l[515.404]: selected best master clock b0227a.fffe.d8b7e3
   ptp4l[515.404]: foreign master not using PTP timescale
   ptp4l[516.135]: master offset -1660108720858311656 s1 freq   -6965 path delay    145597
   ptp4l[517.135]: master offset      -2379 s2 freq   -9344 path delay    145597
   ptp4l[517.135]: port 1 (eth0): UNCALIBRATED to SLAVE on MASTER_CLOCK_SELECTED
   ptp4l[518.136]: master offset     -12603 s2 freq  -20282 path delay    145597
   ptp4l[519.136]: master offset      49256 s2 freq  +37796 path delay    110374
   ptp4l[520.136]: master offset     -59315 s2 freq  -55998 path delay    173739
   ptp4l[521.136]: master offset      -9282 s2 freq  -23759 path delay    173739
   ptp4l[522.136]: master offset     -34935 s2 freq  -52197 path delay    215742
   ptp4l[523.136]: master offset      59415 s2 freq  +31673 path delay    167165
   ptp4l[523.222]: selected best master clock b0227a.fffe.d8b7e3 on port 1
   ptp4l[523.222]: selected best master clock b0227a.fffe.d8b7e3
   ptp4l[523.222]: foreign master not using PTP timescale
   ptp4l[524.136]: master offset      69431 s2 freq  +59513 path delay    118589
   ptp4l[525.136]: master offset     -34194 s2 freq  -23283 path delay    156913
   ptp4l[526.136]: master offset     -56535 s2 freq  -55882 path delay    195237
   ptp4l[527.137]: master offset      24678 s2 freq   +8371 path delay    163169
   ptp4l[528.137]: master offset       9448 s2 freq    +544 path delay    163169
   ptp4l[529.137]: master offset      25778 s2 freq  +19708 path delay    139827
   ptp4l[529.242]: selected best master clock b0227a.fffe.d8b7e3 on port 1
   ptp4l[529.242]: selected best master clock b0227a.fffe.d8b7e3
   ptp4l[529.242]: foreign master not using PTP timescale
   ptp4l[530.137]: master offset       3067 s2 freq   +4731 path delay    135917
   ptp4l[531.137]: master offset      -8098 s2 freq   -5514 path delay    135917
   ptp4l[532.137]: master offset     -18361 s2 freq  -18206 path delay    144642
   ptp4l[533.138]: master offset      -6540 s2 freq  -11894 path delay    144642
   ptp4l[534.137]: master offset      -1649 s2 freq   -8965 path delay    144642
   ptp4l[535.138]: master offset     -13636 s2 freq  -21446 path delay    159134
   ptp4l[536.138]: master offset        789 s2 freq  -11112 path delay    159134
   ptp4l[536.208]: selected best master clock b0227a.fffe.d8b7e3 on port 1
   ptp4l[536.208]: selected best master clock b0227a.fffe.d8b7e3
   ptp4l[536.208]: foreign master not using PTP timescale

On J7VCL:

.. code:: console

   root@j7200-evm:~/PTP# ptp4l -E -2 -H -i eth1 -s -l 6 -m -q -f ptp.cfg
   ptp4l[425.608]: selected /dev/ptp2 as PTP clock
   ptp4l[425.677]: port 1 (eth1): INITIALIZING to LISTENING on INIT_COMPLETE
   ptp4l[425.677]: port 0 (/var/run/ptp4l): INITIALIZING to LISTENING on INIT_COMPLETE
   ptp4l[425.705]: port 1: new foreign master b0227a.fffe.d8b7e3-1
   ptp4l[429.705]: selected best master clock b0227a.fffe.d8b7e3 on port 1
   ptp4l[429.705]: selected best master clock b0227a.fffe.d8b7e3
   ptp4l[429.705]: foreign master not using PTP timescale
   ptp4l[429.705]: port 1 (eth1): LISTENING to UNCALIBRATED on RS_SLAVE
   ptp4l[431.706]: master offset -1660108807288380986 s0 freq      +0 path delay    168950
   ptp4l[432.706]: master offset -1660108807288385730 s1 freq   -4743 path delay    168950
   ptp4l[433.706]: master offset     -18439 s2 freq  -23182 path delay    168950
   ptp4l[433.706]: port 1 (eth1): UNCALIBRATED to SLAVE on MASTER_CLOCK_SELECTED
   ptp4l[434.706]: master offset     -12324 s2 freq  -22598 path delay    168950
   ptp4l[435.706]: master offset     -36594 s2 freq  -50565 path delay    197305
   ptp4l[436.706]: master offset     -17848 s2 freq  -42798 path delay    211592
   ptp4l[437.706]: master offset       6950 s2 freq  -23354 path delay    211592
   ptp4l[438.706]: master offset      34748 s2 freq   +6529 path delay    190271
   ptp4l[439.706]: master offset       9819 s2 freq   -7976 path delay    190271
   ptp4l[440.707]: master offset     -12612 s2 freq  -27461 path delay    202810
   ptp4l[441.706]: master offset      -6574 s2 freq  -25207 path delay    206237
   ptp4l[442.707]: master offset       4474 s2 freq  -16131 path delay    202810
   ptp4l[443.707]: master offset      18718 s2 freq    -545 path delay    186632
   ptp4l[444.707]: master offset      -7992 s2 freq  -21639 path delay    196330
   ptp4l[445.707]: master offset      -4577 s2 freq  -20622 path delay    196330
   ptp4l[446.707]: master offset      -1473 s2 freq  -18891 path delay    196330
   ptp4l[447.707]: master offset      15459 s2 freq   -2401 path delay    180152
   ptp4l[448.707]: master offset        256 s2 freq  -12966 path delay    180152
   ptp4l[449.707]: master offset      -4951 s2 freq  -18096 path delay    180152
