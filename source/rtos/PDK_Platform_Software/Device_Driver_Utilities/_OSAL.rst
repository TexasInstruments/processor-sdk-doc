.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_OSAL

Overview
--------

Introduction
^^^^^^^^^^^^

The OSAL library provides operating system abstraction layer API sample
implementations that are required for processor SDK drivers. Scope of
APIs supported in the module is limited to support OS services required
for RTOS or bare metal drivers

-  Supported Operating Systems

   -  TIRTOS
   -  NONOS

-  Supported SOCs

   -  Please refer to component release notes

Operating System Extension
--------------------------

APIs
^^^^

Porting of OSAL component will enable extending PDK components to
additional OS environment. Reference top level API header file
includes:

::

    #include <ti/osal/osal.h>

Application Integration Details
-------------------------------

**Baremetal or No-OS Use case**

Reference library path to be included in application build environment:

::

     <ti/osal/lib/nonos/[soc]/[[cpu]/>


**SysBIOS based application**

Any RTSC application that needs to use osal library, should have below
RTSC configuration lines before any other processor sdk components
(e.g., board, gpio, uart etc).

::


     /* set the operating system type,
      * supported types are "tirtos" and "nonos"
      */
     var osType           = "tirtos";

     /* set the soc type
      * (applicable only when osTYpe
      *  is "nonos" only)
     */
     var socType           = "am572x";

     /* Setup the OSAL Library */
     var Osal = xdc.loadPackage('ti.osal');
     Osal.Settings.osType  = osType;
     Osal.Settings.socType = socType;



|

Application
------------

Examples
^^^^^^^^

.. rubric:: Sysbios Example
   :name: sysbios-example

This sysbios example OSAL_BasicExample_<board>_<coretype>TestProject
tests Hwi, Timer, Delay, Semaphores etc and prints output on UART
console.

.. rubric:: Introduction
   :name: introduction

This sysbios based example tests Hwi, Timer, Semaphores etc.

.. rubric:: Supported platforms
   :name: supported-platforms

::

    evmAM335x
    evmAM437x
    idkAM571x
    idkAM574x
    evmAM572x
    evmK2G
    evmK2H
    evmOMAPL137
    lcdkOMAPL138
    am65xx_evm
    am65xx_idk
    j721e_evm

.. rubric:: Build instructions
   :name: build-instructions

::

    Run pdkProjectCreate to create the OSAL_BasicExample_<evm>_<device>TestProject
    Load the project on to CCS and build the same.
    Build the example
    Load the OSAL_BasicExample_<evm>_<device>TestProject
    Run the example

.. rubric:: Testing the example
   :name: testing-the-example

The output for each of the tests (Hwi, Timer, Delay, Semaphores etc) can
be seen on the UART console. After a successful run, "All tests have
PASSED" will be displayed on the screen.

.. rubric:: Baremetal Example
   :name: baremetal-example

.. rubric:: Introduction
   :name: introduction-1

This baremetal example 'osal_baremetal_test' tests Hwi, Timer,
Semaphores etc and prints output on UART console.

.. rubric:: Supported platforms
   :name: supported-platforms-1

::

    evmAM572x
    evmAM335x
    evmAM437x
    evmDRA72x
    evmDRA75x
    evmDRA78x
    iceK2G
    idkAM574x
    idkAM572x
    idkAM571x
    idkAM437x
    am65xx_evm
    am65xx_idk
    j721e_evm

.. rubric:: Build instructions
   :name: build-instructions-1

OSAL tests are built using makefiles. The below steps are used to build
the baremetal test binaries.

::

    cd pdk_<ver>/packages/
    Run pdksetupenv.bat
    Run "make osal"
    Find the executable at ti/<pdk>/packages/ti/binary/osal_baremetal_test/bin
    Load the executable on the board
    Before running the executable, please make sure you have the UART connected and notice the test output on the UART console. Osal prints out the results there.

.. rubric:: Testing the example
   :name: testing-the-example-1

The output for each of the tests (Hwi, Timer, Delay, Semaphores, etc)
can be seen on the UART console. After a successful run, "All tests have
passed" will be displayed on the screen.

.. rubric:: Output
   :name: output

The output of osal example looks like below. The below sample output is
from idkAM571x on the UART console.

::

    HWI tests have passed.
    TimerTestLog: got 100 ticks from timer id = 1
    TimerTestLog: got 100 ticks from timer id = 2

::

    Timer tests have passed.

::

    Running Osal_Delay test:..........

::

    Osal_Delay tests have passed.

::

    Clock tests have passed.

::

    Semaphore tests have passed.

::

    Semaphore Statistics:
    PeakSemObjs = 5,
    numMaxSemObjs = 100,
    numFreeSemObjs = 97

::

    Hwi Statistics:
    PeakHwiObjs = 3,
    numMaxHwiObjs = 100,
    numFreeHwiObjs = 98

::

    Timer Statistics:
    PeakTimerObjs = 2,
    numMaxTimerObjs = 100,
    numFreeTimerObjs = 99

::

    All tests have passed.


Additional References
---------------------

+---------------------------------------------------------------------------------------------------+
|                    **Operating System Abstraction Layer Library Summary**                         |
+---------------------+-----------------------------------------------------------------------------+
| **Component Type**  |                               **Library**                                   |
+---------------------+-----------------------------------------------------------------------------+
| Install Package     | PDK                                                                         |
+---------------------+-----------------------------------------------------------------------------+
| Install Directory   | pdk_AMX_<version>\\packages\\ti\\osal                                       |
+---------------------+-----------------------------------------------------------------------------+
| Project Type        | `Eclipse RTSC`_                                                             |
+---------------------+-----------------------------------------------------------------------------+
| Endian Support      | Little                                                                      |
+---------------------+-----------------------------------------------------------------------------+
| Linker Path         | $(TI_PDK_INSTALL_DIR)\\packages\\ti\\osal                                   |
+---------------------+-----------------------------------------------------------------------------+
| Linker Sections     | .vecs , .switch, .args, .cio                                                |
+---------------------+-----------------------------------------------------------------------------+
| Include Paths       | $(TI_PDK_INSTALL_DIR)\\packages\\ti\\osal                                   |
+---------------------+-----------------------------------------------------------------------------+
| Reference Guides    | $(TI_PDK_INSTALL_DIR)\\packages\\ti\\osal\\docs\\doxygen\\html\\index.html  |
+---------------------+-----------------------------------------------------------------------------+
| Release Notes       | $(TI_PDK_INSTALL_DIR)\\packages\\ti\\osal\\docs\\ReleaseNotes_OSAL.pdf      |
+---------------------+-----------------------------------------------------------------------------+

.. _Eclipse RTSC: http://www.eclipse.org/rtsc/

|

