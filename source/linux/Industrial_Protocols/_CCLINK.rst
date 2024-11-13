.. http://processors.wiki.ti.com/index.php/Processor_SDK_Linux_CCLINK
.. rubric:: Overview

Control and Communication Link (CC-Link) is an open network administered
as a fully-open architecture by the CC-Link Partner Association (CLPA).
CC-Link is available in multiple formats: CC-Link, CC-Link Safety,
CCLink IE (Industrial Ethernet) Control, and CC-Link IE Field. CC-Link
IE Field Basic (or IEF Basic) is a new addition to the family of CC-Link
IE open network technologies that enable device vendors to easily add
CC-Link IE compatibility to any product with a 100-Mbit Ethernet port.

| The CC-Link IE Field Basic operates with Processor SDK Linux, using
  the Linux networking stack based on either EMAC or PRU-ICSS. This page
  will describe how to get the source code of CCLINK IEF Basic, how to
  compile it with Processor SDK Linux, and how to run it on the
  supported TI platforms.

.. rubric:: Supported TI Platforms
   :name: supported-ti-platforms

The table below lists the TI platforms which support CCLINK IEF Basic
with EMAC, and PRU-ICSS, respectively.

**Device**
**EVM**
**IEF Basic on EMAC**
**IEF Basic on PRU-ICSS**
AM572x
AM572x EVM
X
AM572x IDK
X
X
AM571x
AM571x IDK
X
X
AM437x
AM437x EVM
X
AM437x SK
X
AM437x IDK
X
X
AM335x
AM335x EVM
X
AM335x BeagleBoneBlack
X
AM335x SK
X
AM335x ICE
X
X
K2G
K2G EVM
X
K2G ICE
X
X
|

|

.. rubric:: Source Code for CCLINK IEF Basic
   :name: source-code-for-cclink-ief-basic

The CCLINK IEF basic source code for Linux can be requested from
`CLPA <http://am.cc-link.org/en/index.html>`__. It can also be retrieved
from `Processor SDK CCLink
Source <http://git.ti.com/processor-sdk/cclink/trees/master>`__.

|

.. rubric:: Compile CCLINK IEF Basic with Processor SDK Linux
   :name: compile-cclink-ief-basic-with-processor-sdk-linux

Starting from Processor SDK Linux Releases 4.1.0, the pre-built binaries
and configuration files for CCLINK IEF Basic will be part of the
filesystem of Processor SDK Linux. The binaries (Master\_sample and
Slave\_sample) can be located under the /usr/bin folder. The
configuration files (MasterParameter.csv and SlaveParameter.csv) are
placed at /usr/share/cclink.

If it is needed to rebuild the sources, the CCLINK IEF Basic sources can
be fetched directly to the EVM and compiled natively on target. Using
the source code at `Processor SDK CCLink
Source <http://git.ti.com/processor-sdk/cclink/trees/master>`__ as the
example:

-  CCLINK IEF Basic for Master

First change directory to the Linux build folder for master, i.e.,
CCIEF-BASIC\_Master/build/linux. Then, run "make" which generates
Master\_sample

-  CCLINK IEF Basic for Slave

First change directory to the Linux build folder for slave,
CCIEF-BASIC\_Slave/build/linux. Then, run "make" which generates
Slave\_sample

An alternative to rebuild CCLINK IEF Basic is cross-compilation on X86
using the Yocto recipe. In order to do that, please refer to
:ref:`Processor SDK Building The SDK <building-the-sdk-with-yocto>`
to set up the build environment, and
:ref:`Processor SDK Yocto Recipes <building-the-sdk-recipes>`
to bitbake the recipes and install the newly built packages for CCLINK
IEF Basic:

::

    MACHINE=am57xx-evm bitbake ccief-basic

After the bitbake commands above are successfully done, the newly built
ccief-basic binaries can found from the folder of
./build/arago-tmp-external-arm-toolchain/work/armv7ahf-neon-linux-gnueabi/ccief-basic/<ver\_number>/packages-split/ccief-basic/usr/bin.

|

|

.. rubric:: Run CCLink IEF Basic Sample Application
   :name: run-cclink-ief-basic-sample-application

The picture below shows the test setup for the CCLINK IEF basic master
and slave applications running on the supported TI platforms. For both
the master and the slave stations, connect the Ethernet ports to be
tested to a switch.

.. Image:: /images/Cclink_setup_pic.PNG

Please note that the jumper setting for AM335x ICE V2 EVM needs to be
set correctly based on the type of application demonstrated:

-  If running with EMAC, connect the jumper J18 and J19 for both boards
   into EMAC mode. Hence, connect pin1 and pin2.
-  If running with PRU\_ICSS, connect the jumper J18 and J19 for both
   boards into ICSS mode. Hence, connect pin2 and pin3.

| Location of these two jumpers J18 and J19 can be found from
  http://processors.wiki.ti.com/index.php/AM335x_Industrial_Communication_Engine_EVM_Rev2_1_HW_User_Guide#Component_Positions.

.. rubric:: Master Sample Application
   :name: master-sample-application

Before running the master sample application, first obtain the IP
address of the slave Ethernet port to be tested. Then, modify
/usr/share/cclink/MasterParameter.csv to update "Slave1 IP address"
using the IP address of the Slave station. After that, run the master
sample application: “Master\_sample
/usr/share/cclink/MasterParameter.csv”

The figure below shows the sample output from the console of the master
station.

.. Image:: ../images/Cclink_master_screeshot_linux.png

|

.. rubric:: Slave Sample Application
   :name: slave-sample-application

On the slave station, simply run the slave sample application:
“Slave\_sample /usr/share/cclink/SlaveParameter.csv”

The figure below shows the sample output from the console of the slave
station.

.. Image:: /images/Cclink_slave_screenshot_linux.png

|

|

.. rubric:: Compliance Testing
   :name: compliance-testing

Every CCLINK IEF Basic application when demonstrated on any platform has
to pass the conformance testing for various functionalities of IEF
Basic. The conformance test results are sent to CLPA for approval. Upon
approval from CLPA, the platform is accepted as CC-Link IEF Basic
complaint.

|

