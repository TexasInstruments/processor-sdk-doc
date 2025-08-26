Boot Time Optimizations
=======================

Introduction
------------

In today's fast-paced automotive industry, the ability to achieve quick processor boot times is more crucial than ever. This guide will walk you through the necessary steps and considerations for achieving faster boot times on |__PRODUCT_LINE_NAME__| |__PART_FAMILY_DEVICE_NAMES__| devices. From adjusting configurations to implementing best practices, you'll gain the insights needed to deliver a seamless, responsive user experience in your automotive applications. By implementing specific modifications, the default SDK offering can be optimized to boot much faster.

Reducing boot time is essential for enhancing user experience and operational efficiency. Quick boot times lead to more responsive systems, which are critical in automotive applications where every second counts. This ensures that drivers and passengers have immediate access to essential features and systems, contributing to overall safety and satisfaction.

Moreover, in the context of the rapid technological advancements and increasing demands for smart, connected vehicles, optimizing boot times can provide a competitive edge. Whether it's for infotainment systems, advanced driver-assistance systems (ADAS), or other critical automotive functions, minimizing boot times can significantly improve performance and reliability.

.. note::

    The same workflow is applied to the entire Sitara MPU family, but for each SoC, specific steps will differ and will be highlighted

The objectives of this document are as follows:

- Explain various techniques to reduce boot time

- Highlight the tradeoffs to reach the milestone

- Measurement and breakdown of default boot time

- Measurements after optimizations

Software environment
^^^^^^^^^^^^^^^^^^^^
This guide uses 10.0 Processor SDK as reference.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    - `PROCESSOR-SDK-LINUX-AM62X <https://www.ti.com/tool/download/PROCESSOR-SDK-LINUX-AM62X>`_

    - `MCU+ SDK AM62X <https://www.ti.com/tool/download/MCU-PLUS-SDK-AM62X>`_

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

    - `PROCESSOR-SDK-LINUX-AM62AX <https://www.ti.com/tool/download/PROCESSOR-SDK-LINUX-AM62A>`_

    - `MCU+ SDK AM62AX <https://www.ti.com/tool/download/MCU-PLUS-SDK-AM62A>`_

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

    - `PROCESSOR-SDK-LINUX-AM62PX <https://www.ti.com/tool/download/PROCESSOR-SDK-LINUX-AM62P>`_

    - `MCU+ SDK AM62PX <https://www.ti.com/tool/download/MCU-PLUS-SDK-AM62P>`_

Hardware setup and equipment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
-  Development kit used for testing

    .. ifconfig:: CONFIG_part_variant in ('AM62X')

        -  `SK-AM62 <https://www.ti.com/tool/SK-AM62>`_

    .. ifconfig:: CONFIG_part_variant in ('AM62AX')

        -  `SK-AM62A <https://www.ti.com/tool/SK-AM62A>`_

    .. ifconfig:: CONFIG_part_variant in ('AM62PX')

        -  `SK-AM62P-LP <https://www.ti.com/tool/SK-AM62P-LP>`_

-  Micro-USB cables for UART connection

-  Logic Analyzer with at least 4 channels and a sample rate of 10MS/s

Typical boot flow
^^^^^^^^^^^^^^^^^
This section details the Out-Of-Box boot sequence:

.. Image:: /images/typical_bootflow_spl_mpu.png
     :align: center


**PMIC** or Power Management IC controls the power supply to the SoC. As a unit, it consists of diode controllers, DC-DC conversion and voltage regulation. TI's Fulton PMIC needs about 30ms to supply power while Burton PMIC requires 18ms.

**BootROM** (Primary Program Loader) is executed first from ROM and performs basic initializations such PLLs and SRAM configuration. It then loads a bootloader image in the boot device specified by the boot switches. This entity takes about 12ms to complete.

**SPL** (Secondary Program Loader) is the first stage of the bootloader. It consists of code that fits into the SRAM and is run by the Main R5. R5 SPL initializes some peripherals and, most importantly, DDR. Subsequently, it loads TF-A, OPTEE and A53 SPL into DDR and then jumps to TF-A. A53 SPL is an intermediate Linux friendly bootloader stage used to jump to U-boot.

**TF-A** (Trusted Firmware - Arm) provides a reference trusted code base for the Armv8 architecture. It implements various ARM interface standards. The binary is typically included in the bootloader binary. It starts in the early stages of U-Boot. Without ATF, the kernel cannot setup the services which need to be executed in the Secure World environment

**OPTEE** (Trusted Execution Environment) is designed as a companion to a non-secure Linux kernel running on Arm; Cortex-A cores using the TrustZone technology.

**U-boot** proper is the second stage bootloader. It offers a flexible way to load and start the Linux Kernel and provides a minimal set of tools to interact with the board’s hardware via a command line interface. It runs from DRAM, initializing additional hardware devices (network, USB, DSI/CSI, etc.). Then, it loads and prepares the device tree (FDT). The main task handled by the U-Boot is the loading and starting of the kernel image itself.

**Kernel** runs from DDR and takes over the system completely.

**Userspace** process is executed by a user in the operating system, rather than being part of the operating system itself. It might also be executed by an init system (e.g. systemd), but it isn't part of the kernel. User space is the area of memory that non-kernel applications run in non-privileged execution mode.

Optimized bootflow
^^^^^^^^^^^^^^^^^^
This section describes an overview of the modifications that can be done to achieve shorter boot times. The succeeding sections will detail how to achieve these sequences.

.. Image:: /images/optimized_bootflow_sbl_mpu.png
     :align: center

Reducing bootloader time
------------------------

- Falcon Mode:

    This is a feature that allows us to skip **A53 SPL** and **U-boot proper** and jump to TF-A and then the kernel directly saving ~5s in our boot time. It is implemented differently depending on the bootloader.

- Choosing the right bootmedia:

    +------------------+--------------+--------------------+----------------------------------+
    |     Part         | Bootmedia    | Theoretical Read   |        Default offering          |
    |                  |              | performance (MBps) |                                  |
    +------------------+--------------+--------------------+----------+-----------+-----------+
    |                  |              |                    | AM62 EVM | AM62A EVM | AM62P EVM |
    +==================+==============+====================+==========+===========+===========+
    |    S28HS512T     | OSPI-NOR     |        330         |   YES    |     NO    |    YES    |
    +------------------+--------------+--------------------+----------+-----------+-----------+
    |   W35N01JWTBAG   | OSPI-NAND    |         50         |    NO    |    YES    |     NO    |
    +------------------+--------------+--------------------+----------+-----------+-----------+
    | MTFC16GAPALBH-IT | eMMC (HS200) |        200         |   YES    |    YES    |     NO    |
    +------------------+--------------+--------------------+----------+-----------+-----------+
    | MTFC32GAZAQHD-IT | eMMC (HS400) |        400         |    NO    |     NO    |    YES    |
    +------------------+--------------+--------------------+----------+-----------+-----------+

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    You can track current performance numbers here: `AM62X <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62X/latest/exports/docs/api_guide_am62x/DATASHEET_AM62X_EVM.html#autotoc_md184>`_

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

    You can track current performance numbers here: `AM62AX <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62AX/11_01_00_16/exports/docs/api_guide_am62ax/DATASHEET_AM62AX_EVM.html#autotoc_md148>`_

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

    You can track current performance numbers here: `AM62PX <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62PX/latest/exports/docs/api_guide_am62px/DATASHEET_AM62PX_EVM.html#autotoc_md119>`_


- Flashing binaries:

    .. ifconfig:: CONFIG_part_variant in ('AM62X')

        - `UART flashing tool AM62X <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62X/latest/exports/docs/api_guide_am62x/TOOLS_FLASH.html>`_

        - U-Boot eMMC flashing tool AM62X: :ref:`u-boot-build-guide-environment-k3`

        - :ref:`U-Boot SPI flashing tool AM62X <u-boot-introduction-qspi-ug>`

    .. ifconfig:: CONFIG_part_variant in ('AM62AX')

        - `UART flashing tool AM62AX <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62AX/11_01_00_16/exports/docs/api_guide_am62ax/TOOLS_FLASH.html>`_

        - U-Boot eMMC flashing tool AM62AX: :ref:`u-boot-build-guide-environment-k3`

        - :ref:`U-Boot SPI flashing tool AM62AX <u-boot-introduction-qspi-ug>`

    .. ifconfig:: CONFIG_part_variant in ('AM62PX')

        - `UART flashing tool AM62PX <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62PX/latest/exports/docs/api_guide_am62px/TOOLS_FLASH.html>`_

        - U-Boot eMMC flashing tool AM62PX: :ref:`u-boot-build-guide-environment-k3`

        - :ref:`U-Boot SPI flashing tool AM62PX <u-boot-introduction-qspi-ug>`

Secondary Boot Loader (SBL)
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. ifconfig:: CONFIG_part_variant in ('AM62X')

    The following section will reference `AM62X MCU+ SDK's SBL examples <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62X/latest/exports/docs/api_guide_am62x/EXAMPLES_DRIVERS_SBL.html>`_.

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

    The following section will reference `AM62AX MCU+ SDK's SBL examples <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62AX/11_01_00_16/exports/docs/api_guide_am62ax/EXAMPLES_DRIVERS_SBL.html>`_.

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

    The following section will reference `AM62PX MCU+ SDK's SBL examples <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62PX/latest/exports/docs/api_guide_am62px/EXAMPLES_DRIVERS_SBL.html>`_.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    - `AM62X Falcon Mode <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62X/latest/exports/docs/api_guide_am62x/TOOLS_BOOT.html#LINUX_APPIMAGE_GEN_TOOL>`_

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

    - `AM62AX Falcon Mode <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62AX/11_01_00_16/exports/docs/api_guide_am62ax/TOOLS_BOOT.html#LINUX_APPIMAGE_GEN_TOOL>`_

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

    - `AM62PX Falcon Mode <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62PX/latest/exports/docs/api_guide_am62px/TOOLS_BOOT.html#LINUX_APPIMAGE_GEN_TOOL>`_

- Removing unnecessary prints

    The default examples contain a large number of prints that impact boot time and need to be removed.

    - Navigate to the main.c of your example and remove calls to the following functions
        - ``Bootloader_profileAddCore``
        - ``Bootloader_profileAddProfilePoint``
        - ``Bootloader_profileUpdateAppimageSize``
        - ``Bootloader_profileUpdateMediaAndClk``
        - ``Bootloader_profilePrintProfileLog``

    - Navigate to :file:`<mcu-plus-sdk>/source/drivers/device_manager/sciclient_direct/sciclient_direct_wrapper.c` and remove the ``DebugP_log`` calls from `Sciclient_getVersionCheck` function.

    .. note::

        If an RTOS example is being used, remove prints of the additional files in :file:`<mcu-plus-sdk>/examples/drivers/boot/common/`

- Skipping OSPI PHY tuning (in case of OSPI bootmedia)

    PHY calibration allows the flash to function at maximum performance but this tuning consumes a significant amount of time that is dependent on the current algorithm implementation. In the SDK, only stage 2 examples are skipped by default.

    To validate this, do not remove the log prints from the previous subsection and observe the ``SBL Board_driversOpen`` parameter. Currently, the tuning algorithm takes 22ms to complete. If skipping is successful, it should drop down to ~150us.

    Open the relevant example's syscfg by navigating into :file:`<mcu-plus-path>/examples/drivers/boot/<example>/<soc-name>/<example-type>/ti-arm-clang/` and running :code:`make syscfg-gui`. Navigate to the `OSPI` section and enable **OSPI skip Tuning option**. Ensure that **Enable PHY** is checked as well.

    .. Image:: /images/SBL_enable_ospi_phy_skip.png
         :align: center

- Enabling DMA in the bootloader

    Open the relevant example's syscfg and navigate to the `Bootloader` section and click on **Enable DMA** if not enabled by default.

    .. Image:: /images/SBL_enable_dma.png
         :align: center

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

    - FastXSPI

        This is a special OSPI-NOR boot mode where ROM tunes OSPI PHY values when provided with the right parameters. If successful, OSPI PHY tuning need not be done by the bootloader at SBL-stage1 otherwise it will switch to the regular OSPI-NOR mode where tuning has to be done by a subsequent stage.

        Flash the relevant binary at :code:`0x3fc0000`:

            - :download:`OSPI-NOR @100MHz </files/fastxspi_pattern_am62p_100MHz.bin>`

            - :download:`OSPI-NOR @133MHz </files/fastxspi_pattern_am62p_133MHz.bin>`

            - :download:`OSPI-NOR @166MHz </files/fastxspi_pattern_am62p_166MHz.bin>`

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

    - Use DDR in single rank configuration

        The number of ranks on any DIMM is the number of independent sets of DRAMs that can be accessed for the full data bit-width of the DIMM. Dual rank gives us access to a bigger memory bank but consumes twice the tuning time. By default, DDR is in dual rank configuration and takes ~35ms that is visible in ``System_init`` in the SBL logs.

        Navigate to the DDR section in SBL-stage1 syscfg and update it to the single rank file given below to reduce the time to ~20ms.

        :download:`ddr_1600_singlerank_am62p.h </files/ddr_1600_singlerank_am62p.h>`

        .. Image:: /images/SBL_singlerank_ddr.png
         :align: center

Reducing Linux kernel boot time
-------------------------------

- Adding :code:`quiet`

    - To save 8+ seconds, add "quiet" argument in the Kernel "bootargs". It suppresses most messages during the Linux start-up sequence. To access the logs after login, you can run :code:`dmesg` for the logs to be printed. By default, quiet is at a loglevel of 4 and should be adequate to suppress the majority of logs but if finer control is required :code:`quiet` can be replaced with :code:`loglevel=x` where x can be 1-14.

    - The kernel looks for bootargs in 3 places: U-Boot environment variable, the device tree and the kernel config. You can add the following in any of the 3 locations.

        U-Boot console:

        .. code-block:: console

            U-Boot=> setenv bootargs 'console=ttyS2,115200n8 fsck.mode=skip sysrq_always_enabled quiet'

        Device Tree:

        .. code-block:: dts

            chosen {
                ...
                bootargs = "console=ttyS2,115200n8 earlycon=ns16550a,mmio32,0x02800000 quiet";
                ...
            };

        Kernel config:

        .. code-block:: kconfig

            CONFIG_CMDLINE="console=ttyS2,115200n8 earlycon=ns16550a,mmio32,0x02800000 quiet"

- Using a smaller kernel system

    -  By default, the kernel image contains a lot of drivers and filesystems to enable the functionality supported for the board but are not necessary for early boot. Trim kernel capabilities by using

        - `ti_arm64_prune.config` - removes irrelevant platform drivers
        - `ti_early_display.config` - converts the majority of functionality into loadable modules

    Usage:

    .. code-block:: console

        kernel$ make ARCH=arm64 CROSS_COMPILE=<path-to-compiler>/aarch64-none-linux-gnu- defconfig ti_arm64_prune.config ti_early_display.config

    .. tip::

        You can access :file:`<kernel-path>/kernel/configs/ti_early_display.config` and see the breakdown of how much time is saved by disabling each module and take a call on whether the functionality is required and its effect on boot time

- Disabling nodes in DT

    Unnecessary nodes can be disabled by adding :code:`status = "disabled"` to the nodes. While this will not directly affect boot time, the minimal kernel will not throw probe errors during boot.

Reducing userspace boot time
----------------------------

It is recommended to use a tiny intermediate filesystem that can be used to run applications early with minimal configuration and then mount into a filesystem with full functionality. For this purpose, the installer packages a filesystem: :file:`<PSDK_PATH>/filesystem/<machine>/tisdk-tiny-initramfs-am62xx-evm.cpio` that can be used as an initramfs.

In order to package the filesystem as initramfs into the kernel, follow these steps:

1. Extract the cpio archive to a preferred location via GUI or

    .. code-block:: console

        $ mkdir output
        $ cd output
        $ cpio -idv < tisdk-tiny-initramfs-am62xx-evm.cpio


2. Edit the kernel config:

    .config:

    .. code-block:: kconfig

        CONFIG_INITRAMFS_SOURCE="/path/to/filesystem"

    or using :code:`menuconfig`:

    .. code-block:: kconfig

        kernel$ make ARCH=arm64 CROSS_COMPILE=<path-to-compiler>/aarch64-none-linux-gnu- menuconfig

        General setup ->
            Initial RAM filesystem and RAM disk (initramfs/initrd) support ->
                Initramfs source file(s)
                    /path/to/filesystem

3. Rebuild the kernel

    .. code-block:: console

        kernel$ make ARCH=arm64 CROSS_COMPILE=<path-to-compiler>/aarch64-none-linux-gnu- Image -j64

The time taken to boot filesystem is measured from Process ID 1(PID1) to login prompt which is 1.98s with the initramfs filesystem. In order to further drop this time, you can:

.. caution::

    Please ensure that you do not mistakenly affect the host computer while making the below changes

- Remove startup scripts from the tiny filesystem

    .. code-block:: console

        host$ rm <filesystem>/etc/rc5.d/*
        host$ cd <filesystem>/etc/rcS.d
        host$ rm S02banner.sh S04udev S05checkroot.sh S06modutils.sh S07bootlogd S29read-only-rootfs-hook.sh S36bootmisc.sh S37populate-volatile.sh S38dmesg.sh S38urandom

    This shaves off 1.536s from filesystem boot time. udev alone takes up 1.152s.

- Remove package manager, console logo and add /dev/null in the filesystem

    .. code-block:: console

        host$ rm -r <filesystem>/usr/lib/opkg
        host$ rm <filesystem>/etc/issue
        host$ cd <filesystem>/dev
        host$ mknod -m 0600 null c 1 3

    This removes 52ms from the boot up time.

Measurements
------------

The following section displays the time taken by each stage to start and end. Four profile points were used:

    - PMIC time is taken from the datasheet
    - MCU_PORz (White)
    - SBL_start (Brown)
    - SBL_end (Red)
    - Kernel_end (Gold)

| Range 1 (Power ON to PMIC):
| It is not convenient to measure this range since it is dependent on the hardware to provide the power to the PMIC quickly. While TI experts can give suggestions to reduce the time, it will not be TI's commitment.

| Range 2 (MCU_PORz to SBL_start):
| MCU_PORz is the Power-On-Reset pin that is set HIGH as soon as the PMIC powers the voltage rails. This can be probed using Pin #28 on the MCU Header (J11) of the |__PART_FAMILY_DEVICE_NAMES__|. All pins are automatically set HIGH at this point.

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

    SBL_start is set to LOW as soon as the Bootloader comes up. To enable this, navigate into the main.c of your bootloader (Example: :file:`<mcu-plus-path>/examples/drivers/boot/sbl_ospi_linux_multistage/sbl_ospi_linux_stage1/<soc-name>/<example-type>/main.c`) and add the following section to set MCU_I2C0_SCL (Pin #24 on the MCU Header J11) to LOW. It can be modified for any other pin as well.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    SBL_start is set to LOW as soon as the Bootloader comes up. To enable this, navigate into the main.c of your bootloader (Example: :file:`<mcu-plus-path>/examples/drivers/boot/sbl_ospi_linux_multistage/sbl_ospi_linux_stage1/<soc-name>/<example-type>/main.c`) and add the following section to set MCU_I2C0_SCL (Pin #24 on the MCU Header J11) to LOW. It can be modified for any other pin as well.

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

    SBL_start is set to LOW as soon as the Bootloader comes up. To enable this, navigate into the main.c of your bootloader (Example: :file:`<mcu-plus-path>/examples/drivers/boot/sbl_ospi_nand_linux_multistage/sbl_nand_ospi_linux_stage1/<soc-name>/<example-type>/main.c`) and add the following section to set MCU_I2C0_SCL (Pin #24 on the MCU Header J11) to LOW. It can be modified for any other pin as well.

.. code-block:: C

    #include <drivers/gpio.h>

    /* GPIO PIN Macros */
    #define CONFIG_GPIO0_BASE_ADDR (CSL_MCU_GPIO0_BASE)
    #define CONFIG_GPIO0_PIN (17)
    #define CONFIG_GPIO0_DIR (GPIO_DIRECTION_OUTPUT)
    #define CONFIG_GPIO0_TRIG_TYPE (GPIO_TRIG_TYPE_NONE)
    #define CONFIG_GPIO_NUM_INSTANCES (1U)

    static Pinmux_PerCfg_t gPinMuxMcuCfg[] = {
        /* MCU_GPIO0 pin config MCU_GPIO0_17 -> MCU_I2C0_SCL (E11) */
        {
            PIN_MCU_I2C0_SCL,
            ( PIN_MODE(7) | PIN_INPUT_ENABLE | PIN_PULL_DISABLE )
        },
        {PINMUX_END, PINMUX_END}
    };

    int main()
    {
        Pinmux_config(gPinMuxMcuCfg, PINMUX_DOMAIN_ID_MCU); // Configure PinMux
        GPIO_setDirMode(CONFIG_GPIO0_BASE_ADDR, CONFIG_GPIO0_PIN, CONFIG_GPIO0_DIR);    //Set GPIO direction
        GPIO_pinWriteLow(CONFIG_GPIO0_BASE_ADDR, CONFIG_GPIO0_PIN); // Set GPIO state to LOW

        ...


| Range 3 (SBL_start to SBL_end):
| This range measures the time the bootloader takes to configure the DDR, load + start the default HSM core, MCU core and Application Core. The GPIO that was set to LOW for SBL_start can be set to HIGH by copying the above code section and using `GPIO_pinWriteHigh`.

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

    For this measurement, the FreeRTOS IPC example was used for second stage bootloader (:file:`<mcu_plus_sdk>/examples/drivers/ipc/ipc_rpmsg_echo_linux/am62px-sk/wkup-r5fss0-0_freertos`). Open the :file:`examples/drivers/boot/common/soc/am62px/sbl_ospi_linux_stage2.c`. Turn the GPIO HIGH after ``App_loadLinuxImages`` function.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    For this measurement, the OSPI NOR example was used (:file:`<mcu_plus_sdk>/examples/drivers/boot/sbl_ospi_linux_multistage/sbl_ospi_linux_stage2/am62x-sk/r5fss0-0_nortos/main.c`). Turn the GPIO HIGH after ``App_loadLinuxImages`` function.

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

    For this measurement, the OSPI NAND example was used (:file:`<mcu_plus_sdk>/examples/drivers/boot/sbl_ospi_nand_linux_multistage/sbl_ospi_nand_linux_stage2/am62ax-sk/r5fss0-0_nortos/main.c`). Turn the GPIO HIGH after ``App_loadLinuxImages`` function.

| Range 4 (SBL_end to Kernel_end):
| To toggle GPIO inside the kernel, the Device Tree(DT) and kernel has to be updated. In this example, it was decided to add GPIO functionality into a driver that is definitely being probed quite early on like serial driver (:file:`drivers/tty/serial/8250/8250_omap.c`). We will be using GPIO0_39 pin on the User Expansion Header (J4).

In the relevant dts, add the following:

.. code-block:: dts

    &main_gpio0 {
        ...
        status = "okay";
        pinctrl-names = "default";
        pinctrl-0 = <&test_gpio_default>;
    };

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

    In `&main_pmx0` node, add the relevant IOPAD:

    .. code-block:: dts

        test_gpio_default: test-gpio {
            pinctrl-single,pins = <
                AM62PX_IOPAD(0x00a0, PIN_INPUT, 7) /* (P24) GPMC0_WPn.GPIO0_39 */
            >;
        };

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

    In `&main_pmx0` node, add the relevant IOPAD:

    .. code-block:: dts

        test_gpio_default: test-gpio {
            pinctrl-single,pins = <
                AM62AX_IOPAD(0x00a0, PIN_INPUT, 7) /* (K17) GPMC0_WPn.GPIO0_39 */
            >;
        };

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    In `&main_pmx0` node, add the relevant IOPAD:

    .. code-block:: dts

        test_gpio_default: test-gpio {
            pinctrl-single,pins = <
                AM62X_IOPAD(0x00a0, PIN_INPUT, 7) /* (K25) GPMC0_WPn.GPIO0_39 */
            >;
        };

In the `&main_uart0` node, connect the GPIO by adding

.. code-block:: dts

    test-gpios = <&main_gpio0 39 GPIO_ACTIVE_HIGH>;

Update the :file:`drivers/tty/serial/8250/8250_omap.c` driver. Add the following section before the `omap8250_probe` function:

.. code-block:: C

    static struct gpio_desc *gpio;

    void test_gpio_on(void)
    {
	    gpiod_direction_output(gpio, 1);
	    gpiod_set_value(gpio, 1);
    }
    EXPORT_SYMBOL_GPL(test_gpio_on);
    void test_gpio_off(void)
    {
	    gpiod_direction_output(gpio, 0);
	    gpiod_set_value(gpio, 0);

    }
    EXPORT_SYMBOL_GPL(test_gpio_off);

and the following in the `omap8250_probe` function:

.. code-block:: C

    gpio = devm_gpiod_get(&pdev->dev, "test", GPIOD_OUT_LOW);
	 if (IS_ERR(gpio)) {
		 return PTR_ERR(gpio);
	 }

To measure the instance when the filesystem starts, navigate to :file:`init/main.c` and toggle the GPIO:

.. code-block:: C

       /* Declare test_gpio somewhere before the kernel_init function */
       void test_gpio_on(void);

       /* Inside the kernel_init function and before ramdisk_execute_command, place this*/
       test_gpio_on();

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    .. Image:: /images/am62x_ospi_boot_analyser.png
     :align: center

    .. code-block:: console

        [2024-03-29 11:52:40.318] NOTICE:  BL31: v2.10.0(release):v2.10.0-367-g00f1ec6b87-dirty
        [2024-03-29 11:52:40.318] NOTICE:  BL31: Built : 16:09:05, Feb  9 2024
        [2024-03-29 11:52:41.098]
        [2024-03-29 11:52:41.098] am62xx-evm login:

    +-------------------+-----------+
    |       Stage       | Time (ms) |
    +===================+===========+
    | PMIC (TPS6521904) |     30    |
    +-------------------+-----------+
    |        ROM        |     33    |
    +-------------------+-----------+
    |        SBL        |    238    |
    +-------------------+-----------+
    |    Linux Kernel   |    415    |
    +-------------------+-----------+
    |      Tiny FS      |    365    |
    +-------------------+-----------+
    |             Total |   1081    |
    +-------------------+-----------+

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

    .. Image:: /images/am62ax_ospi_boot_analyser.png
     :align: center

    -622ms includes SBL C7x image load

    .. code-block:: console

        [2024-03-29 13:02:19.196] NOTICE:  BL31: v2.10.0(release):v2.10.0-367-g00f1ec6b87-dirty
        [2024-03-29 13:02:19.196] NOTICE:  BL31: Built : 16:09:05, Feb  9 2024
        [2024-03-29 13:02:19.991]
        [2024-03-29 13:02:19.991] am62xx-evm login:

    +--------------------+-----------+
    |       Stage        | Time (ms) |
    +====================+===========+
    | PMIC (TPS65931211) |     30    |
    +--------------------+-----------+
    |        ROM         |     48    |
    +--------------------+-----------+
    |        SBL         |    622    |
    +--------------------+-----------+
    |    Linux Kernel    |    450    |
    +--------------------+-----------+
    |      Tiny FS       |    345    |
    +--------------------+-----------+
    |              Total |   1495    |
    +--------------------+-----------+

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

    .. Image:: /images/am62px_ospi_boot_analyser.png
     :align: center

    .. code-block:: console

        [2025-07-10 17:37:54.176] NOTICE:  BL31: v2.13.0(release):v2.13.0-240-gd90bb650fe-dirty
        [2025-07-10 17:37:41.176] NOTICE:  BL31: Built : 21:37:18, Jun 23 2025
        [2025-07-10 17:37:42.972]
        [2025-07-10 17:37:42.972] am62xx-evm login:

    +-----------------+-----------+
    |      Stage      | Time (ms) |
    +=================+===========+
    | PMIC (TPS65224) |     15    |
    +-----------------+-----------+
    |       ROM       |     30    |
    +-----------------+-----------+
    |       SBL       |    186    |
    +-----------------+-----------+
    |  Linux Kernel   |    548    |
    +-----------------+-----------+
    |     Tiny FS     |    248    |
    +-----------------+-----------+
    |           Total |   1027    |
    +-----------------+-----------+

Bootloader loads HSM binary (9KB), MCU/DSP image (50KB) and Kernel+FS image (22MB) in the above measurements

.. note::

   Filesytem time is measured using minicom time stamp. ( Boot Time via minicom - Kernel time by GPIO = Filesystem Time )

Additional notes
----------------

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62PX')

    .. note::

        Ensure that you are not affecting your host computer when making the changes detailed below.
        For early display with OLDI panel, disable bridge-hdmi or sii9022 node in device tree.
        Also use fdtoverlay command to modify dtb file (base tree) with dtbo overlay for OLDI panel.

    - This statically compiled :download:`modetest </files/modetest>` can be added to the filesystem to test out display at boot on an OLDI panel.

        - `init` is a symbolic link to /sbin/init. Remove the file sbin/init

            .. code-block:: console

                rm <filesystem>/sbin/init

        - Create a new sbin/init and add the following.

             .. code-block:: sh

                #!/bin/sh

                mount -t proc none /proc
                mount -t sysfs none /sys
                mount -t devtmpfs  dev  /dev

                # Run modetest in the background
                # 40 - connector ID
                # 38 - CRTC ID
                # 1920x1200 - resolution of panel
                (modetest -M tidss -s 40@38:1920x1200 0<&- 2>/tmp/output.log) &

                exec /sbin/init.sysvinit $*

            You can get the connector ID and CRTC ID of your OLDI panel by running :code:`kmsprint` or :code:`modetest -M tidss`

        - Make it executable

            .. code-block:: console

                chmod +x <filesystem>/sbin/init


.. ifconfig:: CONFIG_part_variant in ('AM62AX')

    - While AM62A ships with OSPI-NAND, it can be replaced with the OSPI-NOR flash with ease. NAND flash support needs to be replaced with NOR flash support

        - SPL:

            Rebuild :ref:`Build-U-Boot-label` with OSPI NOR support.

        - SBL:

            Update the Flash type in Flash section in syscfg to reflect NOR. Save and build SBL.

Troubleshooting
---------------

- If the following logs are noticed and kernel does not come up, it suggests that TF-A is not receiving data from DM which probably hasn't had enough time to run completely

    .. code-block:: console

        ERROR:   Timeout waiting for thread SP_RESPONSE to fill
        ERROR:   Thread SP_RESPONSE verification failed (-60)
        ERROR:   Message receive failed (-60)
        ERROR:   Failed to get response (-60)
        ERROR:   Transfer send failed (-60)
