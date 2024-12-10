.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_CSL

|

.. rubric:: Overview
   :name: overview-1

The Chip Support Library constitutes a set of well-defined APIs that
abstract low-level details of the underlying SoC device so that a user
can configure, control (start/stop, etc.) and have read/write access to
peripherals without having to worry about register bit-field details.
The CSL services are implemented as distinct modules that correspond
with the underlying SoC device modules themselves. By design, CSL APIs
follow a consistent style, uniformly across Processor Instruction Set
Architecture and are independent of the OS. This helps in improving
portability of code written using the CSL.

CSL is realized as twin-layer – a basic register-layer and a more
abstracted functional-layer. The lower register layer comprises of a
very basic set of macros and type definitions. The upper functional
layer comprises of “C” functions that provide an increased degree of
abstraction, but intended to provide “directed” control of underlying
hardware.

It is important to note that CSL does not manage data-movement over
underlying h/w devices. Such functionality is considered a prerogative
of a device-driver and serious effort is made to not blur the boundary
between device-driver and CSL services in this regard.

CSL does not model the device state machine. However, should there exist
a mandatory (hardware dictated) sequence (possibly atomically executed)
of register reads/writes to setup the device in chosen “operating modes”
as per the device data sheet, then CSL does indeed support services for
such operations.

The CSL services are decomposed into modules, each following the
twin-layer of abstraction described above. The APIs of each such module
are completely orthogonal (one module’s API does not internally call API
of another module) and do not allocate memory dynamically from within.
This is key to keeping CSL scalable to fit the specific usage scenarios
and ease the effort to ROM a CSL based application.

In general for application recommended interfaces to be used will be
driver API. CSL Functional layer APIs could be used for low-level access
when required. CSL Register layer memory map is available for being used
under rare cases in application when required.

The source code of the CSL is located under $(TI_PDK_INSTALL_DIR)\\packages\\ti\\csl directory.


.. rubric:: AM335x/AM437x
   :name: am335xam437x

The CSL component of AM335x/AM437x Processor SDK is referred as
StarterWare in the legacy baseline releases.To maintain backward
compatibility for existing applications on AM335x/AM437x SOCs,
StarterWare low level package is retained. Customers are recommended
to use driver interfaces for ease of migration of application software
across SOCs.


+-----------------------+------------------------------------------------------+
|                       Chip Support Library/DAL Summary                       |
+=======================+======================================================+
|   **Component Type**  |   **Library**                                        |
|                       |                                                      |
+-----------------------+------------------------------------------------------+
|   Install Package     |   PDK                                                |
|                       |                                                      |
+-----------------------+------------------------------------------------------+
|   Install Directory   |   pdk_AMX_<version>\\packages\\ti\\starterware       |
|                       |                                                      |
+-----------------------+------------------------------------------------------+
|   Endian Support      |   Little                                             |
|                       |                                                      |
+-----------------------+------------------------------------------------------+
|   Linker Path         |   PDK_INSTALL_DIR\\packages\\ti\\starterware\\binary |
|                       |                                                      |
+-----------------------+------------------------------------------------------+
|   Include Paths       |   PDK_INSTALL_DIR\\packages\\ti\\starterware\\include|
|                       |                                                      |
+-----------------------+------------------------------------------------------+


AM57x/K2x/C66x/C674x
---------------------

Application Integration
^^^^^^^^^^^^^^^^^^^^^^^^^

CSL is common package supporting multiple devices.Software layer using
CSL source would need to pass compile time define -DSOC_XXX. Refer
ti\csl\soc.h for list of devices/SOC's

Refer list of APIs/interfaces available under <PDK_INSTALL_DIR\\packages\\ti\\csl> directory.


+--------------------------+----------------------------------------+
|                   Chip Support Library Summary                    |
+==========================+========================================+
|   Component Type         |   Library                              |
|                          |                                        |
+--------------------------+----------------------------------------+
|   Install Package        |   PDK                                  |
|                          |                                        |
+--------------------------+----------------------------------------+
|   Install Directory      |   PDK_INSTALL_DIR\\packages\\ti\\csl   |
|                          |                                        |
+--------------------------+----------------------------------------+
|   Endian Support         |   Little                               |
|                          |                                        |
+--------------------------+----------------------------------------+
|   Linker Path            |   PDK_INSTALL_DIR\\packages\\ti\\csl   |
|                          |                                        |
+--------------------------+----------------------------------------+
|   Include Paths          |   $(TI_PDK_INSTALL_DIR)\\packages\\    |
|                          |                                        |
+--------------------------+----------------------------------------+
|   Reference Guides       |   See docs under Install Directory     |
|                          |                                        |
+--------------------------+----------------------------------------+


CSL-FL EXAMPLES
-----------------

These are example projects to test the functionality of API in CSL-FL
layers. The following is the list of CSL-FL test examples which are
supported with the CSL library:

-  DCAN
-  EDMA
-  GPIO
-  MAILBOX
-  I2C
-  QSPI
-  WDTIMER (WWDT)
-  MMCSD
-  MMU
-  SPINLOCK
-  UART
-  ECC : Limited to applicable SOC's/Boards:idkAM574x
-  GPMC : Limited to a15 core on idkAM572 and evmAM572x
-  ePWM : Duty Cycle example application - Limited to applicable SoC's/Boards: am65xx_evm, j721e_evm

In order build the projects:

-  Navigate to pdk_[soc]_[version]\\packages
-  Run pdksetupenv.bat (windows) OR pdksetupenv.sh (linux).
-  Navigate to pdk_[soc]_[version]\\packages\\ti\\csl

All CSL-FL examples can be cleaned and rebuilt with the following
commands on windows:

::

    C:\ti\pdk_[soc]_[version]\packages\ti\csl>gmake app_clean
    C:\ti\pdk_[soc]_[version]\packages\ti\csl>gmake apps

All CSL-FL examples can be cleaned and rebuilt with the following
commands on linux:

::

    ~/ti/pdk_[soc]_[version]/packages/ti/csl$ make app_clean
    ~/ti/pdk_[soc]_[version]/packages/ti/csl$ make apps

-  All the output binary files will be generated in common location i.e.
   pdk_[soc]_[version]\\packages\\ti\\binary\\[EXAMPLE]\\bin\\[BOARD]\\

-  DCAN RTOS example

TI RTOS support is available for CSL DCAN example on AM572x platform.
Refer to the readme document at below path for more details.

<PDK Root>/packages/ti/csl/example/dcan/dcanLoopback

|

