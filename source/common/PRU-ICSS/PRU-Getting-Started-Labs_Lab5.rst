.. _pru_getting_started_labs_lab_5:

Lab 5: Basic Debugging of PRU Firmware
--------------------------------------

.. contents:: :local:

.. note::

   AM62x support for PRU debug from CCS is added in **Sitara device support
   version 1.6.1**. To check the version number of the currently installed
   **Sitara device support**, go **Help > About Code Composer Studio >
   Installation Details > Installed Software > Sitara device support**.
   The package can be updated from that menu, or from **Help > Check for
   Updates**.

.. _pru_getting_started_labs_debugging_from_ccs:

Debugging the PRU from CCS
^^^^^^^^^^^^^^^^^^^^^^^^^^

This section demonstrates how to use different features in CCS to debug
the PRU Firmware.

.. contents:: :local:


.. _pru_getting_started_labs_debugging_from_ccs_c_code:

Debugging C Code
""""""""""""""""

This section is based on the **c_code** example. Before following these steps, build
the **c_code** firmware, initialize the PRU from CCS, and load the **c_code** firmware
into the PRU.

#. Set up the debugging environment in CCS:

   * Select **Window -> Show View -> Registers**

   * Select **Window -> Show View -> Memory Browser**

   * Select **Window -> Show View -> Disassembly**

   * Select **Window -> Show View -> Variables**

   * Take note of where the windows have appeared. Some Views may be different
     tabs sharing the same window.

#. In the **Debug** view, select the PRU core that has the firmware loaded. The
   core should say **(Suspended - SW Breakpoint)**.

   .. TODO: add an image here

#. Get familiar with important buttons in the debug interface. Hover the mouse
   over a button to see the button's name.

   * "Resume" places the PRU firmware into a "running" state

   * "Suspend" pauses the PRU core. The PRU core must be paused in order to view
     memory values, edit variables, etc.

   * "Terminate" closes the debug session.

   * "Step Into" takes one step through the C code, and then pauses the PRU
     core. Note that a single step in C
     code may translate to several steps in the generated assembly code running
     on the PRU core. If there is a function, "Step Into" will jump into the
     function and pause at the first C instruction within the function.

   * "Step Over" takes one step through the C code, and then pauses the PRU
     core. Note that a single step in C
     code may translate to several steps in the generated assembly code running
     on the PRU core. If there is a function, "Step Over" will step over the
     function and pause at the first C instruction after the function.

   * "Restart" moves the Program Counter (PC) back to the program entry point.
     It does NOT actually reset the core under debug.

   * "Assembly Step Into" is like "Step Into", but it steps to the next assembly
     instruction instead of stepping to the next line of C code.

   * "Assembly Step Over" is like "Step Over",but it steps to the next assembly
     instruction instead of stepping to the next line of C code.

   .. TODO: Place image here

   .. TODO: Discuss breakpoints, suspend, resume?

#. If you clicked on any of the buttons in the previous step, click on "Restart"
   to get back to the program entry point.

#. Use the "Step Over" or "Step Into" buttons to step through the PRU function
   to the beginning of the while loop.


.. rubric:: Reading and modifying values in memory

Navigate to the **Memory Brower** window.

   #. Select **Data_Memory**.

   #. In the **Enter location here** box, type in the address for **a** (0x110).
      The value assigned to **a** should be stored there. The value assigned to
      **b** should be stored in 0x114, and 0x118 should hold the value for
      **c**.

   #. Step through the loop once. The value at 0x118 should now equal **a** + **b**.

   #. Double click the block of memory at 0x110 in the memory browser. Change
      the value to a new number (i.e., assign a new value to **a**). Press the
      **enter** key on the keyboard to save the new value of **a**.

   #. Step through the loop again. The value at 0x118 (i.e., **c**) should change.


.. rubric:: Reading and modifying variable values

Navigate to the **Variables** window. Variables x, y, and z are defined here.

.. note::

   CCS 11.2 has a bug in the **Variables** window at the time of writing. The
   variables are stored in one location on the stack, but the CCS debugger
   thinks that the variables are stored in a different location. This bug does
   not affect PRU functionality, but it does mean that the **Variables** window
   is not useful for debugging. The bug is fixed in CCS 12.1 as per
   `this e2e thread <https://e2e.ti.com/support/processors-group/processors/f/processors-forum/1104252/am6442-pru-ccs-variables-view-pointing-to-the-wrong-memory-location/4109925#4109925>`__.
   Lab steps are written as if the Variables window is working properly.
   Workaround steps are documented as notes.

The **Variables** window shows the value of a variable, as well as the
variable's location in memory.

Variables x, y, and z should be saved to the stack.

Check the linker command file to see where the stack is located:

 #. Look in the
    upper right of the screen. CCS is currently in the "CCS Debug" perspective.
    Click on the "CCS Edit" perspective to exit the "CCS Debug" perspective.

    .. TODO: Add image

 #. In the PRU project, open the linker command file.

    * AM64x example: Open AM64x_PRU0.cmd

 #. Scroll down to the **SECTIONS {** portion of the linker command file.

 #. The PSSP examples place .stack at the very beginning of the PRU data memory.

    * AM64x example:

      ::

         /* Specify the sections allocation into memory */
         SECTIONS {
             /* Forces _c_int00 to the start of PRU IRAM. Not necessary when loading
                an ELF file, but useful when loading a binary */
             .text:_c_int00*	>  0x0, PAGE 0

             .text		>  PRU_IMEM, PAGE 0
             .stack		>  PRU0_DMEM_0, PAGE 1

The stack will begin at address 0x0 in the PRU core's data memory. But how large
is the stack?

 #. Select **Project -> Properties -> Build -> PRU Linker -> Basic Options**

 #. The heap and stack sizes are blank. The default stack size is 0x100. If a
    different stack size is needed for the project, change it here.

 #. CCS notifies the user about the default stack size. After building
    the PRU project, check the **Problems** view. CCS will say that a default
    size of 0x100 was used for the stack.

.. TODO: Add image

.. TODO: Should we talk about modifying the stack in the "Writing PRU code" section?

Now we know that the stack has a size of 0x100 and begins at address 0x0 in the
PRU data memory. Click the "CCS Debug" button in the upper right of the
screen to return to the Debug perspective.

Make sure the **Variables** window is still visible. In the **Memory Brower**
window:

   #. Select **Data_Memory**.

   #. In the **Enter location here** box, type in the address of the stack
      (0x0 by default).

   #. The variable values listed in the **Variables** view should be visible in
      the **Memory Browser** at the location listed in the **Variables** table:

      .. TODO: Add image

      .. note::

         As of June 2022, the location of x, y, z in the stack does NOT
         match the location of x, y, and z in the variables view. For example,
         in my tests, x was stored in the stack at 0xF0, y was stored at 0xF4,
         and z was stored at 0xF8. However, the **Variables** view thought
         that x, y, and z were stored at 0x0, 0x4, and 0x8, respectively. Check
         whether the values of x, y, and z in the **Variables** view match the
         values of the variables in the main.c code. If they do not match, then
         variable values cannot be changed through the **Variables** view.

   #. Click on the **Value** cell of a variable in the **Variables** view. type
      a new number, and press the **enter** key on the keyboard. The value in
      the **Memory Browser** will change:

      .. TODO: Add image

      .. note::

         If the **Variables** view bug happens, do NOT change the variable
         values in the **Variables** view. Instead, find the true location of
         the variables in the stack. An easy way to do this is to press the
         "Terminate" button to terminate the debug session. Power cycle the
         board, and start a new debug session. This will reset the PRU data
         memory. Then,
         watch the **Memory Browser** while stepping through the variable
         initialization. Note the memory address of each variable as it is
         initialized and its value is placed on the stack. Then, adjust variable
         values through the **Memory Browser**.


.. rubric:: Reading and modifying register values

Navigate to the **Registers** window. Click on "Restart" to return to the
program entry point.

#. Expand the **core registers** dropdown.

#. Step through the C code. The register values will change. PRU programs
   written in assembly code specify exactly which core register is doing
   what. However, for C code, the PRU compiler determines which values go in
   which registers.

#. If needed, register values can be changed by clicking on the **Value**
   cell and typing in a new hexadecimal value.


.. rubric:: Viewing and navigating assembly code

#. Navigate to the **Disassembly** window. This window shows what
   assembly code was generated from the C code.

#. Click the "Step Into" button several times. Note that the blue arrow
   representing the Program Counter (PC) in the main.c view matches the blue
   arrow representing the PC in the **Disassembly** view.

#. Return to the **Register** window. Under **Core Registers**, select PC and
   change it to a different memory location. The PC arrows in main.c and the
   Disassembly view should jump to the new program counter location.

   .. note::

      Be careful when manually changing the Program Counter. The PRU firmware
      does not know when the PC value is manually changed, so register values,
      memory values, etc may be different from what the PRU firmware expects.

#. Click on "Restart" to return to the program entry point.

#. In the **Disassembly** view, notice how there can be multiple assembly
   instructions under a single line of C code. Click the "Step Into" button.
   The PC will jump forward to the next line of C code, instead of the next
   assembly instruction.

#. Click the "Assembly Step Into" button. This
   button allows us to step from one assembly instruction to the next. There are
   also "Assembly Step Into" and "Assembly Step Over" buttons within the
   **Disassembly** view.

   .. TODO: Add image

.. note::

   The disassembly instructions in the Getting Started Guide directly
   align with the C code because the PRU compiler is not performing any code
   optimization. If the PRU compiler performs software optimization for speed or
   memory size, the generated assembly may be organized differently from the
   original C code. If the PRU use case requires exact timing, we suggest
   writing the time sensitive code in assembly rather than C in order to give
   the developer complete control over the PRU instructions.

.. TODO: Link to other debugging resources here?


.. _pru_getting_started_labs_debugging_from_ccs_assembly:

Debugging Assembly Code
"""""""""""""""""""""""

This section is based on the assembly_code example. Before following these
steps, build the assembly_code firmware, initialize the PRU from CCS, and load
the assembly_code firmware into the PRU.

#. Set up the debugging environment in CCS:

   * Select **Window -> Show View -> Registers**

   * Select **Window -> Show View -> Memory Browser**

   * Select **Window -> Show View -> Disassembly**

   * Select **Window -> Show View -> Variables**

   * Take note of where the windows have appeared. Some Views may be different
     tabs sharing the same window.

#. In the **Debug** view, select the PRU core that has the firmware loaded. The
   core should say **(Suspended - SW Breakpoint)**.

   .. TODO: add an image here

#. Get familiar with important buttons in the debug interface. Hover the mouse
   over a button to see the button's name.

   * "Resume" places the PRU firmware into a "running" state

   * "Suspend" pauses the PRU core. The PRU core must be paused in order to view
     memory values, edit variables, etc.

   * "Terminate" closes the debug session.

   * "Restart" moves the Program Counter (PC) back to the program entry point.
     It does NOT actually reset the core under debug.

   * "Assembly Step Into" takes a single step to the next assembly instruction
     and pauses. If there is a subroutine or function, "Step Into" will jump
     into the subroutine or function and pause at the first assembly instruction
     within the subroutine or function.

   * "Assembly Step Over" takes a single step to the next assembly instruction
     and pauses. If there is a subroutine or function, "Step Into" will jump
     over the subroutine or function and pause at the first assembly instruction
     after the subroutine or function.

   .. TODO: Place image here

   .. TODO: Discuss breakpoints, suspend, resume?


.. rubric:: Reading and modifying values in memory

The assembly_code project does not read or modify values in memory. Refer to
:ref:`pru_getting_started_labs_debugging_from_ccs_c_code` for steps on how
to read and modify memory values in the **Memory Brower** window.


.. rubric:: Reading and modifying variable values

The assembly_code project does not read or modify variables. Refer to
:ref:`pru_getting_started_labs_debugging_from_ccs_c_code` for steps on how
to read and modify variable values in the **Variables** window.

.. TODO: Should we talk about the stack here, since we talk about it in the C
   code section?


.. rubric:: Reading and modifying register values

Navigate to the **Registers** window. Click on "Restart" to return to the
program entry point.

#. Expand the **core registers** dropdown.

#. Step through the assembly code. The register values will change.

#. If needed, register values can be changed by clicking on the **Value**
   cell and typing in a new hexadecimal value.

Before changing any register values, let's take a closer look at exactly what
the assembly code is doing.


.. rubric:: Viewing and navigating assembly code

#. Navigate to the **Disassembly** window. This window shows what
   processor instructions were generated from the assembly code.

#. Click the "Assembly Step Into" button several times. Note that the blue arrow
   representing the Program Counter (PC) in the main.asm view matches the blue
   arrow representing the PC in the **Disassembly** view. One assembly
   instruction in main.asm will be related to one assembly instruction in the
   **Disassembly** window.

#. Return to the **Register** window. Under **Core Registers**, select PC and
   change it to a different memory location. The PC arrows in main.c and the
   Disassembly view should jump to the new program counter location.

   .. note::

      Be careful when manually changing the Program Counter. The PRU firmware
      does not know when the PC value is manually changed, so register values,
      memory values, etc may be different from what the PRU firmware expects.

#. Click on "Restart" to return to the program entry point.

#. Click the  "Assembly Step Into" button until the PC reaches the
   **while_true** function.

#. Notice how the command **ldi	x_register, x** was interpreted in the
   **Disassembly** view. **x** was converted into a static value of **1**
   instead of a variable that can be changed.

   .. TODO: Add image

#. Step all the way through the **while_true** loop. The value of R22 should
   update to equal R20 + R21.

#. What if we want to change the values getting passed to the assembly
   instruction **add z_register, x_register, y_register**? The LDI commands
   will overwrite any value in R20 and R21 every while loop.

#. Step until the PC is pointing to **add z_register, x_register, y_register**.
   At this point, the two LDI commands just executed. The very next PRU clock
   cycle, the ADD command will execute.

#. Go to the **Registers** view and enter new values in for R20 and R21.

#. Step one more time. R22 should update with the sum of the new values that
   were entered in. Stepping through the loop again should replace all register
   values with the values that were hardcoded in instruction memory.

.. TODO: point to other debugging resources here?


.. _pru_getting_started_labs_debugging_from_linux:

Debugging the PRU from Linux Core
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section is based on the **c_code** project. Before following these steps, build
the **c_code** firmware, and use the sysfs interface to load the **c_code** firmware
into the PRU.

.. TODO: How to set up CCS to debug while Linux is running? probably a later section.

CCS gives the developer many debug tools that Linux does not have access to
(pausing code, stepping through instructions, viewing internal registers, etc).
However, there are some basic tools that can be used to test firmware from Linux.

This section discusses using devmem2 to read and write values from memory.

Why is it useful for Linux to read from memory? The
PRU cores do not have an output log like other remote cores. However, the PRU
cores can write debug values to a known memory location (performing a similar function
as print() commands for other cores).

It is useful for Linux to write to memory whenever the developer wants to
pass information into the PRU.

For example, if the developer wants to inspect
memory values at a certain point during the PRU execution, they could implement
a breakpoint in their PRU firmware where the PRU waits for a value to be written
to a known memory address before it continues running. That allows the developer
to inspect memory values once the breakpoint has been reached, and then tell the
PRU core to continue running once they have finished. Such a breakpoint may look
like this:

::

   /* breakpoint1 is at PRU data memory, address 0x110 */
   #define breakpoint1  (*((volatile unsigned int *)0x110))

   ...

   breakpoint1 = 0;
   while( breakpoint1 != 1 ) {}

PRU firmware written in C can also use RPMsg to send messages to and from the
PRU cores.


.. rubric:: Determining the memory addresses to use

Variables **a**, **b**, and **c** are stored in the PRU data memory (DRAM) at
addresses 0x110, 0x114, 0x118 respectively.

In order to read the variable values from Linux, use the processor's Technical
Reference Manual (TRM) to determine where the
PRU DRAM is located. devmem2 uses the hardware addresses (not the kernel's
virtual addresses). Reference the TRM chapters for **Memory Map** and **PRU**
to find the addresses.

* AM335x example: PRU1

  *  **Memory Map > ARM Cortex-A8 Memory Map** places the **PRU_ICSS** at
     address 0x4A30_0000.

  * **PRU-ICSS > PRU-ICSS Memory Map Overview > Global Memory Map** says
    that PRU1's data memory (Data 8KB RAM 1) is at offset 0x0000_2000. Note
    that the global memory address for DRAM1 (i.e., the address that the ARM
    core uses to access that memory) is different from the local memory
    address for DRAM1 (PRU1 sees DRAM1 at offset 0x0000_0000 as per the
    **Local Data Memory Map** section).

  * Thus, **a** is at 0x4A30_2110, **b** is at 0x4A30_2114, and **c** is at
    0x4A30_2118.

* AM64x example: ICSSG1, PRU0

  *  **Memory Map > MAIN Domain Memory Map** starts listing **PRU_ICSSG1** at
     address 0x03008_0000. It also lists **PRU_ICSSG1_DRAM0_SLV_RAM** at
     address 0x03008_0000. However, let us double check the PRU chapter as
     well.

  * **Processors and Accelerators > PRU_ICSSG > PRU_ICSSG Top Level
    Resources Functional Description > PRU_ICSSG Memory Maps > Global Memory
    Map** says that PRU0's data memory (Data 8KB RAM0) is at offset
    0x0000_0000. Note that the global memory address for DRAM0 / DRAM1
    (i.e., the address that the ARM core uses to access that memory) may be
    different from the local memory address for DRAM0 / DRAM1 (i.e., cores in
    slice 1 see DRAM1 at offset 0x0000_0000 as per the
    **Local Data Memory Map** section).

  * PRU_ICSSG shared memory is different from PRU-ICSS or PRU-SS. With
    PRU_ICSSG, data memory is shared between all PRU cores in a slice
    (i.e., PRU0, RTU0, TX_PRU0 all share DRAM0, while PRU1, RTU1, TX_PRU1 all
    share DRAM1). Check the linker command file to see how the DRAM is
    divided up between the cores. The PRU Getting Started Labs do not need
    to adjust the memory allocation in the linker command file. Reference
    <PSSP>/examples/am64x/RTU_MAC_Multiply_Accum for an example of modifying
    the memory allocation.

  * Thus, **a** is at 0x03008_0110, **b** is at 0x03008_0114, **c** is at
    0x03008_0118

.. rubric:: Reading and Writing from PRU memory

Use devmem2 to read the values with **devmem2 0xADDRESS**

* AM335x example: PRU1, variable **a**

  ::

     # devmem2 0x4a30110

* AM64x example: ICSSG1, PRU0, variable **b**

  ::

     # devmem2 0x030080114

Use devmem2 to read the values with **devmem2 0xADDRESS w 0xVALUE**. Write
new values to **a** and **b**. Does the PRU update the value of **c**?

* AM335x example: PRU1, variable **a**, writing 0x5

  ::

     # devmem2 0x4a30110 w 0x5

* AM64x example: ICSSG1, PRU0, variable **b**, writing 0x6

  ::

     # devmem2 0x030080114 w 0x6
