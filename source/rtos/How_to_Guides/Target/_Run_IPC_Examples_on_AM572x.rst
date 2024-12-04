.. http://processors.wiki.ti.com/index.php/Running_IPC_Examples_on_DRA7xx/AM572x

DRA7xx/AM572xx IPC Examples
---------------------------

.. rubric:: IPC Hello Example:
   :name: ipc-hello-example

**ex01_hello**

|

The following examples demonstrate some of the rudimentary IPC
capabilities. They are mostly two processors examples. These examples
may be built for any two processors on your device, but only for two
at a time. An IPC Ping example using three processors is also
presented at the end.

Hello example uses the reader/writer design pattern. One processor will
be the reader and the other will be the writer. The reader creates a
message queue and waits on it for messages. The writer opens the
reader's message queue and sends messages to it. The writer allocates
the message from a shared message pool and the reader returns the
message to the pool. Thus, messages are sent in only one direction.
Default settings of the Hello world example configures DSP1 as the
writer and DSP2 as the reader.

.. note::
   if Windows 7 machine is used for building these examples,
   **GnuWin32** make utility needs to be installed to run make which can be
   downloaded from this link
   `http://gnuwin32.sourceforge.net/packages/make.htm <http://gnuwin32.sourceforge.net/packages/make.htm>`__


Set **GnuWin32\\bin** folder on file path and add a system variable
**XDCTOOLS_JAVA_HOME** to point to "**c:\\ti\\ccsv6\\eclipse\\jre**"

::

    set PATH=<YOUR_PROCEEDING_PATH>\GnuWin32\bin;%PATH%
    set XDCTOOLS_JAVA_HOME=c:\ti\ccsv6\eclipse\jre

1. Change to the example folder by entering: cd
~/ti/ipc_nn_nn_nn_nn/examples/DRA7xx_bios_elf/\ **ex01_hello**

2. Open readme.txt file and follow build instructions step-by-step. If
build this example on Ubuntu PC, make sure there is no spaces between
variable name and its value.

|

::

      DEPOT (your depository folder ex: DEPOT=/Your_Ubuntu_home_folder/ti)

::

      BIOS_INSTALL_DIR=$(DEPOT)/bios_n_nn_nn_nn

::

      IPC_INSTALL_DIR=$(DEPOT)/ipc_n_nn_nn_nn

::

      XDC_INSTALL_DIR=$(DEPOT)/xdctools_n_nn_nn_nn

::

      gnu.targets.arm.A15F=$(DEPOT)/ccsv6/tools/compiler/gcc-arm-none-eabi-4_8-2014q3

::

      ti.targets.elf.C66=$(DEPOT)/ccsv6/tools/compiler/c6000_7.4.14

::

      ti.targets.arm.elf.M4=$(DEPOT)/ccsv6/tools/compiler/arm_5.2.4

::

      ti.targets.arp32.elf.ARP32_far=$(DEPOT)/ccsv6/tools/compiler/arm_5.2.4

::

      See the following example, and ensure you are using the latest version
      of folder names present in ~/ti folder:

      DEPOT=/home/Your_Ubuntu_home_folder/ti

      # Use the following environment assignment  (Note you must use 32 bit Java even in Ubuntu 14.04 64 bit OS environment)
      export XDCTOOLS_JAVA_HOME=/home/Your_Ubuntu_home_folder/ti/ccsv6/eclipse/jre

      #### BIOS-side dependencies ####
      BIOS_INSTALL_DIR=$(DEPOT)/bios_6_41_04_54
      IPC_INSTALL_DIR=$(DEPOT)/ipc_3_36_01_11
      XDC_INSTALL_DIR=$(DEPOT)/xdctools_3_31_02_38

      #### BIOS-side toolchains ####
      gnu.targets.arm.A15F=$(DEPOT)/ccsv6/tools/compiler/gcc-arm-none-eabi-4_8-2014q3
      ti.targets.elf.C66=$(DEPOT)/ti-cgt-c6000_8.0.3
      ti.targets.arm.elf.M4=$(DEPOT)/ccsv6/tools/compiler/ti-cgt-arm_5.2.4
      ti.targets.arp32.elf.ARP32_far=$(DEPOT)/ccsv6/tools/compiler/ti-cgt-arm_5.2.4

3. Run make command in current folder to build DSP1 and DSP2 hello examples. Output files are created under debug sub folders.

 - ex01_hello\\dsp1\\bin\\debug
 - ex01_hello\\dsp2\\bin\\debug

4. Launch target configurations.

5. Right click CortexA15_0 and connect target.

6. On CCS --> Scripts --> AM572 Multicore Initialization --> Run AM572x Multicore EnableAllCore

7. Initialize DDR configuration. On CCS --> Scripts --> DDR configurations --> AM572_DDR3_532MHz_config

8. Load DSP1 Hello Example hello_dsp1.xe66 (writer)file on DSP1.

9. Load DSP2 Hello Example hello_dsp2.xe66 (reader) file on DSP2.

10. Run both DSP1 and DSP2.

11. On CCS --> Tools --> RTOS Object view (ROV).

12. Suspend (halt) DSP1 to view test messages on ROV Viewable Modules -->LoggerBuf Refer below image of ROV log messages.

.. Image:: /images/Hello_dsp2.png

13. Suspend (halt) DSP2 and click on ROV icon to view log messages.

|

.. rubric:: IPC Message Queue Example:
   :name: ipc-message-queue-example

**ex02_messageq**

Message queue example sends round-trip message from client to server and
back. MessageQ example uses client/server pattern. It is a two
processors example: the HOST and DSP processors. Either DSP1 or DSP2 can
be built for testing.

The DSP processor is configured as server. It creates a named message
queue. The server does not open any queues because it extracts the
return address from the message header. The server returns all messages
to the sender. It does not access the message pool.

The HOST processor is configured as client application. The client
creates an anonymous message queue. The client also creates and manages
the message pool. The client's return address is set in the message
header for each message before sending it to the server.

1. Change to messageQ folder example by enter:
    cd  ~/ti/ipc_nn_nn_nn_nn/examples/DRA7xx_bios_elf/\ **ex02_messageQ**

2. Open readme.txt file and follow build instructions step-by-step. Make
sure there is no spaces between variable name and its value. See Hello
World example environment varaible settings for reference.

3. Run make command in current folder to build DSP1 and HOST hello examples. Output files are created under debug sub folders

 - ex02_messageq\\host\\bin\\debug : HOST A15 binary
 - ex02_messageq\\dsp1\\bin\\debug : C66x binary

4. Launch target configurations. Note that BH560USB_M is emulator is used to connect to AM572X EVM.

5. Right click CortexA15_0 and connect target.

6. On CCS --> Scripts --> AM572 Multicore Initialization --> Run AM572x Multicore EnableAllCore

7. Initialize DDR configuration. On CCS --> Scripts --> DDR configurations --> AM572_DDR3_532MHz_config

8. **Load DSP1** messageQ Example out file(server_dsp1.xe66) onto DSP1.

9. **Load HOST** messageQ Example out file(app_host.xa15fg) onto ARM CortexA15_0.

10. Run both DSP1 and HOST.

11. On CCS --> Tools --> RTOS Object view (ROV).

12. Suspend (halt) ARM Cortex_A15 to view test messages on ROV Viewable Modules -->LoggerBuf Refer the following ROV message queue screenshot

.. Image:: /images/MesgQ_arm0.png

13. Suspend (halt) DSP1 and click on ROV icon to view log messages.

|

.. rubric:: IPC Notify Peer Example:
   :name: ipc-notify-peer-example

**ex13_notifypeer**

Notify peer example only uses notify to communicate to a peer processor.
This is an example of IPC Scalability. It uses the client/server design
pattern. Initially, the example builds only for two processors: HOST and
DSP1. The client runs on HOST and the server runs on DSP1.

The client (HOST) creates an anonymous message queue. The client also
creates and manages its own message pool. And it opens the server
message queue using its name. The client initiates the data flow by
allocating a message from the pool, placing its return address in the
message header and sending the message to the server. It then waits for
the message to be returned. When it receives the return message, the
message is returned to the pool. The client repeats this in a loop.

The server (DSP1) creates a named message queue, then waits on it for
messages. When a message arrives, the server performs the requested
work. When the work is done, the server extracts the return address from
the message header and sends the message back to the client. The server
never opens any message queues and does not access the message pool.

Since DSP1 will need to wait on both the message queue and the notify
queue, we introduce events. The SYS/BIOS event object can be used to
wait on multiple input sources.


1. Change to notify_peer folder example by enter: cd ~/ti/ipc_nn_nn_nn_nn/examples/DRA7xx_bios_elf/\ **ex13_notifypeer**

2. Open readme.txt file and follow build instructions step-by-step. Make sure there is no spaces between variable name and its value.

3. Run make command in current folder to build DSP1 and HOST notifypeer examples. Output files are created under debug subfolder.

4. Launch target configurations. Note that BH560USB_M is emulator is used to connect to AM572X EVM.

5. Right click CortexA15_0 and connect target.

6. On CCS --> Scripts --> AM572 Multicore Initialization --> Run AM572x Multicore EnableAllCore

7. Initialize DDR configuration. On CCS --> Scripts --> DDR configurations --> AM572_DDR3_532MHz_config

8. **Load DSP1** notifypeer Example out file on DSP1.

9. **Load HOST** notifypeer Example out file on ARM CortexA15_0.

10. Run both DSP1 and CortexA15_0.

11. On CCS --> Tools --> RTOS Object view (ROV).

12. Suspend (halt) ARM CortexA15_0 to view test messages on ROV Viewable Modules -->LoggerBuf. Refer the following image of ROV log messages

.. Image:: /images/Notify_peer_arm0.png

13. Suspend (halt) DSP2 and click on ROV icon to view log messages.

|

.. rubric:: IPC Ping Example:
   :name: ipc-ping-example

**ex11_ping**

ping example sends a message between all cores in the system. This
example is used to exercise every communication path between all
processors in the system (including local delivery on the current
processor). Ping example is also organized in a suitable manner to
develop an application with different compute units on each processor.

Each executable will create two tasks: 1) the server task, and 2) the
application task. The server task creates a message queue and then waits
on that queue for incoming messages. When a message is received, the
server task simply sends it back to the original sender.

The application task creates its own message queue and then opens every
server message queue in the system (including the server queue on the
local processor). The task sends a message to a server and waits for the
message to be returned. This is repeated for each server in the system
(including the local server).

.. note::
   Note that presently EVE is not yet supported and therefore,
   DSP1/DSP2/HOST are built for testing.

1. Change to ping folder example by enter: cd
~/ti/ipc_nn_nn_nn_nn/examples/DRA7xx_bios_elf/\ **ex11_ping**

2. Open readme.txt file and follow build instructions step-by-step. Make
sure there is no space between variable name and its value.

3. Open makefile and remove EVE and IPU from PROC build list.

4. Run make command in current folder to build DSP1, DSP2 and HOST ping examples. Output files are created under debug subfolder.

5. Launch target configurations. Note that BH560USB_M is emulator is used to connect to AM572X EVM.

6. Right click CortexA15_0 and connect target.

7. On CCS --> Scripts --> AM572 Multicore Initialization --> Run AM572x Multicore EnableAllCore

8. Initialize DDR configuration. On CCS --> Scripts --> DDR configurations --> AM572_DDR3_532MHz_config

9. **Load DSP1** Ping Example out file on DSP1.

10. **Load DSP2** Ping Example out file on DSP2.

11. **Load HOST** ping Example onto ARM CortexA15_0

12. Run DSP1, DSP2, and HOST images.

13. On CCS --> Tools --> RTOS Object view (ROV).

14. Halt DSP1 to view test messages on ROV Viewable Modules -->LoggerBuf Refer below image of ROV log messages

.. Image:: /images/Ping_dsp1.png

15. Suspend (halt) DSP2 and click on ROV icon to view log messages.

16. Suspend (halt) ARM CortexA15_0 and click on ROV icon to view log messages.

|

.. rubric:: Expanding IPC Ping Example:
   :name: expanding-ipc-ping-example

To demonstrate the flexibility of IPC architecture, you may include
additional cores to the above example by modifying the make file. For
example, you may add IPU1 in the list of processor in the make file as:
DSP1, DSP2, **IPU1,** HOST. After a clean build, the appropriate
configuration and output executable files will be generated that allow
passing messages between DSP1, DSP2, IPU1 and Host. Procedures are the
same as described in the previous example with the exception of
additional steps to load the IPU1 core with the corresponding executable
and running it in conjunction with DSP1, DSP2 and HOST.

.. note::
   During build process using IPU1, you may encounter a message
   indicating **rtsv7M4_T_le_eabi.lib** library is missing. This is a know
   issue and is being tracked by **SDCOM00118417** IR. However, you may
   create this missing library by going to the compiler installation's
   **lib** directory and execute the following command to regenerate all
   required libraries:

   ::

	./mklib --all

The following example depicts a typical host communications protocol
with other IPC apps (dsp1, dsp2, ipu1) **Note that the following HOST
communications list has been rearranged to further clarify the type of
communications between various cores**. Typically these messages arrive
at different intervals depending on each core processes execution time.

::

       1    xdc.runtime.Main    --> main:
       2    xdc.runtime.Main    main: ipc ready
       3    xdc.runtime.Main    MainHost_svrTskFxn:
       4    SvrHost    --> SvrHost_setup:
       5    SvrHost    SvrHost_setup: slave is ready
       6    SvrHost    <-- SvrHost_setup:
       7    SvrHost    --> SvrHost_run:
       8    xdc.runtime.Main    --> MainHost_appTskFxn:
       9    AppHost    --> AppHost_setup:

       10    AppHost    AppHost_setup: procId=0     opened server queue
       11    AppHost    AppHost_setup: procId=1     opened server queue
       12    AppHost    AppHost_setup: procId=2     opened server queue
       28    AppHost    AppHost_setup: procId=3     opened server queue

       32    AppHost    AppHost_run: ping procId=0
       34    AppHost    AppHost_run: ping procId=0
       36    AppHost    AppHost_run: ping procId=0
       38    AppHost    AppHost_run: ping procId=0
       40    AppHost    AppHost_run: ping procId=0

       33    AppHost    AppHost_run: ack received     procId=0
       35    AppHost    AppHost_run: ack received     procId=0
       37    AppHost    AppHost_run: ack received     procId=0
       39    AppHost    AppHost_run: ack received     procId=0
       41    AppHost    AppHost_run: ack received     procId=0

       13    SvrHost    SvrHost_run: message received     procId=0
       14    SvrHost    SvrHost_run: message received     procId=0
       15    SvrHost    SvrHost_run: message received     procId=0
       16    SvrHost    SvrHost_run: message received     procId=0
       17    SvrHost    SvrHost_run: message received     procId=0

       42    AppHost    AppHost_run: ping procId=1
       44    AppHost    AppHost_run: ping procId=1
       46    AppHost    AppHost_run: ping procId=1
       48    AppHost    AppHost_run: ping procId=1
       50    AppHost    AppHost_run: ping procId=1

       43    AppHost    AppHost_run: ack received     procId=1
       45    AppHost    AppHost_run: ack received     procId=1
       47    AppHost    AppHost_run: ack received     procId=1
       49    AppHost    AppHost_run: ack received     procId=1
       51    AppHost    AppHost_run: ack received     procId=1

       18    SvrHost    SvrHost_run: message received     procId=1
       19    SvrHost    SvrHost_run: message received     procId=1
       20    SvrHost    SvrHost_run: message received     procId=1
       21    SvrHost    SvrHost_run: message received     procId=1
       22    SvrHost    SvrHost_run: message received     procId=1

       52    AppHost    AppHost_run: ping procId=2
       55    AppHost    AppHost_run: ping procId=2
       58    AppHost    AppHost_run: ping procId=2
       61    AppHost    AppHost_run: ping procId=2
       64    AppHost    AppHost_run: ping procId=2

       54    AppHost    AppHost_run: ack received     procId=2
       57    AppHost    AppHost_run: ack received     procId=2
       60    AppHost    AppHost_run: ack received     procId=2
       63    AppHost    AppHost_run: ack received     procId=2
       66    AppHost    AppHost_run: ack received     procId=2

       53    SvrHost    SvrHost_run: message received     procId=2
       56    SvrHost    SvrHost_run: message received     procId=2
       59    SvrHost    SvrHost_run: message received     procId=2
       62    SvrHost    SvrHost_run: message received     procId=2
       65    SvrHost    SvrHost_run: message received     procId=2

       67    AppHost    AppHost_run: ping procId=3
       69    AppHost    AppHost_run: ping procId=3
       71    AppHost    AppHost_run: ping procId=3
       73    AppHost    AppHost_run: ping procId=3
       75    AppHost    AppHost_run: ping procId=3

       68    AppHost    AppHost_run: ack received     procId=3
       70    AppHost    AppHost_run: ack received     procId=3
       72    AppHost    AppHost_run: ack received     procId=3
       74    AppHost    AppHost_run: ack received     procId=3
       76    AppHost    AppHost_run: ack received     procId=3

       23    SvrHost    SvrHost_run: message received     procId=3
       24    SvrHost    SvrHost_run: message received     procId=3
       25    SvrHost    SvrHost_run: message received     procId=3
       26    SvrHost    SvrHost_run: message received     procId=3
       27    SvrHost    SvrHost_run: message received     procId=3

       29    AppHost    AppHost_setup: slave is ready
       30    AppHost    <-- AppHost_setup:
       31    AppHost    --> AppHost_run:
       77    AppHost    <-- AppHost_run: 0
       78    AppHost    --> AppHost_destroy:
       79    AppHost    <-- AppHost_destroy: status=0
       80    xdc.runtime.Main    <-- MainHost_appTskFxn: 0
       81    xdc.runtime.Main    MainHost_done:

