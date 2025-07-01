.. _u-boot-build-guide-ram-device-trees-k3:

####################
RAM and Device Trees
####################

********************************
Available RAM for image download
********************************

To know the amount of RAM available for downloading images or for other
usage, use ``bdinfo`` command.

.. code-block:: console

   => bdinfo
   arch_number = 0x00000000
   boot_params = 0x80000100
   DRAM bank   = 0x00000000
   -> start    = 0x80000000
   -> size     = 0x7F000000
   baudrate    = 115200 bps
   TLB addr    = 0xFEFF0000
   relocaddr   = 0xFEF30000
   reloc off   = 0x7E730000
   irq_sp      = 0xFCEF8880
   sp start    = 0xFCEF8870
   Early malloc usage: 890 / 2000

After booting, U-Boot relocates itself (along with its various reserved
RAM areas) and places itself at end of available RAM (starting at
``relocaddr`` in ``bdinfo`` output above). Only the stack is located
just before that area. The address of top of the stack is in
``sp start`` in ``bdinfo`` output and it grows downwards. Users should
reserve at least about 1MB for stack, so in the example output above,
RAM in the range of ``[0x80000000, 0xFCE00000]`` is safely available for
use.

************
Device Trees
************

A note about device trees. Now all supported boards are required to use a
device tree to boot. To facilitate this in supported platforms, a command
in U-Boot environment **findfdt** is available that will set the **fdtfile**
variable to the name of the device tree to use, as found with the kernel
sources. In the Keystone-2 family devices (K2H/K/E/L/G), it is specified
by **name\_fdt** variable for each platform. The device tree is expected
to be loaded from the same media as the kernel, and from the same relative path.

.. _AM64-SRAM-Layout-label:

**************************************************
SRAM memory Layout during initial bootloader stage
**************************************************

The SRAM memory layout explains the memory used for Bootloader's operation.

   .. ifconfig:: CONFIG_part_variant in ('AM64X')

      .. code-block:: text

         ┌──────────────────────────────────────┐0x70000000
         │                                      │
         │                                      │
         │                                      │
         │    SPL IMAGE (Max size 1.5 MB)       │
         │                                      │
         │                                      │
         │                                      │
         ├──────────────────────────────────────┤0x7017FFFF
         │                                      │
         │           SPL STACK                  │
         │                                      │
         ├──────────────────────────────────────┤0x70192727
         │          GLOBAL DATA(216 B)          │
         ├──────────────────────────────────────┤0x701927FF
         │                                      │
         │       INITIAL HEAP (32 KB)           │
         │                                      │
         ├──────────────────────────────────────┤0x7019A7FF
         │                                      │
         │          BSS  (20 KB)                │
         ├──────────────────────────────────────┤0x7019F7FF
         │         EEPROM DATA (2 KB)           │
         ├──────────────────────────────────────┤0x7019FFFF
         │                                      │
         │                                      │
         │     UNALLOCATED AREA (123 KB)        │
         │                                      │
         │                                      │
         ├──────────────────────────────────────┤0x701BEBFB
         │   BOOT PARAMETER INDEX TABLE (5124 B)│
         ├──────────────────────────────────────┤0x701BFFFF
         │                                      │
         │             TF-A (128 KB)            │
         │                                      │
         ├──────────────────────────────────────┤0x701DFFFF
         │                                      │
         │      DMSC CODE AREA (128 KB)         │
         │                                      │
         └──────────────────────────────────────┘0x701FFFFF

      - In the last 128 KB of memory used by DMSC during run time, initial 80 KB
         gets freed after a security handover happens. The last 48 KB still will be used by DMSC.
      - For more details on Security handover see `here <https://software-dl.ti.com/tisci/esd/latest/6_topic_user_guides/security_handover.html>`__ .

   .. ifconfig:: CONFIG_part_variant in ('AM62X')

      .. code-block:: text

         ┌──────────────────────────────────────┐0x43c00000
         │                                      │
         │                                      │
         │               SPL IMAGE              │
         │           (Max size 192 KB)          │
         │            (excluding BSS)           │
         │             (196608B  Max)           │
         │                                      │
         ├──────────────────────────────────────┤0x43c30000
         │                                      │
         │                                      │
         │            STACK (13568B Max)        │
         │                                      │
         │                                      │
         ├──────────────────────────────────────┤
         │         Global Data (428B Max)       │
         ├──────────────────────────────────────┤
         │                                      │
         │            HEAP (28KB Max)           │
         │                                      │
         ├──────────────────────────────────────┤0x43c3a7f0
         │                                      │
         │             EMPTY (16B)              │
         │                                      │
         ├──────────────────────────────────────┤0x43c3a800
         │                                      │
         │                                      │
         │         DM config data (2KB)         │
         │                                      │
         │                                      │
         ├──────────────────────────────────────┤0x43c3b000
         │                                      │
         │             BSS (12KB)               │
         │                                      │
         ├──────────────────────────────────────┤0x43c3e000
         │                                      │
         │                                      │
         │           EMPTY (4.5KB)              │
         │        (Reserved for ROM)            │
         │                                      │
         ├──────────────────────────────────────┤0x43c3f1e0
         │                                      │
         │       ROM Boot parameter table       │
         │    + Extended boot info (3.5 KB)     │
         │                                      │
         └──────────────────────────────────────┘0x43c3ffff

   .. ifconfig:: CONFIG_part_variant in ('AM62AX','AM62PX')

      .. code-block:: console

         ┌──────────────────────────────────────┐0x43c00000
         │                                      │
         │                                      │
         │               SPL IMAGE              │
         │           (Max size 188 KB)          │
         │            (excluding BSS)           │
         │             (192512B  Max)           │
         │                                      │
         ├──────────────────────────────────────┤0x43c2f000
         │                                      │
         │                                      │
         │            STACK (17KB Max)          │
         │                                      │
         │                                      │
         ├──────────────────────────────────────┤
         │         Global Data (428B Max)       │
         ├──────────────────────────────────────┤
         │                                      │
         │            HEAP (28997B Max)         │
         │                                      │
         ├──────────────────────────────────────┤0x43c3a7f0
         │                                      │
         │             EMPTY (16B)              │
         │                                      │
         ├──────────────────────────────────────┤0x43c3a800
         │                                      │
         │                                      │
         │         DM config data (2KB)         │
         │                                      │
         │                                      │
         ├──────────────────────────────────────┤0x43c3b000
         │                                      │
         │             BSS (12KB)               │
         │                                      │
         ├──────────────────────────────────────┤0x43c3e000
         │                                      │
         │                                      │
         │           EMPTY (4.5KB)              │
         │        (Reserved for ROM)            │
         │                                      │
         ├──────────────────────────────────────┤0x43c3f1e0
         │                                      │
         │       ROM Boot parameter table       │
         │    + Extended boot info (3.5 KB)     │
         │                                      │
         └──────────────────────────────────────┘0x43c3ffff

   .. ifconfig:: CONFIG_part_variant in ('J722S')

      .. code-block:: console

         ┌──────────────────────────────────────┐0x43c00000
         │                                      │
         │                                      │
         │               SPL IMAGE              │
         │            (excluding BSS)           │
         │            (0x6ce00 B  Max)          │
         │                                      │
         ├──────────────────────────────────────┤0x43C6CE00
         │              EMPTY (0x50 B)          │
         │                                      │
         ├──────────────────────────────────────┤0x43C6CE50
         │                                      │
         │                                      │
         │          STACK (0x5000 B Max)        │
         │                                      │
         │                                      │
         ├──────────────────────────────────────┤0x43C71E50
         │       Global Data (0x1AC B Max)      │
         │                 (+0x4)               │
         │                                      │
         ├──────────────────────────────────────┤0x43C72000
         │                                      │
         │            HEAP (0x9000 B Max)       │
         |                                      |
         ├──────────────────────────────────────┤0x43C7B000
         │                                      │
         │            SPL BSS (0x3000 B)        │
         │                                      │
         ├──────────────────────────────────────┤0x43C7E000
         │                                      │
         │       ROM Boot parameter table       │
         │    + Extended boot info (3.5 KB)     │
         │                                      │
         └──────────────────────────────────────┘0x43C7F290


   .. ifconfig:: CONFIG_part_variant in ('AM62LX')

      .. code-block:: text

         ┌────────────────────┐ 0x7081_8000         ┬
         │   Debug Buffers    │                     │
         ├────────────────────┤ 0x7081_6000         │
         │  TIFS ->  A53 IPC  │                     │
         ├────────────────────┤ 0x7081_5000         │
         │  A53  -> TIFS IPC  │                     │
         ├────────────────────┤ 0x7081_4000         │
         │                    │                     │
         │    *Free Space*    │                     │
         │                    │                     │
         ├────────────────────┤ 0x7081_0000  ┬      │
         │ Translation Table  │              │      │
         ├────────────────────┤ 0x7080_D000  │      │
         │        BSS         │              │      │  MSRAM (96k)
         ├────────────────────┤ 0x7080_B9C0  │      │
         │       Stack        │              │      │
         ├────────────────────┤ 0x7080_B1C0  │ BL-1 │
         │        Data        │              │      │
         ├────────────────────┤ 0x7080_B000  │      │
         │      RO-Data       │              │      │
         ├────────────────────┤ 0x7080_6000  │      │
         │        Code        │              │      │
         ├────────────────────┤ 0x7080_0000  ┘     ─┤
         │                    │                     │
         │      ROM Data      │                     │ PSRAM (64k)
         │                    │                     │
         └────────────────────┘ 0x707F_0000         ┴
