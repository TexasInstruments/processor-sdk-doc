.. _pru_cape_building_demos:

PRU Cape Building Demos
------------------------------

.. note::

   This documentation uses legacy code that is no longer supported on the TI
   forums (AM335x Starterware). The documentation has not been updated in
   several years, and some steps may not work with more recent software or
   tools. TI is providing this document as-is.


.. rubric::  Introduction

The PRU Cape is a test, development, and evaluation module system that
enables developers to write software and develop hardware around the PRU
subsystem. This article outlines how to rebuild the Demo software
available for the PRU Cape.

For more details about the PRU Cape and the Demo software, visit:

| :ref:`pru_cape_getting_started_guide`
| :ref:`pru_cape_hardware_user_guide`

|

.. rubric::  Prerequisites

The **PRU Cape Demo Software** is available in the `PRU Software
Support
Package <https://git.ti.com/pru-software-support-package/pru-software-support-package/>`__
hosted on git.ti.com. To download this package, select the "Source Tree"
button from the PRU Software Support Package webpage and then click
"Download master as tar.gz." In Windows, a program such as 7-zip can be
used to open the downloaded file and extract the software package
contents.
**To *EDIT* or *REBUILD* the PRU Cape demos**, the following software is
required:

-  `PRU Cape Demo Source
   Code <https://git.ti.com/pru-software-support-package/pru-software-support-package/trees/master/pru_cape>`__
   *(available in the pru\_cape/pru\_demo and pru\_cape/pru\_fw
   directories of the PRU Software Support Package)*
-  `AM335x Starterware <https://www.ti.com/tool/starterware-sitara>`__
-  `CCSv6 <https://software-dl.ti.com/ccs/esd/documents/ccs_downloads.html>`__
-  PRU Code Generation Tools (through CCS App Center)

|

.. rubric::  Rebuilding the Demo Source Code

***NOTE:*** This section uses the notation *$PRU\_SW\_PATH* to reference
the installed location of the downloaded PRU Software Support Package.

|

#. Launch CCSv6 and select the default Workspace

#. Load the **PRU\_Demo and Firmware projects'** into CCS

#. Select **Project->Import CCS Projects...**

    #. Browse to the **pru\_cape directory** in the PRU Software Package sources (i.e. *$PRU\_SW\_PATH/pru\_cape*)

    #. Select **all projects** that appear (i.e. PRU\_Demo, PRU\_LED0, PRU\_LED1, etc)

    #. Select **Finish**

#. The projects should now be visible in the **Project Explorer**. Don't see the Project Explorer? Select **View->Project Explorer**

#. Configure **PRU\_Demo** project Build Configurations as "Release"

    #. Right click on the **PRU\_Demo** project

    #. Select "Build Configurations -> Set Active -> 2 Release"

#. Link the **PRU\_Demo** project to StarterWare

    #. Right click on the **PRU\_Demo** project

    #. Select **Properties**

    #. Select **CCS Build->Environment**

    #. Edit (or add) the variable named **"STARTERWARE\_ROOT"**

    #. Update the **Value** of this variable to the **StarterWare directory** on your computer (i.e. C:/TI/AM335X\_StarterWare\_02\_00\_01\_01)

    #. Select **OK** and **OK**

#. Update **PRU\_Demo** project Link Order

    #. Right click on the **PRU\_Demo** project

    #. Select **Properties**

    #. Select **CCS Build->Link Order**

    #. Select **Add...** icon

    #. Select **pru.c** and **pru\_cape\_demo.c** files

    #. Select **OK** and **OK**

#. ***(Optional)*** To create an **SD bootable application image**, add a **Post-build** step **Note** this step must be performed in Windows. If this step is skipped, a .out file will still be created, which can be loaded to and executed on the BeagleBone Black through CCS over JTAG.

    #. Right click on the **PRU\_Demo** project

    #. Select **Properties**

    #. Select **CCS Build->Steps**

    #. Add the following text under **Post-build steps**:

       ::

            "${CCS\_INSTALL\_ROOT}/utils/tiobj2bin/tiobj2bin.bat" "${ProjName}.out" "${ProjName}.bin" "${CG\_TOOL\_ROOT}/bin/ofd470.exe"
            "${CG\_TOOL\_ROOT}/bin/hex470.exe" "${CCS\_INSTALL\_ROOT}/utils/tiobj2bin/mkhex4bin.exe" &
            "${STARTERWARE\_ROOT}/tools/ti\_image/tiimage.exe" "0x80000000" "NONE" "${ProjName}.bin" "${ProjName}\_ti.bin"

    #. Select **OK**

#. Build the **PRU\_Demo and PRU Firmware** projects

    #. Select the **PRU\_Demo** project

    #. Select **Project->Build Project**

    #. Note the firmware projects are linked to the PRU\_Demo project. Building the PRU\_Demo project should cause the other projects to build.

    #. Building the PRU\_Demo and PRU\_Firmware projects should create **PRU\_Demo.out** (located in the *$PRU\_SW\_PATH/pru\_cape/pru\_demo/Release* directory). This .out file can be loaded and run on the CortexA8 core through CCS over JTAG.

    #. If creating the optional **SD bootable application image** (Step 6 above), the Post-Build step should create **PRU\_Demo\_ti.bin** (located in the *$PRU\_SW\_PATH/pru\_cape/pru\_demo/Release* directory). Rename **PRU\_Demo\_ti.bin** to **app** and follow the steps on the :ref:`pru_cape_getting_started_guide` to prepare the SD Card.

|

.. rubric:: Running the Demos

Refer to the :ref:`pru_cape_getting_started_guide` for details about running
the demos.
