.. http://processors.wiki.ti.com/index.php/LTP-DDT
.. rubric:: Document License
   :name: document-license

This work is licensed under the Creative Commons Attribution-Share Alike
3.0 United States License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/3.0/us/ or send a letter to
Creative Commons, 171 Second Street, Suite 300, San Francisco,
California, 94105, USA.

.. rubric:: LTP-DDT Overview
   :name: ltp-ddt-overview

LTP-DDT is a test application used by Texas Instruments to validate
Linux releases.

| It is based on `LTP <https://github.com/linux-test-project/ltp>`__.
| LTP validates many kernel areas, such as memory management, scheduler
  and system calls. LTP-DDT extends LTP's core Kernel tests with tests
  to validate Kernel drivers developed by Texas Instruments. LTP-DDT
  focuses on embedded device driver tests. It contains hundreds of tests
  that validate functionality and performance of device drivers. LTP-DDT
  also contains tests to validate System's use cases and overall
  System's stability.

LTP-DDT uses LTP's test infrastructure, such as:

-  Test execution drivers (PAN)
-  Top-level test scripts (i.e. runltp)
-  Same Folder Hierarchy and test case definition format

LTP-DDT test cases are LTP test cases and vice-versa.

The main additions or 'enhacements' of LTP-DDT compared to LTP are:

-  PLATFORM files. LTP-DDT uses PLATFORM files to identify platform
   hardware and software features.
-  OVERRIDE mechanism. Default test case parameters are automatically
   overridden based on PLATFORM features.
-  ATOMIC scripts. Code reuse is foster by writing scripts that
   implement small well-defined actions. Test scripts rely on these
   atomic scripts to execute their actions.
-  AUTOMATIC FILTERING. Test cases are filtered based on the test
   requirements and the PLATFORM features.
-  TESTCASE ANNOTATIONS. Test scenario files are annotated with
   following annotations @name, @desc, @requires and @setup\_requires.
   The @requires and @setup\_requires are used to select test cases at
   run time based on the PLATFORM features.
-  All LTP-DDT test cases and test code reside in <testcases-root>/ddt/
   and <testcode-root>/ddt/ folders respectively.

|

.. rubric:: LTP-DDT Highlights
   :name: ltp-ddt-highlights

-  Easy to use (automatically filter test cases not applicable for
   platform)
-  Easy to support new platforms (just define the platform file)
-  Test cases can be easily wrap or imported to Test Management Systems
   (Use of testcase annotations facilitates this)
-  High Code Reuse (atomic scripts and test scripts are reused and
   parameters are adjusted on the fly)

|

.. rubric:: Test Suites
   :name: test-suites

| LTP-DDT contains tests cases that uses other open source tools such as
  iperf, evtest, rt-tests (cyclictest), lmbench and others.
| Test suites currently available include among others:

-  alsa
-  cpu hotplug
-  crypto
-  timers
-  emmc
-  mmc/sd
-  ethernet
-  fbdev
-  gpio
-  gstreamer (multimedia)
-  hdmi
-  i2c
-  ipc
-  latency under different use cases (important for RT kernel)
-  lmbench
-  memory tests
-  mm (ltp's memory management)
-  msata
-  nand
-  nor
-  pci
-  pipes (ltp)
-  power management
-  programmable real-time unit (PRU)
-  pwm
-  qspi
-  realtime (ltp)
-  rng
-  rtc
-  sata
-  scheduler (ltp)
-  sgx (graphics)
-  smp
-  spi
-  syscalls (ltp)
-  system (use-cases, e.g. multiple tests running in parallel)
-  thermal
-  timers (ltp)
-  touchscreen
-  uart
-  usb host (multiple tests with different classes)
-  usb device
-  v4l2
-  vlan
-  dwt
-  wlan

|

.. rubric:: Device Under Tests Supported
   :name: device-under-tests-supported

Supported platforms with LTP-DDT
- can be found `here <https://git.ti.com/cgit/test-automation/ltp-ddt/tree/platforms>`__

|

.. rubric:: Host Platform Requirements
   :name: host-platform-requirements

Linux host is required :

-  for compiling LTP-DDT.
-  to host the NFS server to boot the EVM with NFS as root filesystem
-  to run host utilities - e.g.iperf

|

.. rubric:: Host Software Requirements
   :name: host-software-requirements

-  GCC Tool chain for ARM
-  Serial console terminal application
-  TFTP and NFS servers. NFS server is required only in case of NFS
   boot.
-  iperf utility on the host.

|

.. rubric:: Filesystem Requirements
   :name: filesystem-requirements

LTP-DDT relies on other open source test tools. The following test tools
must be available in the target filesystem to run ltp-ddt:

-  alsa utilities
-  evtest
-  hdparm
-  iperf
-  lmbench
-  rt-tests (cyclictest)

There is an Arago/OE recipe
`here <https://git.ti.com/cgit/arago-project/meta-arago/tree/meta-arago-distro/recipes-core/packagegroups/ti-world.bb>`__
that builds a filesystem image w/ the above tools plus:

-  bonnie++
-  iozone3
-  ltp-ddt

.. rubric:: Installation
   :name: installation-ltp-ddt

Clone the project

::

    git clone https://git.ti.com/git/test-automation/ltp-ddt.git

| Installation instructions are in the README-DDT file. Check sections
  6) and 7)
| There is also an Arago/OE recipe to build ltp-ddt
  `here <https://git.ti.com/cgit/arago-project/meta-arago/tree/meta-arago-test/recipes-devtools/ltp-ddt>`__

.. rubric:: Running Tests
   :name: running-tests

-  Run DDT tests the same way you run LTP tests. Use ltprun program and
   pass to

it the test scenario file in the runtest directory (option -f) to run
and the platform (option -P) to use. For example:

::

    ./runltp -P am180x-evm -f ddt/lmbench

| The platform name specified with -P option must exist in the
  platforms/ dir.
| It is also possible to run tests without -P option, in such case the
  ltprun script won't filter test cases and it is possible that tests
  cases not supported by the platform you are running on will be called.

-  In addition to selecting test scenarios using -f option, users can
   also

| filter test cases using -s PATTERN option. These option select test
  cases based on the test case TAG specified in the test scenario file.

-  The runltp script have lot of options. Some useful ones for stress
   tests are:

::

    -t DURATION: Define duration of the test in s,m,h,d.
    -x INSTANCES: Run multiple test instances in parallel.
    -c <options>: Run test under additional background CPU load
    -D <options>: Run test under additional background load on Secondary storage
    -m <options>: Run test under additional background load on Main memory
    -i <options>: Run test under additional background load on IO Bus
    -n          : Run test with network traffic in background.

Please refer to README-DDT file section 8) for more details.

-  Running NAND Sanity Tests

-- Run all NAND sanity tests

Using below command to run NAND sanity tests.

::

    ./runltp -P <platform> -s "NAND_S_" -S skiplist

If there are more than one flash filesystem supported, say, jffs2 and
ubifs and you don't run jffs2 test cases. You need create a file called
'skiplist' (this filename could be anything) and put to-be-skipped test
case tag in this file. Here is the content of skiplist to skip jffs2
test cases.

::

    @ cat skiplist
    _JFFS2

-- Run NAND performance test

::

    ./runltp -P <platform> -s "NAND_L_PERF" -S skiplist

|

.. rubric:: Join
   :name: join

| LTP-DDT is an open source project.
| The LTP-DDT sources are hosted here
  https://git.ti.com/git/test-automation/ltp-ddt.git
| Developers are encouraged to join the Arago mailing list at
  meta-arago@lists.yoctoproject.org
| Of course patches and comments are welcome, please send them to
  meta-arago@lists.yoctoproject.org mailing list.
| Developers are encouraged to read sections 3) and 4) in the README-DDT
  file before submitting patches.

