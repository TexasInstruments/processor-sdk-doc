.. http://processors.wiki.ti.com/index.php/XDS560

.. rubric:: Overview
   :name: overview

-  The XDS560 Emulator is a high speed JTAG connection between Code
   Composer Studio and the target device.
-  More information can be found here:
   `[1] <http://focus.ti.com/docs/toolsw/folders/print/xds560.html>`__
-  The XDS560 Emulators support `High Speed RTDX
   (HSRTDX) <http://processors.wiki.ti.com/index.php/High_Speed_RTDX_(HSRTDX)>`__

+-----------------------------------+-----------------------------------+
| **Warning**:                      | As of 6/24/2010 RTDX and HS-RTDX  |
|                                   | are no longer supported.          |
|                                   | Alternative transports should be  |
|                                   | considered for the acquision of   |
|                                   | data, such as serial ports and    |
|                                   | ethernet. If you are currently    |
|                                   | using the technology and have no  |
|                                   | issues, there is no need to       |
|                                   | change. However, no action will   |
|                                   | be taken for support inqueries.   |
+-----------------------------------+-----------------------------------+

-  The XDS560 Emulators support `Advanced Event
   Triggering <http://processors.wiki.ti.com/index.php/Advanced_Event_Triggering>`__
-  The XDS560 Emulators support `IEEE 1149.1
   (JTAG) <http://processors.wiki.ti.com/index.php/IEEE_1149.1_(JTAG)>`__
-  A general overview of TI emulation capabilities is
   `here <http://focus.ti.com/dsp/docs/dspfindtoolswbytooltype.tsp?sectionId=3&tabId=2093&toolTypeId=12&familyId=44>`__.
-  For information about JTAG headers, please check the WIKI page `JTAG
   Connectors <http://processors.wiki.ti.com/index.php/JTAG_Connectors>`__.
-  For debugging issues with JTAG, you may want to check the topic
   `Debugging JTAG Connectivity
   Problems <http://processors.wiki.ti.com/index.php/Debugging_JTAG_Connectivity_Problems>`__
-  An XDS560 with Ethernet LAN support is available from
   `here <http://www.blackhawk-dsp.com/Lan560.aspx>`__
-  `XDS560v2 System Trace <http://processors.wiki.ti.com/index.php/XDS560v2_System_Trace>`__

|

.. rubric:: XDS560v2 System Trace
   :name: xds560v2-system-trace

-  The `XDS560v2 System Trace <http://processors.wiki.ti.com/index.php/XDS560v2_System_Trace>`__
   emulator is now available. It offers increased performance and
   features.

.. rubric:: XDS560 Rev D Cable
   :name: xds560-rev-d-cable

In addition to the standard XDS560 features, the XDS560 Rev D cable also
supports:

-  Compact TI 20-pin target card connector
-  Adaptive clocking for TI devices with ARM processors
-  EMU pin boot modes
-  Remote system reset `System Reset
   (Emulation) <http://processors.wiki.ti.com/index.php/System_Reset_(Emulation)>`__
-  RTCK/TCK looback

Rev D cables can be identified by their "00D" at the end of the cable
serial number.

The TI 20-pin target card connector reduces the PWB foot print over the
traditional TI 14-pin target connector while expanding the number of EMU
pins supported. See `JTAG Connectors <http://processors.wiki.ti.com/index.php/JTAG_Connectors>`__
Wiki page for the TI 20-pin cable's pin assignments and target card
connector part number. The board requirements provided in `XDS560
Emulator Technical
Reference <http://focus.ti.com/lit/ug/spru589a/spru589a.pdf>`__ are
valid except in the adaptive clocking case. The additional EMU pins are
treated electrically identical to EMU0 and EMU1. See below for SYSRST
board requirment.

Adaptive clocking for ARM devices can be enabled through CCSetup’s
Connection Properties page (see “JTAG TCKL Frequency (MHz)” selection
options). See the `Adaptive Clocking <http://processors.wiki.ti.com/index.php/Adaptive_Clocking>`__
Wiki page for more information and board requirements. Generally, in CCS
3.3 Setup, you may need to select the create board option to enable the
rev D capabilities. This can be seen in the screen shot below.

.. Image:: /images/Ccsetup-02.jpg

Once this is done, in the connnection properties, it is possible to
select the "Adaptive Clocking" options.

.. Image:: /images/Ccsetup-04.jpg

For devices that support EMU Boot modes the XDS560 Rev D cable drives
the selected EMU pin polarity on the rising edge of nTRST or TVD. The
EMU pin polarity selection is enabled through CCSetup’s Connection
Properties page (see “JTAG nTRST Boot Mode” or “Power on-Reset Boot
Mode” selection options).To determine if your device supports boot
modes, which modes are supported and the proper polarity for each boot
mode see your device’s data sheet.

.. Image:: /images/Ccsetup-05.jpg

The XDS560 Rev D cable supports a remote system reset capability. The
SYSRST signal from the 20-pin Emulator header on your board must be
pulled up (we suggest a 4.7 ohm pull-up) to the target voltage level
required by your board’s power-up-reset circuit. You can then remotely
through CCS apply a reset your target system from the Debug->Advance
Reset->System Reset menu. The STSRST signal will be active for ~1
millisecond.

.. rubric:: Adapters
   :name: adapters

**This page is no longer maintained and is kept here for reference only!
Please go to this
`link <http://dev.ti.com/tirex/#/?link=Development%20Tools%2FDebug%20Probes%2FXDS%2FDocuments%2FJTAG%20Adapters>`__
for the most current version.**

.. rubric:: JTAG Adapter Overview
   :name: jtag-adapter-overview

There are two types of connectors:

#. Emulator-This is the connector on the emulator/JTAG ICE/UIF/XDS unit
#. Target-This is the connector on the target card

Types of adapters:

#. Pin Converters-Passive conversion of one connector type to another
#. Adapter-Some active components for different purposes. Ex: Addition
   of adaptive clocking, buffering of TCK/RTCK signals, Isolation, etc.

.. rubric:: JTAG connectors cross reference
   :name: jtag-connectors-cross-reference

| TI Part Number, Link to product, or 3rd party product Number
| **Note:** The table below only references adapters available by TI and
  its direct third parties. It is possible to find other adapters for
  sale from external companies.

**Target connector**

**10-pin ARM**

**14-pin TI**

**20-pin TI**

**20-pin ARM**

**60-pin TI**

**60-pin MIPI**

**microSD**

**Emulator Connector**

**10-pin ARM**

N/A

N/A

N/A

**`MDL-ADA2 <http://processors.wiki.ti.com/index.php/JTAG_Adapters#MDL-ADA2>`__**

N/A

N/A

N/A

**14-pin TI**

N/A

| **`TMDSADP1414-ISO <http://processors.wiki.ti.com/index.php/JTAG_Adapters#TMDSADP1414-ISO>`__**\ :sup:`1`
| **`TMDSADP1414 <http://processors.wiki.ti.com/index.php/JTAG_Adapters#TMDSADP1414>`__**\ :sup:`2,3,4`
| **701208**\ :sup:`2,7`
| **701210**\ :sup:`2,3,4,7`

| **`TMDSADP1420 <http://processors.wiki.ti.com/index.php/JTAG_Adapters#TMDSADP1420>`__**\ :sup:`2,3,4`
| **`TMDSADPEMU-20T <http://processors.wiki.ti.com/index.php/JTAG_Adapters#TMDSADPEMU-20T>`__**\ :sup:`3`
| **701212**\ :sup:`2,3,4,7`
| **701219**\ :sup:`7`
| **14e_TI-20t_cTI**\ :sup:`6`

| **`TMDSADPEMU-20A <http://processors.wiki.ti.com/index.php/JTAG_Adapters#TMDSADPEMU-20A>`__**\ :sup:`3`
| **701280**\ :sup:`7`

| **`TMDSADP1460 <http://processors.wiki.ti.com/index.php/JTAG_Adapters#TMDSADP1460>`__**
| **14e_TI-60t_TI**\ :sup:`6`

 **`701282 <http://www.spectrumdigital.com/product_info.php?cPath=33&products_id=264&osCsid=0275b43739c81e0cb6aae06df25ced81>`__**\ :sup:`7`

N/A

**20-pin TI**

**selected emulators**\ :sup:`8,15`

| **20e_cTI-14t_TI**\ :sup:`6`
| **701218**\ :sup:`7`
| **selected emulators**\ :sup:`8,9,10,11,12,15`

N/A

| **20e_cTI-20t_ARM**\ :sup:`6`
| **selected emulators**\ :sup:`10,15`

**20e_cTI-60t_TI**\ :sup:`6`

N/A

**701206**\ :sup:`7`

**20-pin ARM**

**`MDL-ADA2 <http://processors.wiki.ti.com/index.php/JTAG_Adapters#MDL-ADA2>`__**

**LA-7748**\ :sup:`5`

**`TMDSADPEMU-20T <http://processors.wiki.ti.com/index.php/JTAG_Adapters#TMDSADPEMU-20T>`__**\ :sup:`3`

**`TMDSADPEMU-20A <http://processors.wiki.ti.com/index.php/JTAG_Adapters#TMDSADPEMU-20A>`__**\ :sup:`3`

N/A

N/A

N/A

**60-pin TI**

N/A

**60e_TI-14t_TI**\ :sup:`6`

N/A

N/A

**60e_TI-60t_TI**\ :sup:`6`

N/A

N/A

**60-pin MIPI**

N/A

| **60e_MIPI-14t_TI**\ :sup:`6`
| **selected emulators**\ :sup:`13,14`

| **60e_MIPI-20t_cTI**\ :sup:`6`
| **selected emulators**\ :sup:`13,14`

| **60e_MIPI-20t_ARM**\ :sup:`6`
| **selected emulators**\ :sup:`13,14`

| **60e_MIPI-60t_TI**\ :sup:`6`
| **selected emulators**\ :sup:`14`

N/A

N/A

|
| :sup:`1` Isolation adapter
| :sup:`2` Voltage Translation
| :sup:`3` RTCK Signal Boost
| :sup:`4` Adaptive Clocking
| :sup:`5` http://www.lauterbach.com/frames.html?order/ord__7748.html -
  Code JTAG-ARM-CON-20-TI14
| :sup:`6` http://www.blackhawk-dsp.com/products/PinConverters.aspx
| :sup:`7` http://www.spectrumdigital.com/index_orig.php?cPath=33
| :sup:`8` Bundled with `Blackhawk XDS100v2 Model
  D <http://www.blackhawk-dsp.com/products/USB100v2D.aspx>`__
| :sup:`9` Bundled with `Spectrum Digital
  XDS100v3 <http://www.spectrumdigital.com/product_info.php?cPath=22&products_id=251>`__
| :sup:`10` Bundled with Spectrum Digital
  `XDS200 <http://www.spectrumdigital.com/product_info.php?cPath=22&products_id=261>`__
  and
  `XDS220 <http://www.spectrumdigital.com/product_info.php?cPath=22&products_id=260>`__
  emulators
| :sup:`11` Bundled with Blackhawk XDS560 emulators:
  `BP <http://www.blackhawk-dsp.com/products/USB560BP.aspx>`__ (only 20
  TI to 14 TI),
  `m <http://www.blackhawk-dsp.com/products/USB560.aspx>`__,
  `LAN <http://www.blackhawk-dsp.com/products/LAN560.aspx>`__,
  `PCI <http://www.blackhawk-dsp.com/products/PCI560.aspx>`__.
| :sup:`12` Bundled with `Spectrum Digital XDS560v2 LC
  Traveler <http://www.spectrumdigital.com/product_info.php?products_id=254>`__
  and `Spectrum Digital XDS560v2 STM
  Traveler <http://www.spectrumdigital.com/product_info.php?cPath=22&products_id=249>`__
| :sup:`13` Bundled with `Blackhawk
  USB560v2 <http://www.blackhawk-dsp.com/products/USB560v2.aspx>`__
| :sup:`14` Bundled with `Blackhawk
  XDS560v2 <http://www.blackhawk-dsp.com/products/XDS560v2.aspx>`__ and
  `Spectrum Digital XDS560v2 STM with target
  adapters <http://www.spectrumdigital.com/product_info.php?cPath=22&products_id=236>`__
| :sup:`15` Bundled with `Blackhawk
  XDS200 <http://store.blackhawk-dsp.com/default/usb200-jtag-emulator-1.html>`__
  emulators

Part numbers:
=============

TMDSADP1414
-----------

| Product page:
  http://focus.ti.com/docs/toolsw/folders/print/tmdsadp.html

.. raw:: html

   <div class="floatnone">

.. Image:: /images/TMDSADP1414.jpg

.. raw:: html

   </div>

|

TMDSADP1414-ISO
---------------

| Product page:
  http://focus.ti.com/docs/toolsw/folders/print/tmdsadp.html

.. raw:: html

   <div class="floatnone">

.. Image:: /images/TMDSADP1414-ISO.jpg

.. raw:: html

   </div>

|

TMDSADP1420
-----------

| Product page:
  http://focus.ti.com/docs/toolsw/folders/print/tmdsadp.html

.. raw:: html

   <div class="floatnone">

.. Image:: /images/TMDSADP1420.jpg

.. raw:: html

   </div>

|

TMDSADP1460
-----------

| Product page:
  http://focus.ti.com/docs/toolsw/folders/print/tmdsadp.html

.. raw:: html

   <div class="floatnone">

.. Image:: /images/TMDSADP1460.jpg

.. raw:: html

   </div>

|

TMDSADPEMU-20A
--------------

| Product page:
  http://focus.ti.com/docs/toolsw/folders/print/tmdsadp.html

.. raw:: html

   <div class="floatnone">

.. Image:: /images/TMDSADPEMU-20A.png

.. raw:: html

   </div>

|

TMDSADPEMU-20T
--------------

| Product page:
  http://focus.ti.com/docs/toolsw/folders/print/tmdsadp.html

.. raw:: html

   <div class="floatnone">

.. Image:: /images/TMDSADPEMU-20T.png

.. raw:: html

   </div>

|

MDL-ADA2
--------

| Replica of the old Luminary product page at
  `Digi-key <http://media.digikey.com/pdf/Data%20Sheets/Texas%20Instruments%20PDFs/MDL-ADA2.pdf>`__
  and at `Farnell <http://www.farnell.com/datasheets/1520171.pdf>`__

.. raw:: html

   <div class="floatnone">

.. Image:: /images/MDL-ADA2_cables.jpg

.. raw:: html

   </div>

|

|

|

--------------

Frequently Asked Questions
==========================

Q: I have an XDS560 right now, but it is an older one (ex: XDS560 v1 but not revision D). How do I upgrade my XDS560 cable to gain the additional features such as wait in reset, additional connection types, etc. (i.e. revison D)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-  A: You can order from TI distributors the part number: TMDSCBL560
   (6/18/2010: This product is no longer available. You may be able to
   order one from Blackhawk)
-  A: Recommend you contact your XDS560 manufacturer and determine what
   upgrade options are available.

Q: What if I want to use the XDS560 Trace capability to collect trace from the pins?
------------------------------------------------------------------------------------

-  A: You will need the XDS560 Trace unit. There are more details here:
   `XDS560 Trace <http://processors.wiki.ti.com/index.php/XDS560_Trace>`__

Q: Do any XDS560-class Emulators support Linux Operating Systems?
-----------------------------------------------------------------

-  A: Yes. Starting with CCS v5, the following Blackhawk models support
   operation on Linux:

**LAN560** (BH-LAN-560), **USB560-M** (BH-USB-560m), **USB560-BP**
(BH-USB-560bp), **USB560** (BH-USB-560)

For XDS560v2 models, see `XDS560v2 System
Trace <http://processors.wiki.ti.com/index.php/XDS560v2_System_Trace>`__

Q: Does the XDS560 support ARM Adaptive clocking?
-------------------------------------------------

-  A: Yes, any XDS560 which is Revision D and above supports adaptive
   clocking. See: `Adaptive Clocking <http://processors.wiki.ti.com/index.php/Adaptive_Clocking>`__
   for details on Adaptive Clocking.
-  A: For CCSv3.3 with Service Release 12 and above, you can setup for
   adaptive clocking as in the photo below:

.. Image:: /images/Ccsv33adaptive.jpg

-  A: For CCS v4.x, you can setup adaptive clocking as in the photo
   below:

.. Image:: /images/Ccsv4adaptive.jpg

Q: What is the difference between `XDS510 <http://processors.wiki.ti.com/index.php/XDS510>`__ and XDS560?
----------------------------------------------------------------------------

-  A: XDS560 is capable of `High Speed RTDX
   (HSRTDX) <http://processors.wiki.ti.com/index.php/High_Speed_RTDX_(HSRTDX)>`__, essentially it has
   the same functionality of an `XDS510 <http://processors.wiki.ti.com/index.php/XDS510>`__ class
   emulator but is significantly faster, with data rates of over 2MBps.

Q: Where to get an XDS560
-------------------------

-  XDS560 are available from `TI E-store <http://www.ti.com/xds560>`__.
-  Embest's TDS560 plus
   `Here <http://www.timll.com/chinese/product/TDS560.asp>`__.
-  Ashling's Opella-XDS560
   `here <http://ashling.com/index.php?option=com_content&task=view&id=326>`__.

Q: Problems with XDS560.sys Loading
-----------------------------------

-  A: While working with CCS emulation (Blackhawk) setup, receives error
   stating TMS320C62XX" is not supported. It is because "XDS560.SYS" was
   not loading correctly.

There are two versions of xds560.sys in the system. Version A and
Version B

Version A: c:\winnt\system32\xds560.sys Version B:
c:\winnt\system32\drivers\xds560.sys

The system actually looks in the second location for the driver, but
this version (B) can hang at boot time. Sometimes the xds560.inf file
may not copy the correct files from/to the appropriate directories.
Rather than edit xds560.inf, the workaround is to create a dummy
directory c:\winnt\system32\drivers\Win2000_XP and put the working (A)
version of the file in it. Then the New Hardware Found dialogue runs to
completion and copies the correct file to the correct directory.

Q: I have a Blackhawk XDS560 USB/Lan560. What does the LED indicate?
--------------------------------------------------------------------

-  A: On the USB560m/LAN560, the USB LED is bi-color (red and green).
   This is the same for the USB560bp LED on the end panel.

Start-up: Power-up: RED Enumeration Complete: GREEN

|
| In operation, USB status: Ready: GREEN Busy: RED

Q: My JTAG is not working with CCS...
-------------------------------------

-  A: Please check: `Debugging JTAG Connectivity
   Problems <http://processors.wiki.ti.com/index.php/Debugging_JTAG_Connectivity_Problems>`__

Q: Are there lower cost options?
--------------------------------

-  A: Yes, Please see `XDS510 <http://processors.wiki.ti.com/index.php/XDS510>`__ and
   `XDS100 <http://processors.wiki.ti.com/index.php/XDS100>`__
-  Ashling's Opella-XDS560
   `here <http://ashling.com/index.php?option=com_content&task=view&id=326>`__
   is less than $1500.

Q: Why does my Windows Device Manager show a warning for the TI XDS560 PCI Emulator?
------------------------------------------------------------------------------------

.. Image:: /images/560pcierror.jpg

-  A: The Windows Device Manager is showing this error because a TI
   XDS560 PCI emulator is not installed. Windows cannot start the driver
   because the hardware is not installed in the PC. If you are NOT using
   this hardware emulator, then there is no issue and other emulators
   are not affected.

Q: I am a TI 3rd party, and I want to create my own XDS510. What do I do?
-------------------------------------------------------------------------

-  A: Approved, TI 3rd parties can purchase an `Emulation Porting
   Kit <http://processors.wiki.ti.com/index.php/Emulation_Porting_Kit>`__

Q: How do I get looback in a TI XDS560 Rev D cable to work?
-----------------------------------------------------------

-  A: You will need to fix the connection XML file or as an extra board
   config file. You will need to insert one of the following
   combinations depending on what you are doing. (Note, this is not
   tested extensively.)
-  A: This has been filed as an enhancement request (SDSCM00036610) for
   a fix in a future release.

::

    # This combination loops the TCLKO/TCKI signals in the pod – the timing between return data and clock is modified.
    # DBGJTAG handles this OK if the target provides compatible return data timing.
    # CCS drivers won’t will handle this OK if the target provides compatible return data timing.
    # The XDS560 Trace pod also comprehends this combination and uses it with specific targets.
    loopback_mode=enable
    loopback_value=clock

    # this combination loops the TDI/TDO signals in the pod – the IR/DR scan-paths become 0-bits long
    # DBGJTAG handles this OK.
    # CCS drivers fail – they won’t find the target DSP/ARM/icepick
    loopback_mode=enable
    loopback_value=data

    # This combination loops the TDI/TDO and TCLKO/TCKI signals in the pod and disables the cable-break/power-loss detection.
    # The intention is to allow DBGJTAG to run emulator and cable tests even when the cable is not connected to any target al all.
    # DBGJTAG handles this OK.
    # CCS drivers fail – they won’t find the target DSP/ARM/icepick
    loopback_mode=enable
    loopback_value=total

    # this combination does nothing
    loopback_mode=disable
    loopback_value=disable

Q: How do I get loopback in a Blackhawk XDS560 with a 20 pin cable (Rev D) cable to work?
-----------------------------------------------------------------------------------------

-  In CCS v4.x, you need to select the loopback option.

.. Image:: /images/Bh560m-revd-loopbackenable.jpg

Q: Can I use Boundary Scan with XDS560?
---------------------------------------

-  Corelis has software which works with Blackhawk XDS560. See
   `here <http://blackhawk-dsp.com/boundaryscan.aspx>`__

Q: Is RTDX supported with C2000 processors on the XDS560?
---------------------------------------------------------

-  No

Related
=======

-  `XDS100 <http://processors.wiki.ti.com/index.php/XDS100>`__
-  `XDS510 <http://processors.wiki.ti.com/index.php/XDS510>`__
-  `XDS560v2 System Trace <http://processors.wiki.ti.com/index.php/XDS560v2_System_Trace>`__
-  `XDS560 Trace <http://processors.wiki.ti.com/index.php/XDS560_Trace>`__
