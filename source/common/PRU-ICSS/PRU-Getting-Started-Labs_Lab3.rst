.. _pru_getting_started_labs_lab_3:

Lab 3: How to Compile PRU Firmware
----------------------------------

.. contents:: :local:

PRU firmware is compiled into different binary formats depending on what loads
the firmware into the PRU.

 * If a Linux core loads the PRU firmware, then the PRU firmware must be
   compiled into an ELF file (i.e., a .out file).
 * If an RTOS core loads the PRU firmware, then the PRU firmware must be
   compiled into a hex array.
 * If CCS loads the PRU firmware, then the PRU firmware can be compiled into
   an ELF file (i.e., a .out file).

.. note::

   If generating a hex array, please use PRU Compiler 2.3.1 or later.


.. _pru_getting_started_labs_compiling_from_ccs:

Compiling From CCS
^^^^^^^^^^^^^^^^^^


.. _pru_getting_started_labs_compiling_to_dot_out_file:

Compiling to a .out File
""""""""""""""""""""""""

#. Select Project -> Build Project.

#. The project should compile successfully! If not, correct any errors
   until the software build completes.

Jump to :ref:`pru_getting_started_labs_ccs_compiler_settings` for more details
about C compiler settings.


.. _pru_getting_started_labs_compiling_to_hex_array_file:

Compiling to a Hex Array File
"""""""""""""""""""""""""""""

#. Select **Project -> Properties -> Build -> PRU Linker -> Advanced Options ->
   Symbol Management.**

   * In the box labled **Specify program entry point for the output module** enter
     the label for the main program (if unsure, enter "main").

   .. TODO: insert image


#. Select **Project -> Properties -> Build -> PRU Hex Utility**

   * Check the **Enable PRU Hex Utility** box.

#. Select **Project -> Properties -> Build -> PRU Hex Utility -> Output Format Options**

   * Set Output format to **Array (--array)**.

   .. TODO: insert image

#. Select **Apply and Close**.

#. Select Project -> Build Project.

#. There should be a **.hex** file within the **Debug** folder. This .hex can be
    renamed to a .h and added to a Cortex project, which will allow the Cortex
    to load the PRU code to the IRAM of the PRU.


.. _pru_getting_started_labs_ccs_compiler_settings:

CCS Compiler Settings
"""""""""""""""""""""

The PRU C Compiler settings can be adjusted at **Project -> Properties -> Build
-> PRU Compiler**. In particular, these compiler settings may be of interest:

 * **Optimization**: The PRU Getting Started Labs use optimization level "off"
   to make it easier to relate the generated PRU assembly instructions to the C
   code. Different optimization levels will be useful for different projects.
   Reference the `PRU Optimizing C/C++ Compiler User's Guide <https://www.ti.com/lit/spruhv7>`__,
   chapter "Optimizing Your Code" for more information.

 * **Advanced Options > Assembler Options**: The C compiler can generate
   assembly code from C code. The generated assembly code can be used as a
   starting point for assembly development. Select "Keep the generated assembly
   language (.asm) file (--keep_asm, -k)".

.. TODO: Add screenshot

.. TODO: Any other C compiler settings to point to?

Ready to load the PRU firmware? Go to :ref:`pru_getting_started_labs_lab_4`.


.. _pru_getting_started_labs_compiling_from_linux:

Compiling From Linux
^^^^^^^^^^^^^^^^^^^^

#. Navigate to the PRU project directory.

#. Run "make" from the terminal.

   * If the PRU_CGT (PRU code generation tools) environment variable was not
     set, there will be an error.

     * Most Processor SDK Linux distributions package the PRU_CGT at
       sdk/linux-devkit/sysroots/x86_64-arago-linux/usr/share/ti/cgt-pru

     * If needed, the PRU code generation tools (PRU_CGT) can be downloaded from
       https://www.ti.com/tool/PRU-CGT

   * Some of the include paths in the Makefile may need to be adjusted depending
     on where the PRU project is located.

   * If needed, Makefiles in projects under <PSSP_PATH>/examples/<processor> can
     be used as a template.

 * The generated project files will be available in a folder named **gen** in
   the project directory

 * Previously generated files can be removed with "make clean"


.. _pru_getting_started_labs_linux_compiler_settings:

Linux Compiler Settings
"""""""""""""""""""""""

The PRU C Compiler settings can be adjusted in the project Makefile with
variable **CFLAGS**. In
particular, these compiler settings may be of interest:

 * **Optimization**: Different projects in the PSSP have different levels of
   optimization. For example, projects under <PSSP>/examples have optimization
   level 2 (-O2) by default, while projects under
   <PSSP>/labs/Getting_Started_Labs/<project>/solution/<processor>/ have
   optimization turned off (-Ooff).The PRU Getting Started Labs folders use
   optimization level "off"
   to make it easier to relate the generated PRU assembly instructions to the C
   code. Different optimization levels will be useful for different projects.
   Reference the `PRU Optimizing C/C++ Compiler User's Guide <https://www.ti.com/lit/spruhv7>`__,
   chapter "Optimizing Your Code" for more information.

 * **Advanced Options > Assembler Options**: The C compiler can generate
   assembly code from C code. The generated assembly code can be used as a
   starting point for assembly development. Keep the generated assembly
   language (.asm) file with compiler flags **--keep_asm or -k**.

.. TODO: Add screenshot

.. TODO: Any other C compiler settings to point to?

Ready to load the PRU firmware? Go to :ref:`pru_getting_started_labs_lab_4`.
