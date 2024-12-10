.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_FATFS

Overview
--------

Introduction
^^^^^^^^^^^^

FATFS module provides an interface to configure a driver for FAT file
system compatible device that connects via MMCSD, USB, etc. It
configures FATFS for disk operations driver disk Initialize, disk
read, disk write

Driver Overview
---------------

PDK FATFS driver provides support for both single and multiple partition on a given
SD/MMC card. The driver uses a volume to partition mapping technique to handle multiple
storage device with multiple partition. The driver supports file operations such as
open, read and wirte on to the SD/MMC card. The FATFS driver access the SD/MMC card
through the PDK MMCSD driver which needs to be configured from the application as part
of the FATFS_config structure. The FATFS driver is used in other PDK module application
such as MMCSD, USB and SBL.

FATFS file operation API's can be accessed from the application only after FATFS_open
function is invoked.

.. code-block:: c

   FATFS_init();
   FATFS_open(0U, NULL, &fatfsHandle);


User Interface
--------------

Driver Configuration
^^^^^^^^^^^^^^^^^^^^^

.. rubric:: **Board Specific Configuration**
   :name: board-specific-configuration

All board specific configurations eg:enabling clock and pin-mux for UART
pins are required before calling any driver APIs.By default Board_Init()
API supports all initialization sequence for TI supported EVMs. In
addition it initializes UART instance for Console/STDIO.Refer `Processor
SDK RTOS Board Support <index_board.html#board-support>`__
for additional details.Once board specific configuration is complete
FATFS_init() API can be called to initialize FATFS for the driver.


.. rubric:: **FATFS Configuration Structure**
   :name: fatfs-configuration-structure

Application is expected to perform driver specific configuration for
FATFS_config structure. The structure supports initialization of
multiple drivers for FATFS, i.e. both MMCSD and USB can be configured
to use FATFS file system by configuring each driver to different drive
instance. This structure must be provided to the FATFS driver. It must
be initialized before the FATFS_init() function is called and cannot
be changed subsequently. For details about individual fields of this
structure, see the Doxygen
help:PDK_INSTALL_DIR\\packages\\ti\\fs\\fatfs\\docs\\doxygen\\html\\index.html.

APIs
^^^^^

In order to use the FATFS module APIs, the FATFS.h and ff.h header file
should be included in an application as follows:

.. code-block:: c

    #include <ti/fs/fatfs/FATFS.h>
    #include <ti/fs/fatfs/ff.h>

.. rubric:: API Call Flow
   :name: api-call-flow

Below sequence indicates the calling sequence of FATFS driver APIs:

.. code-block:: c

     FATFS_Handle FATFS;
     FATFS_Params FATFSParams;
     FATFS_Params_init(&FATFSParams);
     FATFS = FATFS_open(peripheralNum, &FATFSParams);



At this point application can invoke additional FAT File system API
eg: f_open(), f_write(), f_read() etc to perform file operations on
device


Application
------------

Examples
^^^^^^^^

+------------------------------+-----------------------+-----------------------+----------------+--------------+
| Name                         | | Description         | Expected Results      | Supported SOCs | Build Type   |
+==============================+=======================+=======================+================+==============+
| FATFS_Console_ExampleProject | | Example will        | When a card is        |                |              |
|                              |   initialize card and | detected with valid   |  AM335x        | CCS  Project |
|                              |   checks for valid    | FAT partition console |  AM437x        |              |
|                              |   FAT partition. When | interface output will |  AM571x        |              |
|                              |   a valid FAT         | indicate "0:> "       |  AM572x        |              |
|                              |   partition is        |                       |  AM574x        |              |
|                              |   detected console    |                       |                |              |
|                              |   interface for       |                       |                |              |
|                              |   command execution   |                       |                |              |
|                              |   is provided.        |                       |                |              |
|                              |   Supported console   |                       |                |              |
|                              |   commands include ls |                       |                |              |
|                              |   (to list files of   |                       |                |              |
|                              |   directory), cd      |                       |                |              |
|                              |   (change directory), |                       |                |              |
|                              |   pwd (present        |                       |                |              |
|                              |   working directory)  |                       |                |              |
|                              |   and cat (text file  |                       |                |              |
|                              |   read operation).    |                       |                |              |
+------------------------------+-----------------------+-----------------------+----------------+--------------+
| FATFS_Console_TestApp        | | Same as above       | Same as above         | AM65x          | Makefile     |
+------------------------------+-----------------------+-----------------------+----------------+--------------+
| FATFS_Console_SMP_Example    | | Example will        | When a card is        |                |              |
| Project                      |   initialize card and | detected with valid   |   AM572x-EVM   | CCS  Project |
|                              |   checks for valid    | FAT partition console |   (A15 core)   |              |
|                              |   FAT partition. When | interface output will |                |              |
|                              |   a valid FAT         | indicate "0:> "       |                |              |
|                              |   partition is        |                       |                |              |
|                              |   detected console    |                       |                |              |
|                              |   interface for       |                       |                |              |
|                              |   command execution   |                       |                |              |
|                              |   is provided.        |                       |                |              |
|                              |   Supported console   |                       |                |              |
|                              |   commands include ls |                       |                |              |
|                              |   (to list files of   |                       |                |              |
|                              |   directory), cd      |                       |                |              |
|                              |   (change directory), |                       |                |              |
|                              |   pwd (present        |                       |                |              |
|                              |   working directory)  |                       |                |              |
|                              |   and cat (text file  |                       |                |              |
|                              |   read operation)     |                       |                |              |
|                              |   with SMP enabled.   |                       |                |              |
+------------------------------+-----------------------+-----------------------+----------------+--------------+
| FATFS_Console_SMP_TestApp    | | Same as above       | Same as above         | AM65x(A53 core)| Makefile     |
+------------------------------+-----------------------+-----------------------+----------------+--------------+


Building CCS projects based examples
------------------------------------

CCS Projects mentioned in the above table are built using pdkProjectCreate.bat/sh as explained in
`PDK Example and Test Project Creation <index_overview.html#pdk-example-and-test-project-creation>`__


Building FATFS Test applications via makefiles
----------------------------------------------

- FATFSD Test applications and dependent libraries are built from the top level fatfs makefile
- Refer to the `Processor SDK RTOS Getting Started Guide <index_overview.html#setup-environment>`__  for details
  of how to setup the build environment. Once you have setup the build environment, issue the following commands:

    -  cd <pdk>/packages/
    -  To build: make fatfs
    -  To clean: make fatfs_clean

- Similarly, to build at the module level, issue the following commands for rebuilding :

    - cd <pdk>/packages/ti/fs/fatfs
    - To build: make all
    - To clean: make clean




Additional References
---------------------

+-----------------------------------+-----------------------------------------+
| **Document**                      | **Location**                            |
+-----------------------------------+-----------------------------------------+
| API Reference Manual              | $(TI_PDK_INSTALL_DIR)\\packages\\ti     |
|                                   | \\fs\\fatfs\\docs\\doxygen\\html\\index |
|                                   | .html                                   |
+-----------------------------------+-----------------------------------------+
| Release Notes                     | $(TI_PDK_INSTALL_DIR)\\packages\\ti     |
|                                   | \\fs\\fatfs\\docs\\ReleaseNotes_FATFS   |
|                                   | _LLD.pdf                                |
+-----------------------------------+-----------------------------------------+

