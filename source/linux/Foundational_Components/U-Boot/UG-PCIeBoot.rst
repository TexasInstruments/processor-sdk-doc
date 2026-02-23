.. _pcie_boot:

==============
PCIe Boot Mode
==============

Overview
--------

PCIe (Peripheral Component Interconnect Express) boot mode allows
|__PART_FAMILY_NAME__| family of devices, configured as a PCIe endpoint, to boot by
receiving boot loader images over PCIe from a host system acting as a
PCIe root complex (RC). In this mode, the root complex is
responsible for discovering the endpoint device and transferring the
required boot loader images for each boot stage.

This document provides a step-by-step guide to configuring and using
PCIe boot mode. PCIe boot is supported on the |__PART_FAMILY_NAME__| SoC family. The
following instructions and switch settings are specific to the |__PART_FAMILY_NAME__| EVM;
for other boards, consult the corresponding hardware documentation.

Boot Mode Switch Settings
-------------------------

To enable PCIe boot mode, configure the boot mode switches as follows:

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   .. code-block:: text

      SW2 (B0 - B7):   1 1 0 1 0 1 1 0
      SW3 (B8 - B15):  0 0 0 0 0 0 0 0

.. ifconfig:: CONFIG_part_variant in ('J784S4')

   .. code-block:: text

      SW7:   0 1 0 1 0 0 0 0
      SW11:  1 0 0 0 1 0 0 0

.. note::

   DIP switch settings are EVM-specific and may not apply to all board designs.

Board Setup (Connection Example)
--------------------------------

The following is an example of a connection in which the root complex (host) and the
endpoint (|__PART_FAMILY_NAME__| device) are physically connected using a PCIe cable
or connector, as shown in the figure below.

.. image:: /images/AM64X_PCIe_boot.jpg

Both boards should be powered off before making the connection, and the PCIe link
securely established before powering on the devices.

Other hardware configurations are possible. So adapt the setup steps as
applicable to given board design.

Endpoint Configuration
----------------------

The following configuration options are used to set up the |__PART_FAMILY_NAME__| device
as a PCIe endpoint for PCIe boot. These options must be set in the
board's defconfig in U-BOOT for the corresponding boot loader image.

- ``CONFIG_SPL_PCI_DFU_BAR_SIZE``:
  Configures the size of the PCIe Base Address Register (BAR) that is
  exposed for device firmware update (DFU) and boot loader image download.

- ``CONFIG_SPL_PCI_DFU_VENDOR_ID``:
  Specifies the PCIe vendor ID to be advertised by the endpoint.

- ``CONFIG_SPL_PCI_DFU_DEVICE_ID``:
  Specifies the PCIe device ID to be advertised by the endpoint.

- ``CONFIG_SPL_PCI_DFU_MAGIC_WORD``:
  Magic word written by the root complex at the end of the image transfer to
  signal to the endpoint that the boot loader image is ready for processing.

- ``CONFIG_SPL_PCI_DFU_BOOT_PHASE``:
  Specify the current boot phase when booting via DFU over PCIe.
  This value can be read by the root complex to determine the
  current boot phase. Value of this config is written to memory
  location (BAR_start + PCI_DFU_BAR_SIZE - 70). Max size of this
  config is 63 bytes.

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   .. note::

      All the configs required for PCIe boot are enabled in
      ``am64x_evm_a53_defconfig`` and ``am64x_evm_r5_defconfig`` by default.

      By default, PCIe root complex mode is enabled in the device tree.
      To enable endpoint mode, the boot loaders must be built with the
      device tree overlay ``k3-am642-evm-pcie0-ep.dtso``.

.. ifconfig:: CONFIG_part_variant in ('J784S4')

   .. note::

      All the configs required for PCIe boot are enabled in
      ``j784s4_evm_a72_defconfig`` and ``j784s4_evm_r5_defconfig`` by default.

      By default, PCIe root complex mode is enabled in the device tree.
      To enable endpoint mode, the boot loaders must be built with the
      device tree overlay ``k3-j784s4-evm-pcie0-pcie1-ep.dtso``.

Ensure these configuration options are set appropriately in the build
environment to enable a successful PCIe boot process.

PCIe Boot Procedure
-------------------

Before starting, compile the sample host program provided in the next section:

.. code-block:: bash

   gcc -o pcie_boot_copy pcie_boot_copy.c

1. After configuring the boot mode switches on the endpoint and
   connecting it to the root complex as shown in the figure, power
   on the endpoint.

2. On the root complex, check the initial PCIe enumeration using ``lspci``:

   .. code-block:: bash

      lspci

   The endpoint will appear as a RAM device or with many functions.
   The enumeration might look similar to the following:

   .. code-block:: text

      0000:00:00.0 PCI bridge: Texas Instruments Device b012
      0000:01:00.0 RAM memory: Texas Instruments Device b012
      0000:01:00.1 Non-VGA unclassified device: Texas Instruments Device 0100
      0000:01:00.2 Non-VGA unclassified device: Texas Instruments Device 0100

   .. note::

      The exact device IDs and number of functions can vary depending on the
      platform and boot stage.

3. Copy ``tiboot3.bin`` to the endpoint using the sample host program.
   Use ``lspci -vv`` to identify the BAR (Base Address Register) region
   to write to.

   .. ifconfig:: CONFIG_part_variant in ('AM64X')

      Example command to copy ``tiboot3.bin`` (assuming BAR address ``0x68200000``):

      .. code-block:: bash

         sudo ./pcie_boot_copy am64x 0x68200000 tiboot3.bin

      After the root complex has finished copying the image,
      it must write the PCIe boot data address to ``0x701BCFE0``.

      For example, if the root complex loads the image at offset
      ``0x1000``, then it should write ``0x70001000`` (Internal RAM
      memory base + offset) to ``0x701BCFE0``. This notifies the ROM
      that the image is ready to be authenticated and processed.

   .. ifconfig:: CONFIG_part_variant in ('J784S4')

      Example command to copy ``tiboot3.bin`` (assuming BAR address ``0x4007100000``):

      .. code-block:: bash

         sudo ./pcie_boot_copy j784s4 0x4007100000 tiboot3.bin

      After the root complex has finished copying the image, the R5 ROM
      waits for two specific checks to continue the boot sequence:

      - The root complex must write the start address (32-bit) of the image
        to address location ``0x41CF3FE0``.
      - The root complex must write the magic word ``0xB17CEAD9`` to address
        location ``0x41CF3FE4``.

      These two writes signal to the ROM that the image has been fully copied
      and is ready to be authenticated and processed. The sample program handles
      these writes automatically.

4. Once the ``tiboot3.bin`` transfer is complete, the PCIe link will go down briefly.
   Scan the PCIe bus on the root complex again to enumerate the endpoint device
   for transferring the next stage boot loader:

   .. code-block:: bash

      echo 1 > /sys/bus/pci/devices/0000\:00\:00.0/rescan

   Check the new enumeration with ``lspci``:

   .. code-block:: bash

      lspci

   The enumeration will look similar to the following:

   .. code-block:: text

      0000:00:00.0 PCI bridge: Texas Instruments Device b012
      0000:01:00.0 RAM memory: Texas Instruments Device b010 (rev dc)

   Use ``lspci -vv`` to identify the new BAR address for the memory region.

5. At this stage, only one memory region will be visible. Copy
   ``tispl.bin`` to this region using the sample host program.

   .. ifconfig:: CONFIG_part_variant in ('J784S4')

      Example command (assuming BAR address ``0x4000400000``):

      .. code-block:: bash

         sudo ./pcie_boot_copy j784s4 0x4000400000 tispl.bin

   .. ifconfig:: CONFIG_part_variant in ('AM64X')

      Example command (assuming BAR address ``0x12000000``):

      .. code-block:: bash

         sudo ./pcie_boot_copy am64x 0x12000000 tispl.bin

   After the copy, the root complex must write a 4-byte magic word (defined
   in the defconfig) at the end of the memory region. This indicates to the
   endpoint that the host has copied the boot loader image. The sample program
   handles this automatically.

6. The PCIe link will go down again after the endpoint processes ``tispl.bin``.
   Remove and scan the PCIe device again to enumerate it for the final stage:

   .. code-block:: bash

      echo 1 > /sys/bus/pci/devices/0000\:01\:00.0/remove
      echo 1 > /sys/bus/pci/devices/0000\:00\:00.0/rescan

   Copy ``u-boot.img`` using the same procedure as step 5.

   .. ifconfig:: CONFIG_part_variant in ('J784S4')

      Example command (assuming BAR address ``0x4000400000``):

      .. code-block:: bash

         sudo ./pcie_boot_copy j784s4 0x4000400000 u-boot.img

   .. ifconfig:: CONFIG_part_variant in ('AM64X')

      Example command (assuming BAR address ``0x12000000``):

      .. code-block:: bash

         sudo ./pcie_boot_copy am64x 0x12000000 u-boot.img

7. After ``u-boot.img`` is successfully loaded and executed, the boot process
   is complete and U-Boot should be running on the endpoint device.

.. note::

   During the boot process, "PCIe LINK DOWN" messages might be displayed in the
   kernel logs. The endpoint resets and re-initializes the PCIe link after
   processing each boot stage, so this behaviour matches expectations.


Sample Host Program for Image Transfer
--------------------------------------

The following sample C program can be used on the root complex to
copy boot loader images (such as ``tiboot3.bin``, ``tispl.bin``, and
``u-boot.img``) to the PCIe endpoint device by writing them to the
appropriate memory regions using ``/dev/mem``.

.. code-block:: c

   #include <sys/mman.h>
   #include <sys/stat.h>
   #include <fcntl.h>
   #include <unistd.h>
   #include <stdio.h>
   #include <stdlib.h>
   #include <string.h>

   int main(int argc, char *argv[])
   {
      char *bootfilename = NULL;
      char *platform = NULL;
      off_t bar1_address = 0;
      int fd;
      void *map_base;
      long image_size, map_size;
      char *buffer;
      unsigned int *buffer_32;
      int i;
      FILE * fptr;
      off_t load_addr, load_addr_offset, start_addr_offset;
      unsigned int magic_word = 0;
      int use_magic_word = 0;

      if (argc != 4) {
         printf("Usage: %s <platform> <bar_address> <binary_file>\n", argv[0]);
         printf("  platform: am64x or j784s4\n");
         return 0;
      }

      platform = argv[1];
      bar1_address = strtoul(argv[2], NULL, 16);
      bootfilename = argv[3];

      printf("platform: %s\n", platform);
      printf("bootfilename: %s\n", bootfilename);
      printf("bar1_address: 0x%lx\n", bar1_address);

      if(!strcmp(bootfilename,"tiboot3.bin"))
      {
         if(!strcmp(platform, "am64x"))
         {
            load_addr = 0x70000000;
            load_addr_offset = 0x1000;
            start_addr_offset = 0x1bcfe0;
         }
         else if(!strcmp(platform, "j784s4"))
         {
            load_addr = 0x41C00000;
            load_addr_offset = 0x00;
            start_addr_offset = 0xf3fe0;
            magic_word = 0xB17CEAD9;
            use_magic_word = 1;
         }
         else
         {
            printf("Unsupported platform: %s\n", platform);
            return 0;
         }
      }
      else
      {
         load_addr = 0xdeadbeef;
         load_addr_offset = 0x00;
         start_addr_offset = 0x3ffffc;
      }

      printf("load_addr: 0x%lx\n", load_addr);
      printf("load_addr_offset: 0x%lx\n", load_addr_offset);
      printf("start_addr_offset: 0x%lx\n", start_addr_offset);
      if (use_magic_word)
         printf("magic_word: 0x%x\n", magic_word);

      printf("try to open /dev/mem.\n");
      fd = open("/dev/mem", O_RDWR | O_SYNC);
      if (fd < 0) {
         printf("open /dev/mem failed.\n");
         return 0;
      }
      printf("/dev/mem opened.\n");
      (void)fflush(stdout);

      fptr = fopen(bootfilename, "rb");
      if (!fptr) {
         printf("open %s failed.\n", bootfilename);
         return 0;
      }
      printf("%s opened.\n", bootfilename);

      (void)fseek(fptr, 0L, SEEK_END);
      image_size = ftell(fptr);
      printf("image_size: %ld\n", image_size);
      fseek(fptr, 0, SEEK_SET);

      printf("%s: image_size: %ld\n", __func__, image_size);

      map_size = 0x400000;

      printf("%s: map_size: %ld\n", __func__, map_size);

      map_base = mmap(0, map_size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, bar1_address);
      if (map_base == MAP_FAILED) {
         printf("mmap failed.\n");
         return 0;
      }
      printf("map_base: 0x%lx\n", (unsigned long)map_base);
      (void)fflush(stdout);

      buffer = malloc(image_size);
      if (!buffer) {
         printf("malloc failed.\n");
         return 0;
      }

      buffer_32 = (unsigned int *)buffer;
      fread(buffer, (size_t)image_size, 1, fptr);
      printf("Read image of %ld bytes\n", image_size);

      printf("Writing image to memory\n");
      for(i = 0; i < (int)image_size; i+=4)
      {
         *(unsigned int *)( map_base + load_addr_offset + i) = buffer_32[i/4];
      }
      printf("done.\n");
      fflush(stdout);

      sleep(1);

      *(unsigned int *)(map_base + start_addr_offset) = (unsigned int)(load_addr_offset + load_addr);

      // Write magic word for J784S4 at R5 stage
      if(use_magic_word)
      {
         *(unsigned int *)(map_base + start_addr_offset + 4) = magic_word;
         printf("Magic word written.\n");
      }

      return 0;
   }

Usage Example
^^^^^^^^^^^^^

To copy a boot loader file (e.g., ``tiboot3.bin``) to the PCIe device,
specify the platform, BAR address, and binary file.

For AM64X:

.. code-block:: bash

   sudo ./pcie_boot_copy am64x 0x68200000 tiboot3.bin

For J784S4:

.. code-block:: bash

   sudo ./pcie_boot_copy j784s4 0x12000000 tiboot3.bin

Replace the BAR address with the appropriate BAR region address as
enumerated on the root complex for specific setup.
