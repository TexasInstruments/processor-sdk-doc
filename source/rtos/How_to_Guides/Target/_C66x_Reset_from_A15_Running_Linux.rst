.. http://processors.wiki.ti.com/index.php/Taking_the_C66x_Out_Of_Reset_with_Linux_Running_on_the_ARM_A15

How to take the C66x DSP out of reset with Linux running on A15
---------------------------------------------------------------

This document describes the procedure to bring the C66x core out of reset after
booting Linux, or at the u-boot prompt.These steps are necessary in to order to
load an application on the C66x core, without interfering with the operation of
Linux running on the A15.

.. note::
   Prior to proceeding with the below instructions, please ensure that the latest :ref:`Emulation Package<>`
   is downloaded/installed through CCS. This will ensure the GEL files in your machine
   has the reset routines described below.

1) Once Linux has booted, launch the target configuration.

.. Image:: /images/Outofreset_1_lali.JPG

2) With the target configuration launched, right click on K2x.ccxml and select
   “Show all cores”

.. Image:: /images/Outofreset_2_lali.JPG

3) This will bring up the Non-Debuggable Devices section.
   Right click and connect the CS_DAP_Debug_SS core.

.. Image:: /images/Outofreset_3_lali.JPG

4) Go to Tools>GEL files and load the evmk2x.gel file by right clicking on the GEL file window.
   The Gel file would typically be located in the CCS installation under
   \\ccsv6\\ccs_base\\emulation\\boards\\evmk2x\\gel\\

.. Image:: /images/Outofreset_4_lali.png

5) Once the GEL has been successfully loaded, go to Scripts>default and select K2x_TakeDSPOutofReset.

.. Image:: /images/Outofreset_5_lali.png

6) At this point the console would indicate that the DSP is out of reset.

.. Image:: /images/Outofreset_6_lali.png

7) Now the DSP cores can be right-clicked and connected successfully.

.. Image:: /images/Outofreset_7_lali.png

Target Configuration
--------------------

.. note::
   Once the DSP core is connected following the above out of reset routine, the DDR and PLL settings
   done by u-boot would be overwritten by what's in the GEL. In order to avoid this, please ensure that
   the gel is NOT preloaded on the DSP core in the ccxml by leaving the initialization script blank.


.. Image:: /images/Outofreset_8_lali.JPG

