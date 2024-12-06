.. _pru_header_files:

Header Files
============

.. rubric:: Introduction

The header files for the PRU-ICSS were written in such a way so as to
sit on top of the memory-mapped registers. They can be directly linked
to that address range via the Linker Command File, but in the existing
examples the header files are accessed via the Constant Table registers. The
process of using cregister attributes to link header files to an address range
through the Constant Table registers is described in the `PRU Optimizing C/C++ Compiler User's Guide <https://ti.com/lit/pdf/spruhv7>`__.
Information on cregisters are in the "Type
Attributes" section. Information on the near and far keywords used in
the current examples can be found in the section "The near and far Keywords".

.. rubric:: Layout
   :name: layout

The register sets are grouped up into structures containing the
appropriate gaps for reserved registers. Each register can be accessed
as a full 32-bit register (although the ECAP peripheral does have some
16-bit registers) or at the bit-field level. This is so as to eliminate
the need to do bit-masking at the register level.

.. rubric:: Using the Headers
   :name: using-the-headers

The process of using the headers is described in more detail in the
"Type Attributes" section of the `PRU Optimizing C/C++ Compiler User's Guide <https://ti.com/lit/pdf/spruhv7>`__.

In order to tie the structures to the appropriate Constant Table
register we have to use a special trick with the PRU Code Generation
Tools package. This process is described in more detail in the CGT
Documentation here. For our purposes the linker command file found in
each example project contains a "Memory" range for each of the Constant
Table entries.

Once this is completed you will be able to access a peripheral register
via the structure by accessing that structure's members. The basic
layout is like this:

| struct{

union{
u32 register_name;
struct {
bit_field_names : bit_size;
. . .
} register_name_bit;
};
. . .
| } register_set;

Thus you can access a register programmatically through the structure
(e.g., register_set.register_name[_bit.bitfield_name] = value).

