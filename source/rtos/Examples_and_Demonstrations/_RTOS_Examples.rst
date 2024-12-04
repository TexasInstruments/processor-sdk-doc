.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_Examples

Overview
========

The SYS/BIOS examples gets user started with development of code using a
real-time operating system. These are simple examples that does not get
into details of software components provided in the SDK.


ARM Cortex-A53
==============

The hello example serves as a basic sanity check program for SYS/BIOS.
It demonstrates how to print the string 'hello world' to stdout. As a
sample we will use the AM65x device to describe the steps for the Cortex-A53.

.. Note:: For future Device Support Package releases, the Hello World example for the Cortex-A53 will be added to CCS as an out-of-box experience.

1. Create a work space folder to be used for Hello Example project
(e.g. /ti/am65x_am53_hello_workspace), and start CCS. If prompted with
**New Products Discovered**, install any desired products and restart
CCS if required.

2. In CCS, go to File --> New -->
CCS Project.

3. Enter a project name and configure the new CCS project as follows:

 * **Target**: GPEVM_AM65x
 * **Cortex A**
 * **Device Endianness**: little

4. Under "Project Templates and examples", select "More Examples... --> Search Using Import Wizard".
Select "hello" project and click "Finish".

5. Remove AM6548.lds from the project. Add the file **linker_a53.lds** located in the folder (PDK INSTALL PATH)/packages/ti/build/am65xx/
to the project.

6. Remove hello.cfg from the project. Add the file **sysbios_a53.cfg** located in the folder (PDK INSTALL PATH)/packages/ti/build/am65xx/
to the project.

7. Add the file **InitMmu.c** located under (IPC INSTALL PATH)/examples/AM65XX_bios_elf/ex02_messageq/host
to the project.

8. Select Compiler: right-click on the project, select "Properites". Under "Tool-chain",
select "GNU v7.2.1 (Linaro aarch64)" (or higher).

9. Build the project: right-click on the project and
select "Build Project".

10. Launch the target configuration using the appropriate emulator to connect to AM65x EVM
as described in the AM65x EVM Hardware Setup Guide.

11. Right click on DMSC_Cortex_M3_0 and click Connect Target.

12. Connect to the CortexA53_0_0 core. Load and run Hello Example out file.
You should see Hello World string displayed on console window.

|

ARM Cortex-A15
==============

The hello example serves as a basic sanity check program for SYS/BIOS.
It demonstrates how to print the string 'hello world' to stdout. As a
sample we will use the AM572x device to describe the steps. The same
steps can be used for create hello world examples for A15 cores in
Keystone 2 family of devices.

.. note::

   -  The K2G, K2E and K2H devices, can be located under Unclassified
      devices in the Resource Explorer. Refer below Screenshot for Keystone II

.. Image:: /images/KSII_RS.png

1. Create a work space folder (\ti\am_572x_hello_workspace) under ti
folder to be used for Hello Example project, and start CCS. You may be
prompted with **New Products Discovered**, so select all and **click on
Finish**

2. On CCS click View --> Resource Explorer (Examples).

3. On SYS/BIOS scroll down to AM572X --> Cortex A --> Generic Example
--> click on Hello Example.

.. Image:: /images/Sys_bios_hello_example_screen_1.jpg

4. To import Hello Example, on the right window click on step 1. Import
The Example to CCS Project.

5. On New CCS Project window enter project name and then click Next.

.. Image:: /images/Sys_bios_hello_example_screen_2.jpg

6. On RSTC window select platform name: **ti.platforms.evmAM572X** and
check that the target is set to **gnu.targets.arm.A15F**

7. Click Finish. Your project should show up on Project Explorer window.

8. To get log message to print on console add this variable to hello.cfg
file:

.. raw:: html

   <div class="mw-geshi mw-code mw-content-ltr" dir="ltr">

.. raw:: html

   <div class="c source-c">

.. code:: c

    var SemiHostSupport = xdc.useModule('ti.sysbios.rts.gnu.SemiHostSupport');

.. raw:: html

   </div>

.. note::
   You also need to replace the nosys library in linker with
   rdimon which is the Semi-Hosting enabled BSP library.

Right click on project --> Show Build Settings... --> Build --> GNU
Linker --> Libraries

9. Build Hello Example project by Right click on Hello Project and click
Build project.

10. Create new target configuration (if one doesn`t exist) as described
in here :ref:`Create Target Configuration File for EVM <Create-Target-Configuration-File-for-EVM-label/>`

11. Right click on the target configuration and Launch target
configurations.

12. Right click CortexA15_0 and connect target.

13. Load and run Hello Example out file. You should see **Hello World**
string displayed on console window.

|

ARM Cortex-A9
=============

The hello example serves as a basic sanity check program for SYS/BIOS.
It demonstrates how to print the string 'hello world' to stdout.

1. Create a work space folder (\\ti\\am_437x_hello_workspace) under ti
folder to be used for Hello Example project, and start CCS. You may be
prompted with **New Products Discovered**, so select all and **click on
Finish**

2. On CCS click View --> Resource Explorer (Examples).

3. On SYS/BIOS scroll down to AM4378 --> Cortex A --> Generic Example
--> click on Hello Example.

.. Image:: /images/RTOS_CortexA9_HelloWorld.png

4. To import Hello Example, on the right window click on step 1. Import
The Example to CCS Project.

5. On New CCS Project window enter project name and then click Next.

.. Image:: /images/HelloWorld_cortexA9.png

6. On RSTC window select platform name: **ti.platforms.evmAM437X** and
check that the target is set to **gnu.targets.arm.A9F**

7. Click Finish. Your project should show up on Project Explorer window.

8. To get log message to print on console add this variable to hello.cfg
file:

.. raw:: html

   <div class="mw-geshi mw-code mw-content-ltr" dir="ltr">

.. raw:: html

   <div class="c source-c">

.. code:: c

    var SemiHostSupport = xdc.useModule('ti.sysbios.rts.gnu.SemiHostSupport');

.. raw:: html

   </div>

.. raw:: html

   </div>

.. note::
   You also need to replace the nosys library in linker with
   rdimon which is the Semi-Hosting enabled BSP library.

Right click on project --> Show Build Settings... --> Build --> GNU
Linker --> Libraries

9. Build Hello Example project by Right click on Hello Project and click
Build project.

10. Create new target configuration (if one doesn`t exist) as described
here :ref:`Create Target Configuration File for EVM <Create-Target-Configuration-File-for-EVM-label>`

11. Right click on the target configuration and Launch target
configurations.

12. Right click CortexA9_0 and connect target.

13. Load and run Hello Example out file. You should see **Hello World**
string displayed on console window.

|

ARM Cortex-A8
=============

The hello example serves as a basic sanity check program for SYS/BIOS.
It demonstrates how to print the string 'hello world' to stdout.

1. Create a work space folder (\\ti\\am_335x_hello_workspace) under ti
folder to be used for Hello Example project, and start CCS. You may be
prompted with **New Products Discovered**, so select all and **click on
Finish**

2. On CCS click View -->
Resource Explorer (Examples).

3. On SYS/BIOS scroll down to AM3352 --> Cortex A --> Generic Example
--> click on Hello Example.

.. Image:: /images/RTOS_CortexA8_HelloWorld.png

4. To import Hello Example, on the right window click on step 1. Import
The Example to CCS Project.

5. On New CCS Project window enter project name and then
click Next.

.. Image:: /images/HelloWorld_cortexA8.png

6. On RSTC window select platform name: **ti.platforms.evmAM335X** and
check that the target is set to **gnu.targets.arm.A8F**

7. Click Finish. Your project should show up on
Project Explorer window.

8. To get log message to print on console add this variable to hello.cfg
file:

.. raw:: html

   <div class="mw-geshi mw-code mw-content-ltr" dir="ltr">

.. raw:: html

   <div class="c source-c">

.. code:: c

    var SemiHostSupport = xdc.useModule('ti.sysbios.rts.gnu.SemiHostSupport');

.. raw:: html

   </div>

.. raw:: html

   </div>

.. note::
   You also need to replace the nosys library in linker with
   rdimon which is the Semi-Hosting enabled BSP library.

Right click on project --> Show Build Settings... --> Build --> GNU
Linker --> Libraries

9. Build Hello Example project by Right click on Hello Project and click
Build project.

10. Create new target configuration (if one doesn`t exist) as described
here :ref:`Create Target Configuration File for EVM <Create-Target-Configuration-File-for-EVM-label>`

11. Right click on the target configuration and Launch target
configurations.

12. Right click CortexA8_0 and connect target.

13. Load and run Hello Example out file. You should see **Hello World**
string displayed on console window.

|

ARM Cortex-R5
=============

The hello example serves as a basic sanity check program for SYS/BIOS.
It demonstrates how to print the string 'hello world' to stdout.

1. Create a work space folder (/ti/am65x_r5_hello_workspace) under ti
folder to be used for Hello Example project, and start CCS. You may be
prompted with **New Products Discovered**, so select all and **click on
Finish**

2. Select File --> New -->
CCS Project.

3. Select Target:
AM6548.

4. Select Cortex R
[ARM] tab.

5. Under Project templates and examples,
expand SYS/BIOS. Expand More Examples..., click Search using Import Wizard.

6. Select "hello" project,
click Finish.

7. Launch the target configuration using the appropriate emulator to
connect to AM65x EVM as described in the AM65x EVM Hardware Setup Guide.

8. Right click on DMSC_Cortex_M3_0 and
click Connect Target.

9. Connect to the MCU_PULSAR_Cortex_R5_0 core. Load and run Hello Example
out file. You should see Hello World string displayed on console window.


ARM Cortex-M4
=============

The hello example serves as a basic sanity check program for SYS/BIOS.
It demonstrates how to print the string 'hello world' to stdout.

1. Create a work space folder (/ti/am_572x_hello_workspace) under ti
folder to be used for Hello Example project, and start CCS. You may be
prompted with **New Products Discovered**, so select all and **click on
Finish**

2. On CCS click View --> Resource Explorer
(Examples).

3. on SYS/BIOS scroll down to AM572X --> Cortex M --> Generic Example
--> click on Hello Example.

.. Image:: /images/SYSBIOS_hello_world_M4_template.jpg

4. To import Hello Example, on the right window click on step 1. Import
The Example to CCS Project.

5. Go to Project Explorer window and click on project properties.

.. Image:: /images/SYSBIOS_M4_platformSelect.jpg

6. On RSTC window select platform name: **ti.platforms.evmAM572X** and
check that the target is set to **gnu.targets.arm.elf.M4**

7. Click Finish. Your project should show up on
Project Explorer window.

8. Build Hello Example project by Right click on Hello Project and click
Build project.

9. Launch target configurations using appropriate emulator to connect to
AM572X EVM.

10. Right click CortexA15_0 and connect target. From the Scripts menu
select `AM572x Multicore
Initialization->IPU1SSClkEnable_API <index_how_to_guides.html#connect-to-am57x-target-cores>`__.

11. Connect to the Cortex_M4_IPU1_C0. Load and run Hello Example out
file. You should see **Hello World** string displayed on console window.

|

ARM9
====

The hello example serves as a basic sanity check program for SYS/BIOS.
It demonstrates how to print the string 'hello world' to stdout. As a
sample we will use the OMAP-L138 device to describe the steps.

1. Create a workspace folder inside the ti
folder to be used for the Hello Example project, and start CCS. You may be
prompted with **New Products Discovered**, so select all and **click on
Finish**

2. On CCS click View --> Resource Explorer Classic (Examples).

3. On SYS/BIOS scroll down to OMAP-L1x --> LCDKOMAPL138 --> TI Target Examples --> Generic Examples
--> click on Hello Example.

.. Image:: /images/omapl13x_arm9_hello_rtos_tirex.png

4. To import Hello Example, on the right window click on step 1. Import
The Example to CCS Project.

5. On New CCS Project window enter project name and then click Next.

.. Image:: /images/omapl13x_arm9_hello_rtos_ccs.png

6. On RSTC window select platform name: **ti.platforms.evmOMAPL138** and
check that the target is set to **ti.targets.arm.elf.Arm9**

7. Click Finish. Your project should show up on Project Explorer window.

8. Build Hello Example project by Right click on Hello Project and click
Build project.

9. Create new target configuration (if one doesn`t exist) as described
in here :ref:`Create Target Configuration File for EVM <Create-Target-Configuration-File-for-EVM-label/>`

10. Right click on the target configuration and Launch target
configurations.

11. Right click ARM9_0 and connect target.

12. Load and run Hello Example out file. You should see **Hello World**
string displayed on the console window.

|

DSP C66x
========

The hello example serves as a basic sanity check program for SYS/BIOS.
It demonstrates how to print the string 'hello world' to stdout. As a
sample we will use the AM572x device to describe the steps but the same
steps can be used for create hello world examples for C66x cores in
Keystone I and Keystone 2 family of devices.

.. note::

   -  The C66x examples corresponding Keystone I devices can be located
      under C66x Multi-core DSP devies in the Resource Explorer. Refer
      below screenshot

.. Image:: /images/KSI_RS.png

.. note::

   -  The K2G, K2E and K2H devices, can be located under Unclassified
      devices in the Resource Explorer. Refer below screen shot

.. Image:: /images/KSII_RS.png

1. Create a work space folder (\ti\am_572x_hello_workspace) under ti
folder to be used for Hello Example project, and start CCS. You may be
prompted with **New Products Discovered**, so select all and **click on
Finish**

2. On CCS click View --> Resource Explorer (Examples).

3. on SYS/BIOS scroll down to AM572X --> C66x --> Generic Example -->
click on Hello Example.

.. Image:: /images/SYSBIOS_hello_world_dsp_template.jpg

4. To import Hello Example, on the right window click on step 1. Import
The Example to CCS Project.

5. On New CCS Project window enter project name and then click Next.

.. Image:: /images/SYSBIOS_DSP_platformSelect.jpg

6. On RSTC window select platform name: **ti.platforms.evmAM572X** and
check that the target is set to **ti.targets.elf.C66** (Auto populated)

7. Click Finish. Your project should show up on Project Explorer window.

8. Build Hello Example project by Right click on Hello Project and click
Build project.

10. Create new target configuration (if one doesn`t exist) as described
`here <index_how_to_guides.html#create-target-configuration-file-for-evm>`__.

11. Right click on the target configuration and Launch target
configurations.

12. Right click CortexA15_0 and connect target. From the Scripts menu
select `AM572x Multicore
Initialization->DSP1SSClkEnable_API <index_how_to_guides.html#connect-to-am57x-target-cores>`__.

13. Route the GPTimer5 suspend ctrl signal to the DSP using the Scripts
menu GP timer Suspend Ctrl -> GPTimer5SuspendCtl_DSP1SS_BIOS as
described `here <index_how_to_guides.html#timer-suspend-control-options-for-dsp>`__.

14. Connect to C66x_DSP1 Load and run Hello Example out file. You should
see **Hello World** string displayed on console window.

DSP C674x
=========

The hello example serves as a basic sanity check program for SYS/BIOS.
It demonstrates how to print the string 'hello world' to stdout. As a
sample we will use the C6748 device to describe the steps but the same
steps can be used for create hello world examples for C674x cores in
OMAPL1x/DA8x family of devices.

.. note::

   -  Locate the appropriate device that you are using to make sure the
      correct SYSBIOS platform definiition gets used in the build

1. Create a work space folder ( Eg. tirtos_hello_workspace) that can be
used for Hello Example project, and start CCS. You may be prompted with
**New Products Discovered**, so select all and **click on Finish** Note:
at this stage the version of SYSBIOS and corresponding dependencies are
assumed to be discovered by CCS. If not please follow the steps
described here:
`Discovering_SDK_products <index_how_to_guides.html#discovering-sdk-products>`__

2. On CCS click View --> Resource Explorer Classic (Examples).

3. on SYS/BIOS scroll down to C6748 /OMAPL1x and select --> C674x -->
Generic Example --> click on Hello Example.

.. Image:: /images/OMAPL138_SYSBIOS_TI_RTOS_CCSv7.png

4. To import Hello Example, on the right window click on step 1. Import
The Example to CCS Project.

5. On New CCS Project window enter project name and then click Next.

.. Image:: /images/Create_Project_Step1.png

6. On RSTC window select platform name: **ti.platforms.evmc6748** and
check that the target is set to **ti.targets.elf.C674** (Auto populated)

.. Image:: /images/Create_Project_Step2.png

7. Click Finish. Your project should show up on Project Explorer window.

8. Build Hello Example project by Right click on Hello Project and click
Build project.

10. Create new target configuration (if one doesn`t exist) as described
`here <index_how_to_guides.html#create-target-configuration-file-for-evm>`__.

11. Right click on the target configuration and Launch target
configurations.

12. Developers can Connect to the C674x on OMAPL137/C6747/C6748 can
connect directly to the DSP. For OMAPL138 device, you will need to
connect to the ARM as this is ARM master boot device and ARM needs to
power up the DSP You should see the following log in the Console

::

    C674X_0: Output:   Target Connected.
    C674X_0: Output:    ---------------------------------------------
    C674X_0: Output:    Memory Map Cleared.
    C674X_0: Output:    ---------------------------------------------
    C674X_0: Output:    Memory Map Setup Complete.
    C674X_0: Output:    ---------------------------------------------
    C674X_0: Output:    PSC Enable Complete.
    C674X_0: Output:    ---------------------------------------------
    C674X_0: Output:    PLL0 init done for Core:300MHz, EMIFA:25MHz
    C674X_0: Output:    DDR initialization is in progress....
    C674X_0: Output:    PLL1 init done for DDR:150MHz
    C674X_0: Output:    Using DDR2 settings
    C674X_0: Output:    DDR2 init for 150 MHz is done
    C674X_0: Output:    ---------------------------------------------

13. Connect to C674x_DSP1 Load and run Hello Example out file. You
should see **Hello World** string displayed on console window.

.. Image:: /images/Hello_world_dsp674x_rtos.png

|

Usage Notes
===========

After execution of the hello world examples on the core, the CCS Editor
may report "Can't find a source file" error messages when you pause or
the application exits/aborts after completion. This occurs due to source
files from SYSBIOS or XDC packages not being in the default search path
of the CCS Editor. when you run into this issue, you can navigate to the
file using Locate file option in the Editor. Once you provide the
location the CCS Editor will be able to locate all the other required
files from that package based on relative path.

For example, when running SYS/BIOS Hello Example using AM57x-GP EVM if
you see the message

::

     Can't find a source file at "/db/ztree/library/trees/xdctargets/xdctargets-i02/src/gnu/targets    /arm/rtsv7A/syscalls.c"
     Locate the file or edit the source lookup path to include its location. The above file is located  under file path ${PROC_SDK_DIR}\bios_6_42_02_29\packages\gnu\targets\arm\rtsv7A

You can also prevent these issues by adding the Processor SDK components
to file search path under Windows->Preferences options in CCS GUI.

|

Known Issues
============

-  **SYS/BIOS examples for Cortex-A15 generate linker errors due to the
   FPU related flags**

Some versions of CCS are impacted by linker setting used in CCS RTOS
templates and may need some manual modification to set the correct
-mfpu, -mcpu and -march. If you are seeing VFP errors in the link step,
you are most likely running into this issue. To correct this issue
please check the resolution here:
https://e2e.ti.com/support/development_tools/code_composer_studio/f/81/t/539973

|


Useful Resources
================

-  `TI RTOS
   training <http://processors.wiki.ti.com/index.php/Introduction_to_the_TI-RTOS_Kernel_Workshop>`__
-  `SYS/BIOS
   Information <http://processors.wiki.ti.com/index.php/Category:SYSBIOS>`__
-  `SYS/BIOS
   FAQ <http://processors.wiki.ti.com/index.php/SYS/BIOS_FAQs>`__

|

