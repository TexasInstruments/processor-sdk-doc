.. http://processors.wiki.ti.com/index.php/ICSS_EMAC_LLD_debug_guide

Introduction
^^^^^^^^^^^^^^

This is a companion guide to `ICSS EMAC Developer
Guide <index_device_drv.html#development-with-icss-emac-driver>`__,
if you have not read the developer guide it's highly suggested that you
do so.

Based upon the combined experience of development team, this document
covers the most obvious use cases and debug scenarios present in ICSS
EMAC LLD. Frequently asked questions from `E2E <https://e2e.ti.com/>`__
forums which are relevant have also been added here.

For individual protocols like Ethernet/IP, Profinet, EtherCat etc
separate debugging guides are available which discuss specific use
cases.

As mentioned previously in developer guide, a discussion of EMAC LLD
covers most of the ethernet driver/firmware issues and goes a long way
in the understanding of other industrial protocol implementations. This
applies to debug guide as well.

Assumption
"""""""""""

Assumptions are same as those in developer guide. A basic understanding
of ICSS Architecture and SoC is assumed, some level of familiarity with
Ethernet driver development is also assumed. In addition to this a basic
familiarity with the following tools is also assumed.

-  Code Composer Studio
-  Any serial terminal (Putty/Tera Term)
-  Wireshark or any other packet sniffing tool
-  Any PC based tool capable of sending packets

Scope of the document
""""""""""""""""""""""

This document is meant to help the developer

-  Familiarize with common debugging tools and techniques
-  Identify and resolve frequently faced issues

Common Debugging Tasks
^^^^^^^^^^^^^^^^^^^^^^^^

Loading and running on CCS
""""""""""""""""""""""""""""

1. Connect JTAG Emulator to EVM in-case of IDK or Connect USB cable to
board in-case of ICE

2. Select View->Target Configurations. Right click on the required
configuration in the list and Select Launch Selected Configuration

3. Right Click on the Cortex A9/A8 listed in Debug view and select
Connect. (Click View->Debug to view debug window, if not visible)

4. Select System Reset

5. Select Suspend

6. Load the GEL file and execute initialization script.

7. Once the initialization is completed, Select Run->Load ->Load
Program. Here browse to the required executable and click OK

8. After a successful load, the program is expected to be in suspended
state and program counter is pointing to main function. If the program
is not in suspended state :

i. Suspend the application by selecting Run->Suspend

ii. Restart the application by selecting Run->Restart

9. Run the application by selecting Menu->Run->Resume. This will execute
the application.

.. Image:: /images/De1.png

NOTE

• While launching a debug session for the first time, CCS will ask for
the CPU to which the program needs to be loaded. Please select
Cortex-A9/A8 and continue.

• If TeraTerm does not display an output upon program execution.
TeraTerm can be initialized just prior to program execution by
performing steps 1-8 and then

Disconnect the terminal session using File -> Disconnect

Reconnect the terminal session with File -> New Connection

• If there is a valid application in SPI or NOR flash(in their
corresponding boot mode), on "System Reset" the application loads right
away. This might cause issues on the application you load via JTAG. To
avoid this, put a hardware breakpoint at 0x402f_0400(in case of MMSCD
boot mode) or 0x30000000(in case of qSPI boot mode) and then do a
"System Reset". You can then continue with Step 4 after this step.

Connecting the PRU's
"""""""""""""""""""""

Check Link Status
""""""""""""""""""

Link Status is available as an array **linkStatus** in
**ICSSEMAC_Object**. The status is updated in the Link ISR
**ICSS_EmacLinkISR**. It's possible that the link interrupt is
configured incorrectly or MDIO is not triggering the interrupts. (see
`here <index_device_drv.html#link-interrupt>`__
on how to configure Link Interrupt) In which case one needs to put a
breakpoint in the ISR **ICSS_EmacLinkISR** and disconnect or connect the
cable on any one port. The breakpoint should get hit, if it does not
then there is some issue with the interrupt configuration.

PHY status is read and status updated as shown below

::

    /*Read Link status for Port 0*/
    linkStatus = ENETPhyDevLinkStatus(DEVICE_ID_ENET_PHY_MII, 0, 3);
    ((ICSSEMAC_Object*)icssEmacHandle->object)->linkStatus[0]=(uint8_t)linkStatus;

Even if the ISR is hit it's also possible; in case different PHY's
(compared to those on EVM) are used that the PHY status registers are
read incorrectly, if that's the issue then please consult the porting
guide and reference manual for your PHY to figure out where the issue
could be.

Checking if Receive is working
"""""""""""""""""""""""""""""""

The receive path has been explained previously in the developer guide.
See `here <index_device_drv.html#rx-data-path>`__.
Rx issues can manifest themselves in several ways, the following table
covers most of them (not exhaustively!)

.. table::  **Receive issues and causes**

   +-----------------------------------+-----------------------------------+
   | Issue                             | Probable Cause                    |
   +===================================+===================================+
   | Host not receiving                | Rx interrupt not configured       |
   | Multicast/Broadcast frames        | correctly,                        |
   |                                   | Firmware not receiving, Storm     |
   |                                   | Prevention enabled Rx is disabled |
   +-----------------------------------+-----------------------------------+
   | Unicast Packets (for Host)being   | Same as above except Storm        |
   | dropped                           | Prevention                        |
   |                                   | Interface MAC not configured      |
   |                                   | correctly                         |
   +-----------------------------------+-----------------------------------+
   | Multicast/Broadcast frames not    | Storm Prevention enabled          |
   | being forwarded                   | Firmware not receiving, Rx is     |
   |                                   | disabled                          |
   +-----------------------------------+-----------------------------------+
   | Unicast frames (not for Host) not | Firmware not receiving            |
   | being forwarded                   | Rx is disabled                    |
   +-----------------------------------+-----------------------------------+
   | Driver receiving packets but Raw  | NDK issues (there is a known      |
   | socket not receiving frames       | issue, please see below)          |
   +-----------------------------------+-----------------------------------+
   | Packets are getting dropped       | Storm Prevention enabled          |
   |                                   | Data is coming in too fast. See   |
   |                                   | Interrupt pacing                  |
   |                                   | `section <http://processors.wiki. |
   |                                   | ti.com/index.php/ICSS_EMAC_LLD_de |
   |                                   | velopers_guide#Interrupt_Pacing>` |
   |                                   | __                                |
   |                                   | to understand this behavior       |
   +-----------------------------------+-----------------------------------+

The first step is to identify the exact problem, to do that please
perform these steps in order.

#. **Check if Rx is disabled** : It's possible to disable Rx in firmware
   through IOCTL. This is controlled through a location in ICSS memory.
   See `memory map <index_device_drv.html#memory-map>`__.
   Check this as a very first step. It's not a common error but it's
   possible that user is invoking the IOCTL by mistake.
#. **Check if firmware is receiving packets** : See statistics `this <index_device_drv.html#statistics>`__
   and `this <index_device_drv.html#check-statistics>`__
   and find out if PRU is receiving the frames. Failure to receive
   frames in firmware can indicate other issues like corrupted frames,
   link negotiation failure or PHY related issues.
#. **Check if Rx interrupt is being asserted** : This can be one of the
   reasons why Host would not receive packets. Put a break point in
   **ICSS_EmacRxInterruptHandler** and send a single packet using any PC
   based tool. The ISR should get hit. Refer to this
   `section <index_device_drv.html#rx-interrupt>`__
   on how to configure the interrupt properly if interrupt is not being
   asserted.
#. **Check if Packets are being copied in driver** : If the interrupt is
   asserted but packets do not reach the application, check Host
   statistics to verify if packets are being received correctly in the
   driver. Refer to the
   `section <index_device_drv.html#rx-data-path>`__\ on
   Rx data path and put a breakpoint in **RxTask**. Step through to
   verify that the priority is set correctly and packets are being
   copied properly. If interrupt is being asserted correctly but packet
   length is zero it indicates some data corruption in the receive
   queues or firmware behaving incorrectly, this scenario should not
   occur.
#. **Check if NDK is receiving the frames** : If driver is receiving the
   frames and user cannot see frames in socket then it indicates issues
   with TCP/IP stack. Refer to `NDK User's
   guide <http://www.ti.com/lit/ug/spru523i/spru523i.pdf>`__ on correct
   usage of sockets. The example socket application provided in the
   developer guide `here <index_device_drv.html#usage>`__
   is known to work though. In addition to this check if NDK buffers
   have been allocated correctly. If you are using your own TCP/IP stack
   refer to the Porting Guide and double check.
#. **Check if Storm prevention is enabled** : This is one of the most
   common reasons why throughput may get lowered or if the threshold is
   set incorrectly packets may not reach Host at all. Check if storm
   prevention module is enabled by checking the variable
   **suppressionEnabled** for both ports. Refer to
   `this <index_device_drv.html#id59>`__
   for more details. Additionally one should check the statistics to see
   if the PRU statistics **stormPrevCounter** is getting incremented.
#. **Check Interface MAC** : The firmware compares the interface MAC
   written to the PRU memory by the Host against the incoming packets
   destination MAC to verify if the packet must be forwarded to Host or
   cut-through. Please refer to the `memory
   map <index_device_drv.html#memory-map>`__
   and check if the MAC value is what you are expecting it to be.
#. **Queue Overflow** : If too many packets are received on a single
   queue without Host emptying them out then overflow may occur, packets
   will be lost in such a scenario. This is somewhat related to
   throughput issues but may occur independently as well.
#. **Check throughput** : This is applicable in case everything else
   appears to be correct but the number of packets reaching the Host is
   not 100% of the transmitted value. This can happen because of two
   reasons. 1. Data rate is too fast and interrupt pacing is disabled.
   2. Processing on Host is too slow and driver cannot cope with the
   rate at which firmware is putting data in the queue. In such a
   scenario first turn on Interrupt pacing to find if it solves the
   issue (interrupt pacing has it's own limitations, refer to
   `this <index_device_drv.html#interrupt-pacing>`__
   to know more about it), if issue is still not resolved then try to
   find the throughput by comparing the number of packets received on
   the Host vs that in the firmware.

**More on Throughput** : If throughput is low then try to find out how
the Rx processing on Host can be sped up or if any other high priority
task is blocking the execution of **RxTask**. The EMAC and switch are
tested during release to cope with 100% throughput at line rate (960 IPG
and 64 byte size packet) so any drop in throughput can only be caused by
additional loading on the CPU. Use UIA which comes SYSBIOS for this
purpose. Usage given
`here <index_device_drv.html#checking-the-system-performance-using-uia>`__

Checking if Transmit is working
""""""""""""""""""""""""""""""""

Because of it's nature Tx is much more reliable and there are far fewer
issues related to it when compared to Rx. Transmit issues can be
classified into two types. See `Tx data
path <index_device_drv.html#tx-data-path>`__ for
more information.

#. **Cut-through issues** : Packets received on one port and meant to go
   out of the opposite port. (Not applicable to EMAC)
#. **Transmit from Host** : Packets sent out from the Host on any one
   port.

As a first step please check the statistics on firmware as well as Host
to see if any packets have been sent out. Try to trace where the issue
is by comparing transmit statistics for Host and firmware.

The probable causes for transmit not working are listed below. This can
also be used as a checklist for debugging.

#. **Link down** : The link event is mapped to an ISR
   **ICSS_EmacLinkISR** which in turn calls another API
   **ICSS_EmacUpdatePhyStatus** to update the link status in firmware.
   If this is not done correctly then it's possible that firmware will
   read the event as link down even though physically the link is up.
   Please check the link status to make sure that this is not the case.
   The Tx API checks for link and will not transmit if the link is down
   so this issue is more relevant to cut-through/store-forward. More on
   Link status `here <index_device_drv.html#check-link-status>`__.
#. **Incorrect speed** : The link ISR also checks for speed and
   duplexity values. The values are written to in the same ISR
   **ICSS_EmacUpdatePhyStatus**, if the speed is read incorrectly then
   it's possible that firmware will not send out packets or may send out
   garbage. In such a scenario firmware statistics will count the
   packets as successful transmit but Tx might not actually happen. The
   quickest way to debug this issue is to read the ICSS memory directly
   in CCS memory window. Interface speed is written directly in memory
   at the offset mentioned in `memory map <index_device_drv.html#memory-map>`__, please
   verify the value (as mentioned in memory map) and compare with the
   actual interface speed.
#. **Incorrect pinmux for Collision/Carrier Sense** : This is applicable
   in case of developers using their custom boards, it's important that
   the collision and carrier sense signals be wired correctly (see ICEv2
   `layout <http://www.ti.com/tool/tmdsice3359#Technical%20Documents>`__)
   because the transmit code relies on these two signals to implement
   half duplex functionality and wrong values may result in transmit
   problems. If there is an issue with pinmuxing these two pins it's
   recommended that half duplex functionality be disabled. Half Duplex
   functionality is controlled by the variable **halfDuplexEnable**
#. **Queue contention issues** : Looking at the QoS
   `scheme <index_device_drv.html#quality-of-service-and-queues>`__
   it's possible that there is a contention for the transmit queue when
   both Host and the opposite port are trying to transmit on the same
   port. In such cases if there are too many packets vying for the
   contention queue they will be dropped. Such conditions are rare.
#. **Queue overflow** : As the name suggests if too many packets are
   sent out on a single queue then overflow can happen and packets may
   get lost.
#. **NDK transmit** : Issues with NDK buffers may cause issues with Tx,
   in such cases put a breakpoint in **ICSS_EmacTxPacket** to see if NDK
   is calling it.

Check Statistics
"""""""""""""""""

Statistics form the core of debugging so this section is very important.
A brief introduction to statistics has been provided previously in the
statistics
`section <index_device_drv.html#statistics>`__ of
developer guide. This part explains how to use it for the purpose of
debugging.

As previously explained, statistics can be divided into two groups

-  On Firmware
-  Host based

Host statistics are a subset of Firmware based statistics except some
specialized statistics like **rxUnknownProtocol** and **linkBreak**.
This property can be used to find out how many packets are being
received in the firmware and how many are reaching Host.

Getting the values
''''''''''''''''''''

Statistics are accessible in three ways

-  **IOCTL calls** : IOCTL calls (including an example) have been
   previously explained
   `here <index_device_drv.html#ioctl>`__ in
   developer guide.
-  **Reading directly in memory window** : (This applies only to PRU
   based statistics). Use the statistics `memory
   map <index_device_drv.html#id63>`__ to find
   out the offset and look at the memory directly. Information on how to
   access the ICSS memory is provided
   `here <index_device_drv.html#accessing-memory>`__.
-  **In CCS watch window** : When using CCS the statistics can be read
   directly through the ICSS EMAC handle. Host statistics are available
   through **hostStat** while PRU statistics are available through
   **pruStat**. An example code snippet from **TxPacketEnqueue** API
   shows host statistics being accessed.

::

    hostStatistics_t* hostStatPtr;
    hostStatPtr = (hostStatistics_t*)((((ICSSEMAC_Object*)icssEmacHandle->object)->hostStat));
    /*Access port specific statistics by incrementing the pointer*/
    hostStatPtr += (portNumber - 1);
    ICSS_EmacUpdateTxStats(macAddr,(unsigned int)lengthOfPacket, hostStatPtr);

**NOTE :** Since they are void members they need to be typecast to
access the members in CCS watch window.

Example Usage
'''''''''''''''

Described below are some scenarios which involve multiple statistics,
this will help the developer understand how to use statistics.

**Example 1:** For example assume that 100k multicast packets of size 64
bytes each are sent to Port 1 of switch (EtherNet/IP adapter example)
and storm prevention is enabled such that 10k out of those 100k packets
are dropped, out of those 990k, 10k packets have CRC error so the total
number of packets reaching Host is only 980k but 990k packets get
cut-through (multicast packets are cut-through except some protocol
specific packets) because CRC is not verified for cut-through frames.
For this example the statistics will look like this (only relevant
fields have been populated)

+--------------------+------------+--------------+--------------+
| Member             | Host Stats | Port 0 Stats | Port 1 Stats |
+====================+============+==============+==============+
| *rxMcast*          | 980,000    | Example      | Example      |
+--------------------+------------+--------------+--------------+
| *txMcast*          | 0          | Example      | Example      |
+--------------------+------------+--------------+--------------+
| *rxCRCFrames*      | NA         | 10,000       | 0            |
+--------------------+------------+--------------+--------------+
| *stormPrevCounter* | NA         | 10,000       | 0            |
+--------------------+------------+--------------+--------------+

Accessing Memory
^^^^^^^^^^^^^^^^^^

ICSS Shared RAM
"""""""""""""""""

This section explains how to access ICSS memory. The icss_emacSwitch.h
file contains the offset information.

The DRAM base addresses for Port 1 and Port 2 can be obtained by adding
emacHandle1 to Expressions tab in CCS and typecasting it to
ICSSEMAC_HwAttrs.

For AM335x, the addresses are:

.. Image:: /images/Dramaddr.png

|
| **Example:** For example, if storm prevention counter location needs
  to be accessed for Port 1 of ICEv2 EVM, the following steps give the
  value of the location to be entered in the Memory Browser of CCS:

::

    #define STORM_PREVENTION_OFFSET      STATISTICS_OFFSET + STAT_SIZE

where, STATISTICS_OFFSET is 0x1f00 and STAT_SIZE is
RX_1024_MAX_BYTE_FRAME_OFFSET + 4, RX_1024_MAX_BYTE_FRAME_OFFSET is
defined as 0x88. This gives 0x1f00 + 0x88 + 4 = 0x1f8c

Hence enter 0x4a301f8c in the Memory Browser and check the content. If
the value is 01, storm prevention functionality is enabled and if it is
00, it is disabled.

.. Image:: /images/Stormprev.png

|
| Similarly, the value would be 0x4a302000 + 0x1f8c (DRAM base address
  for Port 2 + Storm Prevention Offset) = 0x4a303f8c for Port 2 of
  ICEv2.

For AM437x, the DRAM base addresses are as follows:

.. Image:: /images/Dramaddram4.png

|

System Debug
^^^^^^^^^^^^^^

SYS/BIOS
"""""""""

Using ROV to Debug RTOS
'''''''''''''''''''''''''

To view ROV tab, goto Tools -> RTOS Object View (ROV) and halt the debug
session.

.. Image:: /images/Rov.png

|

Checking the system performance using UIA
'''''''''''''''''''''''''''''''''''''''''''

The UIA (Unified Instrumentation Architecture) is a target-side package
that provides instrumentation services which can be downloaded from
`[1] <http://software-dl.ti.com/dsps/dsps_public_sw/sdo_sb/targetcontent/uia/index.html>`__.
System Analyzer is a suite of host-side tools that use data captured
from software instrumentation, hardware instrumentation, and CPU trace
to provide visibility into the real-time performance of the target
application, which includes the menu commands in Tools > RTOS Analyzer
menu of CCS.

The following code needs to be added to the configuration file to enable
performance tests on AM335x/AM437x using UIA 2.x version:

::

    var LoggingSetup = xdc.useModule('ti.uia.sysbios.LoggingSetup');
    var SysStd = xdc.useModule('xdc.runtime.SysStd');

::

    System.SupportProxy = SysStd;

::

    /* Enable CPU Load logging */
    LoggingSetup.loadLogging = true;

::

    /*
     *  Enable Task, Swi, and Hwi Load logging. This allows the Idle Task
     *  usage to make more sense. Otherwise Hwi and Swi load is factored into
     *  each task's usage.
     */
    LoggingSetup.loadTaskLogging = true;
    LoggingSetup.loadSwiLogging = true;
    LoggingSetup.loadHwiLogging = true;

::

    LoggingSetup.sysbiosHwiLogging = true;
    LoggingSetup.sysbiosSwiLogging = true;
    LoggingSetup.sysbiosLoggerSize = 65536;
    Main.common$.diags_ENTRY = Diags.ALWAYS_ON;
    Main.common$.diags_EXIT = Diags.ALWAYS_ON;
    LoggingSetup.disableMulticoreEventCorrelation = true;

For new log records, the ARM should be paused. The CPU load graph gives
the loading percentage which can be used to determine the additional
task needed to load CPU to a specific level to perform NDK tests at
different loads.

|

Using SYS/BIOS Timer to measure performance
'''''''''''''''''''''''''''''''''''''''''''''

NDK
""""""

Performing NDK tests
''''''''''''''''''''''

The steps to be followed in order to enable NDK Performance Tests are:

1. Add this code snippet to the respective configuration files
(am335x_app.cfg or am437x_app.cfg)

::

    Global.networkOpenHook = "&netOpenHook";
    Global.networkCloseHook = "&netCloseHook";

2. Ensure that nethooks.c file is present in the application folder. (If
not, copy it from \\ti_internal\examples\ethernet_switch\Tcp)

3. Build and load the application.

4. In windows command prompt, navigate to the location where send.exe
resides in the test PC (e.g.,
C:\ti\ndk_2_24_02_31\packages\ti\ndk\winapps).

5. Enter this command: send.exe %DUT_IP_ADDRESS% 100

where,

DUT_IP_ADDRESS=192.168.2.3 for Port 1 and 192.168.1.3 for Port 2 in case
of EMAC application

100 is the console print interval, i.e., a console print appears for
every 100 packets transmitted

6. Similarly, recv.exe, echoc.exe and testudp.exe applications are run
to test performance.

|

Measuring network performance
'''''''''''''''''''''''''''''''

The network performance can be measured from the console output upon
running the above tests. Consider the log when send.exe application is
run for a few minutes till it stabilizes as below:

.. Image:: /images/Ndksend.png

Here, 8192 bytes are being sent at 12800000 bytes/s. As NDK performance
is measured at MBPS (Megabits per second), conversion is:

1 byte = 7.6294e-6 megabits

which gives (12800000*8/1024)/1024 = 97.65 MBPS

**Note:** The above procedure is applicable for send.exe, recv.exe and
echoc.exe tests. The testudp.exe application tests UDP packet payloads
from 1 to 1472 bytes and test loop should pass.

|

Checking NDK Buffers
'''''''''''''''''''''

Frequently Encountered Issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Build Issues
"""""""""""""

Tools compatibility
'''''''''''''''''''''

One of the frequent issues faced during build are issues of tools
compatibility. The SDK build is dependent on NDK, SysBIOS and XDC Tools.
While we try to maintain backward compatibility it's not always possible
to do so, hence it's recommended that the correct versions of the tools
are downloaded and used. The compatible versions are listed in the user
guide
(`sample <http://processors.wiki.ti.com/index.php/SYSBIOS_Industrial_SDK_02.01.00.01_User_Guide>`__)
of every SDK release.

System Variables
''''''''''''''''''

The variable *IA_SDK_HOME* must point to *(place where SDK is
installed)/public/sdk*, most often than not this is the main reason for
build issues, especially when multiple SDK's are installed. This
variable is used everywhere during the build process to select include
files, libraries, tools etc.

Migration from 1.1 to 2.1 Industrial SDK
'''''''''''''''''''''''''''''''''''''''''

There is a possibility of build issue while migrating from 1.1 to 2.1
Industrial SDK. The “Debug” folder needs to be removed from the project
as separate build configurations are available for AM335x and AM437x
EVMs in 2.1 SDK.

