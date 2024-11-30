***************************************
Frequently Asked Questions
***************************************

How to verify IPC between Linux and MCU R5 in Keystone devices?
---------------------------------------------------------------------

Automotive applications have different memory needs and use a different memory
map defined in the auto-common.dtbo file. Therefore, the default |__SDK_FULL_NAME__|
is shipped with firmwares for only a few auxiliary cores in the Keystone devices.

Although the out-of-the-box experience does not allow to verify the
interprocessor communication (IPC) between Linux and the MCU R5,
the following steps describe how this can be done using the SDK.

.. rubric:: Steps to build IPC echotest binaries
   :name: faq-steps-to-build-ipc-echotest-binaries

All the IPC echotest binaries are built as a Yocto package **ipc-lld-fw**.
Since these binaries conflict with the automotive demos, this package is not
built in the SDK installed by default. This can be built using Yocto and installed
into the filesystem on target.

Make sure that you have setup the Yocto build environment for this. Refer to
`Building the SDK <Overview_Building_the_SDK.html>`__ section for all details.

Once the Yocto build is setup, use bitbake to build the specific package ipc-lld-fw
as shown below:

::

    TOOLCHAIN_BASE=<PATH_TO_TOOLCHAIN> MACHINE=<machine> bitbake -k ipc-lld-fw

This will create the firmware package for all the remoteproc cores in the system
where the IPC echotest functionality is implemented. The package will be located
at the directory **<Yocto work directory>/j7_evm-linux/ipc-lld-fw/<version>/deploy-ipks/**.

.. rubric:: Installing the IPC echotest binaries
   :name: faq-installing-ipc-echotest-binaries


Once the package is built on the host machine, copy it to the target filesystem.
Run thethe  following commands to install the package to target filesystem.

The **update-alternatives** command in the below instructions will set the priority
for the IPC firmware very high. This is to ensure that the symlinks are updated
appropriately. Typical firmwares will have priorities up to 20, setting the IPC
firmware priority to 100 gives it highest priority.

.. note::

    priority override is done only for the automotive firmwares like ethernet firmware
    and display sharing firmware. If you have installed additional firmwares,
    you should do it for others as well.

::

    opkg install ipc-lld-fw*.ipk
    update-alternatives --install /lib/firmware/j7-main-r5f0_0-fw j7-main-r5f0_0-fw /lib/firmware/pdk-ipc/ipc_echo_test_mcu2_0_release.strip.xer5f 100
    update-alternatives --install /lib/firmware/j7-main-r5f0_1-fw j7-main-r5f0_1-fw /lib/firmware/pdk-ipc/ipc_echo_test_mcu2_1_release.strip.xer5f 100


After this, make sure that all the firmwares are pointing to the pdk-ipc/
version of the binaries by running the following:

::

    ls -l /lib/firmware/j7*

Reboot the board and you will see the IPC echotest binaries loaded onto different
CPU cores.

How to configure K3 MSMC memory for use as SRAM or L3 cache?
---------------------------------------------------------------------

In Keystone devices, there exists on-chip memory at the MSMC interconnect.
This can be configured either as SRAM or as L3 cache.

Automotive ADAS applications, which use C7x, benefit a lot when the MSMC memory
is configured as SRAM. Alternatively, the CPU benchmark applications get performance
boost when the memory is configured as cache.

Typically, MSMC memory needs to be split between SRAM and cache with the split boundary
being aligned at 1MB. System firmware partitions SRAM between cache and SRAM at
the bootup based on the board config data structure.

Rebuild the system firmware image (sysfw.itb) with right board config to
change to desired behavior. Following are the steps to achieve this:

Modify the file **soc/j721e/evm/board-cfg.c** in **system-firmware-image-gen** repo
from the installer.

::

    /* boardcfg_msmc */
    .msmc = {
            .subhdr = {
                    .magic = BOARDCFG_MSMC_MAGIC_NUM,
                    .size = sizeof(struct boardcfg_msmc),
            },
            .msmc_cache_size = 0x0,
    },

Here, the msmc_cache_size variable can take values from 0x0 to 0xf, where 0x0
describes zero cache and 0xf describes full cache. Note that due to hardware
restriction, the total memory that gets configured as cache is rounded up to 1MB.

Following table describes an example of this for J721e platform.

+-----------------+-----------------------------------------------------------+
| msmc_cache_size | Description                                               |
+=================+===========================================================+
| 0x0             | All of MSMC memory (i.e. 8MB) configured as SRAM          |
+-----------------+-----------------------------------------------------------+
| 0x3             | 2MB of MSMC memory configured as cache, rest 6MB is SRAM  |
+-----------------+-----------------------------------------------------------+
| 0x6             | 3MB of MSMC memory configured as cache, rest 5MB is SRAM  |
+-----------------+-----------------------------------------------------------+
| 0xf             | All of MSMC memory (i.e. 8MB) configured as cache         |
+-----------------+-----------------------------------------------------------+

How to check some device tree information from user-space of Linux?
---------------------------------------------------------------------
You might need to check value of some dtb entry, for debugging, checking that
your dtb really got updated after you modfified, etc. Though you can't have a
.dts-file-like view of the device tree which was loaded, you can check values
using the entries in /proc/device-tree.

In the command prompt of Linux, you should see something similar to the
following in the /proc/device-tree directory:

::

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

- Let's say you don't know the exact path of the device tree entry you are
  trying to check. There is a __symbol__ directory in /proc/device-tree, which
  is very helpful in such cases. It has an entry for each symbol label in the
  device tree. You can find the exact path for that symbol by running ``cat``
  command on that entry. Following is an example demonstrating the use:

  ::

        root@j721e-evm:~# cat /proc/device-tree/__symbols__/main_i2c0
        /interconnect@100000/i2c@2000000

        root@j721e-evm:~# ls /proc/device-tree/interconnect@100000/i2c@2000000/
        #address-cells   clock-names  gpio@20     name       pinctrl-names
        #size-cells      clocks       gpio@22     phandle    power-domains
        clock-frequency  compatible   interrupts  pinctrl-0  reg

- You can check the value of a device tree entry using ``cat`` command if it is a
  string. But if the value is an integer or some numeric data, you will have to
  run the ``xxd`` command instead of ``cat``, to get output in a readable format.
  Following is an example demonstrating the use:

  ::

        # Example for a string value
        root@j721e-evm:~# cat /proc/device-tree/interconnect@100000/i2c@2000000/compatible
        ti,j721e-i2cti,omap4-i2c

        # Example for an integer value
        root@j721e-evm:~# xxd -g4 /proc/device-tree/interconnect@100000/i2c@2000000/clock-frequency
        00000000: 00061a80                             ....

        # The above value is in hexadecimal. You can calculate it's value in decimal by using following command
        root@j721e-evm:~# echo $((0x00061a80))
        400000

- One common scenario of a device tree change is tweaking the memory for
  remoteproc processors like R5F. You can check if it got updated correctly, by
  running a command similar to following for the specific processor core.

  ::

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
        root@j721e-evm:~# xxd -g4 /proc/device-tree/reserved-memory/r5f-memory@a2100000/reg
        00000000: 00000000 a2100000 00000000 01f00000  ................

        root@j721e-evm:~# xxd -g4 /proc/device-tree/reserved-memory/r5f-dma-memory@a2000000/reg
        00000000: 00000000 a2000000 00000000 00100000  ................
