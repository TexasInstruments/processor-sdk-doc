.. _key-writer-lite-label:

###############
Key Writer Lite
###############

This OTP (One Time Programmable) key writer lite guide describes
the procedure to be followed to populate customer keys in eFuses
of the SoC.

.. caution::

   Once the SoC eFuses are programmed using keywriter lite,
   there is no going back. This action of burning the OTP fields is
   irreversible.

**High Security (HS) Device Sub-types**

*HS-FS (High Security - Field Securable)*:
Device type before customer keys are programmed (the state in which
the device leaves TI factory). In this state, device protects the
ROM code, TI keys and certain security peripherals. HS-FS devices do
not enforce secure boot process.

*HS-SE Lite (High Security - Security Enforced Lite)*:
Device type after only the customer public key hashes are programmed.
HS-SE Lite devices enforce secure boot (without encryption).

**HS-FS to HS-SE Lite Conversion**

In order to convert a HS-FS device to HS-SE Lite device, one has to
program the customer root key (optionally backup key) on the target
device, using OTP Keywriter Lite.

Customer key information is put in a structured format to create a
binary blob (Uboot key writer lite structure).

**Uboot Key Writer Lite Structure**

.. code-block:: c

   struct fuse_otp_header {
       uint32_t version_info;
       uint32_t fuse_mode;
   } __attribute__((packed));

   struct fuse_otp {
       struct fuse_otp_header fuse_otp_hdr;
       struct fuse_otp_blob fuse_otp_blb;
   } __attribute__((packed));

* version_info : Customer can use this field to denote the version of uboot fuse programming.
* fuse_mode    : Fuse mode with value 0x00009045.

The overall fuse_otp structure is shown below:

.. Image:: /images/Uboot_fuse_writebuff_OTP_structure.png

.. attention::

   For information on the fuse_otp_blob structure,
   visit `keywriter_lite_cert_gen_procedure`_.

.. _keywriter_lite_cert_gen_procedure: https://software-dl.ti.com/tisci/esd/latest/6_topic_user_guides/key_writer_lite.html

**Generate the Binary Blob**

Generate the binary blob based out of Uboot Key Writer Lite
structure by populating the structure and extracting the
.data section to a bin file and copy it to SD card.

**Typical Key Writer Lite Flow**

A typical flow to do OTP key writer lite is as follows:

#. The cache has to be flushed after loading the binary blob into memory, so enable the config
   CONFIG_CMD_CACHE=y in <path-to-tisdk>/board-support/<ti-u-boot-source-code>/configs/<device_defconfig>
   and re-build uboot.

#. Addr 0x82000000 is the dedicated address to store the generated
   key writer lite binary blob. Clear out 1Kb of memory starting
   from 0x82000000:

    .. code-block:: text

       => mw 0x82000000 0 0x400

#. The binary blob copied to SD card can be loaded into memory using
   commands like:

    .. code-block:: text

       => fatload mmc 1:1 0x82000000 key_writer_lite_blob.bin

#. Flush the cache.

    .. code-block:: text

       => dcache flush
       => md 0x82000000

#. Efuse modification requires a voltage to be applied on a specific pin (Vpp) during the programming.
   To program the efuses, the Vpp pin on the System-on-Chip (SoC) must be powered at 1.8V. It is the
   responsibility of the SoC user to design a suitable circuit that enables the Vpp pin to be powered.

   Texas Instruments (TI)  EVMs feature an I2C-based IO expander, which has one of its IO pins
   connected to the SoC's Vpp pin. The software required to control the power to the Vpp pin depends
   on the specific circuit implementation.

   In the case of TI AM62L PROC181E1 EVMs, an I2C driver is necessary to send command packets to the IO expander,
   which then toggles the IO pin connected to the Vpp pin, thereby controlling the power supply to the pin.
   On TI EVM, Vpp pin can be turned on using the below commands:

    .. rubric:: Select i2c bus 2, as chip 22 is connected to it, and probe the chip:

    .. code-block:: text

       => i2c dev 2
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

   Changes made to efuses, by programming them, take effect (like become
   visible in Memory-Mapped Registers (MMRs), device type change etc.)
   after a complete System-on-Chip (SoC) power cycle.
