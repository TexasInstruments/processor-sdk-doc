.. _RTOS-SDK-Migration-Guide-label:

***************
Migration Guide
***************

Overview
========

This page covers migration information for applications built on top
of the Processor SDK RTOS.

Processor SDK 06.xx Releases
============================

Processor SDK 06.03
-------------------

Building PDK components from GIT repositories
=============================================

**Migration:** Change in git repository for PDK components.

**Impact Scope:** Applicable for most drivers packaged in the PDK when used in development environment

**Additional Details**:
Prior to this release, libraries/applications of drivers included in pdk (pdk_xx/packages/ti) had their own git respositories which could be cloned and used for development or picking up bugfixes which are not yet released through a processor sdk release.
From this release onwards, most of the drivers in the PDK are moved to the new pdk.git repository(https://git.ti.com/cgit/processor-sdk/pdk) and its components (drivers) moved in to their respective locations inside the pdk_<soc>_<ver> of the Processor SDK installation.
For example the i2c driver has been moved from https://git.ti.com/cgit/keystone-rtos/i2c-lld to https://git.ti.com/cgit/processor-sdk/pdk/tree/packages/ti/drv/i2c. Consequently, the latest updates on a PDK driver should be fetched from the new pdk.git repo (https://git.ti.com/cgit/processor-sdk/pdk) as the older repos are rendered obselete.

Building of libraries of individual PDK components
==================================================

**Migration:** Building individual drivers' librabries/apps of PDK from PDK's top level makefile is not supported

**Impact Scope:** Applicable for PDK top level makefile

**Additional Details**:
Prior to this release, libraries/applications of drivers included in pdk (pdk_xx/packages/ti) could be built from
the top level makefile (pdk_xx/packages/makefile) using commands like "make uart_lib/uart_apps". This is no longer supported.
Instead, the libraries and applications could either be built using "make all" from the top level makefile or issuing "make libs/apps" from within the module's directory.


Processor SDK 06.01
-------------------

NIMU
====

**Migration:** Udma init sequence call has been moved from NIMU library to NIMU example for AM65xx

**Impact Scope:** Applicable for all NIMU applications using NIMU tranport library for AM65xx

**Additional Details**:
Applications will need to implement the following function to provide UDMA drive handle which will be called by the NIMU driver at startup

 Udma_DrvHandle nimu_app_get_udma_handle(void)

Processor SDK 06.00
-------------------

PRUSS
^^^^^
**Migration:**
Calls that passed ``PRUICCSS_INSTANCE_MAX`` as a parameter to PRUSS driver API
calls will now pass ``PRUICCSS_INSTANCE_THREE`` instead.

**Impact Scope:**
Applicable for all AM65xx applications using PRUSS driver for ICSSG use case.

**Additional Details:**
The following new enumeration, ``PRUICCSS_INSTANCE_THREE``, for PRU-ICSS
instance 3 has been added to ``PRUICSS_MaxInstances`` enumeration list as
``PRUICCSS_INSTANCE_MAX`` is not longer valid when making PRUSS driver API
calls.

Board Library
^^^^^^^^^^^^^
**Migration:**
MMU configuration is needed to enable NBO CFG registers access on A53 core.

**Impact Scope:**
Applicable for all AM65xx RTOS applications calling ``Board_init()`` with
``BOARD_INIT_ICSS_ETH_PHY`` flag.

**Additional Details:**
Board library is setting ``NAVSS THREADMAP`` register to give higher priority
for MSMC access from ICSSG which requires access to ``NBO CFG`` registers.


Processor SDK 05.xx Releases
============================

Processor SDK 05.03
-------------------

EMAC
^^^^
**Migration-1:**
ICSS-G EMAC firmware binary directory location update for future extension.

**Impact Scope:**
Applicable for all applications using EMAC driver with ICSS-G dual EMAC
firmware.

**Additional Details:**
Applications will need to update the include path to location of firmware header
files for ICSSG use case:

- **Prevous location:** ``ti/drv/emac/firmeare/icss_eth/src/dm``

- **New location:** ``ti/drv/emac/firmware/icss_dualmac/bin``

**Migration-2:**
Release introduces support for additional firmware specific configuration
files. Added for future extension to support multiple firmwares using same EMAC
driver.

**Impact Scope:**
Applicable for all applications using EMAC driver with ICSS-G dual EMAC
firmware.

**Additional Details:**
Firmware configuration has been moved to firmware specific configuration files,
``emac_fw_config_dual_mac.h`` and ``emac_fw_config_dual_mac.c``. Previously the
firmware configuration was specified in the test application. It is not expected
that applicatons will need to modify these files as the are closely tied to the
firmware.

- **Previous location:** firmware specific configuration was specified in the
  text application (``ti/drv/emac/test/EmacLoopbackTest/test_utils_k3.c``)

- **New location:** ``ti/drv/emac/firmware/icss_dualmac/config/``

Applications will need to update their makefiles to include c source file
``emac_fw_config_dual_mac.c``.

At time of ``emac_open()`` API call, applications need to udpate configuruation
parameters to pass get firmware configuration pointer :

.. code-block:: c

   EMAC_HwAttrs_V5 emac_cfg;
   EMAC_socGetInitCfg(0, &emac_cfg);
   emac_cfg.portCfg[port_num].getFwCfg = &emacGetDualMacFwConfig;
   EMAC_socSetInitCfg(0, &emac_cfg);

CSL
^^^
**Migration:**
API changes on CSL-FL of AM65xx on ecc aggregator, vim, esm modules

**Impact Scope**:
Limited to the case if application is using the CSL-FL APIs

**Additional Details**:
The CSL-FL for ECC aggregator, ESM and VIM are modified to return API
functionality success/failures and additional arguments are added as and when
needed (especially during the cases where the return was the value instead of
API success/failure). Applications that use these CSL-FL calls are impacted and
are needed to align to new calling conventions. If applicable application
modification required to align to updated APIs, refer doxygen API documentation
for API details.


DSP- TI CGT Compiler
^^^^^^^^^^^^^^^^^^^^

**Migration:**
In DSP TI CGT compiler version 8.3.2 the rts library boot object file name is
changed from ``boot.obj`` to ``boot.c.obj``.

**Impact Scope:**
Limited only to DSP applications that explicitly uses rts library object files
in linker command file.

**Additional Details:**
The DSP application which is using linker command file of CSL module should
change boot object name from boot.obj file to ``boot.c.obj``. If the user is
using cpp version of boot object file then it should be mentioned as
``boot.cpp.obj``. In general it can be also be used as ``boot.*.obj``. This can
be referred from the following linker command file in the PDK package
``<PDK>/packages/ti/csl/example/lnk_dsp.cmd``

Processor SDK 05.02
-------------------

SBL
^^^
**Migration:**
Image integration and memory map changes.

**Additional Details:**
Release supports optimized boot times for booting MCU1_0 core from OSPI
flash. To reduce the size of the SBL,  the system firmware image, which was
earlier embedded in the SBL, is now a separate binary. The system firmware image
can be found at ``<PDK>/packages/ti/drv/sciclient/soc/V0/sysfw.bin``

For MMC/SD boot, if the steps followed in :ref:`Windows SD Card Creation Guide
<windows-sd-card-creation-guide>` or :ref:`Linux SD Card
Creation Guide <tools-create-sd-card-linux-label>` are
used, no additional steps are need. If the SD card is being created manually,
then the ``sysfw.bin`` file also needs to be copied into the root directory of
the MMC SD card, along with ``tiboot3.bin`` and ``app``.

For OSPI boot, the flash offsets have changed. ``sysfw.bin`` needs to be
programmed into OSPI flash at offset ``0x40000`` (new for this release), along
with ``sbl_ospi_img_mcu1_0_release.tiimage`` at offset ``0x0`` (no change from
previous release) and the ``app`` at offset ``0xA0000`` (was ``0x80000``
previous release).  For details please refer `Programming the OSPI flash
<http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/Board_EVM_Abstration.html#uniflash>`__

Applications that the SBL loads must co-exist with the SBL's memory usage.In the
application's linker command file, care must be taken to not use the first 0x100
bytes of MCU1_0's ATCM memory and SBL reserved memory from ``0x41C00100 to
0x41C28000``. If the applications violate the SBL memory usage, then apps that
were working with the last release might not work any more, as the memory
constraints are tighter. For details, refer the `SBL Memory Utilization
<http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/Foundational_Components.html#am655x-sbl-memory-usage>`__

PDK
^^^
**Migration:**
AM65xx PDK component dependency on sciclient module.

**Impact Scope:**
Applications will need to link to sciclient module library. No migration impact
if application is already linking the library.

**Additional Details**:
All application using PDK components on AM65xx platform will need to link
sciclient library  as components internally will be using sciclient API for PLL
and interrupt configuration. In this release, requirement for application will
be more mandated as more components are using common infrastructure.

DMSC firmware should be loaded onto Cortex-M4 core using SBL or :ref:`CCS GEL script
<advanced-am65x-debug-setup-with-dmsc-firmware-load>`
before calling the Board Init API with 'BOARD_INIT_PLL' flag.

Board
^^^^^
**Migration:**
New APIs for EEPROM Board ID Information

**Impact Scope:**
Applications using Board ID info APIs on AM65xx platform. No migration impact
for existing applications and boards using version 1 API.

**Additional Details**:
TI Board ID information format has been updated to new version on AM65xx. New
board library APIs ``Board_getIDInfo_v2()`` and ``Board_writeIDInfo_v2()`` are
added to support new Board ID information format. Old Board ID info APIs are
still avaialble to retain the backward build compatibility but returns error
when used on AM65xx platform.

FATFS
^^^^^
**Migration:**
FATFS module in this release includes multipartition support and capability of
detecting single vs multiple partitions run time.

**Impact Scope:**
Limited to the case if user had used MS-DOS Floppy disk format for formatting
the SD/eMMC memory. No impact if the SD/eMMC is formatted using the steps
provided by :ref:`Windows SD Card Creation Guide
<windows-sd-card-creation-guide>`/:ref:`Linux SD Card Creation
Guide <tools-create-sd-card-linux-label>`.

**Additional Details**:
Partition entry information may be wrongly detected for the storage media
formated to  MS-DOS Floppy disk format. FATFS APIs fail to access the disk in
this case.

**Workaround**:
Format the storage media using the steps provided by :ref:`Windows SD Card Creation
Guide <windows-sd-card-creation-guide>`/:ref:`Linux SD Card
Creation Guide <tools-create-sd-card-linux-label>`
in case this issue is observed.

Processor SDK 05.01
-------------------

Build
^^^^^
**Migration:**
Applicable for applications migrating from SOCs supporting EDMA LLD to AM65x
with updated DMA infrastructure. Additional UDMA driver support is available in
package to support enhanced DMA infrastrcuture for AM65x Drivers for AM65x SOC
is extended to support UDMA LLD abstracting changes needed by
application. Limited change will be required for application using drivers
included in Processor SDK.

**Additional Details**:
Modifications needed at application will be limited to initialization of UDMA
driver using Udma_init() API in addition to linking  UDMA driver library. Driver
Test code could be used as reference Additional migration details for all cases
are covered in ``/ti/drv/udma/docs`` folder inside PDK package.

DMA
^^^
**Migration:**
For all drivers using DMA mode EDMA driver is updated to UDMA driver.

**Additional Details:**
Application will need to initialize UDMA driver and SCIClient interface using
``Udma_init()`` and ``Sciclient_init()`` API. Test code could be used as
reference.

Networking
^^^^^^^^^^
**Migration:**
Applicable for applications using NDK and Posix port of SysBIOS.

**Additional Details:**
Release introduces NS (Network Services Component) as independent portable
networking API abstracting different network stacks. Detailed migration details
is available at `NDK 2.x to 3.x Migration Guide <NDK_Migration_Guide_>`__

Processor SDK 05.00
-------------------

Build
^^^^^
**Migration:**
``TOOLS_INSTALL_PATH`` macro value changed to ``SDK_INSTALL_PATH``. No migration
impact if tools and SDK are installed in same location.

**Additional Details:**
``TOOLS_INSTALL_PATH`` macro value is set to ``SDK_INSTALL_PATH`` by
default. For accessing the tools from a different path, modify
``TOOLS_INSTALL_PATH`` in ``packages/ti/build/Rules.make`` file or can be
overriden from the build console as shown below.

Windows

.. code:: console

       set TOOLS_INSTALL_PATH=<Path for the tools root folder>

Linux

.. code:: console

       TOOLS_INSTALL_PATH=<Path for the tools root folder>


Build Setup
^^^^^^^^^^^
**Migration:**
There is no migration need for components used within processor SDK. Application
Software outside processor SDK may require a change if there is a dependency to
internal Processor SDK environment variables. See more details below.

**Additional Details:**
Rules.make file is used instead of pdksetupenv to setup the build environment
variables. Components inside processor SDK are updated to align with this
change. Any applications making use of pdksetupenv from processor SDK to setup
the build environment variables should include below line in the application
makefile.

.. code-block:: c

  include $(RULES_MAKE)

Processor SDK 04.xx Releases
============================

Processor SDK 04.03
-------------------

OSAL
^^^^
**Migration:**
No impact expected if Semaphore allocation and HwIP registration from OSAL is
not invoked by application.

**Additional Details:**
OSAL module is fine tuned for optimized number of semaphores required internally
within drivers. Module provides additional API to application for additional
semaphore allocation if required.Application can configure for either default
internal static allocation or it can select external memory block that can be
provided to create these objects. Note that this decision to go with external
memory block or internal memory block need to be done during init configuration
of application (near to main) just after ``Board_init()`` is called. Below
sample code sets SemaphoreP/HwiP to be used from external memory block:

.. code-block:: c

   /* Get the Hw Attrs */
   osal_ret = Osal_getHwAttrs(&hwAttrs);
   if (osal_ret != osal_OK)
   {
       return (false);
   }

   /* This API should set to use external memory block */
   hwAttrs.extSemaphorePBlock.base = (uintptr_t) &semPMemBlock[0];
   hwAttrs.extSemaphorePBlock.size = SEMP_BLOCK_SIZE;
   hwAttrs.extHwiPBlock.size       = HWIP_BLOCK_SIZE;
   hwAttrs.extHwiPBlock.base       = (uintptr_t) &hwiPMemBlock[0];
   osal_ret = Osal_setHwAttrs(ctrlBitMap, &hwAttrs);


Board
^^^^^
**Migration:**
Section details applicable only to applications based on DRA7xx SoCs.

**Additional Details**:
DRA7xx board libraries have refactored pad configuration sequence by removing
manual pinmux entries and replacing them with a full IODELAY reconfiguration
procedure. This was done in order to simplify transition from a standalone
application development in CCS to booting the whole device via SBL, ensuring
that pad configuration is 100% consistent between the two application loading
methods.

The IODELAY and pin control data structures are maintained in each of evmDRA72x
and evmDRA75x board library source directories. These structures are also
included in the SBL compilation and used in the SBL's IODELAY
reconfiguration. Therefore, changes can be made in one location but reused by
both Board and SBL components just through recompilation.

Note that DRA78x does not require IODELAY reconfiguration and pinmux setup is
always contained entirely in the application. Hence, there are no corresponding
changes to this library.

All of this is done in a transparent manner, so there is **no API change** and
will not affect existing applications. However, there are considerations with
respect to memory placement and potential conflicts between the board library
and SBL code. These restrictions have always existed but are now more clearly
defined and documented. Please refer to :ref:`Board Support
<board-board-support>` for more details.

I2C
^^^
**Migration:**
No migration required for existing user application.

**Additional Details:**
PRUICSS based I2C Firmware have been introduced in this release. This new
features increases the number of I2C interface available in the SOC. I2C LLD now
depends on PRUSS LLD for compilation of this new feature. All of this is done in
a transparent manner, so there is **no API change** and will not affect existing
applications. However, for using the I2C FW feature refer :ref:`I2C FW
<PRU-ICSS-I2C-FIRMWARE-label>` for additional details.

Processor SDK 04.02
-------------------

GCC Toolchain Migration to 6-2017-q1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Migration:**
Limited to TI-RTOS based application on ARM Cortex-A cores.

**Additional Details:**
Processor SDK RTOS components includes updates to be compatible with GCC tool
chain. This includes updates to SysBIOS, compiler and linker options. Following
migration changes required for applications:

- Compiler options: Add nano libs to Include path

  - Example:
    ``gcc-arm-none-eabi-6-2017-q1-update/arm-none-eabi/include/newlib-nano``

- Linker Options: Replace fpu lib paths with hard lib and enable nano specs

  - Example: ``"<SYS/BIOS Root>/packages/gnu/targets/arm/libs/install-native/arm-none-eabi/lib/fpu"``
     with ``"<SYS/BIOS
     Root>/packages/gnu/targets/arm/libs/install-native/arm-none-eabi/lib/hard --specs=nano.specs”``

**Additional References:**

- PDK Project Creation Scipt:
  ``<pdk_soc_x_x_x/packages/pdkProjectCreate.[bat/sh]>``

**Note:** For baremetal applications, stack section needs to be aligned to 8
bytes. Updated GCC toolchain is more stringent on memory alignment requirement.
Misalignment can result in unexpected run time failures.

EMAC Library
^^^^^^^^^^^^
**Migration:**
Limited to C6657, OMAPL137/C6747 and OMAPL138/C6748 SoCs.

**Additional Details:**
Interrupt setup and ISR functions are implemented in the driver. Interrupt
handling in applications need to be removed to use the latest driver
version. Use ``EMAC_socGetInitCfg()`` and ``EMAC_socSetInitCfg()`` functions to
change the default interrupt mapping in HW attributes if required.

Example:

.. code-block:: c

   EMAC_HwAttrs_V0             emac_hwattr;  /* Local instance for HW attributes */
   EMAC_OPEN_CONFIG_INFO_T     open_cfg;

   EMAC_socGetInitCfg(port_num, &emac_hwattr);  /* Get default SOC HW attributes */
   emac_hwattr.txIntrNum = <Int Num>  /* Change default interrupt mapping Optional: if needed */
   EMAC_socSetInitCfg(port_num, &emac_hwattr); /* Change the default HW attributes */
   open_cfg.hwAttrs = &emac_hwattr;  /* Assign HW attributes to configuration parameters */
   emac_open(port_num, &open_cfg);


Processor SDK 04.01
-------------------

Common CSL Library
^^^^^^^^^^^^^^^^^^
**Migration:**
Limited to Bare metal Application and Keystone SoCs such as K2HK/K2LE/K2G. No
change required for other SoCs such as AM571x/AM572x/C6678/C6657.

**Additional Details:**
Default start address for the vectors modified to beginning of MSMCSRAM
(``0x0C000000``) compared to previous release end of the MSMC. This matches to
both secured and non secured devices Application is required to reserve
(``0x0C000000 to 0x0C000040``) size 0x40 bytes.

Bare metal Application needs to reserve this location for vectors when using CSL
startup library. There is still option for overriding default configuration by
defining ``vector_base`` to desired start address: Example: if the vector
location desired is say ``0xC0E0000``, then add below line in the application's
linker command file:

.. code-block:: c

   __vector_base__= 0xC0E0000;

No change needed for application using default configuration matching CSL.

ICSS_EMAC Library
^^^^^^^^^^^^^^^^^
**Migration:**
*Optional. No migration required for applications using default icss_dualemac
and icss_switch firmware.*

The location of ``icss_emacFwConfig.c/.h`` has moved from
``ti/drv/icss_emac/firmware/<SOC_TYPE>`` directory to
``ti/drv/icss_emac/firmware/icss_dualemac/config/`` directory. If applications
are compiled with ``icss_emacFwConfig.c``, please update your build/make
infrastructure.

Processor SDK 04.00
-------------------
MCSDK 1.1 to Processor SDK Migration for OMAPL13x/C674x devices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This release includes additional support for OMAPL13x/C674x
architecture/SOCs. For more information on migrating aplications from
MCSDK(OMAPL13x) to Processor SDK, see `this migration page
<MCSDK_Migration_for_OMAPL13x_>`__.

ICSS_EMAC Library
^^^^^^^^^^^^^^^^^
**Migration:**
*Required. Application will need to link to firmware binaries.*

ICSS EMAC driver component includes source code support for Dual-emac firmware
with support for rebuilding. Firmware is no longer supported as header format
*.h in order to align to PRUSS compiler.

- In order to include new binary application will need to link the PRUSS
  firmware binary as demonstrated through ``*project.txt``. **Note: firmware
  binary to be linked will be dependent on the SOC as shown below**

**Example:**
*AM572x have support for both version so include both version of
binaries and linker \*.cmd files.*

.. code-block:: c

   ${PDK_INSTALL_PATH}/ti/drv/icss_emac/firmware/icss_dualemac/bin/<SOC>/<HOSTCORE>/<REVISION>/icss_dualemac_PRU0.bin
   ${PDK_INSTALL_PATH}/ti/drv/icss_emac/firmware/icss_dualemac/bin/<SOC>/<HOSTCORE>/<REVISION>/icss_dualemac_PRU1.bin

- Default linker command file is available in PDK software which can be linked
  by application based on cores where application is running. For A8, A9, A15
  cores below linker command can be linked in makefile or CCS project. Refer the
  ICSS-EMAC Unittest for additional details.

.. code-block:: c

   -Wl,-T,${PDK_INSTALL_PATH}/ti/build/pruss/lnk_a8_a9_a15_<REVISION>.cmd

- For c66 and m4 cores

.. code-block:: c

   -Wl,-T,${PDK_INSTALL_PATH}/ti/build/pruss/lnk_c66_m4_<REVISION>.cmd

Board Library
^^^^^^^^^^^^^
**Migration:**
*Optional. No migration impact in case of applications using custom board
library which is not following similar approach as default board library for
Ethernet PHY configurations.*

Updated Board library for OMAPL137 in this release includes additional Ethernet
PHY initialization support for reference EVM during init and hence requiring
dependency on I2C LLD. This is applicable to applications using default OMAPL137
board library similar to other PDK/Processor SDK applications in the
release. For all those cases linking to additional I2C LLD library will be
required.

Examples for including I2C LLD library for:

- Baremetal Applications

Include the I2C LLD library from below mentioned path in makefile or linker
command file:

- **ARM Core** -
  ``<PDK_INSTALL_DIR>/packages/ti/drv/i2c/lib/omapl137/arm9/release/ti.drv.i2c.ae9``
- **DSP Core** -
  ``<PDK_INSTALL_DIR>/packages/ti/drv/i2c/lib/omapl137/c674/release/ti.drv.i2c.ae674``

- SYS/BIOS RTOS Applications

Include the I2C LLD library in SYS/BIOS config file using xdc load package
module:

.. code-block:: c

   var devType = "omapl137"
   var I2c     = xdc.loadPackage('ti.drv.i2c');
   I2c.Settings.socType = devType;

McASP Library
^^^^^^^^^^^^^
**Migration:**
*Optional. No migration impact for applications initializing the structure using
memset and default configuration: ``Mcasp_WordBitsSelect_LSB()``.*

McASP driver includes additional configuration field in
``Mcasp_ChanParams->wordBitsSelect`` to enable newly introduced mode
Mcasp_WordBitsSelect_MSB. Configuration needs to be initialized by application.

Processor SDK 03.xx Releases
============================

Processor SDK 03.03
-------------------

Processor SDK 03.02
-------------------

PDK I2C LLD
^^^^^^^^^^^
To support I2C slave mode, added ``I2C_transactionInit()`` API. Applications
need to call ``I2C_transactionInit()`` API before calling ``I2C_transfer()``
API.

**Example:**

.. code-block:: c

   I2C_Transaction   transaction;
   I2C_transactionInit(&transaction);
   transaction.masterMode   = false;
   transaction.writeCount = wrLen;
   transaction.readCount  = rdLen;
   transaction.timeout    = timeout;
   I2C_transfer(i2c, &transaction);

PDK MCASP LLD
^^^^^^^^^^^^^
The call back function's behavior has changed. The MCASP driver no longer
modifies the ``cArg`` parameter of the registered call back function to indicate
the transaction type(TX or RX). The cArg paramter will be unchanged and passed
back to the application. Please refer to the examples, which have been updated
to reflect this change.

PDK MMCSD LLD
^^^^^^^^^^^^^
No update required for use of default SOC dependent library.This is applicable
for applications which choose to include the ``soc/MMCSDDMA_soc.c``. The
``soc/MMCSDDMA_soc.c`` file has now been removed as a part of combining the DMA
and Non-DMA source code of the MMCSD library. Applications may include
``soc/MMCSD_soc.c`` file instead.

PDK USB LLD
^^^^^^^^^^^
- Cache is now supported. Buffers that are passed to low level USB bulk API's
  need to be cache-size aligned. These include buffers passed to:
  ``USBHMSCBlockWrite()``, ``USBHMSCBlockRead()``, ``USBHostRead()``,
  ``USBHostWrite()``, or ``usbSetupEpReq()``, etc.

- DMA is enabled by default on AM335x. Remove DMA_MODE flag in
  ``build/makefile.mk`` to go back to FIFO mode.

PDK ICSS EMAC LLD
^^^^^^^^^^^^^^^^^
Support has been added to all allow the icss-emac LLD to be configured with
custom firmware memory map parameters which fall into the following 2
categories:

- *Static configuration*: Tied directly to the firmware. For example, location and
  size of statistics, port status and conrol address offsets.

- *Dynamic configuration*: Tuneable parameters based on application. For
  example, sizes of TX/RX queues, port specific buffer/buffer descriptor
  offsets.

A complete list of these parameters can be found in
``ti/drv/icss_emac/icss_emacDrv.h``. Refer to ``ICSS_EmacFwStaticMmap`` and
``ICSS_EmacFwDynamicMmap`` structures.

Firmare binaries which reside in ``ti/drv/icss_emac/firmware/<SOC>`` directory
should be accompanied by a ``icss_emacFwConfig.c`` file. For existing firmware
binaries in this release, there is an equivelent ``icss_emacFwConfig.c`` file
already present. This file basically defines the 2 stuctures mentioned
above. This file needs to be compiled in as part of the user application. User
application can then use the following 2 newly introduced API's to "get" and
"set" firmware memory map configuration parameters with the LLD and firmware.

- ``icss_emacGetFwMMapInitConfig()``: Allows for retrieval of default firmware
  memory map configuration. User application may call this if they wish to
  update dynamic firmware memory map configuration paremeters. Static
  configuration parameters MUST not be updated.

- ``icss_emacSetFwMMapInitConfig()``: Allows for static and dynamic firmware
  memory map configuration parameters to be configured into the the LLD and
  firmware.

Note that these API's need to be called prior to calling ``ICSS_EmacInit()``
which is LLD's initialization function.

Backward compatibility is also supported. If user application does not wish to
update any configuration parameters, LLD will operate of default configuration
parameters as specified in respective ``icss_emacFwConfig.c`` file which is
being delivered as part of this release.

TI-RTOS
^^^^^^^
The updated version of TI-RTOS (SYS/BIOS) includes a check to ensure the proper
run-time library is linked. If you face a compilation issue, see `this note on
RTOS FAQ <SYSBIOS_reentsupport_error_faq_>`__ for more information.

Processor SDK 03.01
-------------------
PDK CSL
^^^^^^^
- ``csl_a15init`` module is renamed to ``csl_init`` to support portability. The
  impact of this change is limited to bare metal application using PDK makefile
  infrastructure. As part of migration, the module name need to be updated.

- ``csl_a15Aux.h`` is removed as it is duplicate of ``csl_a15.h``. The impact of
  this change is limited to applications that include ``csl_a15Aux.h``. As part
  of migration, the modification required is to include ``csl_a15.h`` instead.

PDK SA LLD (K2x, C66x)
^^^^^^^^^^^^^^^^^^^^^^
Added a feature to select Air Cipher Engine over the default Encryption engine
for algorithms such as AES_CTR part of ``Sa_DataModeConfigParams_t`` API. There
is no migration impact if application is initializing the structure to zero
using memset.

Processor SDK 03.00
-------------------
This release is a maintenance update with new features and bug fixes. The major
number in the version changed to stay aligned with the Linux package that moved
to 2016 LTS.

Device Drivers
^^^^^^^^^^^^^^
- Locations of precompiled libraries have moved for the following PDK
  components: ``CSL, PDK Examples, GPIO, GPMC, I2C, ICSS-EMAC, McASP, McSPI,
  MMC-SD, PCIe, PRUSS, QSPI, UART, USB, VPS, PDK Utils, FATFS, BOARD, OSAL,
  NIMU, NIMU_ICSS``. The overall change is to rename armv7 to a15/a8/a9 as
  appropriate for the device. All cores have moved the libraries compiled with
  optimization to ``release``, while a debug folder is available (but not
  prebuilt) for libraries with ``-g``.

  - No changes are needed for applications configured with a XDC/BIOS *.cfg with
    dependancies specified through xdc.useModule or xdc.loadPackage because
    updated library paths are autogenerated.

  - For other applications which explicitly set libraries and/or library include
    paths via ``-l, -I, or -L`` flags passed to the linker, the library paths
    need to be updated. For example, for GPIO on A15, the path changes from
    ``ti/drv/gpio/lib/am572x/armv7`` to ``ti/drv/gpio/lib/am572x/a15/release``.

- The drivers GPIO, I2C, SPI and UART now use CSL-FL. Applications using these
  drivers need to add include and library dependencies by adding xdc.useModule
  for CSL-FL for XDC/BIOS based applications, or by adding ``-I/-l/-L`` paths to
  the compilation/linker flags for the application. For XDC, here is a sample
  code for adding CSL-FL:

.. code-block:: javscript

   /*use CSL package*/
   var socType = "am571x";
   var Csl     = xdc.loadPackage('ti.csl');

   Csl.Settings.deviceType = socType;

- The driver I2C has an API change for I2C_transfer, a new timeout field is
  added to ``I2C_Transaction`` structure, and the return value type of this API
  is changed from ``bool`` to ``int16_t``. In the test/example application,
  timeout value need to be initialized before calling this API:

**Example:**

.. code-block:: c

   int16_t status;

   i2cTransaction.slaveAddress = I2C_EEPROM_ADDR;
   i2cTransaction.writeBuf = (uint8_t *)&txBuf[0];
   i2cTransaction.writeCount = I2C_EEPROM_TEST_LENGTH + I2C_EEPROM_ADDR_SIZE;
   i2cTransaction.readBuf = NULL;
   i2cTransaction.readCount = 0;
   i2cTransaction.timeout   = I2C_TRANSACTION_TIMEOUT;

   status = I2C_transfer(handle, &i2cTransaction);

Processor SDK 02.xx Releases
============================

Processor SDK 02.00.02
----------------------
This release primarily adds support for K2G device. There is no migration impact
to customers using devices supported in the previous release (AM3, AM4, AM5,
C665x, C667x, K2E, K2H, K2K, K2L).

Processor SDK 02.00.01
----------------------
This release primarily adds support for devices from the KeyStone architecture:
C665x, C557x, K2E, K2H, K2K, and K2L. There is no migration impact to customers
using devices supported in the previous release (AM3, AM4, AM5).

For information on migrating from BIOS-MCSDK (C66x) or MCSDK (K2x) to Processor
SDK, see `this migration page <MCSDK_Migration_Guide_>`__.

Processor SDK 02.00.00
----------------------
**This is the initial Processor SDK RTOS release from Texas Instruments unifying
platform software across multiple SOC's.**

The strategy for forward/backwards compatibility is as follows:

- `Device Drivers <Device_Drivers_>`__

  - All new development efforts should use Device Drivers because:

    - Device Drivers will maintain common APIs for all supported SoCs
    - Customer applications can be easily ported to new and additional SoCs
      hence providing scalable software platform
    - All new features and development will occur only in the Device Drivers.

- StarterWare is included for AM335x and AM437x for backwards compatibility with
  Industrial SDK 02.01.00.01

  - This will be maintenance only (bugs will be fixed, no new features)

For applications that already depend on StarterWare from Industrial SDK
02.01.00.01 on AM335x/AM437x, those APIs remain in Processor SDK in:

- **AM335x SOC:** ``pdk_am335x_1_0_0/ti/starterware``
- **AM437x SOC:** ``pdk_am437x_1_0_0/ti/starterware``

.. _Linux_SD_Card_Creation: http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index_overview.html?highlight=bootable#tools-create-sd-card-linux-label
.. _Windows_SD_Card_Creation: http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index_overview.html?highlight=bootable#windows-sd-card-creation-guide
.. _NDK_Migration_Guide: http://software-dl.ti.com/targetcontent/ndk/3_40_01_01/exports/ndk_3_40_01_01/docs/ndk/NDK_2_to_3_Migration_Guide.html
.. _Device_Drivers: http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index.html#Device_Drivers
.. _MCSDK_Migration_Guide: http://software-dl.ti.com/processor-sdk-linux/esd/docs/04_03_00_05/linux/Release_Specific.html#mcsdk-to-processor-sdk-migration-guide
.. _MCSDK_Migration_for_OMAPL13x: http://software-dl.ti.com/processor-sdk-linux/esd/docs/04_03_00_05/linux/Release_Specific.html#mcsdk1-1-to-processor-sdk-linux-migration-guide-for-omapl13x-devices
.. _SYSBIOS_reentsupport_error_faq: http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/FAQ.html#Why_do_I_get_a_.22undefined_reference_to_.60ti_sysbios_rts_gnu_ReentSupport_checkIfCorrectLibrary.27.22_error_when_compiling_my_application.3F
