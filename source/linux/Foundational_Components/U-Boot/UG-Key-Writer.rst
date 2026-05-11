.. _key-writer-label:

##########
Key Writer
##########

This OTP (One Time Programmable) key writer guide describes how to
populate customer keys in eFuses of the SoC.

.. caution::

   Once you program the SoC eFuses using keywriter,
   there is no going back. This action of burning the OTP fields is
   irreversible.

**High Security (HS) Device Sub-types**

*HS-FS (High Security - Field Securable)*:
Device type before you program customer keys (the state in which
the device leaves TI factory). In this state, device protects the
ROM code, TI keys and certain security peripherals. HS-FS devices do
not enforce secure boot process.

*HS-SE (High Security - Security Enforced)*:
Device type after you program the customer keys.
HS-SE devices enforce secure boot (with encryption).

**HS-FS to HS-SE Conversion**

To convert a HS-FS device to HS-SE device, program the customer
root key (optionally backup key) on the target device by using
OTP Keywriter.

Customer key information is encrypted into a x509 certificate
to create a binary blob.

**U-Boot Key Writer Structure**

.. code-block:: c

   struct fuse_otp_header {
       uint32_t version_info;
       uint32_t fuse_mode;
   } __attribute__((packed));

   struct fuse_otp {
       struct fuse_otp_header fuse_otp_hdr;
       struct fuse_otp_blob fuse_otp_blb;
   } __attribute__((packed));

* version_info : Customer can use this field to denote the version of U-Boot fuse programming.
* fuse_mode    : Fuse mode with value 0x00009031.

The following shows the overall fuse_otp structure:

.. Image:: /images/Uboot_fuse_writebuff_OTP_keywriter_structure.png

.. attention::

   For information about the fuse_otp_blob x509 keywriter certificate,
   visit `keywriter_cert_gen_procedure`_.

.. _keywriter_cert_gen_procedure: https://software-dl.ti.com/tisci/esd/latest/6_topic_user_guides/key_writer.html

**Generate the Binary Blob**

Generate the binary blob based out of U-Boot Key Writer
x509 certificate and copy the bin file to a SD card.

**Typical Key Writer Flow**

A typical flow to do OTP key writer is as follows:

#. Addr 0x82000000 is the dedicated address to store the generated
   key writer binary blob. Clear out 12Kb of memory starting
   from 0x82000000:

    .. code-block:: text

       => mw 0x82000000 0 0x3000

#. Load the binary blob from SD card into memory using
   commands such as:

    .. code-block:: text

       => fatload mmc 1:1 0x82000000 key_writer_blob.bin

#. Read the memory addr 0x82000000 to verify that you loaded the blob successfully.

    .. code-block:: text

       => md 0x82000000

#. Efuse modification requires a voltage to be applied on a specific pin (Vpp) during the programming.
   To program the efuses, the Vpp pin on the System-on-Chip (SoC) must be powered at 1.8V. It is the
   responsibility of the SoC user to design a suitable circuit that enables the Vpp pin to be powered.

   Texas Instruments (TI)  EVMs feature an I2C-based IO expander, which has one of its IO pins
   connected to the SoC's Vpp pin. The software required to control the power to the Vpp pin depends
   on the specific circuit implementation.

   In the case of TI AM62L PROC181E1-1 EVMs, an I2C driver is necessary to send command packets to the IO expander,
   which then toggles the IO pin connected to the Vpp pin, thereby controlling the power supply to the pin.
   On TI EVM, turn on the Vpp pin using the following commands:

    .. rubric:: Select i2c bus 1, as chip 22 is connected to it, and probe the chip:

    .. code-block:: text

       => i2c dev 1
       => i2c probe 22

    .. rubric:: To turn off Vpp:

    .. code-block:: text

       => i2c mw 0x22 0x04 0x00

    .. rubric:: To configure Vpp (port 04) as output:

    .. code-block:: text

       => i2c mw 0x22 0xC 0xEF

    .. rubric:: To turn on Vpp:

    .. code-block:: text

       => i2c mw 0x22 0x04 0x10

#. Call fuse writebuff sub-system command with the address 0x82000000:

    .. code-block:: text

       => fuse writebuff -y 0x82000000

#. Turn off Vpp after programming is successful:

    .. code-block:: text

       => i2c mw 0x22 0x04 0x00

.. note::

   Changes made to efuses, by programming them, take effect (such as becoming
   visible in Memory-Mapped Registers (MMRs), device type change and so on)
   after a complete System-on-Chip (SoC) power cycle.
