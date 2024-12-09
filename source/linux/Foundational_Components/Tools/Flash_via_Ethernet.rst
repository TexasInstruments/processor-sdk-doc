##################
Flash via Ethernet
##################

Ethernet is used for peripheral boot and then to flash the files to on board memory
using DHCP server and TFTP.

********
Get Tool
********

SDK installer
=============

Download and install Processer SDK Installer. For steps refer :ref:`download-and-install-sdk`.

Clone repository
================

Clone the sources from `here <https://git.ti.com/cgit/processor-sdk/uboot-flash-writer/>`__.

.. code-block:: console

    git clone https://git.ti.com/git/processor-sdk/uboot-flash-writer.git
    git checkout master

***************
Important files
***************

Environment variable text files are located at following path.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    .. code-block:: console

        In SDK installer
        <TI_SDK_PATH>/bin/Ethernet_flash/am62xx-evm/

        In source repo
        tools/Ethernet_flash/bin/am62xx-evm/

.. ifconfig:: CONFIG_part_variant in ('AM64X')

    .. code-block:: console

        In SDK installer
        <TI_SDK_PATH>/bin/Ethernet_flash/am64xx-evm/

        In source repo
        tools/Ethernet_flash/bin/am64xx-evm/

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   .. note::

        This documentation note is applicable only for am62xx-evm.

***********************
Requirements on host PC
***********************

Set up Ethernet boot. For details of Ethernet boot refer :ref:`booting-over-ethernet`.

***********************************************************
Building bootloader binaries for flashing and Ethernet Boot
***********************************************************

First you need to override the bootcmd command to send the environment variable
text file.

.. code-block:: text

    CONFIG_BOOTCOMMAND="dhcp <name of your uEnv.txt file>; env import -t ${loadaddr} $filesize; run user_commands;"

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    Add above line to :file:`am62x_evm_a53_defconfig` file

.. ifconfig:: CONFIG_part_variant in ('AM64X')

    Update CONFIG_BOOTCOMMAND in :file:`am64x_evm_a53_defconfig` file as above

It will enable sending :file:`uEnv.txt` after Ethernet boot, import the environment
variable and run *user_commands* after Ethernet boot.

Next build the bootloader binaries for Ethernet boot. For details refer :ref:`booting-over-ethernet`.

**********************
Getting ready to flash
**********************

Make sure that the bootloader binaries for flashing and Ethernet boot is built for
the EVM and place them in the TFTP directory.

Place the files to be flashed to TFTP directory.

Make sure to set up Ethernet boot.

For connection refer :ref:`booting-over-ethernet`.

*******************************************
Environment variable text file for flashing
*******************************************

It will be used to set environment variables in U-Boot for flashing. Create a new
:file:`uEnv.txt` file by using existing uEnv files as reference

It assigns U-Boot commands to run the list of commands specified by user to variable
:code:`user_commands`. Ex. for transfer to eMMC following commands are assigned to variable
:code:`user_commands`.

.. code-block:: text

    user_commands=echo Flashing_on_emmc; run command_list;

To add new U-Boot commands, assign them to a variable in text file. For example

.. code-block:: text

    example_command1=echo Flash
    example_command2=mmc list

Now add the variables to :code:`command_list` to run them. By this way you can add or remove
commands as per your choice.

.. code-block:: text

    command_list=run example_command1; run example_command2;

Also make sure to replace file names in text files with the actual names of files
to be flashed. Ex. to transfer :file:`tiboot3.bin` over TFTP to EVM

.. code-block:: text

    #Enter your filename in place of tiboot3.bin
    cmd_3=dhcp tiboot3.bin

**Flash to eMMC**

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    Use :file:`uEnv_ethernet_emmc_am62xx-evm.txt` file as reference located at following path.

    .. code-block:: console

        In SDK installer
        <TI_SDK_PATH>/bin/Ethernet_flash/am62xx-evm/uEnv_ethernet_emmc_am62xx-evm.txt
     
        In source repo
        tools/Ethernet_flash/bin/am62xx-evm/uEnv_ethernet_emmc_am62xx-evm.txt


.. ifconfig:: CONFIG_part_variant in ('AM64X')

    Use :file:`uEnv_ethernet_emmc_am64xx-evm.txt` file as reference located at following path.

    .. code-block:: console

        In SDK installer
        <TI_SDK_PATH>/bin/Ethernet_flash/am62xx-evm/uEnv_ethernet_emmc_am64xx-evm.txt

        In source repo
        tools/Ethernet_flash/bin/am62xx-evm/uEnv_ethernet_emmc_am64xx-evm.txt

.. ifconfig:: CONFIG_part_variant in ('AM64X','AM62X')

**Flash to OSPI NOR**

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    Use :file:`uEnv_ethernet_ospi-nor_am62xx-evm.txt` file as reference located at following path.

    .. code-block:: console

        In SDK installer
        <TI_SDK_PATH>/bin/Ethernet_flash/am62xx-evm/uEnv_ethernet_emmc_am62xx-evm.txt

        In source repo
        tools/Ethernet_flash/bin/am62xx-evm/uEnv_ethernet_emmc_am62xx-evm.txt

.. ifconfig:: CONFIG_part_variant in ('AM64X')

    Use :file:`uEnv_ethernet_ospi-nor_am64xx-evm.txt` file as reference located at following path.

    .. code-block:: console

        In SDK installer
        <TI_SDK_PATH>/bin/Ethernet_flash/am64xx-evm/uEnv_ethernet_ospi-nor_am64xx-evm.txt

        In source repo
        tools/Ethernet_flash/bin/am64xx-evm/uEnv_ethernet_ospi-nor_am64xx-evm.txt

    **Flash to GPMC NAND**

    Use :file:`uEnv_ethernet_gpmc-nand_am64xx-evm.txt` file as reference located at following path.

    .. code-block:: console

        In SDK installer
        <TI_SDK_PATH>/bin/Ethernet_flash/am64xx-evm/uEnv_ethernet_gpmc-nand_am64xx-evm.txt

        In source repo
        tools/Ethernet_flash/bin/am64xx-evm/uEnv_ethernet_gpmc-nand_am64xx-evm.txt

