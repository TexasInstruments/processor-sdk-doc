.. _u-boot-build-guide-ram-device-trees-omap:

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
