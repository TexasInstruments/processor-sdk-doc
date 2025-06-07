.. _programming-user-otp-fuses-label:

##########################
Programming user OTP fuses
##########################

This guide describes how to read and write User One Time Programmable (OTP)
fuses and boot-mode fuses by using U-Boot's fuse commands.

.. caution::

   Programming fuses is an irreversible operation. Once an OTP fuse is
   programmed, it cannot be undone. Please verify all values carefully before
   programming.

Commands overview
=================

See U-Boot fuse command `documentation
<https://docs.u-boot.org/en/latest/usage/cmd/fuse.html>`__

Reading fuses
=============
Read is only permitted from bank 0.

Below example shows reading 4 x 32-bit words starting from bank 0, offset 5:

   .. code-block:: text

      => fuse read 0 5 4

Programming fuses
=================

.. warning::

   Before programming fuses, apply proper voltage to the Vpp pin.
   The :ref:`key-writer-lite-label` document explains how to control
   Vpp voltage.

The `fuse prog` command programs two types of OTP bits:

- Bank 0 - General Purpose User defined OTP bits.
- Bank 0xFF - Reduced pin boot-mode related OTP bits.

Programming sequence
--------------------

Programming fuses requires applying a voltage to a specific pin (Vpp).
Refer to device data sheet for more details.

On TI AM62L Evaluation Module, an I2C-based IO expander controls the Vpp pin.
Follow these steps to enable or disable Vpp:

1. Select and probe the I2C bus:

   .. code-block:: text

      # Select i2c bus 2 (chip 22 is connected to it)
      => i2c dev 2

      # Probe the chip
      => i2c probe 22

2. Configure and enable Vpp:

   .. code-block:: text

      # Turn off Vpp initially
      => i2c mw 0x22 0x04 0x00

      # Configure Vpp (port 04) as output
      => i2c mw 0x22 0xC 0xEF

      # Turn on Vpp
      => i2c mw 0x22 0x04 0x10

3. Run fuse prog command

   .. code-block:: text

      # Programs word 15 to 0x1234 (each word is 25-bit)
      => fuse prog 0 15 0x1234

4. Disable Vpp after programming:

   .. code-block:: text

      # Turn off Vpp
      => i2c mw 0x22 0x04 0x00

5. Power cycle the device for changes to take effect

.. note::

   - Bank and word numbers are device-specific
   - Changes to fuses only become visible after a full power cycle

For programming many fuses and keys in one-shot using a binary blob
(``fuse writebuff``), see the :ref:`key-writer-lite-label` document.

Programming boot-mode fuses
===========================

.. caution::

   Programming boot-mode fuses is an irreversible operation. Once an OTP fuse is
   programmed, it cannot be undone. boot-mode fuses lock on first write, so
   multi-pass programming is not possible


The boot-mode pin fuses allow configuration of the boot sequence without
requiring physical pin strapping. The following provides an example of
programming boot-mode pin related fuses. |__PART_FAMILY_NAME__| supports
reduced boot-mode configuration by a combination of fuse and boot-mode pins.
When set to fuse boot-mode, the boot-mode pins decode the corresponding fuse
into a 16-bit boot-mode value. Refer to |__PART_FAMILY_NAME__| Technical
Reference Manual (TRM) for more details. Enable Vpp before programming these
fuses, similar to other fuses.

Programming example
-------------------

The document `here
<http://downloads.ti.com/tisci/esd/latest/6_topic_user_guides/boot_mode_writer.html#how-to-derive-to-be-programmed-value>`__
explains how to derive the fuse boot-mode value.

1. Find the raw boot-mode value. For example, to program fuse slot-1
   with GPMC NAND as primary and USB-DFU as backup, full pin count strapping
   would be ``0x45B`` (25MHz Oscillator) based on `Section 5.2.3 of the TRM`.
2. Convert this to 25-bit value based on table
   `here <http://downloads.ti.com/tisci/esd/latest/6_topic_user_guides/boot_mode_writer_encoding.html>`__
   So, ``0x45B`` translates to ``0x18045B``.
3. XOR the value with SoC and slot specific bit-mask value
   `here <http://downloads.ti.com/tisci/esd/latest/5_soc_doc/am62lx/boot_mode_efuse.html#am62lx-boot-mode-efuses>`__.
   For slot 1, ``0x18045B`` xor ``0x012007B`` gives ``0xA0420``.
4. Reversing the bits in the 25-bit value gives ``0x840A0``.

   .. code-block:: text

      => fuse prog 0xFF 1 0x840A0

.. note::

   - Bank 0xFF stores boot-mode pin fuses.
   - Each word in the bank can store one pin configuration.
   - The number of available words depends on the device.
   - Refer to your device's TRM for the valid pin numbers.
   - New boot-mode settings take affect post a power-cycle

.. caution::

   Currently there is no support to read-back the boot-mode related fuses.
