Update environment when installing to a custom path
-----------------------------------------------------

.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_Install_In_Custom_Path

Overview
^^^^^^^^

This page will provide configuration information if the SDK is installed
in a custom path.

**Useful Tip**

To avoid changing environment variable for each new shell, modify
environment variable file directly. This file is the *setupenv* file
located in the SDK root directory.



Changes to CCS Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Installing the SDK in a folder other than where CCS is installed will
require modifications to CCS to be able to discover the SDK. See the
`Setup CCS </index.php/Processor_SDK_RTOS_Setup_CCS>`__ **How To** page
explaining how to update CCS configuration.



Rebuilding the SDK RTOS
^^^^^^^^^^^^^^^^^^^^^^^

Installing the SDK in a folder other than the default (``C:\TI`` for
Windows, ``/home/[user]/ti`` for Linux) requires modifications to SDK
RTOS scripts in order for recompilation and example/test creation to
work properly.

In all the commands below, replace *[version]* with the appropriate
version of the software/tool.

CCS in Custom Path and SDK RTOS in Default Path
"""""""""""""""""""""""""""""""""""""""""""""""

CCS installation and toolchain paths can be customized by setting the
TOOLS_INSTALL_PATH environment variable prior to running the SDK level
setupenv script. This feature is used if CCS and the toolchains are
installed somewhere other than the default C:\\ti location.

For example, environment configuration assuming CCS is installed to
[os_base]\\ti_temp and SDK RTOS has been installed to default path,
[os_base]\\ti :

-  Windows

::

    C:\> set TOOLS_INSTALL_PATH=C:\ti_temp

::

    C:\> cd C:\ti\processor_sdk_rtos_[soc]_[version]

::

    C:\ti\processor_sdk_rtos_[soc]_[version]> setupenv.bat

Gives the output:

::

    Optional parameter not configured : CG_XML_BIN_INSTALL_PATH
    REQUIRED for xdc release build
    Example: set CG_XML_BIN_INSTALL_PATH=C:/ti/cg_xml/bin
    Optional parameter not configured : DOXYGEN_INSTALL_PATH
    REQUIRED for xdc release build
    Example: set DOXYGEN_INSTALL_PATH=C:/ti/Doxygen/doxygen/1.5.1-p1/bin
    **************************************************************************
    Environment Configuration:
        PDK Directory             : /ti/PDK_AM~3/packages/
        CGTOOL INSTALL Directory  : C:/ti_temp/ccsv6/tools/compiler/ti-cgt-c6000_[version]
        TOOLCHAIN A15 Directory   : C:/ti_temp/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]
        TOOLCHAIN A8 Directory    : C:/ti_temp/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]
        TOOLCHAIN A9 Directory    : C:/ti_temp/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]
        TOOLCHAIN M4 Directory    : C:/ti_temp/ccsv6/tools/compiler/ti-cgt-arm_[version]
        FPULIB_PATH               : C:/ti_temp/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]/lib/gcc/arm-none-eabi/[version]/fpu
        CROSS_TOOL_PRFX           : arm-none-eabi-
        XDC_INSTALL_PATH          : C:/ti/xdctools_[version]_core
        BIOS_INSTALL_PATH         : C:/ti/bios_[version]
        IPC_INSTALL_PATH          : C:/ti/ipc_[version]
        EDMA3LLD_BIOS6_INSTALLDIR : C:/ti/edma3_lld_[version]
        NDK_INSTALL_PATH          : C:/ti/ndk_[version]
        IMGLIB_INSTALL_PATH       : C:/ti/imglib_c66x_[version]
        UIA_INSTALL_PATH          : C:/ti/uia_[version]
        PROC_SDK_INSTALL_PATH     : C:/ti/processor_sdk_rtos_[soc]_[version]
    **************************************************************************
    Changing to short name to support directory names containing spaces
    current directory: C:/ti/processor_sdk_rtos_[soc]_[version]
    PROCESSOR SDK BUILD ENVIRONMENT CONFIGURED
    **************************************************************************

-  Linux

::

    $ export TOOLS_INSTALL_PATH=~/ti_temp

::

    $ cd ~/ti/processor_sdk_rtos_[soc]_[version]/

::

    ~/ti/processor_sdk_rtos_[soc]_[version]$ source setupenv.sh

Gives the output:

::

    Optional parameter not configured : CG_XML_BIN_INSTALL_PATH
    REQUIRED for xdc release build
    Example: export CG_XML_BIN_INSTALL_PATH="~/ti/cg_xml/bin"
    Optional parameter not configured : DOXYGEN_INSTALL_PATH
    REQUIRED for xdc release build
    Example: export DOXYGEN_INSTALL_PATH="~/ti/Doxygen/doxygen/1.5.1-p1/bin"
    **************************************************************************
    Environment Configuration:
        PDK Directory             : /home/[user]/ti/pdk_[soc]_[version]/packages
        CGTOOL INSTALL Directory  : /home/[user]/ti_temp/ccsv6/tools/compiler/ti-cgt-c6000_[version]
        TOOLCHAIN A15 Directory   : /home/[user]/ti_temp/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]
        TOOLCHAIN A8 Directory    : /home/[user]/ti_temp/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]
        TOOLCHAIN A9 Directory    : /home/[user]/ti_temp/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]
        TOOLCHAIN M4 Directory    : /home/[user]/ti_temp/ccsv6/tools/compiler/ti-cgt-arm_[version]
        FPULIB_PATH               : /home/[user]/ti_temp/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]/lib/gcc/arm-none-eabi/[version]/fpu
        CROSS_TOOL_PRFX           : arm-none-eabi-
        XDC_INSTALL_PATH          : /home/[user]/ti/xdctools_[version]_core
        BIOS_INSTALL_PATH         : /home/[user]/ti/bios_[version]
        IPC_INSTALL_PATH          : /home/[user]/ti/ipc_[version]
        EDMA3LLD_BIOS6_INSTALLDIR : /home/[user]/ti/edma3_lld_[version]
        NDK_INSTALL_PATH          : /home/[user]/ti/ndk_[version]
        IMGLIB_INSTALL_PATH       : /home/[user]/ti/imglib_c66x_[version]
        UIA_INSTALL_PATH          : /home/[user]/ti/uia_[version]
        PROC_SDK_INSTALL_PATH     : /home/[user]/ti/processor_sdk_rtos_[soc]_[version]

    PROCESSOR SDK BUILD ENVIRONMENT CONFIGURED
    *******************************************************************************

The `RTOS SDK top level
Makefile <index_overview.html#top-level-makefile>`__
can now be used to rebuild SDK RTOS components with CCS and toolchains
installed in a custom installation path.

CCS in Default Path and SDK RTOS in Custom Path
"""""""""""""""""""""""""""""""""""""""""""""""

SDK RTOS component installation paths can be customized by setting the
SDK_INSTALL_PATH variable prior to running the SDK level setupenv
script. This feature is used if the SDK is installed somewhere other
than the default ``C:\ti`` location.

For example, environment configuration assuming CCS is installed to the
default path, ``[os_base]\ti`` and SDK RTOS has been installed to
``[os_base]\ti_temp``:

-  Windows

::

    C:\> set SDK_INSTALL_PATH=C:/ti_temp

::

    C:\> cd C:\ti_temp\processor_sdk_rtos_[soc]_[version]

::

    C:\ti_temp\processor_sdk_rtos_[soc]_[version]> setupenv.bat

Gives the output:

::

    Optional parameter not configured : CG_XML_BIN_INSTALL_PATH
    REQUIRED for xdc release build
    Example: set CG_XML_BIN_INSTALL_PATH=C:/ti/cg_xml/bin
    Optional parameter not configured : DOXYGEN_INSTALL_PATH
    REQUIRED for xdc release build
    Example: set DOXYGEN_INSTALL_PATH=C:/ti/Doxygen/doxygen/1.5.1-p1/bin
    **************************************************************************
    Environment Configuration:
        PDK Directory             : /ti_temp/PDK_AM~3/packages/
        CGTOOL INSTALL Directory  : C:/ti/ccsv6/tools/compiler/ti-cgt-c6000_[version]
        TOOLCHAIN A15 Directory   : C:/ti/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]
        TOOLCHAIN A8 Directory    : C:/ti/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]
        TOOLCHAIN A9 Directory    : C:/ti/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]
        TOOLCHAIN M4 Directory    : C:/ti/ccsv6/tools/compiler/ti-cgt-arm_[version]
        FPULIB_PATH               : C:/ti/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]/lib/gcc/arm-none-eabi/[version]/fpu
        CROSS_TOOL_PRFX           : arm-none-eabi-
        XDC_INSTALL_PATH          : C:/ti_temp/xdctools_[version]_core
        BIOS_INSTALL_PATH         : C:/ti_temp/bios_[version]
        IPC_INSTALL_PATH          : C:/ti_temp/ipc_[version]
        EDMA3LLD_BIOS6_INSTALLDIR : C:/ti_temp/edma3_lld_[version]
        NDK_INSTALL_PATH          : C:/ti_temp/ndk_[version]
        IMGLIB_INSTALL_PATH       : C:/ti_temp/imglib_c66x_[version]
        UIA_INSTALL_PATH          : C:/ti_temp/uia_[version]
        PROC_SDK_INSTALL_PATH     : C:/ti_temp/processor_sdk_rtos_[soc]_[version]
    **************************************************************************
    Changing to short name to support directory names containing spaces
    current directory: C:/ti_temp/processor_sdk_rtos_[soc]_[version]
    PROCESSOR SDK BUILD ENVIRONMENT CONFIGURED
    **************************************************************************

-  Linux

::

    $ export SDK_INSTALL_PATH=~/ti_temp

::

    $ cd ~/ti_temp/processor_sdk_rtos_[soc]_[version]/

::

    ~/ti_temp/processor_sdk_rtos_[soc]_[version]$ source setupenv.sh

Gives the output:

::

    Optional parameter not configured : CG_XML_BIN_INSTALL_PATH
    REQUIRED for xdc release build
    Example: export CG_XML_BIN_INSTALL_PATH="~/ti/cg_xml/bin"
    Optional parameter not configured : DOXYGEN_INSTALL_PATH
    REQUIRED for xdc release build
    Example: export DOXYGEN_INSTALL_PATH="~/ti/Doxygen/doxygen/1.5.1-p1/bin"
    **************************************************************************
    Environment Configuration:
        PDK Directory             : /home/[user]/ti_temp/pdk_[soc]_[version]/packages
        CGTOOL INSTALL Directory  : /home/[user]/ti/ccsv6/tools/compiler/ti-cgt-c6000_[version]
        TOOLCHAIN A15 Directory   : /home/[user]/ti/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]
        TOOLCHAIN A8 Directory    : /home/[user]/ti/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]
        TOOLCHAIN A9 Directory    : /home/[user]/ti/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]
        TOOLCHAIN M4 Directory    : /home/[user]/ti/ccsv6/tools/compiler/ti-cgt-arm_[version]
        FPULIB_PATH               : /home/[user]/ti/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]/lib/gcc/arm-none-eabi/[version]/fpu
        CROSS_TOOL_PRFX           : arm-none-eabi-
        XDC_INSTALL_PATH          : /home/[user]/ti_temp/xdctools_[version]_core
        BIOS_INSTALL_PATH         : /home/[user]/ti_temp/bios_[version]
        IPC_INSTALL_PATH          : /home/[user]/ti_temp/ipc_[version]
        EDMA3LLD_BIOS6_INSTALLDIR : /home/[user]/ti_temp/edma3_lld_[version]
        NDK_INSTALL_PATH          : /home/[user]/ti_temp/ndk_[version]
        IMGLIB_INSTALL_PATH       : /home/[user]/ti_temp/imglib_c66x_[version]
        UIA_INSTALL_PATH          : /home/[user]/ti_temp/uia_[version]
        PROC_SDK_INSTALL_PATH     : /home/[user]/ti_temp/processor_sdk_rtos_[soc]_[version]

    PROCESSOR SDK BUILD ENVIRONMENT CONFIGURED
    *******************************************************************************

The `RTOS SDK top level
Makefile <index_overview.html#top-level-makefile>`__
can now be used to rebuild SDK RTOS components installed in the custom
installation path.

.. note::
   The following known issue impacts this step:
   **PRSDK-1263**: PDK AM437x: Make fails on Windows if CCS is installed in
   custom path. **Workaround:** Edit the UTILS_INSTALL_DIR variable in
   <pdk_root_dir>/packages/ti/starterware/Rules.make to point to the CCS
   installation on your Windows PC.

CCS and SDK RTOS in Custom Path
"""""""""""""""""""""""""""""""

When CCS and the SDK RTOS are both installed to custom paths the SDK can
be rebuilt by setting the SDK_INSTALL_PATH and TOOLS_INSTALL_PATH
variables prior to running the SDK RTOS top level environment setup
script. The Windows and Linux environment setup scripts can be found in
the following locations, respectively:

-  Windows -
   C:\\custom\\install\\path\\processor_sdk_rtos_[soc]_[version]\\setupenv.bat
-  Linux -
   /home/[user]/custom/install/path/processor_sdk_rtos_[soc]_[version]/setupenv.sh

The SDK_INSTALL_PATH and TOOLS_INSTALL_PATH environment variables must
be set to the custom install path **prior to running** the environment
setup script.

For example, environment configuration assuming CCS and the SDK have
been installed to [os_base]\\new_sdk_release\\ :

-  Windows

::

    C:\> set SDK_INSTALL_PATH=C:\new_sdk_release
    C:\> set TOOLS_INSTALL_PATH=C:\new_sdk_release

::

    C:\> cd C:\new_sdk_release\processor_sdk_rtos_[soc]_[version]

::

    C:\new_sdk_release\processor_sdk_rtos_[soc]_[version]> setupenv.bat

Gives the output:

::

    Optional parameter not configured : CG_XML_BIN_INSTALL_PATH
    REQUIRED for xdc release build
    Example: set CG_XML_BIN_INSTALL_PATH=C:/ti/cg_xml/bin
    Optional parameter not configured : DOXYGEN_INSTALL_PATH
    REQUIRED for xdc release build
    Example: set DOXYGEN_INSTALL_PATH=C:/ti/Doxygen/doxygen/1.5.1-p1/bin
    **************************************************************************
    Environment Configuration:
        PDK Directory             : /NEW_SD~1/PDK_AM~1/packages/
        CGTOOL INSTALL Directory  : C:/new_sdk_release/ccsv6/tools/compiler/ti-cgt-c6000_[version]
        TOOLCHAIN A15 Directory   : C:/new_sdk_release/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]
        TOOLCHAIN A8 Directory    : C:/new_sdk_release/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]
        TOOLCHAIN A9 Directory    : C:/new_sdk_release/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]
        TOOLCHAIN M4 Directory    : C:/new_sdk_release/ccsv6/tools/compiler/ti-cgt-arm_[version]
        FPULIB_PATH               : C:/new_sdk_release/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]/lib/gcc/arm-none-eabi/[version]/fpu
        CROSS_TOOL_PRFX           : arm-none-eabi-
        XDC_INSTALL_PATH          : C:/new_sdk_release/xdctools_[version]_core
        BIOS_INSTALL_PATH         : C:/new_sdk_release/bios_[version]
        IPC_INSTALL_PATH          : C:/new_sdk_release/ipc_[version]
        EDMA3LLD_BIOS6_INSTALLDIR : C:/new_sdk_release/edma3_lld_[version]
        NDK_INSTALL_PATH          : C:/new_sdk_release/ndk_[version]
        IMGLIB_INSTALL_PATH       : C:/new_sdk_release/imglib_c66x_[version]
        UIA_INSTALL_PATH          : C:/new_sdk_release/uia_[version]
        PROC_SDK_INSTALL_PATH     : C:/new_sdk_release/processor_sdk_rtos_[soc]_[version]
    **************************************************************************
    Changing to short name to support directory names containing spaces
    current directory: C:/new_sdk_release/processor_sdk_rtos_[soc]_[version]
    PROCESSOR SDK BUILD ENVIRONMENT CONFIGURED
    **************************************************************************

-  Linux

::

    $ export SDK_INSTALL_PATH=~/new_sdk_release
    $ export TOOLS_INSTALL_PATH=~/new_sdk_release

::

    $ cd ~/new_sdk_release/processor_sdk_rtos_[soc]_[version]/

::

    ~/new_sdk_release/processor_sdk_rtos_[soc]_[version]$ source setupenv.sh

Gives the output:

::

    Optional parameter not configured : CG_XML_BIN_INSTALL_PATH
    REQUIRED for xdc release build
    Example: export CG_XML_BIN_INSTALL_PATH="~/ti/cg_xml/bin"
    Optional parameter not configured : DOXYGEN_INSTALL_PATH
    REQUIRED for xdc release build
    Example: export DOXYGEN_INSTALL_PATH="~/ti/Doxygen/doxygen/1.5.1-p1/bin"
    **************************************************************************
    Environment Configuration:
        PDK Directory             : /home/[user]/new_sdk_release/pdk_[soc]_[version]/packages
        CGTOOL INSTALL Directory  : /home/[user]/new_sdk_release/ccsv6/tools/compiler/ti-cgt-c6000_[version]
        TOOLCHAIN A15 Directory   : /home/[user]/new_sdk_release/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]
        TOOLCHAIN A8 Directory    : /home/[user]/new_sdk_release/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]
        TOOLCHAIN A9 Directory    : /home/[user]/new_sdk_release/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]
        TOOLCHAIN M4 Directory    : /home/[user]/new_sdk_release/ccsv6/tools/compiler/ti-cgt-arm_[version]
        FPULIB_PATH               : /home/[user]/new_sdk_release/ccsv6/tools/compiler/gcc-arm-none-eabi-[version]/lib/gcc/arm-none-eabi/[version]/fpu
        CROSS_TOOL_PRFX           : arm-none-eabi-
        XDC_INSTALL_PATH          : /home/[user]/new_sdk_release/xdctools_[version]_core
        BIOS_INSTALL_PATH         : /home/[user]/new_sdk_release/bios_[version]
        IPC_INSTALL_PATH          : /home/[user]/new_sdk_release/ipc_[version]
        EDMA3LLD_BIOS6_INSTALLDIR : /home/[user]/new_sdk_release/edma3_lld_[version]
        NDK_INSTALL_PATH          : /home/[user]/new_sdk_release/ndk_[version]
        IMGLIB_INSTALL_PATH       : /home/[user]/new_sdk_release/imglib_c66x_[version]
        UIA_INSTALL_PATH          : /home/[user]/new_sdk_release/uia_[version]
        PROC_SDK_INSTALL_PATH     : /home/[user]/new_sdk_release/processor_sdk_rtos_[soc]_[version]

    PROCESSOR SDK BUILD ENVIRONMENT CONFIGURED
    *******************************************************************************

The `RTOS SDK top level Makefile <index_overview.html#top-level-makefile>`__
can now be used to rebuild SDK RTOS components installed in the custom
installation path using CCS and toolchains installed in a custom path as
well.


Rebuilding the PDK
^^^^^^^^^^^^^^^^^^

Installing the PDK in a folder other than the default (C:\TI for
Windows, /home/[user]/ti for Linux) requires modifications to PDK
scripts in order for recompilation and example/test creation to work
properly.

CCS in Custom Path and PDK in Default Path
""""""""""""""""""""""""""""""""""""""""""

The instructions provided in the `CCS in Custom Path and SDK RTOS in
Default
Path </index.php/Processor_SDK_RTOS_Install_In_Custom_Path#CCS_in_Custom_Path_and_SDK_RTOS_in_Default_Path>`__
section can be used to rebuild components at the PDK level. The only
difference is the PDK level setup script should be used instead of the
SDK RTOS level setup script. The PDK level setup scripts are found in
the following locations on Windows and Linux, respectively:

-  Windows -
   C:\\custom\\install\\path\\pdk_[soc]_[version]\\packages\\pdksetupenv.bat
-  Linux -
   /home/[user]/custom/install/path/pdk_[soc]_[version]/packages/pdksetupenv.sh

CCS in Default Path and PDK in Custom Path
""""""""""""""""""""""""""""""""""""""""""

The instructions provided in the `CCS in Default Path and SDK RTOS in
Custom
Path </index.php/Processor_SDK_RTOS_Install_In_Custom_Path#CCS_in_Default_Path_and_SDK_RTOS_in_Custom_Path>`__
section can be used to rebuild components at the PDK level. The only
difference is the PDK level setup script should be used instead of the
SDK RTOS level setup script. The PDK level setup scripts are found in
the following locations on Windows and Linux, respectively:

-  Windows -
   C:\\custom\\install\\path\\pdk_[soc]_[version]\\packages\\pdksetupenv.bat
-  Linux -
   /home/[user]/custom/install/path/pdk_[soc]_[version]/packages/pdksetupenv.sh

CCS and PDK in Custom Path
""""""""""""""""""""""""""

The instructions provided in the `CCS and SDK RTOS in Custom
Path </index.php/Processor_SDK_RTOS_Install_In_Custom_Path#CCS_and_SDK_RTOS_in_Custom_Path>`__
section can be used to rebuild components at the PDK level. The only
difference is the PDK level setup script should be used instead of the
SDK RTOS level setup script. The PDK level setup scripts are found in
the following locations on Windows and Linux, respectively:

-  Windows -
   C:\\custom\\install\\path\\pdk_[soc]_[version]\\packages\\pdksetupenv.bat
-  Linux -
   /home/[user]/custom/install/path/pdk_[soc]_[version]/packages/pdksetupenv.sh


Creating PDK Example/Test Projects When CCS is Installed to Custom Path
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The pdkProjectCreate scripts must be modified in order to build PDK
example and test projects only if CCS has been installed to a custom
path. The modification is the same for both Windows and Linux. Inside
the pdkProjectCreate scripts is a CCS_INSTALL_PATH variable which points
to the Code Composer Studio root directory. This variable must be
redefined to the new location of the CCS root directory if CCS is
installed to a custom path.

-  Windows

::

    REM Install Location for CCS
    set CCS_INSTALL_PATH="C:\ti\ccsv6"

-  Linux

::

    # Install Location for CCS
    export CCS_INSTALL_PATH=~/ti/ccsv6

.. note::
   Prior to invoking the pdkProjectCreate script, make sure to start CCS
   and register the SDK RTOS components installed. Project creation will
   fail if the RTOS SDK components installed to the custom path have not
   been registered with CCS. Please see `CCS and SDK installed in different
   directories </index.php/Processor_SDK_RTOS_Setup_CCS#CCS_and_SDK_installed_in_different_directories>`__
   for instructions on how to register SDK RTOS components installed to a
   custom path with CCS

