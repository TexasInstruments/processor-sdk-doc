.. http://processors.wiki.ti.com/index.php/Processor_SDK_Jailhouse_Hypervisor

.. rubric:: Overview
   :name: overview

Jailhouse is a static partitioning hypervisor that runs bare metal
binaries. It cooperates closely with Linux. Jailhouse doesn't emulate
resources that don't exist. It just splits existing hardware resources
into isolated compartments called "cells" that are wholly dedicated to
guest software programs called "inmates". One of these cells runs the
Linux OS and is known as the "root cell". Other cells borrow CPUs and
devices from the root cell as they are created.

|
.. Image:: /images/Jailhouse.png

*The picture above shows the jailhouse on a system a) before the
jailhouse is enabled; b) after the jailhouse is enabled; c) after a cell
is created.
*

|

Jailhouse consists of three parts: kernel module, hypervisor firmware
and tools, which a user uses to enable the hypervisor, create a cell,
load inmate binary, run and stop it. Jailhouse is an example of
Asynchronous Multiprocessing (AMP) architecture. When we boot Linux on
AM57XX-EVM, which has 2 ARM cores, Linux uses the both cores. After we
enable hypervisor it moves Linux to the root-cell. The root cell still
uses the both ARM cores. When we create a new cell, hypervisor calls
cpu_down() for the ARM1 core, leaving for Linux ARM0 only. The new cell
will use the ARM1 core and hardware resources dedicated for this cell in
the cell configuration file.

|

Jailhouse is an open source project, which can be found on
https://github.com/siemens/jailhouse.

|

.. rubric:: Demo
   :name: demo

| Processor Linux SDK delivers Jailhouse’s prebuilt binaries. You may
  try it immediately after installation. This section assumes that you
  have already installed PSDK, and have Linux booted on the AM572X-EVM
  or AM572x-IDK.

| **NOTE:** *to use Jailhouse hypervisor*

| *1) set u-boot environment variable optargs*: setenv optargs
  vmalloc=512M

*2) use \ **am572x-evm-jailhouse.dtb** for AM572x-EVM
or \ **am572x-idk-jailhouse.dtb** for AM572x-IDK
*

|

.. rubric:: Pre-built components
   :name: pre-built-components

| As it was mentioned in the previous section, Jailhouse consists of
  following components, which are prebuilt and copied to the target
  filesystem:

#. jailhouse.ko kernel module located at
   /lib/modules/4.9.28-<gitid>/extra/driver directory;
#. jailhouse.bin - hypervisor itself located at /lib/firmware directory;
#. Jailhouse management tools are located at
   /usr/local/libexec/jailhouse and /usr/sbin directories;

In order to create the root-cell and an inmate cell we need to provide
cell configuration files. Those configuration files and example binaries
are located at /usr/share/jailhouse/examples directory:

::

    root@am57xx-evm:/usr/share/jailhouse/examples# ls -1
    am572x-rtos-icss.cell
    am572x-rtos-pruss.cell
    am57xx-evm-ti-app.cell
    am57xx-evm.cell
    am57xx-pdk-leddiag.cell
    icss_emac.bin
    led_test.bin
    linux-loader.bin
    pruss.bin
    ti-app.bin

where

-  **am57xx-evm.cell** - root cell configuration file;
-  **ti-app.bin** and **am57xx-evm-ti-app.cell** - bare metal inmate and
   its cell configuration;
-  **led_test.bin** and **am57xx-pdk-leddiag.cell** - PDK led_test
   inmate example and its cell configuration (led_test.bin can be run on
   AM572x-EVM only);
-  **pruss.bin** and **am572x-rtos-pruss.cell** - TI-RTOS PRUSS inmate
   examples and its cell configuration (pruss.bin can be run on
   AM572x-IDK only);
-  **icss_emac.bin** and **am572x-rtos-icss.cell** - TI-RTOS ICSS-EMAC
   inmate example and its cell configuration (icss_emac.bin can be run
   on AM572x-IDK only);
-  **linux-loader.bin** - loader required to run inmates, which start
   address is not 0x0;

|

.. rubric:: Running the Demo on AM572x-EVM
   :name: running-the-demo-on-am572x-evm

.. rubric:: Running bare-metal ti-app.bin
   :name: running-bare-metal-ti-app.bin

Here are the steps to run the demo:

-  Boot the Linux
-  Insert jailhouse.ko kernel module

::

    root@am57xx-evm:~# modprobe jailhouse

-  Enable the hypervisor using am57xx-evm.cell root-cell configuration
   file

::

    root@am57xx-evm:~# jailhouse enable /usr/share/jailhouse/examples/am57xx-evm.cell
    Initializing Jailhouse hypervisor v0.6 on CPU 1
    Code location: 0xf0000030
    Page pool usage after early setup: mem 30/4073, remap 32/131072
    Initializing processors:
     CPU 1... OK
     CPU 0... OK
    Page pool usage after late setup: mem 39/4073, remap 38/131072
    Activating hypervisor
    [ 4155.880217] The Jailhouse is opening.

-  Create a cell for the inmate

::

    root@am57xx-evm:~# jailhouse cell create /usr/share/jailhouse/examples/am57xx-evm-ti-app.cell
    [ 5270.449687] CPU1: shutdown
    [ 5270.453221] NOHZ: local_softirq_pending 20
    Created cell "AM57XX-EVM-timer8-demo"
    Page pool usage after cell creation: mem 51/4073, remap 38/131072
    [ 5270.487970] Created Jailhouse cell "AM57XX-EVM-timer8-demo"

-  Load the ti-app.bin inmate binary

::

    root@am57xx-evm:~# jailhouse cell load 1 /usr/share/jailhouse/examples/ti-app.bin
    Cell "AM57XX-EVM-timer8-demo" can be loaded

-  Start the binary

::

    root@am57xx-evm:~# jailhouse cell start 1
    Hey, I'm working !!!!!!!!!!!
    timer id 4fff2b01
    timer value fffffc17; irq status 00000002; raw 00000002
    min 00000017; avr 0000001b; max 000002c1
    min 00000017; avr 0000001b; max 000000f3
    min 00000017; avr 0000001b; max 000002c8
    min 00000017; avr 0000001b; max 00000148
    min 00000017; avr 0000001b; max 000002d4
    min 00000017; avr 0000001b; max 00000158

**NOTE**: *becase all of the components: root-cell, hypervisor and demo
inmate use the same UART, there is a conflict. Once the inmate started
to use the UART, Linux stops getting any input from console. To
workaround this and continue to control the hypervisor, you may telnet
to the EVM and issue all commands from the telnet shell. Hypervisor
still will use Linux console to print it sdebug messages*

-  Stop the binary

::

    root@am57xx-evm:~# jailhouse cell shutdown 1

**NOTE**: *You may restore Linux console by killing the "/bin/login --"
process from telnet session.*

-  destroy cell

::

    root@am57xx-evm:~# jailhouse cell destroy 1
    Closing cell "AM57XX-EVM-timer8-demo"
    Page pool usage after cell destruction: mem 39/4073, remap 38/131072
    [ 6201.111168] Destroyed Jailhouse cell "AM57XX-EVM-timer8-demo"

-  disable hypervisor

::

    root@am57xx-evm:~# jailhouse disable
    Shutting down hypervisor
     Releasing CPU 0
     Releasing CPU 1
    [ 6248.149728] The Jailhouse was closed.

**NOTES**:

You may shutdown and start the same binary multiple times. Every time
you start the binary, it starts from the beginning.

If you have different binaries which use the same cell resources, you
may reuse the created cell to run them. You need just shutdown the cell,
load another binary and start it. If you need to run different binaries
that requires different resources, you need to shutdown the running
cell, destroy it, create a new one with required resources, load a new
binary and start it.

.. rubric:: Running PDK led_test.bin example
   :name: running-pdk-led_test.bin-example

After you enable hyprevisor, create a pdk cell  

::

    root@am57xx-evm:~# jailhouse cell create /usr/share/jailhouse/examples/am57xx-pdk-leddiag.cell
    [  312.419978] CPU1: shutdown
    Created cell "AM57XX-EVM-PDK-LED"
    Page pool usage after cell creation: mem 54/4075, remap 38/131072
    [  312.470723] Created Jailhouse cell "AM57XX-EVM-PDK-LED"
    root@am57xx-evm:~#

| load the led_test.bin binary

::

    root@am57xx-evm:~# jailhouse cell load 1 /usr/share/jailhouse/examples/led_test.bin
    Cell "AM57XX-EVM-PDK-LED" can be loaded

and start it

::

    root@am57xx-evm:~# jailhouse cell start 1
    Started cell "AM57XX-EVM-PDK-LED"
    root@am57xx-e
    *********************************************
    *                 LED Test                  *
    *********************************************

    Testing LED
    Blinking LEDs...
    Press 'y' to verify pass, 'r' to blink again,
    or any other character to indicate failure: r

    Blinking again
    Press 'y' to verify pass, 'r' to blink again,
    or any other character to indicate failure: y
    Received: y

    Test PASSED!

You may see blinking leds, press "r" to repeat the test.

| **NOTE:**
| This example just demonstrates hypervisor's ability to run binaries
  that were built outside of jailhouse source tree. This and other RTOS
  examples were ported for this purpose. Look to RTOS SDK documentation
  for description of the examples functionality.  

.. rubric:: Running the Demo on AM572x-IDK
   :name: running-the-demo-on-am572x-idk

Two TI-RTOS example applications were ported for Jailhouse hypervisor:
pruss.bin and icss_emac.bin. In contrast to led_test.bin, which has its
own startup code, linker script and was linked to start from address
0x0, the pruss.bin and icss_emac.bin used the TI-RTOS building
infrustructure as much as possible. Therefore they are linked to EVM's
DDR address space (starting from 0x80000000 ) and their entry points are
not 0x0. To support loading and running such applicaiton a special
command shell be used.

To run the pruss.bin applicaton enable the hypervisor the same way as
for other examples.

::

    cd /usr/share/jailhouse/examples/
    root@am57xx-evm:/usr/share/jailhouse/examples# modprobe jailhouse
    root@am57xx-evm:/usr/share/jailhouse/examples# jailhouse enable ./am57xx-evm.cell

    Initializing Jailhouse hypervisor  on CPU 0
    Code location: 0xf0000030
    Page pool usage after early setup: mem 30/4075, remap 32/131072
    Initializing processors:
     CPU 0... OK
     CPU 1... OK
    Page pool usage after late setup: mem 39/4075, remap 38/131072
    Activating hypervisor
    [  710.008555] The Jailhouse is opening.

Create a cell for pruss.bin

::

    root@am57xx-evm:/usr/share/jailhouse/examples# jailhouse cell create ./am572x-rtos-pruss.cell
    [  745.067783] CPU1: shutdown
    Created cell "AM572X-IDK-PRUSS"
    Page pool usage after cell creation: mem 54/4075, remap 38/131072
    [  745.107324] Created Jailhouse cell "AM572X-IDK-PRUSS"
    root@am57xx-evm:/usr/share/jailhouse/examples#

Use cell load command to load several required components:

::

    root@am57xx-evm:/usr/share/jailhouse/examples# jailhouse cell load 1 linux-loader.bin -a 0 -s "kernel=0x80005128" -a 0x100 pruss.bin -a 0x80000000
    Cell "AM572X-IDK-PRUSS" can be loaded

where

-  linux-loader.bin is a small application provided and built by
   jailhouse source tree. As you can see (-a 0) it is loaded to virtual
   address 0x0;
-  "-s "kernel=0x80005128" -a 0x100" - is the linux_loader argument
   loaded as string to virtual address 0x100, which instructs the
   linux-loader to branch to the pruss.bin 0x80005128 entry point;
-  pruss.bin itself, loaded to the virtual address 0x80000000 - the
   address where this application is lined to;

|
| After loading run the inmate as usual:

::

    root@am57xx-evm:/usr/share/jailhouse/examples# jailhouse cell start 1
    Started cell "AM572X-IDK-PRUSS"
    root@am57xx-evm:/usr/share/jailhouse/examples# passed verify constant tbl entry for instance 1: pruNum: 0
    eventwait: waiting for the INTC event from PRU
    sending the INTC event to the PRU for instance: 1 , pru num: 0
    eventwait: got the INTC event from PRU, count: 1
    eventwait: waiting for the INTC event from PRU
    sending the INTC event to the PRU for instance: 1 , pru num: 0
    eventwait: got the INTC event from PRU, count: 2
    eventwait: waiting for the INTC event from PRU
    sending the INTC event to the PRU for instance: 1 , pru num: 0
    eventwait: got the INTC event from PRU, count: 3
    eventwait: waiting for the INTC event from PRU
    sending the INTC event to the PRU for instance: 1 , pru num: 0
    eventwait: got the INTC event from PRU, count: 4
    eventwait: waiting for the INTC event from PRU
    sending the INTC event to the PRU for instance: 1 , pru num: 0
    eventwait: got the INTC event from PRU, count: 5
    eventwait: waiting for the INTC event from PRU
    Testing for instance: 1, pru num: 0 is complete
    passed verify constant tbl entry for instance 1: pruNum: 1
    sending the INTC event to the PRU for instance: 1 , pru num: 1
    eventwait: got the INTC event from PRU, count: 1
    eventwait: waiting for the INTC event from PRU
    sending the INTC event to the PRU for instance: 1 , pru num: 1
    eventwait: got the INTC event from PRU, count: 2
    eventwait: waiting for the INTC event from PRU
    sending the INTC event to the PRU for instance: 1 , pru num: 1
    eventwait: got the INTC event from PRU, count: 3
    eventwait: waiting for the INTC event from PRU
    sending the INTC event to the PRU for instance: 1 , pru num: 1
    eventwait: got the INTC event from PRU, count: 4
    eventwait: waiting for the INTC event from PRU
    sending the INTC event to the PRU for instance: 1 , pru num: 1
    eventwait: got the INTC event from PRU, count: 5
    Testing for instance: 1, pru num: 1 is complete
    passed verify constant tbl entry for instance 2: pruNum: 0
    eventwait2: waiting for the INTC event from PRU
    sending the INTC event to the PRU for instance: 2 , pru num: 0
    eventwait2: got the INTC event from PRU, count: 1
    eventwait2: waiting for the INTC event from PRU
    sending the INTC event to the PRU for instance: 2 , pru num: 0
    eventwait2: got the INTC event from PRU, count: 2
    eventwait2: waiting for the INTC event from PRU
    sending the INTC event to the PRU for instance: 2 , pru num: 0
    eventwait2: got the INTC event from PRU, count: 3
    eventwait2: waiting for the INTC event from PRU
    sending the INTC event to the PRU for instance: 2 , pru num: 0
    eventwait2: got the INTC event from PRU, count: 4
    eventwait2: waiting for the INTC event from PRU
    sending the INTC event to the PRU for instance: 2 , pru num: 0
    eventwait2: got the INTC event from PRU, count: 5
    eventwait2: waiting for the INTC event from PRU
    Testing for instance: 2, pru num: 0 is complete
    passed verify constant tbl entry for instance 2: pruNum: 1
    sending the INTC event to the PRU for instance: 2 , pru num: 1
    eventwait2: got the INTC event from PRU, count: 1
    eventwait2: waiting for the INTC event from PRU
    sending the INTC event to the PRU for instance: 2 , pru num: 1
    eventwait2: got the INTC event from PRU, count: 2
    eventwait2: waiting for the INTC event from PRU
    sending the INTC event to the PRU for instance: 2 , pru num: 1
    eventwait2: got the INTC event from PRU, count: 3
    eventwait2: waiting for the INTC event from PRU
    sending the INTC event to the PRU for instance: 2 , pru num: 1
    eventwait2: got the INTC event from PRU, count: 4
    eventwait2: waiting for the INTC event from PRU
    sending the INTC event to the PRU for instance: 2 , pru num: 1
    eventwait2: got the INTC event from PRU, count: 5
    Testing for instance: 2, pru num: 1 is complete
    All tests have passed

|
| You may run the **icss_emac.bin** in similar way using appropriate
  cell configuration. **Note that icss_emac has different entry point -
  0x80000000**.

.. rubric:: Jailhouse Performance on AM5728
   :name: jailhouse-performance-on-am5728

To verify the real-time performance of Jailhouse Sitara AM5728 was setup
to run Linux on one of the ARM Cortex A15 cores, and a TI-RTOS inmate on
the other A15 core. A test was run to measure interrupt latency. Poll
mode driver based application performance of an inmate should be
identical to a system without virtualizationion in a static partitioning
system like Jailhouse. Anything interrupt based is required to share the
interrupt controller (GIC) which will introduce some interference from
Linux to the real-time application. The measurements shown below over a
million interrupts clearly shows the interference, and captures the
upper bound at 8.8us. For the first run of interrupt latency test an
unloaded Linux running on core 0 is in the first column. In the second
column Linux on core 0 is running STREAM. STREAM is an external memory
access benchmark that fully utilizes the number of outstanding reads and
writes to memory. It is scalable from individual processors to clusters
supercomputers, here it is used at the processor level. It was chosen as
representative of a worst case memory access behaviour of a Linux based
application on a Cortex A15, essentially with a memory access profile
like an optimized memorytomemory copy. In AM5728 the two Cortex A15
cores share L2 cache and access to the rest of the SoC, which the STREAM
benchmark running on core 0 stresses while core 1 access GIC registers
to respond to the interrupt.

|

.. table::  **Interrupt latency of a bare metal inmate (core 1)**

   +-----------------------+-----------------------+-----------------------+
   |                       | Unloaded Linux on     | Linux Running STREAM  |
   |                       | core 0                | benchmark on core 0   |
   +=======================+=======================+=======================+
   | | Interrutp count     | 99.3756%              | 33.9323%              |
   | | Bucket 1.6 us - 3.2 |                       |                       |
   |   us                  |                       |                       |
   +-----------------------+-----------------------+-----------------------+
   | | Interrutp count     | 0.6244%               | 66.0632%              |
   | | Bucket 3.2 us - 6.4 |                       |                       |
   |   us                  |                       |                       |
   +-----------------------+-----------------------+-----------------------+
   | | Interrutp count     | none                  | 0.0045%               |
   | | Bucket 6.4 us -     |                       |                       |
   |   12.8 us             |                       |                       |
   +-----------------------+-----------------------+-----------------------+
   | Minimum interrupt     | 2.2 microseconds      | 1.8 microseconds      |
   | latency               |                       |                       |
   +-----------------------+-----------------------+-----------------------+
   | Maximim interrupt     | 5.0 microseconds      | 8.8 microseconds      |
   | latency               |                       |                       |
   +-----------------------+-----------------------+-----------------------+

|

|

.. rubric:: Building Jailhouse from Sources
   :name: building-jailhouse-from-sources

Jailhouse sources are located at
$TI_SDK_PATH/board-support/extra-drivers/jailhouse-0.7 directory. The
directory contains the following subdirectories:

-  **Documentation**
-  **ci** - configuration files for different platforms. ***Copy the
   jailhouse-config-am57xx-evm.h file into hypervisor/include/jailhouse
   directory and rename it to config.h***
-  **configs** - cell configuration files.
-  **driver** - jailhouse.ko kernel module code
-  **hypervisor** - hypervisor code
-  **inmates** - inmates demos. It also contains code for ti_app inmate
   example.
-  **scripts**
-  **tools** - jailhouse management utility

The top level SDK Makefile has the *jailhouse_clean*, *jailhouse* and
*jailhouse_install* targets which can be used to clean, build and
install jailhouse to the target file system.

|

.. rubric:: Building and Running the Ethercat Slave Demo
   :name: building-and-running-the-ethercat-slave-demo

To build and run the Ethercat Slave Demo, you need to install the
PSDK-RT, PRSDK and PRU-ICSS-ETHERCAT-SLAVE builds. We assume that you
already have the first two SDKs installed. The PRU-ICSS-ETHERCAT-SLAVE
can be downloaded from
http://software-dl.ti.com/processor-industrial-sw/esd/PRU-ICSS-ETHERCAT-SLAVE/01_00_05_00/index_FDS.html.

Once you have this SDK installed you may build Ethercat slave
components.

If the am572x-ethercat.cell is not installed on target filesystem yet,
build it from PSDK-RT top level makefile "make jailhouse" and copy it
to target under /usr/share/jailhouse/examples.

To build the ethercat_slave_demo.bin:

-  Modify the IA_SDK_HOME at
   ~/ti/processor_sdk_rtos_am57xx_[version]/demos/jailhouse-inmate/rtos/ethercat_slave_demo/Makefile
   to point to the install directory of PRU-ICSS-ETHERCAT-SLAVE.
-  At
   ~/ti/processor_sdk_rtos_am57xx_[version]/demos/jailhouse-inmate/makefile:
   add ethercat_slave_demo\* entries as pruss-test/icss-emac-test to the
   end of the makefile

::

    ethercat_slave_demo:
        $(MAKE) -C ./rtos/ethercat_slave_demo

    ethercat_slave_demo_clean:
        $(MAKE) -C ./rtos/ethercat_slave_demo clean

    ethercat_slave_demo_install:
        $(MAKE) -C ./rtos/ethercat_slave_demo install

-  cd ~/ti/processor_sdk_rtos_am57xx_[version]/
-  source setupenv.sh
-  cd ~/ti/processor_sdk_rtos_am57xx_[version]/demos/jailhouse-inmate
-  source setenv.sh
-  make ethercat_slave_demo

After the steps above, copy ethercat_slave_demo.bin to target under
/usr/share/jailhouse/examples.

To run the inmate refer to the instructions for `**Running the Demo on
AM572x-IDK** <#Running_the_Demo_on_AM572x-IDK>`__ . Be aware that the
inmate start address is 0x80000000. So, you need to use it as a
parameter at the "jailhouse cell load" command:

::

    jailhouse cell load 1 linux-loader.bin -a 0 -s "kernel=0x80000000" -a 0x100 ethercat_slave_demo.bin -a 0x80000000

|
| Procedure to check two-way communication between the slave inmate and
  the master station:

-  Refer to
   http://processors.wiki.ti.com/index.php/PRU_ICSS_EtherCAT#Running_EtherCAT_Slave_Application
   to setup Ethercat master.
-  Master: Online write [data] to RxPDO 32Bit Output. After this, the
   slave should report the corresponding value via Board_setDigOutput.
   The value can be checked with “devmem2 0xeef00000” also.
-  Slave: devmem2 0xeef00004 b [data]. After this, Master should display
   the corresponding value in TXPDO 32Bit Input.

|

.. rubric:: Jailhouse Internals
   :name: jailhouse-internals

This section gives some Jailhouse details and required kernel
modifications.

.. rubric:: Linux Kernel Modifications
   :name: linux-kernel-modifications

In order to run hypervisor itself and inmates Jailhouse requires
additional nodes in kernel dtb. See the am572x-evm-jailhouse.dts and
am572x-idk-jailhouse.dts. They add required nodes or modify existing
nodes of the default am57xx-evm-reva3.dts and am57xx-idk.dts DTS files.

.. rubric:: Memory Reservation
   :name: memory-reservation

Linux kernel has to reserve some memory for jailhouse hypervisor and for
inmate. This memory has to be reserver statically. In this release we
reserved 16MB of physical memory for hypervisor and 16MB for inmates.

::

    / {

        reserved-memory {
            jailhouse: jailhouse@ef000000 {
                reg = <0x0 0xef000000 0x0 0x1000000>;
                no-map;
                status = "okay";
            };

            jh_inmate: jh_inmate@ee000000 {
                reg = <0x0 0xee000000 0x0 0x1000000>;
                no-map;
                status = "okay";
            };
        };
    };

.. rubric:: Hardware Modules Reservation
   :name: hardware-modules-reservation

Linux kernel enables all SOC HW modules which are required for its
configuration. Appropriate drivers configure required clocks and
initialize HW registers. For all unused IPs clocks are not configured.
Also kernel power management can put a module into the sleep mode. A
jailhouse inmate doesn't share the same hardware module with Linux
kernel (except debug UART). But the inmate doesn't configure required
clocks and doesn't deal with power domains. So, we still relay on Linux
kernel (at least at the current release) to configure clocks to inmate
HW modules. If we want to use some hardware modules for an inmate, we
have to tell kernel about this in advance.

The following nodes disable using of the timer8 and uart9 by kernel.
Also this restricts kernel to put those IPs to sleep mode.

::

    &timer8 {
        status = "disabled";
        ti,no-idle;
    };

    &uart9 {
        status = "disabled";
        ti,no-idle;
    };

You may see other nodes in the jailhouse DTSes which reserve other IPs
to be used for inmates. Thus IDK's DTS disables nodes, which IPs are
used for icss_emac and pruss inmates.

.. rubric:: GIC Interrupt Inputs Reservation
   :name: gic-interrupt-inputs-reservation

Interrupt lines from hardware modules don't go to ARM interrupt
controller (GIC) directly. They go to a crossbar register, which selects
a GIC distributor input. The selection is done dynamically by Linux
kernel. Linux keeps track of all used and unused GIC inputs. If a
jailhouse inmate has to use an interrupt, it has to configure the
crossbar register by itself. To prevent conflicts between the Linux
crossbar manager and the inmate, and give to the inmate some unused GIC
input lines, which it can use, we need to reserve some of them in the
kernel dts.

This can be done by adding GIC input numbers to the "ti,irqs-skip"
property of the "crossbar_mpu:" node. Lines 134 and 135 are added to the
following node.

::

           crossbar_mpu: crossbar@4a002a48 {
                ti,irqs-skip = <10 133 134 135 139 140>;
            };

| **Note:** The icss_emac.bin application uses much more interrupt
  lines. Thats is why IDK's dtb skips aditional interrupts.

::

            crossbar_mpu: crossbar@4a002a48 {
                ti,irqs-skip = <10 44 127 129 133 134 135 136 137 139 140>;
            };

.. rubric:: Root-cell configuration
   :name: root-cell-configuration

When hypervisor is being enabled it creates a cell for Linux and moves
it to that cell. The cell is called as "root-cell". The cell
configuration as a "*.c" file which is compiled to a special binary
format "*.cell" file. The hypervisor uses the "cell" file to create a
cell. The cell configuration describes memory regions and their
attributes which will be used by the cell,

::

       .mem_regions = {
            /* OCMCRAM */ {
                .phys_start = 0x40300000,
                .virt_start = 0x40300000,
                .size = 0x80000,
                .flags = JAILHOUSE_MEM_READ | JAILHOUSE_MEM_WRITE |
                    JAILHOUSE_MEM_IO,
            },
            /* 0x40380000 - 0x48020000 */ {
                .phys_start = 0x40380000,
                .virt_start = 0x40380000,
                .size = 0x7ca0000,
                .flags = JAILHOUSE_MEM_READ | JAILHOUSE_MEM_WRITE |
                    JAILHOUSE_MEM_IO,
            },
            /* UART... */ {
                .phys_start = 0x48020000,
                .virt_start = 0x48020000,
                .size = 0xe0000,//0x00001000,
                .flags = JAILHOUSE_MEM_READ | JAILHOUSE_MEM_WRITE |
                    JAILHOUSE_MEM_IO,
            },
          ...
            /* RAM */ {
                .phys_start = 0x80000000,
                .virt_start = 0x80000000,
                .size = 0x6F000000,
                .flags = JAILHOUSE_MEM_READ | JAILHOUSE_MEM_WRITE |
                    JAILHOUSE_MEM_EXECUTE,
            },
            /* Leave hole for hypervisor */

            /* RAM */ {
                .phys_start = 0xF0000000,
                .virt_start = 0xF0000000,
                .size = 0x10000000,
                .flags = JAILHOUSE_MEM_READ | JAILHOUSE_MEM_WRITE |
                    JAILHOUSE_MEM_EXECUTE,
            },

bitmap of CPU cores dedicated for the cell,

::

    .cpus = {
            0x3,
        },

bitmap of interrupt controller SPI interrupts

::

       .irqchips = {
            /* GIC */ {
                .address = 0x48211000,
                .pin_base = 32,
                .pin_bitmap = {
                    0xffffffff, 0xffffffff, 0xffffffff, 0xffffffff
                },
            },
            /* GIC */ {
                .address = 0x48211000,
                .pin_base = 160,
                .pin_bitmap = {
                    0xffffffff, 0, 0, 0
                },
            },
        },

and some other parameters. That is for all cells.

In addition to that the root cell also allocates the physical memory for
the hypervisor.

::

           .hypervisor_memory = {
                .phys_start = 0xef000000,
                .size = 0x1000000,
            },

The "memory regions" section is used by hypervisor to create the second
stage MMU translation table. Usually for root-cell the identical mapping
is being used - "VA = PA".

See the am57xx-evm.c file is the complete am57xx-evm root cell
configuration.

.. rubric:: Bare Metal Inmate Example
   :name: bare-metal-inmate-example

Jailhouse comes with inmate demos located at the *inmates/demos*
directory. Current (v0.6) version has two demo inmates: **gic-demo** and
**uart-demo**. Those are very simple bare-metal applications that
demonstrates a uart and arm-timer interrupt. Those demos are common for
all jailhouse platforms.

More interesting may be the **ti-app**, a demo made especially for
AM572x SOC. The code is located at the *inmate/ti_app* directory.

Basically this application is a sandbox to make some experiments. The
current version demonstrates of using a uart, timer and a GIC SPI
interrupt (timer generates periodic interrupts). The application also
has some extra code, which was used to measure interrupt latency.

|

As any inmate the ti-app inmate works in a cell. The am57xx-evm-ti-app.c
is the cell configuration file. For this cell only ARM1 core will be
used:

::

       .cpus = {
            0x2,
        },

**NOTE:** *Actually on am572 SOC, which has only 2 ARM core and Linux
always uses the ARM0 core only ARM1 can be taken for an inmate.*

The cell configuration has 5 memory regions:

::

           /* UART... */ {
                .phys_start = 0x48020000,
                .virt_start = 0x48020000,
                .size = 0x1000,
                .flags = JAILHOUSE_MEM_READ | JAILHOUSE_MEM_WRITE |
                    JAILHOUSE_MEM_IO | JAILHOUSE_MEM_ROOTSHARED,
            },
            /* UART... */ {
                .phys_start = 0x48424000,
                .virt_start = 0x48424000,
                .size = 0x1000,
                .flags = JAILHOUSE_MEM_READ | JAILHOUSE_MEM_WRITE |
                    JAILHOUSE_MEM_IO | JAILHOUSE_MEM_ROOTSHARED,
            },
            /* TIMER... */ {
                .phys_start = 0x48826000,
                .virt_start = 0x48826000,
                .size = 0x1000,
                .flags = JAILHOUSE_MEM_READ | JAILHOUSE_MEM_WRITE |
                    JAILHOUSE_MEM_IO | JAILHOUSE_MEM_ROOTSHARED,
            },
            /* L4_CFG */ {
                .phys_start = 0x4a000000,
                .virt_start = 0x4a000000,
                .size = 0xE00000,
                .flags = JAILHOUSE_MEM_READ | JAILHOUSE_MEM_WRITE |
                    JAILHOUSE_MEM_IO | JAILHOUSE_MEM_ROOTSHARED,
            },
            /* RAM */ {
                .phys_start = 0xee000000,
                .virt_start = 0,
                .size = 0x800000,
                .flags = JAILHOUSE_MEM_READ | JAILHOUSE_MEM_WRITE |
                    JAILHOUSE_MEM_EXECUTE | JAILHOUSE_MEM_LOADABLE,
            },

Two for UARTs. *The first one for UART3, which is a standard EVM debug
uart. The second for UART9, using of which requires some board
modifications. But UART9 doesn't conflict with Linux or hypervisor and
may be more useful if the inmate needs a dedicated UART.* One region for
timer9 and one for access multiple configuration registers.

The last region is for RAM allocated for the inmate. Similar to
root-cell memory regions configuration memory mapping for all regions
except for RAM are identical (VA = PA). For the RAM region virtual
address has to be '0'. The physical addresses of the region must be
inside of the physical memory reserved for inmates in the Linux DTS
file.

In the .irqchip section of the cell configuration file we reserve GIC
interrupt line #134 (*One of two lines reserved in the kernel DTS*).

::


        /* GIC */ {
            .address = 0x48211000,
            .pin_base = 160,
            .pin_bitmap = {
                0x00000040,
            },
        },

*Here where #134 comes from. The 0x00000040 is the bitmask of the sixth
bit. So, .pin_base(160) + .pin_bitmap(6) - 32(number of SWI and PPI
interrupt) = 134.*

As other jailhouse demos the **ti-app** uses the jailhouse startup code,
which sets the inmate vector table, zeros BSS segment, sets the stack up
and calls the inmate_main(). The initialization of the GIC controller is
done by hypervisor. Also the hypervisor remaps GICC interface to GICV
interface and intercepts all inmates accesses to GICD. It allows to
read/write only GICD registers, related to the lines given in the
.irq_chips section. In our case for the line #134 only.

In the inmate_main() the inmate initializes uart, sets the crossbar and
calls the gic_setup() to set the inmate's interrupt handler. *The
jailhouse provides inmate interrupt controller API. This can be used by
inmate.*

The ti-app initializes the timer and enters to the infinite loop.

Actually the inmate code has only about 100 lines and doesn't require
any more explanation.

.. rubric:: RTOS PDK Inmates
   :name: rtos-pdk-inmates

The jailhouse demo applications and the "ti_app" are built by
jailhouse's makefile inside the jailhouse's source tree. It is more
interesting to build an inmate outside of the jailhouse source tree,
using independent makefile and third party libraries. This release
provides **led_test**, a simple example of a bare-metal application,
which uses prebuilt RTOS PDK libraries and is built independently on
Jailhouse. It also has ports of two TI RTOS SYSBIOS test applications -
pruss and icss_emac. *There are two other examples: 1) bare-metal
memcp_bm - a simple application to measure memory bandwidth; 2)
Ethercat_slave_demo - ported to Jailhouse example from "PRU-ICSS
Industrial Software for Sitara™ Processors". The example requires some
modifications of the PRU-ICSS Industrial Software, which is not
published yet. That is why the ethercat_slave_demo included here as a
reference only.*

The code of the applications is located on the
$(SDK_INSTALL_PATH)/processor_sdk_rtos_am57xx_4_01_00_04/demos/jailhouse-inmate
directory, which contains:

::

    ├── baremetal
    │   ├── led
    │   │   ├── led_test.c
    │   │   └── makefile
    │   ├── memcp_bm
    │   │   ├── makefile
    │   │   └── memcp_bm.c
    │   └── soc
    │       └── am572x
    │           ├── evmAM572x
    │           │   ├── entry.S
    │           │   ├── gic.c
    │           │   ├── linker.cmd
    │           │   └── make.inc
    │           └── rules.mk
    ├── makefile
    ├── rtos
    │   ├── ethercat_slave_demo
    │   │   ├── bios
    │   │   │   ├── am572x_app.cfg
    │   │   │   └── makefile
    │   │   ├── Makefile
    │   │   └── src
    │   │       └── board_jh.c
    │   ├── icss_emac
    │   │   ├── bios
    │   │   │   ├── icss_emac_arm_wSoCLib.cfg
    │   │   │   └── makefile
    │   │   ├── lnk_pruss_fw.cmd
    │   │   ├── Makefile
    │   │   └── src
    │   │       ├── idkAM572x_ethernet_config_jh.c
    │   │       └── idkAM572x_jh.c
    │   ├── pru-icss
    │   │   ├── bios
    │   │   │   ├── makefile
    │   │   │   └── pruss_arm_wSoCLib.cfg
    │   │   ├── Makefile
    │   │   └── src
    │   │       └── idkAM572x_jh.c
    │   └── Rules.mk
    └── setenv.sh

.. rubric:: Bare-metal example
   :name: bare-metal-example

The bare-metal directory has three subdirectories: **soc** - has common
for bare-metal applications soc specific code; **led** - led_test
application code; **memcp_bm** - memcp_bm code;

The **soc/am572x/evmAM572x** sub-directory contains:

-  **entry.S** - startup file for an inmate;
-  **gic.c** - has the dummy \_weak\_ INTCCommonIntrHandler(), which can
   be overridden by an actual application handler.
-  **linker.cmd** - jailhouse requires that an inmate shall start from
   address "0". It also requires that all inmates segments be located in
   contiguous memory. This linker.cmd is to meet these requirements.

The **led** directory contains:

-  The main inmate **led_test.c** code. This file is based on
   $(SDK_INSTALL_PATH)/pdk_am57xx_1_0_6/packages/ti/board/diag/led/src/led_test.c
   diagnostic application. Because the inmate works as a virtual machine
   in order to use caches MMU has to be enabled. So, the application
   creates the MMU translation table with identical mapping and enables
   MMU. It also has the gic_init(), which is now used at this relese.
-  **makefile** is to build the inmate. As you can see, it links number
   of brebuilt PDK libraries.

|
| To build the **led_test.bin** (a jailhouse inmate has to be \*.bin,
  but not \*.out file):

-  cd to $(SDK_INSTALL_PATH)/processor_sdk_rtos_am57xx_4_01_00_04
   drectory
-  source setupenv.sh
-  cd to
   $(SDK_INSTALL_PATH)/processor_sdk_rtos_am57xx_4_01_00_04/demos/jailhouse-inmates
-  source setenv.sh
-  run **make led_test**

That should build the led_test.bin binary, that can be loaded to the
jailhouse cell and run. As any other inmate it has to be run in a cell,
created with appropriate cell configuration. In contrast to the
led_test.bin, which is compiled independently on jailhouse, a
corresponding cell configuration is compiled by jailhouse makefile.

The am57xx-pdk-leddiag.c cell configuration file is located in the
$TI_SDK_PATH/board-support/extra-drivers/jailhouse-0.7/configs
directory. Use the compiled am57xx-pdk-leddiag.cell file when you create
the cell for led_test.bin inmate.

See `Running the Demo <#Running_the_Demo>`__ to run the inmate.

The **memcp_bm** is very similar to led_test. It is built in the same
way as the led_test. Use the am57xx-bm.cell file from
$TI_SDK_PATH/board-support/extra-drivers/jailhouse-0.7/configs to create
the jailhouse cell for the memcp_bm inmate.

|

.. rubric:: RTOS BIOS Examples
   :name: rtos-bios-examples

| The pruss and icss_emac examples are located in the rtos/pruss and
  rtos/icss_emac directories. The structures of the both directories are
  identical. Each directory contains the bios and src subdirectories.
  The bios contains XDC type application configuration file and
  makefile. The configuration file is reworked copy of the original RTOS
  application configuration file. For example the configuration file for
  icss_emac inmate was ported from
  $(SDK_INSTALL_PATH)/ti/pdk_am57xx_1_0_7/packages/ti/drv/icss_emac/test/am572x/armv7/bios/icss_emac_arm_wSoCLib.cfg
  file. As far as jailhouse inmate is not responsible for board related
  configuration, the board library, i2c library, OCRAM MMU sections and
  some other unnecessary for the inmate components were removed from the
  configuration file.

| As far as the application main function calls the board_init()
  function, this function as well as the Board_moduleClockInit() (with
  required for icss_emac application clocks) are implemented in the
  idkAM572x_jh.c file.

| Thus the ported configuration file, the idkAM572x_jh.c and makefiles
  are only new files required to port RTOS SDK existing project to
  jailhouse inmate.

The jailhouse-inmate/Makefile has the "pruss_test" and "icss_emac_test"
targets to build the BIOS inmates.

The structure of the ethercat_slave_demo example is very similar to the
pruss and icss_emac examples. As far as it depends on a particular
version of the "PRU-ICSS Industrial Software", which has to be installed
independently, building of the demo is not included into the top level
makefile.

|

.. rubric:: RTOS BIOS Porting Notes
   :name: rtos-bios-porting-notes

As you can see in the previous section, the RTOS BIOS inmates has only
few new files. Almost all files were reused from RTOS SDK examples. But
following notes have to be considered when porting an RTOS BIOS
application to a Jailhouse inmate.

Jailhouse inmate runs in a small cell. The cell is created by
hypervisor, which was started from already booted Linux OS. That says
that the SOC, board and most clocks are already initialized and the
inmate don't need and usually cannot touch any resources not listed in
the inmate cell configuration file.

Thus the using of board and i2c libraries were removed from
cponfiguration file. Also OCRAM was removed from MMU configuration.

Jailhouse hypervisor allows inmate to access certain GICD registers, but
only for those interrupt lines, which are listed in the cell
configuration file. The cell creating routine reconfigures GICD target
registers by itself. The standard gic_init() BIOS API configures target
registers for all interrupt lines. That is not permitted for an inmate.
To avoid this the latest SYSBIOS release has a special feature, which
allows to disable target configuration from GIC initialization function.
See the following fragment at the configuration file:

::

    var Hwi = xdc.useModule('ti.sysbios.family.arm.gic.Hwi');
    Hwi.initGicd = false;

The RTOS BIOS applications are built to \*.out format. RTOS loader may
load this file to the board even if the image has multiple sections with
their addresses spread across the entire SOC address range. The
Jailhouse supports only \*.bin format, and inmate may use only allocated
for it memory carved out from Linux. Therefore the ported application
shall use only limited memory.

Jailhouse may start an inmate that start from virtual address 0x0, but
an usual RTOS application is linked to the 0x80000000 address and with
different from that entry point. The Jailhouse allows to start such
applications (see above). But using the linux-loader required additional
node in the inmate cell configuration.

::

           /* RAM loader */ {
                .phys_start = 0xed000000,
                .virt_start = 0x0,
                .size = 0x10000,
                .flags = JAILHOUSE_MEM_READ | JAILHOUSE_MEM_WRITE |
                    JAILHOUSE_MEM_EXECUTE | JAILHOUSE_MEM_LOADABLE,
            },
            /* RAM RTOS 224MB*/ {
                .phys_start = 0xe0000000,
                .virt_start = 0x80000000,
                .size = 0xd000000,
                .flags = JAILHOUSE_MEM_READ | JAILHOUSE_MEM_WRITE |
                    JAILHOUSE_MEM_EXECUTE | JAILHOUSE_MEM_LOADABLE,
            },

| You may see that cell configuration for icss_emac inmate configures
  two RAM regions:

#. small one with virtual address 0x0 for the linux-loader;
#. main region for the icss_emac test itself;

|

.. rubric:: General Porting Notes
   :name: general-porting-notes

When you start porting your RTOS or bare-metal application to Jailhouse
inmate, you have to consider several things. They are listed below.
*This list is not complete and has just recommendations based on common
sense and previous porting experience*.

-  **Linux always starts first** before hypervisor. Linux initializes
   all (or almost all) common resources of SOC. Thus it initializes
   memory controller, clocks, interrupt controller etc. It configures
   PINMUX registers. In most cases it takes care about board
   configuration as well.

-  **Inmate Cell Configuration** defines resources, which are available
   for the inmate. The ported application can use only those resources
   and responsible for theirs initialization only. The ported
   application will not run on the board it used to run, but on a
   different **virtual board**, defined by the cell configuration. Thats
   is why the application cannot use any common board_init or soc_init
   functions that may touch used by Linux resources. **Inmate is a guest
   only**.

-  As it mentioned above Linux initializes **Interrupt Controller** and
   dynamically configures crossbar registers. It has to be planned ahead
   which interrupts inmate may use. Those interrupts has to be reserved
   at Linux's dts file. Also used by the inmate interrupts have to
   listed in the inmate cell configuration. Hypervisor configures GIC
   target registers for those interrupt. Inmate is responsible only for
   enabling, disabling and acknowledging the interrupts.

-  Linux owns **I2C** buses. Inmate cannot has its owe driver to control
   I2C bus. It is not practicable even if the both root-cell and inmate
   cell configurations share I2C region and Linux and the Inmate have an
   agreement not to use I2C at the same time. The problem is that the
   Linux I2C driver works in interrupt mode and if the Inmate issues an
   I2C transaction, Linux's interrupt handler will be called. It brakes
   the Linux's and Inmate's I2C drivers state machines (or whatever they
   have).

-  Using **GPIO** may have the same as I2C problem. It is easy to
   disable an entire GPIO bank from using by Linux and use it for the
   Inmate. But it is not practical to share the same bank by the both
   Linux and Inmate.

|

