.. _pru_subsystem_overview:

Overview of PRU Subsystem
=========================

The Programmable Real-time Unit (PRU) is a 32-bit RISC processor core that is
tightly integrated with an IO subsystem, offering low-latency control of IO
pins. The TI Sitara family of devices offer three flavors of PRU Subsystem.

.. rubric:: PRU-ICSS: The Programmable Real-time Unit and Industrial Communication Subsystem

The Programmable Real-time Unit and Industrial Communication Subsystem
(PRU-ICSS) consists of dual 32- bit RISC cores (the PRUs), shared data,
instruction memories, internal peripheral modules, and an interrupt controller
(INTC). The programmable nature of the PRU, along with its access to pins (IOs),
events and all System-on-Chip (SoC) resources, provides flexibility in
implementing fast real-time responses, specialized data handling operations,
custom peripheral interfaces, and in off-loading tasks from the other processor
cores of the SoC.

Devices offering the PRU-ICSS capability include AM335x, AM437x, AM57x and K2G.

.. rubric:: PRU_ICSSG: The Programmable Real-time Unit and Industrial Communication Subsystem - Gigabit

The Programmable Real-time Unit and Industrial Communication Subsystem - Gigabit
(PRU_ICSSG) can be considered a superset of the PRU-ICSS. In addition to all
PRU-ICSS features, the PRU_ICSSG adds two Auxiliary Programmable Real-Time Unit
(RTU) cores, two Transmit PRU (TX_PRU) cores, broadside memories, improved event
management with the task manager, data processing and data movement
accelerators, and new peripherals such as PWM.

Devices offering the PRU_ICSSG capability include AM24x, AM64x, and AM65x.

.. rubric:: PRU-SS: The Programmable Real-time Unit Subsystem

The Programmable Real-time Unit Subsystem (PRU-SS) consists of dual 32-bit RISC
cores (the PRUs), shared data, instruction memories, internal peripheral
modules, and an interrupt controller (INTC). The programmable nature of the PRU
cores, along with their access to pins, events and all device resources,
provides flexibility in implementing fast real-time responses, specialized data
handling operations, custom peripheral interfaces, and in offloading tasks from
the other processor cores of the device.

Industrial Communication Subsystem features including Ethernet (MII signals and
MDIO signals are not pinned out) are not supported.

Devices offering the PRU-SS capability include AM62x.

.. warning::

   While am62 SoC supports PRU-SS, the automotive variants of this SoC do not and therefore
   `AM62 LP SK <https://www.ti.com/tool/SK-AM62-LP>`__ does not support PRU-SS.
   PRU-SS is now disabled in u-boot source: :file:`arch/arm/mach-k3/am62x/am625_fdt.c`
   and might not be explicitly disabled with `status = "disabled"` in Linux kernel DT.

|

The PRU subsystem hardware can be used for two categories of applications:

 * General-purpose applications (using the PRU subsystem)

 * Industrial applications (using the ICSS on applicable processors)

   * See :ref:`pru_overview_evaluation_hardware` for supported boards

This overview page serves as a hub for PRU subsystem collateral and related resources
including software user guides, application notes, training modules, and FAQs.

|

.. contents:: :local:
    :depth: 1

.. _pru_overview_getting_started_information:

Getting Started Information
---------------------------

Detailed information for getting started with PRU development can be found here:

`PRU-ICSS / PRU_ICSSG Getting Starting Guide on Linux <https://www.ti.com/lit/pdf/sprace9>`__

`PRU-ICSS / PRU_ICSSG Getting Started Guide on TI-RTOS <https://www.ti.com/lit/pdf/sprach5>`__

:ref:`getting_started_with_pssp`

|

.. _pru_overview_hardware_information:

Hardware Information
--------------------

Technical Documentation
^^^^^^^^^^^^^^^^^^^^^^^

Technical documentation is provided in device-specific Technical Reference
Manuals (TRMs).

PRU Differences Between Devices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`PRU-ICSS / PRU_ICSSG Feature Comparison Across Devices <https://www.ti.com/lit/sprac90>`__

`PRU-ICSS / PRU_ICSSG Migration Guide <https://www.ti.com/lit/spracj8>`__

Miscellaneous
^^^^^^^^^^^^^

`PRU Read Latencies <https://www.ti.com/lit/sprace8>`__

|

.. _pru_overview_training_material:

Training Material
-----------------

:ref:`pru_getting_started_labs`

:ref:`pru_hands_on_labs`


.. ifconfig:: CONFIG_sdk in ('SITARA','JACINTO','j7_foundational')

   :ref:`rpmsg_quick_start_guide`

|

.. _pru_overview_development_tools:

Development Tools
-----------------

PRU C Compiler
^^^^^^^^^^^^^^

PRU C compiler is available for download through the Code Composer Studio (CCS)
App Center, or through the `PRU-CGT page <https://www.ti.com/tool/PRU-CGT>`__.

`PRU Optimizing C/C++ Compiler User's Guide <https://www.ti.com/lit/pdf/spruhv7>`__

`PRU Assembly Language Tools User's Guide <https://www.ti.com/lit/pdf/spruhv6>`__

PRU Assembly Instructions
^^^^^^^^^^^^^^^^^^^^^^^^^

`PRU Assembly Instruction Guide <https://www.ti.com/lit/pdf/spruij2>`__


|

.. _pru_overview_software_information:

Software Information
--------------------

.. ifconfig:: CONFIG_sdk in ('SITARA','JACINTO','j7_foundational')

   Linux Software information
   ^^^^^^^^^^^^^^^^^^^^^^^^^^

   RemoteProc driver information at :ref:`pru_remoteproc`

   .. ifconfig::  CONFIG_part_family in ('AM335X_family','AM437X_family')

      Information about general purpose Ethernet over PRU is at
      :ref:`pru_icss_ethernet`.

   .. ifconfig::  CONFIG_part_family in ('AM64X_family','J7_family')

      Information about general purpose Ethernet over PRU is at
      :ref:`pru_icssg_ethernet`.

   .. ifconfig:: CONFIG_part_family not in ('AM64X_family', 'AM62X_family')

      Industrial networking documentation at `Industrial Protocols <../../linux/Industrial_Protocols.html>`__

   Other information about PRU development can be found throughout this
   "PRU Subsystem" documentation.

   For RTOS software information, reference the RTOS Processor SDK
   documentation.

Firmware Software Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Information about specific components of PRU projects can be found at
:ref:`pru_resource_tables`, :ref:`pru_intc_configuration`, and
:ref:`pru_header_files`.

`PRU-ICSS / PRU_ICSSG Migration Guide <https://www.ti.com/lit/spracj8>`__

|

U-Boot Software Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^

PRU Ethernet is supported in u-boot. To use PRU Ethernet in u-boot just
select the ICSSG interface as active ethernet interface. The PRU Ethernet
interface can ping and act as a dhcp client at u-boot. PRU Ethernet can
also be used to boot the kernel using tftp.

.. code-block:: text

  setenv ethact icssg1-eth


|

.. _pru_overview_examples:

Examples
--------

.. rubric:: Generic PRU Examples

`PRU Software Support Package <https://git.ti.com/cgit/pru-software-support-package>`__


.. rubric:: Industrial Software (Industrial Drives) Examples with Firmware Source

`PRU-ICSS Industrial Software for Sitara Processors <https://software-dl.ti.com/processor-industrial-sw/esd/docs/indsw/index.html>`__

Reference "Industrial Drives" > "User Guide" > "Applications" for a list of
example firmware.

.. rubric:: Community Projects

The open source community has developed an incredible range of PRU projects:

 * `beagleboard.org <https://beagleboard.org/>`__ has a wide range of hardware,
   tutorials, and open source projects

 * Many individuals have posted projects and tutorials across the web on
   github.com, element14.com, and more. Interested in using PRU to control a
   printer, a stepper motor, or something else? Try typing "PRU beaglebone
   <search term>" into your web search engine and see what you can find!

.. note::

   TI cannot support community projects on the TI forums. For example,
   if a beagleboard.org tutorial is confusing, or a github project does not work
   as expected, please reach out to those communities directly for guidance.
   Some community projects use tools and software that TI does not support, like PASM or
   custom Linux drivers.

|

.. _pru_overview_evaluation_hardware:

Evaluation Hardware
-------------------

PRU evaluation hardware can be ordered from ti.com:

 * `PRU Cape <https://www.ti.com/tool/PRUCAPE>`__

   * :ref:`pru_cape_hardware_user_guide`

   * :ref:`pru_cape_getting_started_guide`

 * AM335x / AMIC110

   * `TMDSICE3359 <https://www.ti.com/tool/TMDSICE3359>`__

   * `TMDXICE110 <https://www.ti.com/tool/TMDXICE110>`__

 * AM437x / AMIC120

   * `TMDSIDK437X <https://www.ti.com/tool/TMDSIDK437X>`__

 * AM57xx

   * `TMDSIDK574 <https://www.ti.com/tool/TMDSIDK574>`__

   * `TMDXIDK5718 <https://www.ti.com/tool/TMDXIDK5718>`__

 * AM62x

   * `SK-AM62 <https://www.ti.com/tool/SK-AM62>`__

 * AM64x

   * PRU Networking

     * `TMDS64EVM <https://www.ti.com/tool/TMDS64EVM>`__

   * Generic PRU Development

     * `SK-AM64 <https://www.ti.com/tool/SK-AM64B>`__

 * AM65x

   * `TMDX654IDKEVM <https://www.ti.com/tool/TMDX654IDKEVM>`__

|

.. _pru_overview_ti_designs:

TI Designs
----------

TI has created multiple
`TI Reference Designs <https://www.ti.com/reference-designs>`__ around PRU
applications. Perform a Quick Search to find PRU-based TI Designs like:

 * `Flexible Interface (PRU-ICSS) Reference Design for Simultaneous, Coherent DAQ Using Multiple ADCs <https://www.ti.com/tool/TIDA-01555>`__

 * `EnDat 2.2 System Reference Design <https://www.ti.com/tool/TIDEP0050>`__

 * and more!

|

.. _pru_overview_support:

Support
-------

TI supports PRU through the `e2e forums <https://e2e.ti.com>`__.

The Beagleboard community discusses PRU `here <https://forum.beagleboard.org/>`__

:ref:`pru_overview_faq`

`FAQ for PRU-ICSS Industrial Software <https://software-dl.ti.com/processor-industrial-sw/esd/docs/indsw/FAQ_Sitara_Industrial.html>`__

|

.. _pru_overview_faq:

PRU FAQ
-------

.. contents:: :local:

PRU Applications & Support questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

What is the difference between the PRU subsystem and ICSS?
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

PRU subsystem and ICSS both refer to the same hardware (PRU-ICSS), but
their distinction lies in the targeted applications. The term "PRU
subsystem" is used for broad market (or non-industrial) applications,
while the term "ICSS" is used for industrial applications. The ICSS is
supported on applicable processors with ICE and IDK boards and Industrial
Software Kit.

Is TI providing libraries for the PRU?
""""""""""""""""""""""""""""""""""""""

TI is not providing libraries for the PRU. Customers will need to
develop their own PRU firmware. However, TI does provide the foundation
for PRU development through example software and other resources
available through the PRU-ICSS SDK Documentation.

One exception is the ICSS firmware supported with the ICE and IDK
boards.

Can I develop my own industrial protocols on the PRU-ICSS?
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

TI only supports the industrial protocols enabled in the IDK (Industrial
Development Kit) available on `ti.com <https://www.ti.com>`__.
Independent development of industrial protocols using the MII_RT and
IEP (Industrial Ethernet Peripheral) blocks in not supported or enabled.

Can the PRU run a High Level Operating System?
""""""""""""""""""""""""""""""""""""""""""""""

No, the PRU cannot run a HLOS such as Linux or Android.

My processor has a PRU. Is the PRU supported in the Linux Processor SDK?
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

It depends. OMAP138 PRU is NOT supported in Processor SDKs, and there are
no plans to add support for it. However, the latest Processor SDKs support
general purpose PRU development for AM335x/AMIC110, AM437x/AMIC120, AM57x,
AM243x, AM62x, AM64x, and AM65x. More processors will be added in
future releases.

|

PRU Memory Access questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Why does my PRU firmware hang when reading or writing to an address external to the PRU Subsystem?
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The OCP master port is in standby and needs to be enabled in the
PRU-ICSS CFG register space, SYSCFG[STANDBY_INIT].

In AM437x, why can PRU-ICSS0 not access memories outside of the ARM?
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Make sure PRU-ICSS1's OCP master port is enabled. PRU-ICSS0 accesses all
external memories through the PRU-ICSS1 OCP master port.

Why can the PRU not edit pinmux settings?
"""""""""""""""""""""""""""""""""""""""""

The PRU does not have privileges to edit the pinmux or pad config
settings in the device-level Control Module. However, the PRU can read
these registers.

|

PRU GPI/O questions
^^^^^^^^^^^^^^^^^^^

What is the maximum speed for toggling PRU GPO pins via PRU software?
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The max PRU IO speed depends on the PRU software executing on the PRU
and is therefore not published.

For example, if the PRU software contained a tight loop that **only**
toggled a PRU GPO pin, then the fastest 50% duty cycle square wave we
could achieve would be 50 MHz. This is based on a 4 instruction loop (1.
**SET** output, 2. **NOP**, 3. **CLEAR** output, 4. **LOOP** back to Set
instruction) with the PRU running at 200 MHz. However, if the PRU needed
to do any processing in addition to toggling the GPO, then that max
speed starts decreasing with the number of PRU instructions that are
executed between the GPO toggles.

When does the PRU start capturing from the input pins?
""""""""""""""""""""""""""""""""""""""""""""""""""""""

The PRU continually captures and shifts the input once the GPI mode is
set to 28-bit shift mode.

Can the module be modified so that the GPI start bit is a zero instead of a one?
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

No, the GPI start bit flag only detects the first 1 captured.

What happens after 28 bit GPI shifts?
"""""""""""""""""""""""""""""""""""""

The shift register overflows into a bit bucket.

Can data be pre-loaded into shadow registers prior to configuring the PRU GPO mode to shift out mode?
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Yes, data can be loaded into the shadow registers even when the PRU is
configured for a different GPO mode by setting PRU<n>_LOAD_GPO_SH0/1.
Note for AM335x, PRU<n>_LOAD_GPO_SH0/1 corresponds to
pru<n>_r30[29/30]. Please refer to the technical reference manuals for
other devices to confirm how PRU<n>_LOAD_GPO_SH0/1 is mapped.

When does PRU<n>_CLOCKOUT start running?
""""""""""""""""""""""""""""""""""""""""

PRU<n>_CLOCKOUT is a free-running clock that begins when the PRU GPO
mode is set to shift out mode. It is independent of
PRU<n>_ENABLE_SHIFT.

When does the PRU start shifting data in the shadow registers?
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The PRU starts shifting data as soon as the PRU<n>_ENABLE_SHIFT bit is
set, regardless of the configured GPO mode. The output on
PRU<n>_DATAOUT would only be seen if in shift out mode, but the shadow
registers would still "drain" when in other GPO modes.

The shadow registers are loaded by writing to PRU<n>_R30 [0:15]. Does this change the state of the corresponding device-level pins?
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

If any device-level pins mapped to PRU<n>_R30 [2:15] are configured for
the PRU<n>_R30 [2:15] pinmux setting, then yes, these pins will reflect
the value written to PRU<n>_R30. Any pin configured for a different
pinmux setting will **not** reflect the value written to PRU<n>_R30.

When the PRU<n>_ENABLE_SHIFT bit is cleared, does the PRU immediately stop shifting PRU<n>_DATAOUT?
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

No, when the shift operation is disabled by clearing the
PRU<n>_ENABLE_SHIFT bit, the PRU will continue shifting all the data
loaded in the shadow register used for GPO shifting (i.e.
GPCFG0/1[PRU0/1_GPO_SH_SEL]).

Does the PRU shift data out LSB or MSB first?
"""""""""""""""""""""""""""""""""""""""""""""

The PRU shifts data out LSB first. PRU<n>_R30[0] = SH0/1[0] = LSB =
first bit to be shifted out.

What happens to the content stored in R30 when the PRU changes to a different GPO mode?
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

R30 holds state when changing between GPO modes.

|

PRU INTC and System Event questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

How can a PRU core interrupt the ARM? How can the ARM interrupt a PRU core?
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The PRU can interrupt the ARM by writing to R31 and generating a system
event. The PRU INTC should be pre-configured to map this system event to
a Host interrupt that is connected to the ARM (ie Host 2-9 on AM335x).
The ARM can interrupt a PRU by writing to the PRU INTC SRSR\ *x*
register and setting a pr<k>_pru_mst_intr<x>_intr_req system event.
The PRU INTC should be pre-configured to map this system event to a Host
interrupt that is connected to the PRU (ie Host 0-1 on AM335x). The PRU
can poll R31 bit 30 or 31 to detect an interrupt on Host 0 or 1,
respectively.

On devices with multiple PRU-ICSSs, how can one PRU-ICSS interrupt the other?
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Check the PRU-ICSS System Event table in your device-specific reference
manual on `ti.com <https://www.ti.com>`__. There will be a System event
tied to a PRU Host event from the other PRU-ICSS. By generating an
interrupt of this Host, one PRU-ICSS can interrupt another PRU-ICSS. The
other PRU-ICSS will detect this interrupt as the corresponding System
event.

For example, on AM437x, the PRU can generate an interrupt on Host 7. The
other PRU-ICSS will receive this as system event 56.

|

PRU Debugger questions
^^^^^^^^^^^^^^^^^^^^^^

When using the XDS510 USB emulator, why does the PRU Program Counter not increment correctly when stepping through PRU Disassembly code?
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

There is a known bug associated with PRU debug in the XDS510 USB class
driver, and a different emulator should be used to debug the PRU. Two
good alternatives are the `XDS200 <https://www.ti.com/tool/TMDSEMU200-U>`_
or the `XDS560v2 <https://www.ti.com/tool/TMDSEMU560V2STM-U>`_ emulators.
Comparative benchmarks for various classes of XDS emulators are available
at `XDS_Performance_comparison <https://software-dl.ti.com/ccs/esd/documents/application_notes/appnote-debug_probe_performance_results.html>`_.

Why are no MMRs outside the PRU subsystem visible from the PRU perspective memory browser window in CCS?
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The PRU core is capable of writing to the 32 bit memory map (i.e. MMRs
outside of the PRU subsystem) but the PRU perspective of the CCS memory
browser just cannot show those addresses. To view the full 32 bit memory
map in a memory browser in CCS, the ARM core perspective or the DAP
(debug access port) perspective should be used.

Note the PRU perspective memory browser includes a drop-down menu for
viewing the following memories:

-  Program_Memory - Instruction ram for the PRU
-  Data_Memory - Data ram for the PRU
-  PRU_Device_Memory - The memory map inside the PRU subsystem
   starting with the base address of the shared memory (0x00010000).
   Includes PRU shared memory and all submodules inside the PRU
   subsystem.

