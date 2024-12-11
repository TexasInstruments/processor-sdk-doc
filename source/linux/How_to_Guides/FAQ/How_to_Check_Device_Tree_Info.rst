How to check some device tree information from user-space of Linux?
===================================================================

You might need to check value of some dtb entry, for debugging, checking that
your dtb really got updated after you modfified, etc. Though you can't have a
.dts-file-like view of the device tree which was loaded, you can check values
using the entries in /proc/device-tree.

In the command prompt of Linux, you should see something similar to the
following in the /proc/device-tree directory:

.. code-block:: console

   root@j721e-evm:~# ls /proc/device-tree/
   #address-cells  firmware                l3-cache0
   #size-cells     fixedregulator-evm12v0  main_r5fss_cpsw9g_virt_mac0
   __symbols__     fixedregulator-sd       memory@80000000
   aliases         fixedregulator-vsys3v3  model
   chosen          fixedregulator-vsys5v0  name
   compatible      gpio-keys               pmu
   connector       interconnect@100000     reserved-memory
   cpus            interrupt-parent        serial-number
   dma_buf_phys    ion                     sound@0
   dummy-panel     l2-cache0               timer-cl0-cpu0

Following are some typical usages you might need:

Let's say you don't know the exact path of the device tree entry you are
trying to check. There is a :file:`__symbols__` directory in /proc/device-tree, which
is very helpful in such cases. It has an entry for each symbol label in the
device tree. You can find the exact path for that symbol by running :command:`cat`
command on that entry. Following is an example demonstrating the use:

.. ifconfig:: CONFIG_part_variant not in ('AM62X', 'AM62PX', 'AM62AX', 'AM64X', 'AM65X')

   .. code-block:: console

      root@j721e-evm:~# cat /proc/device-tree/__symbols__/main_i2c0
      /interconnect@100000/i2c@2000000

      root@j721e-evm:~# ls /proc/device-tree/interconnect@100000/i2c@2000000/
      #address-cells   clock-names  gpio@20     name       pinctrl-names
      #size-cells      clocks       gpio@22     phandle    power-domains
      clock-frequency  compatible   interrupts  pinctrl-0  reg

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62PX', 'AM62AX', 'AM64X', 'AM65X')

   .. code-block:: console

      root@am62xx-evm:~# cat /proc/device-tree/__symbols__/main_i2c0
      /bus@f0000/i2c@20000000

      root@am62xx-evm:~# ls /proc/device-tree/bus@f0000/i2c@20000000/
      '#address-cells'   clock-names	 eeprom@51    phandle	      power-domains   tps6598x@3f
      '#size-cells'	   clocks	 interrupts   pinctrl-0       reg
      clock-frequency   compatible	 name	      pinctrl-names   status

You can check the value of a device tree entry using :command:`cat` command if it is a
string. But if the value is an integer or some numeric data, you will have to
run the :command:`hexdump` command instead to get output in a readable format.
Following is an example demonstrating the use:

.. ifconfig:: CONFIG_part_variant not in ('AM62X', 'AM62PX', 'AM62AX', 'AM64X', 'AM65X')

   .. code-block:: console

      # Example for a string value
      root@j721e-evm:~# cat /proc/device-tree/interconnect@100000/i2c@2000000/compatible
      ti,j721e-i2cti,omap4-i2c

      # Example for an integer value where the first column represents input offsets
      root@j721e-evm:~# hexdump -C /proc/device-tree/interconnect@100000/i2c@2000000/clock-frequency
      00000000  00 06 1a 80                                       |....|
      00000004

      # The above value is in hexadecimal. You can calculate it's value in decimal by using following command
      root@j721e-evm:~# echo $((0x00061a80))
      400000

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62PX', 'AM62AX', 'AM64X', 'AM65X')

   .. code-block:: console

      # Example for a string value
      root@am62xx-evm:~# cat /proc/device-tree/bus@f0000/i2c@20000000/compatible
      ti,am64-i2cti,omap4-i2c

      # Example for an integer value where the first column represents input offsets
      root@am62xx-evm:~# hexdump -C /proc/device-tree/bus@f0000/i2c@20000000/clock-frequency
      00000000  00 06 1a 80                                       |....|
      00000004

      # The above value is in hexadecimal. You can calculate it's value in decimal by using following command
      root@am62xx-evm:~# echo $((0x00061a80))
      400000

One common scenario of a device tree change is tweaking the memory for
remoteproc processors like R5F. You can check if it got updated correctly, by
running a command similar to following for the specific processor core.

.. ifconfig:: CONFIG_part_variant not in ('AM62X', 'AM62PX', 'AM62AX', 'AM64X', 'AM65X')

   .. code-block:: console

      # Finding symbols for R5Fs
      root@j721e-evm:~# ls /proc/device-tree/__symbols__/main_r5fss*
      /proc/device-tree/__symbols__/main_r5fss0                          /proc/device-tree/__symbols__/main_r5fss0_core1_dma_memory_region  /proc/device-tree/__symbols__/main_r5fss1_core0_memory_region
      /proc/device-tree/__symbols__/main_r5fss0_core0                    /proc/device-tree/__symbols__/main_r5fss0_core1_memory_region      /proc/device-tree/__symbols__/main_r5fss1_core1
      /proc/device-tree/__symbols__/main_r5fss0_core0_dma_memory_region  /proc/device-tree/__symbols__/main_r5fss1                          /proc/device-tree/__symbols__/main_r5fss1_core1_dma_memory_region
      /proc/device-tree/__symbols__/main_r5fss0_core0_memory_region      /proc/device-tree/__symbols__/main_r5fss1_core0                    /proc/device-tree/__symbols__/main_r5fss1_core1_memory_region
      /proc/device-tree/__symbols__/main_r5fss0_core1                    /proc/device-tree/__symbols__/main_r5fss1_core0_dma_memory_region

      # Finding location from the symbols
      root@j721e-evm:~# cat /proc/device-tree/__symbols__/main_r5fss0_core0_memory_region
      /reserved-memory/r5f-memory@a2100000

      root@j721e-evm:~# cat /proc/device-tree/__symbols__/main_r5fss0_core0_dma_memory_region
      /reserved-memory/r5f-dma-memory@a2000000

      # Checking the values
      root@j721e-evm:~# hexdump -C /proc/device-tree/reserved-memory/r5f-memory@a2100000/reg
      00000000: 00000000 a2100000 00000000 01<address>0  ................

      root@j721e-evm:~# hexdump -C /proc/device-tree/reserved-memory/r5f-dma-memory@a2000000/reg
      00000000: 00000000 a2000000 00000000 00100000  ................

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62PX', 'AM62AX', 'AM64X', 'AM65X')

   .. code-block:: console

      # Finding symbols for remote cores
      root@am62xx-evm:~# ls /proc/device-tree/__symbols__/ | grep "r5f"; ls /proc/device-tree/__symbols__/ | grep "m4f"; ls /proc/device-tree/__symbols__/ | grep "c7x";
      wkup_r5fss0
      wkup_r5fss0_core0
      wkup_r5fss0_core0_dma_memory_region
      wkup_r5fss0_core0_memory_region
      mcu_m4fss
      mcu_m4fss_dma_memory_region
      mcu_m4fss_memory_region

      # Finding location from the symbols
      root@am62xx-evm:~# cat /proc/device-tree/__symbols__/mcu_m4fss_memory_region
      /reserved-memory/m4f-memory@9cc00000

      root@am62xx-evm:~# cat /proc/device-tree/__symbols__/mcu_m4fss_dma_memory_region
      /reserved-memory/m4f-dma-memory@9cb00000

      # Checking the values
      root@am62xx-evm:~# hexdump -C /proc/device-tree/reserved-memory/m4f-memory@9cc00000/reg
      00000000  00 00 00 00 9c c0 00 00  00 00 00 00 00 e0 00 00  |................|
      00000010

      root@am62xx-evm:~# hexdump -C /proc/device-tree/reserved-memory/m4f-dma-memory@9cb00000/reg
      00000000  00 00 00 00 9c b0 00 00  00 00 00 00 00 10 00 00  |................|
      00000010

.. warning::

   Before tweaking the memory for remote processors, please verify that the memory
   can be modified since some remote processors can be running firmware like DM firmware.
