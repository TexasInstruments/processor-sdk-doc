##############
Flash via UART
##############

UART is used as the transport or interface to send the file to flash to the EVM.

***************
Important files
***************

:file:`uart_uniflash.py` is located at :file:`<TI_SDK_PATH>/bin/uart_uniflash/uart_uniflash.py`

Flashing application and example flash configuration files for GP, HS-FS and HS
are located at

.. ifconfig:: CONFIG_part_variant in ('AM64X')

    :file:`<TI_SDK_PATH>/bin/uart_uniflash/bin/am64xx-evm/`

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    :file:`<TI_SDK_PATH>/bin/uart_uniflash/bin/am62xx-evm/`,
    :file:`<TI_SDK_PATH>/bin/uart_uniflash/bin/am62xx-lp-evm/`,
    :file:`<TI_SDK_PATH>/bin/uart_uniflash/bin/am62xxsip-evm/`

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

    :file:`<TI_SDK_PATH>/bin/uart_uniflash/bin/am62axx-evm/`

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

    :file:`<TI_SDK_PATH>/bin/uart_uniflash/bin/am62pxx-evm/`

***********************
Requirements on Host PC
***********************

The tool is implemented using python and needs python version 3.x on Linux host.

The tool uses additional python packages as listed below.

    * pyserial for UART access on PC
    * xmodem for the file transfer protocol
    * tqdm for progress bar when the tool is run

**********************
Getting ready to flash
**********************

Make sure the flashing application and binaries you want to flash is built for the EVM.

Make sure you have installed python version 3.x and additional packages.

Make sure you have identified the UART port on the EVM.

************************
Flash configuration file
************************

Create a flash configuration file, using the example flash configuration file.

The flashing application (1 or 2 stage) needs to be flashed before flashing the
binaries. Refer the flash configuration files for number of stages needed. Also
modify the flash configuration to specify the correct path. Ex. for HS-FS

.. code-block:: text

    --flash-writer=<enter path to file>/sbl_uart_uniflash_stage1.release.hs_fs.tiimage

Now edit or add path to your binaries in the flash configuration file and also the offset to be flashed at.
Example.

.. code-block:: text

    --file=<path to file>/tiboot3.bin --operation=flash --flash-offset=0x0

.. ifconfig:: CONFIG_part_variant in ('AM62X','AM64X','AM62PX')

    **Flash configuration file for flashing to OSPI NOR**

    Create a flash configuration file. Refer to :file:`example_sbl_ospi_linux.cfg` for GP
    devices, :file:`example_sbl_ospi_linux_hs.cfg` for HS and :file:`example_sbl_ospi_linux_hs_fs.cfg`
    for HS-FS.

    Specify the paths of flashing application and files to be flashed at which
    offset in the flash configuration file.

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

    **Flash configuration file for flashing to OSPI NAND**

    Create a flash configuration file. Refer to :file:`example_sbl_ospi_nand_linux.cfg`
    for GP devices, :file:`example_sbl_ospi_nand_linux_hs.cfg` for HS and :file:`example_sbl_ospi_nand_linux_hs_fs.cfg`
    for HS-FS.

    Specify the paths of flashing application and files to be flashed at which
    offset in the flash configuration file.

******************
Flashing the files
******************

Set EVM in UART BOOT MODE and power on the EVM.

Run below python command on the Windows command prompt (cmd.exe) or Linux bash
shell to flash the files

.. code-block:: console

    cd <TI_SDK_PATH>/bin/uart_uniflash/
    python uart_uniflash.py -p {name of your UART com port} --cfg={path to your edited config file}

At each step in the flashing your will see success or error messages, including
progress as the file is being transferred.

******************
Flash tool options
******************

Type below to see all the possible options with the flashing tool

.. code-block:: console

    cd <TI_SDK_PATH>/bin/uart_uniflash/
    python uart_uniflash.py --help
