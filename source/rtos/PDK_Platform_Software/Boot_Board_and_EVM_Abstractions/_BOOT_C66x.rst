.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_BOOT_C66x

Overview
^^^^^^^^^^^

C66x SOCs use the Intermediate Boot-Loader (IBL) to initialize and setup
the SOC for specific boot modes. The table below illustrates the
supported bootmodes:

+--------------------------------------+-------------+-------------+
| Boot Mode                            | TMDSEVM6678 | TMDXEVM6657 |
+======================================+=============+=============+
| NOR boot via IBL over I2C\ :sup:`1`  | Yes         | Yes         |
+--------------------------------------+-------------+-------------+
| NAND boot via IBL over I2C\ :sup:`1` | Yes         | Yes         |
+--------------------------------------+-------------+-------------+
| TFTP boot via IBL over I2C\ :sup:`1` | Yes         | Yes         |
+--------------------------------------+-------------+-------------+
| I2C POST boot\ :sup:`2`              | Yes         | Yes         |
+--------------------------------------+-------------+-------------+
| Ethernet boot                        | Yes         | Yes         |
+--------------------------------------+-------------+-------------+
| SRIO boot                            | Yes         | Yes         |
+--------------------------------------+-------------+-------------+
| PCIe boot                            | Yes         | Yes         |
+--------------------------------------+-------------+-------------+

.. note::
   #. Support boot over I2C bus address 0x51
   #. Support POST boot over I2C bus address 0x50
   #. Only ELF and BBLOB images are supported for booting
   #. IBL is using the first 128KB L2 local memory, any application booting
      from IBL should NOT use the first 128KB L2 memory, OR should only use
      the first 128KB L2 memory for uninitialized data section

Please refer to the boot mode dip switch settings for different boot
modes on
`TMDSEVM6678L_EVM <http://processors.wiki.ti.com/index.php/TMDXEVM6678L_EVM_Hardware_Setup#Boot_Mode_Dip_Switch_Settings>`__,
and
`TMDSEVM6657L_EVM <http://processors.wiki.ti.com/index.php/TMDSEVM6657L_EVM_Hardware_Setup#Boot_Mode_Dip_Switch_Settings>`__
that IBL supports.

Flashing the Bootloader
^^^^^^^^^^^^^^^^^^^^^^^^^

IBL needs to be flashed into EEPROM address 0x51.

Refer to `Processor SDK RTOS Flashing Bootable
Images <http://processors.wiki.ti.com/index.php/Program_EVM_UG>`__] for
instructions on using the script, program_evm.js, to automatically flash
your device.

Bootloader Execution Sequence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

IBL is flashed into I2C EEPROM bus address 0x51. IBL provides a
workaround for the PLL lockup issue (please refer to C6678 errata
document, February 2011, advisory 8 for details on the PLL lockup
issue). For ROM boot modes (EMAC,SRIO,PCIe,Hyperlink etc) and I2C boot
mode with bus address 0x50, DSP will initially boot from I2C EEPROM bus
address 0x51 which does the PLL reset workaround, updates the DEVSTAT
for appropriate values based on the DIP switch settings (SW3 through SW6
settings) and then re enters the ROM to accomplish the desired boot
mode. Please note that the re entry is done for all boot modes except
for PCIe boot mode and I2C boot mode with bus address 0x51.

Below are the steps done in the IBL:

#. FPGA samples the bootmode pins
#. FPGA forces the DSP to boot via I2C bus address 0x51
#. PLL is initialized correctly by the IBL on the I2C.
#. IBL reads the sampled bootmode from an FPGA register.
#. IBL checks the bootmode, if it is not I2C boot or it is I2C boot but
   with bus address 0x50, IBL writes bootmode into the DEVSTAT register
#. IBL then checks if the bootmode is PCIE boot or not. If it is, it
   executes some PCIE workaround to configure the PCIE registers (mainly
   to accept spread spectrum clock) and stays inside IBL waiting for
   PCIe boot.
#. If it is not PCIE boot mode, IBL writes the Boot ROM entry address
   into the DSP Program Counter, DSP executes the desired internal ROM
   boot mode or boot from I2C bus address 0x50 as normal.

Compilation
^^^^^^^^^^^^^^

The recommended rule-of-thumb to compiling projects in the Processor SDK
RTOS package is to use the makefiles provided. The makefiles are usable
after setting up your shell/terminal/command prompt environment with the
setupenv.bat or setupenv.sh script located in

::

     [SDK Install Path]/processor_sdk_rtos_<platform>_<version>

Refer to `Processor SDK RTOS Building the SDK <index_overview.html#building-the-sdk>`__
guide on how to setup your environment for building within any of the
Processor SDK RTOS packages.

.. note::
   C66x projects are supported by C6000 Code Generation
   Tools 7.4.x. Make sure your environment variable, C6X_GEN_INSTALL_PATH,
   is pointing to a valid C6000 compiler. Compiling IBL invokes the C6000
   compiler, cl6x, directly. Your PATH variable will need to have
   $C6X_GEN_INSTALL_PATH/bin.

The IBL package can be found in:

::

     [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/ibl

To build:

::

     cd [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/ibl/src/make
     make <IBL_BINARY_NAME> ENDIAN=<BINARY_ENDIANNESS> I2C_BUS_ADDR=0x51

*<IBL_BINARY_NAME>* can be of values: **evm_c6657_i2c** or
**evm_c6678_i2c**. (For C6657 or C6678 platforms, respectively)

*<BINARY_ENDIANNESS>* can be of values: **little** or **big**

*I2C_BUS_ADDR* specifies the I2C bus address to use, and has to be 0x51
for C66x SOCs to access the EEPROM.

The resulting output will be in [SDK Install
Path]/pdk_<platform>_<version>/packages/ti/boot/ibl/src/make/bin
directory.

.. note::
   For developers, who want to build IBL in Windows environment. Please
   build this using MinGW environment using the instructions provided in
   the build_instructions.txt that can be found under
   pdk_c66xx_xx_xx\packages\ti\boot\ibl\doc\ibl\doc

|

Flash Writers
^^^^^^^^^^^^^^^^^

There are three types of flash memory provided with the C66x SOCs:
EEPROM, NOR, and NAND. Each of these flash memory can hold bootable
application binaries. As such, respective flash writers are provided in:

::

     [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/writer

.. note::
   Please set your EVM to **NO BOOT** mode before loading
   and running any of the flash writers. Flashing in NO BOOT mode is the
   safest way since it eliminates any unwarranted interactions with booted
   applications.


EEPROM Writer
""""""""""""""

The EEPROM Writer is used to write a binary into the EEPROM memory.

Compilation
'''''''''''''

::

     cd [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/writer/eeprom/<platform>/build
     make all

Usage
'''''''

#. Set your EVM to **NO BOOT**. Power on, launch target configuration in
   CCS, and connect to Core 0. Be sure the GEL file is used and DDR is
   initialized.
#. Copy the desired binary you want to flash to [SDK Install
   Path]/pdk_<platform>_<version>/packages/ti/boot/writer/eeprom/<platform>/bin
   directory.
#. Rename the binary you copied in the previous step to "app.bin".
#. In CCS, select Core 0 and open the Memory Browser
#. In the Memory Browser window, right click and select "Load Memory"
#. Load your app.bin to 0x0C000000. Do so by selecting app.bin for the
   file, click Next, and input 0x0C000000 for Start Address (Type-size
   selected should be 32-bit)
#. Load [SDK Install
   Path]/pdk_<platform>_<version>/packages/ti/boot/writer/eeprom/<SOC>/bin/eepromwriter_<platform>.out
#. Run Core 0. This will program the flash memory.

If it succeeds, the console will print "EEPROM programming completed
successfully"

NOR Writer
"""""""""""

The NOR Writer is used to write a binary into the NOR memory.

Compilation
''''''''''''

::

     cd [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/writer/nor/<platform>/build
     make all

Usage
''''''

#. Set your EVM to **NO BOOT**. Power on, launch target configuration in
   CCS, and connect to Core 0. Be sure the GEL file is used and DDR is
   initialized.
#. Copy the desired binary you want to flash to [SDK Install
   Path]/pdk_<platform>_<version>/packages/ti/boot/writer/nor/<platform>/bin
   directory.
#. Rename the binary you copied in the previous step to "app.bin".
#. In CCS, select Core 0 and open the Memory Browser
#. In the Memory Browser window, right click and select "Load Memory"
#. Load your app.bin to 0x80000000. Do so by selecting app.bin for the
   file, click Next, and input 0x80000000 for Start Address (Type-size
   selected should be 32-bit)
#. Load [SDK Install
   Path]/pdk_<platform>_<version>/packages/ti/boot/writer/nor/<SOC>/bin/norwriter_<platform>.out
#. Run Core 0. This will program the flash memory.

If it succeeds, the console will print "NOR programming completed
successfully"

NAND Writer
""""""""""""

The NAND Writer is used to write a binary into the NAND memory.

Compilation
'''''''''''''

::

     cd [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/writer/nand/<platform>/build
     make all

Usage
''''''

#. Set your EVM to **NO BOOT**. Power on, launch target configuration in
   CCS, and connect to Core 0. Be sure the GEL file is used and DDR is
   initialized.
#. Copy the desired binary you want to flash to [SDK Install
   Path]/pdk_<platform>_<version>/packages/ti/boot/writer/nand/<platform>/bin
   directory.
#. Rename the binary you copied in the previous step to "app.bin".
#. In CCS, select Core 0 and open the Memory Browser
#. In the Memory Browser window, right click and select "Load Memory"
#. Load your app.bin to 0x80000000. Do so by selecting app.bin for the
   file, click Next, and input 0x80000000 for Start Address (Type-size
   selected should be 32-bit)
#. Load [SDK Install
   Path]/pdk_<platform>_<version>/packages/ti/boot/writer/nand/<SOC>/bin/nandwriter_<platform>.out
#. Run Core 0. This will program the flash memory.

If it succeeds, the console will print "NAND programming completed
successfully"

Boot Modes
^^^^^^^^^^^

NAND Boot
""""""""""""

.. Image:: /images/Nandboot.jpg

NAND boot is a multi-stage process which is designed to boot an
application from NAND flash after reset. Figure below illustrates the
elements of the NAND boot process.

On reset the DSP starts execution with the bootrom which transfers
execution to the secondary bootloader from EEPROM using the I2C target
bus address 0x51. The secondary bootloader loads the application program
from NAND flash then transfers control to the application. To execute
the NAND bootloader you must ensure the DIP switches for your platform
are properly configured for I2C Master Boot and address 0x51, AND
the boot parameter index dip switch should be set to 2 or 3.

NAND boot supports multiple images booting. Depending on the boot
parameter index dip switch, maximum 2 boot images can be supported. By
default NAND boot only supports a BBLOB image format, if the customer
wants to boot an ELF image,  the IBL configuration table needs to be
modified and re-programmed to EEPROM.

|

NOR Boot
""""""""""""

.. Image:: /images/Norboot.jpg

NOR boot is a multi-stage process which is designed to boot an
application from NOR flash after reset. Figure below illustrates the
elements of the NOR boot process.

On reset the DSP starts execution with the bootrom which transfers
execution to the secondary bootloader from EEPROM using the I2C target
address 0x51. The secondary bootloader loads the application program
from NOR flash then transfers control to the application. To execute the
NOR bootloader you must ensure the DIP switches for your platform are
properly configured for I2C Master Boot and address 0x51, AND the boot
parameter index switch should be set to 0 or 1.

NOR boot supports multiple images booting. Depending on the boot
parameter index dip switch, maximum 2 boot images can be supported.

|

TFTP Boot
""""""""""""

.. Image:: /images/Emacboot.jpg

EMAC boot is a multi-stage process which is designed to boot an
application from TFTP server after reset. Figure below illustrates the
elements of the EMAC boot process.

On reset the DSP starts execution with the bootrom which transfers
execution to the secondary bootloader from EEPROM using the I2C target
address 0x51. The secondary bootloader loads the application program
from a remote TFTP server then transfers control to the application. To
execute the EMAC bootloader you must ensure the DIP switches for your
platform are properly configured for I2C Master Boot and address 0x51,
AND the boot parameter index switch should be set to 4. By default EMAC
boot only supports a BBLOB image format, if the customer wants to boot
an ELF image, the IBL configuration table needs to be modified and
re-programmed to EEPROM.

|

Updating the IBL Ethernet Configurations
'''''''''''''''''''''''''''''''''''''''''''

There are two ways to update the IBL ethernet configurations for
ethernet boot.

**Using CCS**

#. Turn on and connect to your EVM with the appropriate Target
   Configuration file.
#. Connect to Core 0.
#. Go to Run -> Load Program and select i2cparam_0x51_c667#_le_0x500.out
   located in [SDK Install
   Path]/pdk_<platform>_<version>/packages/ti/boot/ibl/src/make/bin
#. Go to Tools -> GEL Files and then right click on GEL Files window and
   Load the i2cConfig.gel GEL file, located in [SDK Install
   Path]/pdk_<platform>_<version>/packages/ti/boot/ibl/src/make/bin
#. Run the program. The following message will be printed on the CCS
   console: *Run the GEL for the SOC to be configured, press return to
   program the I2C.* **DO NOT PRESS ENTER UNTIL STEP 6 IS DONE**
#. Run the GEL script"Scripts -> EVM c6678 IBL" -> setConfig_c6678_main.
#. Now press "Enter" in the CCS console window, and the program will
   write the boot parameter table to the EEPROM. On success the message
   "I2c table write complete" will be printed on the CCS console.

Please note that the i2cConfig.gel file can be modified via a text
editor before loading and running the script in CCS. Please note that
this gel file contains configuration settings for multiple SOCs and
multiple boot modes.

**Using iblConfig Utility Program**

The second way to update the IBL ethernet configurations is to use
**iblConfig.out**. This utility program is located under:

::

      [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/ibl/src/util/iblConfig/build

In command line, use "make" with the given Makefile to generate
iblConfig.out and input.txt. Please be sure to fill in the parameters
for input.txt before running iblConfig.out; below is an example of
input.txt:

::

    file_name = ibl.bin
    SOC = 6
    offset = 0x500
    ethBoot-doBootp = TRUE
    ethBoot-bootFormat = ibl_BOOT_FORMAT_ELF
    ethBoot-ipAddr = 192.168.1.3
    ethBoot-serverIp = 192.168.1.2
    ethBoot-gatewayIp = 192.168.1.1
    ethBoot-netmask = 255.255.255.0
    ethBoot-fileName =

The first 3 parameters must be filled in for iblConfig.out to work:

-  file_name refers to the IBL binary file to update. This file must be
   in the same directory as iblConfig.out.
-  SOC refers to the SOC being used. Please enter **6 for C6678, and 8
   for C6657**.
-  offset refers to an offset space in the IBL. The value is 0x500 for
   C6678, and C6657

The ethernet parameters (the entries beginning with ethBoot) refer to
specific ethernet configurations. If they are not specified, they will
be defaulted to the values in the [SDK Install
Path]/pdk_<platform>_<version>/packages/ti/boot/ibl/src/util/iblConfig/src/SOC.h
file. In the example above, the ethernet boot file name will be
defaulted to c6678-le.bin when iblConfig.out is run.

After running iblConfig.out and updating the IBL binary, you must
flash the modified IBL binary to your EVM. You can do this as part of
program_evm (refer to `Processor SDK Flashing Bootable
Images <http://processors.wiki.ti.com/index.php/Program_EVM_UG>`__) or
you can flash it individually using eepromwriter (refer to "Flash
Writers" section above).

.. note::
   If you updated the IBL with iblConfig and flashed it
   with eepromwriter, you should **NOT** use
   i2cparam_0x51_c667#_le_0x500.out and iblConfig.gel - this would
   overwrite the changes you made to the IBL.

Compilation
'''''''''''''

::

     cd [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/i2c/tftp/<platform>/build
     make all

Usage
'''''''''''''

After your IBL ethernet settings are configured correctly and flashed
into EEPROM memory, follow these steps to continue the TFTP booting
process:

#. Start a TFTP server on your local PC. Your local PC will be the one
   sending the image to be booted, so make sure your PC and EVM are
   connected to the same subnet via ethernet
#. Copy i2ctftpboot_<platform>.out (refer to compilation step above) to
   your base TFTP directory
#. Rename i2ctftpboot_<platform>.out to app.out
#. Set the IP address of the PC that is running the TFTP server to
   192.168.2.101, since by default IBL will set the EVM IP address to
   192.168.2.100 and the TFTP server IP address to 192.168.2.101
#. Set EVM to TFTP boot mode and power on the EVM

Your PC will send the application image to the EVM to boot. Open an UART
terminal to view the output.

POST Boot
""""""""""""

POST (Power On Self Test) Boot is designed to do a quick self-diagnostic
upon boot. The POST application itself is located in

::

     [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/post

This application should already be compiled and flashed into EEPROM
out-of-box. Below instructions are for re-compilation or re-flashing
only.

Compilation
'''''''''''''

::

     cd [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/post/<platform>/build
     make all
     cd [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/post/<platform>/bin
     ./post_romparse.sh

Note: You would need to use post_romparse.bat instead of the \*.sh
version if your host system is running on Windows.

Usage
'''''''''''''

To flash the POST binary into EEPROM:

#. Refer to above Flash Writers section on flashing EEPROM memory. The
   binary you are flashing is "post_i2crom.bin".
#. Before running the last step of the EEPROM flashing instruction to
   run the DSP core, modify the **eepromwriter_input.txt** to use
   **0x50** for the bus_addr field. The **eepromwriter_input.txt** file
   is located in:

::

     [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/writers/eeprom/<SOC>/bin

Configure your EVM's DIP Switches accordingly to I2C POST BOOT mode. The
POST application will be loaded from EEPROM 0x50 and output will be
available over the UART serial console.

|

ETHERNET Boot
""""""""""""""

ETHERNET Boot uses Ethernet sockets to transfer a bootable image from a
host to the EVM. After powering on in Ethernet boot mode, the EVM will
send BOOTP packets at regular interval - this gives visibility of the
MAC ID of the EVM to the network.

Below are instructions on compiling and running an example to send a
simple program to the EVM while in Ethernet boot mode.

Compilation
'''''''''''''

::

     cd [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/examples/ethernet/Utilities
     make all
     cd [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/examples/ethernet/simple
     make all

Usage
'''''''''''''

#. Set the EVM's DIP switches to Ethernet boot mode. Connect Ethernet
   cables such that the EVM and your Host PC are on the same network.
#. Power on the EVM. The EVM will start sending BOOTP packets. Read the
   packets for the EVM's MAC ID. You can read the packet by using a
   network tool such as Wireshark.
#. On your Host PC, add an ARP entry to associate the EVM's MAC ID with
   an IP address on your network.
#. Use the pcsendpkt utility provided to send the simple.eth program
   compiled in the compilation step to the EVM.

To use pcsendpkt:

::

     cd [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/examples/ethernet/Utilities
     pcsendpkt simple.eth <EVM IP ADDRESS>

*<EVM IP ADDRESS>* is the IP address you assigned the EVM in step 3

.. note::
   If you are on a Linux Host PC, you may need to recompile pcsendpkt locally with GCC

  To verify, connect to the EVM's Core 0 via CCS and check that the A1
  register is set to 0x11223344

|

SRIO Boot
""""""""""""

SRIO boot will attempt to load and run a binary image received via SRIO.
An example can be found in:

::

     [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/examples/srio

Below are instructions on compiling and running the SRIO boot example.

Compilation
'''''''''''''

::

     cd [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/examples/srio/srioboot_ddrinit/<platform>/build
     make all
     cd [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/examples/srio/srioboot_ddrinit/<platform>/bin
     ./srioboot_ddrinit_elf2HBin.sh
     cd [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/examples/srio/srioboot_helloworld/<platform>/build
     make all
     cd [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/examples/srio/srioboot_helloworld/<platform>/bin
     ./helloworld_elf2HBin.sh
     cd [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/examples/srio/srioboot_example/<platform>/build
     make all

Note: You would need to use srioboot_ddrinit_elf2HBin.bat and
helloworld_elf2HBin.bat instead of their \*.sh version respectively if
your host system is running on Windows. Compilation of the projects
should be done in the order stated above.

Usage
'''''''''''''

You will need to have 2 EVMs - both should be set to SRIO boot mode. The
two EVMs will be connected through the AMC breakout board (lane x of one
slot should be connected to lane x of the other breakout slot). One EVM
will be acting as the host (referred to as the HOST EVM) and the other
EVM will be doing the booting (referred to as the BOOTING EVM).

#. Compile srioboot_example_evm66XXl.out
#. Connect the BOOTING EVM's UART serial port to your PC using the
   RS-232 cable
#. Connect a JTAG emulator on the HOST EVM
#. Power on both EVMs
#. Open an UART terminal to view the BOOTING EVM's output. (Remember to
   set the baud rate to 115.2k bps, 8-bit data, no parity, 1-bit stop,
   and no flow control)
#. Connect to the HOST EVM via Code Composer Studio (CCS is recommended
   to be version 6 or higher). Launch target configuration for your HOST
   EVM and connect to DSP0.
#. Load and run srioboot_example_evm66xxl.out on your HOST EVM

CCS console for your HOST EVM should display:

::

     [C66xx_0] SRIO Boot Host Example Version 01.00.00.01
     [C66xx_0]
     [C66xx_0] Transfer DDR init code via SRIO successfully
     [C66xx_0] Transfer boot code via SRIO successfully

Terminal for your BOOTING EVM should display:

::

     SRIO Boot Hello World Example Version 01.00.00.01
     Booting Hello World image on Core 0 from SRIO ...
     Booting Hello World image on Core 1 from Core 0 ...
     Booting Hello World image on Core 2 from Core 0 ...
     Booting Hello World image on Core 3 from Core 0 ...
     Booting Hello World image on Core 4 from Core 0 ...
     Booting Hello World image on Core 5 from Core 0 ...
     Booting Hello World image on Core 6 from Core 0 ...
     Booting Hello World image on Core 7 from Core 0 ...

PCIE Boot
""""""""""""

PCIE boot will attempt to load and run a binary image upon enumeration.
Example is located:

::

     [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/examples/pcie

Below are instructions on compiling and running the PCIE boot example.

Compilation
'''''''''''''

::

     cd [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/examples/pcie/pcieboot_ddrinit/<platform>/build
     make all
     cd [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/examples/pcie/pcieboot_helloworld/<platform>/build
     make all

Additionally for C6678 EVM:

::

     cd [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/examples/pcie/pcieboot_interrupt/<platform>/build
     make all
     cd [SDK Install Path]/pdk_<platform>_<version>/packages/ti/boot/examples/pcie/pcieboot_localreset/<platform>/build
     make all

The POST application can also be used as a PCIE Boot example. Run the
corresponding \*_elf2HBin.bat (or .sh) to convert the .out files into
PCIE bootable binaries.

Usage
'''''''''''''

An AMC to PCIE adaptor card, a TMS320C66xxL EVM card and a Linux PC are
required to do the test. The test is verified on both TMS320C6670L and
TMS320C6678L cards, with both 32-bit and 64-Linux PCs running Ubuntu
10.04. Other Linux OS are expected to work as well.

-  Before connect the system, please update IBL with the latest from
   Processor SDK
-  Set EVM card to PCIE boot (refer to hardware page)
-  Assemble the EVM card into the adaptor card
-  Connect the URAT cable from EVM card to a Linux PC’s USB port or
   serial port
-  Completely shut off the PC power supply (by disconnecting the power
   cord), insert the AMC adaptor card (with EVM mounted) into an open
   PCIE slot in PC’s motherboard
-  Supply the power to PC, wait for a few seconds and power on the PC.
-  Make sure the PCIE device is correctly enumerated by PC by checking
   below, note DEVICE_ID field is changed from 0x8888 to 0xb005 which is
   programmed in IBL.
-  Either enter PC’s BIOS setting when PC is booting up, a new PCIE
   device should be populated in the PCIE slot where card is inserted,
   shown as a “Multimedia device”.
-  Or, type “lspci –n” under Linux command shell after Linux OS is
   loaded, a TI device (VENDOR_ID: 0x104c) should be in the list:

::

     local-ubuntu:~$ lspci -n
     00:00.0 0600: 8086:2774
     00:1b.0 0403: 8086:27d8 (rev 01)
     ….
     00:1f.3 0c05: 8086:27da (rev 01)
     01:00.0 0480: 104c:b005 (rev 01)
     03:00.0 0200: 14e4:1677 (rev 01)
     Similarly, one can type “lspci”,
     local-ubuntu:~$ lspci
     ….
     00:1f.3 SMBus: Intel Corporation N10/ICH 7 Family SMBus Controller (rev
     01)
     01:00.0 Multimedia controller: Texas Instruments Device b005 (rev 01)
     ....

-  The PCIE BARn (n = 0, 1, 2, … , 5) registers are written by Linux PC
   after enumeration, they should be non-zero. Optionally, if a JTAG
   emulator is available, one can verify this by looking at address
   starting from 0x21801010 for 6 32-bit word.
-  Prepare pciedemo.ko in the Linux PC
-  On the Linux PC open a new terminal window to run minicom. First run
   “sudo minicom –s” to set the correct configuration: 115200bps, 8-N-1,
   Hardware flow control: OFF, Software flow control: OFF, and select
   the correct Serial Device. Save then run “sudo minicom” to monitor
   the port.
-  Type “sudo insmod pciedemo.ko”
-  If a JTAG emulator is available, one can verify that the PC registers
   for cores other than core 0 should be inside DDR; and magic address
   for cores other than core 0 should be written with 0xBABEFACE.

Procedure to build and run Linux host loader
''''''''''''''''''''''''''''''''''''''''''''''''''''

-  Create a folder (e.g. pcie_test) in a Linux machine. Copy pciedemo.c,
   Makefile, pcieDdrInit_66xx.h, pcieBootCode_66xx.h,
   pcieInterrupt_66xx.h and post_66xx.h from
   tools\boot_loader\examples\pcie\linux_host_loader to the folder.
-  Type “make”, a pciedemo.ko file should be created
-  By default, this will build the “HelloWorld” demo on little endian
   6678, which is controlled by the following Marcos in pciedemo.c:

::

     #define BIG_ENDIAN 0
     #define HELLO_WORLD_DEMO 1
     #define POST_DEMO 0
     #define EDMA_INTC_DEMO 0
     #define EVMC6678L 1
     #define EVMC6670L 0

One must select the endianness, demo program and target type by toggling
between 0 and 1 accordingly. Then, type “make clean” and type “make” to
rebuild the pciedemo.ko.

Note: “HelloWorld” and EDMA_INTC demos can be run on both endianness.
POST demo can be run on little endian only.

-  To insert the module into kernel, type “sudo insmod pciedemo.ko”; to
   view the kernel message, type “dmesg”; to remove the module from
   kernel, type “sudo rmmod

pciedemo.ko”

The role of IBL in PCIE boot mode
'''''''''''''''''''''''''''''''''''''''

The Intermediate Boot Loader (IBL) is flashed into I2C EEPROM bus
address 0x51. IBL provides a workaround for the PLL lockup issue (please
refer to C6678 errata document, February 2011, advisory 8 for details on
the PLL lockup issue). For ROM boot modes (EMAC, SRIO, PCIE, Hyperlink,
etc) and I2C boot mode with bus address 0x50, DSP will initially boot
from I2C EEPROM bus address 0x51 which does the PLL reset workaround,
updates the DEVSTAT for appropriate values based on the DIP switch
settings (SW3 through SW6 settings) and then re-enters the ROM to
accomplish the desired boot mode. Please note that the re-entry is done
for all boot modes except for PCIE boot mode and I2C boot mode with bus
address 0x51.

Below are the steps done in the IBL in PCIE boot mode:

-  FPGA samples the boot mode pins
-  FPGA forces the DSP to boot via I2C bus address 0x51
-  PLL is initialized correctly by the IBL on the I2C.
-  IBL reads the sampled boot mode from an FPGA register.
-  IBL checks the boot mode, if it is not I2C boot or it is I2C boot but
   with bus address 0x50, IBL writes boot mode into the DEVSTAT register
-  IBL then checks if the boot mode is PCIE boot or not. If it is, it
   executes some PCIE workaround to configure the PCIE registers (mainly
   to accept spread spectrum clock) and stays inside IBL by first
   clearing the magic address and then monitoring it for PCIE boot.

For PCIE demos with DDR memory is used, proper DDR configuration is
required, this doesn’t need the full IBL functionality. Typically DDR
can be initialized in two ways:

-  The Linux host initializes the DDR registers directly through PCIE
   link.
-  A DDR initialization image is downloaded in the L2 first to
   initialize the DDR and then reset the magic address with value 0. And
   then the application image is downloaded in

the DDR. In Processor SDK, the second approach is used.

How HelloWorld boot example works
'''''''''''''''''''''''''''''''''''''''

The Linux host first pushes the DDR init boot image data to L2 memory of
core 0, then writes the boot entry address of the DDR init boot image to
the magic address on core 0, both via PCIE. When the EVM is in PCIE boot
mode, the IBL code running on the DSP core 0 polls the entry address and
jumps to that address and starts to boot (initialize the DDR). After DDR
is properly initialized, the DDR init code clears the magic address and
keeps on polling it.

Linux host then pushes the HelloWorld boot image data to DDR memory,
then writes the boot entry address of the HelloWorld boot image to the
magic address on core 0 to boot core 0. Core 0 starts to boot and print
the “Hello World” booting information, and then boot all the other cores
by writing the address of \_c_int00 to the magic address on other cores
and sending an IPC interrupt to other cores. The RBL running on other
cores will jump to \_c_int00 and start to boot, each core will write
0xBABEFACE to its magic address by running a function
write_boot_magic_number().

Note that host boot application needs to wait for some time after
pushing the DDR init boot image and before pushing the HelloWorld boot
image to the DDR, this will ensure DDR is properly initialized.

How POST boot example works
'''''''''''''''''''''''''''''

The POST example uses L2 only. The Linux host first pushes the POST boot
image data to L2 memory of core 0, then writes the boot entry address of
the POST to the magic address on core 0, both via PCIE. The IBL code
running on the DSP core 0 polls the entry address and jumps to that
address and starts to boot.

How DSP local reset example works
'''''''''''''''''''''''''''''''''''''''

A user may want to re-run a PCIE demo without power cycle the Linux PC.
There is a need to reset the DSP chip from host software. There are
several types of resets: hard reset, soft reset and CPU local reset.
Hard reset will reset everything on the device except the PLLs, test,
emulation logic, and reset isolation modules. Since PCIE doesn’t support
reset isolation, a hard reset will reset PCIE module as well and all the
configured PCIE registers (PCIE MMRs) will be lost. Soft reset will
behave like a hard reset except that the stick bits of PCIE MMRs are
retained. The PC can’t communicate with PCIE card anymore in both hard
reset and soft reset cases.

To reset the DSP while keeping the PCIE untouched, the local reset
example does the following:

-  Put all cores in reset via PSC
-  Disable all modules except PCIE and cores via PSC
-  Configure chip level registers DSP_BOOT_ADDRn and IPCGRn: Here the
   header array converted from DSP local reset example is loaded into
   each core via PCIE; the \_c_int00 is then written to each
   DSP_BOOT_ADDRn; finally IPCGRn is written to jump start the DSP local
   reset example program, which simply polls magic address for a
   secondary boot.
-  Enable all modules previous disabled via PSC
-  Pull all cores out of reset via PSC

.. note::
  It is IBL (in local L2) that monitors magic address
  and boots the DDR init (in local L2) or POST (in local L2) or
  EDMA-interrupt (in local L2) in those demos. If one wants to load
  his/her own boot demo code, then it shouldn’t overlap with the IBL
  code. As a guideline, the IBL uses memory from 0x00800000 to
  0x0081BDFF. To check the exact memory usage, you can re-build the IBL
  by following the instructions in
  tools\boot_loader\ibl\doc\build_instructions.txt and check the
  resulting ibl_c66x_init.map file. In addition, following local L2 is
  reserved by RBL and shouldn’t be used: for 6678 ROM PG 1.0, 0x00872DC0
  – 0x0087FFFF; for 6670 ROM PG 1.0, 0x008F2DC0 – 0x008FFFFF.

