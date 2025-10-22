.. please note that there is no GPIO user guide from LCPD

----
GPIO
----

.. rubric:: GPIO Driver Overview
   :name: gpio-driver-overview

The GPIO Driver enables the GPIO controllers available on the device.
The driver configures the GPIO hardware and interfaces and makes them
available to user space as character device or other device drivers
that need to access pins.
For example, a MMC/SD driver may need to read a GPIO as in input to
determine if a card is present. The H/W GPIO controllers available will vary by SoC and system
configuration.

.. ifconfig:: CONFIG_part_family in ('J7_family', 'AM335X_family', 'AM437X_family')

    .. ifconfig:: CONFIG_part_family in ('J7_family')

        .. rubric:: J721E specifics

        J721E SoCs host DAVINCI GPIO IP.

    Current software supports banked GPIO interrupt only. 16 GPIOs form a bank.
    Each bank can produce an interrupt; this is done to save the number of interrupt
    lines reaching the CPU.
    CONFIG_GPIO_DAVINCI=y should be part of the defconfig.
    Driver source code: drivers/gpio/gpio-davinci.c


.. rubric:: Overview
   :name: overview-gpio-driver

The GPIO controllers allow interaction with GPIO pins for input/output
and interrupt generation.

.. Image:: /images/GPIO_driver_diagram.png

.. rubric:: User Layer
   :name: user-layer

The GPIO driver can be used in user space via Linux CLI. This section provides examples, command-line-tools, and guidance for using GPIOs in user space.

.. note ::

   Since Linux 4.8, the GPIO sysfs interface is deprecated. User space should use the character device instead.

Example: Using GPIOs with the *libgpiod* library in user space to toggle a GPIO pin, which is connected to an LED on the SK-AM62B-P1 board:

#. Locate *Table 2-23* under **2.6.16.3 User Test LEDs** in the *AM62x Starter Kit User's Guide (Rev. C)*: https://www.ti.com/lit/pdf/spruj40.

   - This example uses LED "LD11", AKA the **IO_EXP_TEST_LED**. It is connected to GPIO *U70.24(P27)*, AKA pin 27 of the *GPIO Port Expander* on the SK-AM62B-P1 board:

   .. Image:: /images/sk-am62b-p1-top.png
      :width: 625

#. Detect every available **gpiochip**:

   .. code-block:: console

      $ gpiodetect
      gpiochip0 [600000.gpio] (92 lines)
      gpiochip1 [601000.gpio] (52 lines)
      gpiochip2 [1-0022] (24 lines)

   - This shows 92+52+24=168 total GPIO lines available across 3 GPIO chips: 0, 1, and 2.

#. Read info for every available **gpiochip**:

   .. code-block:: console

      $ gpioinfo
      gpiochip0 - 92 lines:
               line   0:       unnamed                 input
               line   1:       unnamed                 input
               {...}
               line  91:       unnamed                 input
      gpiochip1 - 52 lines:
               line   0:       unnamed                 input
               line   1:       unnamed                 input
               {...}
               line  51:       unnamed                 input
      gpiochip2 - 24 lines:
               line   0:       "GPIO_CPSW2_RST"        input
               line   1:       "GPIO_CPSW1_RST"        input
               {...}
               line  23:       "IO_EXP_TEST_LED"       input

   - This should result in a large output, 168+ lines in this case. It outputs all GPIO lines available on every GPIO chip, as well as their names and input/output directions. The above output is truncated.

   - For more info on *gpioinfo*, see its man page: https://libgpiod.readthedocs.io/en/latest/gpioinfo.html.

   - To see info for a specific GPIO chip, use the '-c' flag and the GPIO chip number.

#. Read info for **gpiochip2** (for this example):

   .. code-block:: console

      $ gpioinfo -c 2
      gpiochip2 - 24 lines:
               line   0:       "GPIO_CPSW2_RST"        input
               line   1:       "GPIO_CPSW1_RST"        input
               line   2:       "PRU_DETECT"            input
               line   3:       "MMC1_SD_EN"            output consumer="regulator-3"
               line   4:       "VPP_LDO_EN"            input
               line   5:       "EXP_PS_3V3_En"         input
               line   6:       "EXP_PS_5V0_En"         input
               line   7:       "EXP_HAT_DETECT"        input
               line   8:       "GPIO_AUD_RSTn"         input
               line   9:       "GPIO_eMMC_RSTn"        input
               line  10:       "UART1_FET_BUF_EN"      input
               line  11:       "WL_LT_EN"              input
               line  12:       "GPIO_HDMI_RSTn"        input
               line  13:       "CSI_GPIO1"             input
               line  14:       "CSI_GPIO2"             input
               line  15:       "PRU_3V3_EN"            input
               line  16:       "HDMI_INTn"             input consumer="interrupt"
               line  17:       "PD_I2C_IRQ"            input
               line  18:       "MCASP1_FET_EN"         input
               line  19:       "MCASP1_BUF_BT_EN"      input
               line  20:       "MCASP1_FET_SEL"        input
               line  21:       "UART1_FET_SEL"         input
               line  22:       "TSINT#"                input
               line  23:       "IO_EXP_TEST_LED"       output

   - We see that **IO_EXP_TEST_LED** is connected to *GPIO2_23* on the SK-AM62B-P1 board.

#. Read the value of the GPIO pin:

   .. code-block:: console

      $ gpioget --numeric -c 2 23
      0

   - Use variations of *gpioget* to read the value of the GPIO pin:

      .. code-block:: console

         $ gpioget -c 2 23
         "23"=inactive
         $ gpioget IO_EXP_TEST_LED
         "IO_EXP_TEST_LED"=inactive
         $ gpioget --numeric IO_EXP_TEST_LED
         0

   - For more info on *gpioget*, see its man page: https://libgpiod.readthedocs.io/en/latest/gpioget.html.

#. Set the GPIO pin to turn on the LED

   .. code-block:: console

      $ gpioset -c 2 23=1
      ^C
      $ gpioset -c 2 23=0
      ^C

   - Note:

      - In Bash, *'^C' (Ctrl + C)* exits the command with *SIGINT*, else the *gpioset* command would not exit on its own. For more info, refer to the *3.7.6 Signals* section in the GNU Bash manual: https://www.gnu.org/software/bash/manual/bash.html.

      - The new GPIO value will remain until an exit signal, like *SIGKILL*, *SIGTERM*, or *SIGINT*; after that, its value is not guaranteed. For more info, reference the *Description* section of the *gpioset* man page: https://libgpiod.readthedocs.io/en/latest/gpioset.html.

   - This should have turned the active-high LED "LD11" on the SK-AM62B-P1 on and off.

   - Use variations of *gpioset* to set the value of the GPIO pin:

      .. code-block:: console

         $ gpioset IO_EXP_TEST_LED=1
         ^C
         $ gpioset IO_EXP_TEST_LED=0
         ^C

   - This should have also turned the active-high LED "LD11" on the SK-AM62B-P1 on and off.

   - Example: Toggle *GPIO2_23* (blink "LD11") at 10Hz, then turn it off:

      .. code-block:: console

         $ gpioset --toggle 50ms IO_EXP_TEST_LED=1
         ^C
         $ gpioset IO_EXP_TEST_LED=0
         ^C

   - For more info on *gpioset*, see its man page: https://libgpiod.readthedocs.io/en/latest/gpioset.html.

- For more command-line tools, refer to the *libgpiod* documentation: https://libgpiod.readthedocs.io/en/latest/gpio_tools.html.

Example: Using GPIOs on the Raspberry Pi Compatible 40-pin Header on the SK-AM62B-P1 board:

.. Image:: /images/sk-am62b-p1-top-2.png
   :width: 625

#. Locate *Table 2-25* under **2.6.17.2 User Expansion Connector** in the *AM62x Starter Kit User's Guide (Rev. C)*: https://www.ti.com/lit/pdf/spruj40.

#. Identify the desired GPIO pin number and pin multiplexed signal. For example, *GPIO1_25* corresponds to physical pin 8 on the 40-pin header.

#. Use *libgpiod* mentioned in the previous example to control the GPIO pin, ensuring that the GPIO pin is not being used already.

Additional Resources

- For more information about GPIO usage in Linux and U-Boot, refer to these resources:

   - SDK:

      - Kernel: ti-processor-sdk-linux-am62xx-evm-<sdk version>/board-support/ti-linux-kernel-<kernel version>+git-ti/Documentation/devicetree/bindings/gpio/gpio.txt
      - U-Boot: ti-processor-sdk-linux-am62xx-evm-<sdk version>/board-support/ti-u-boot-<u-boot version>+git/doc/device-tree-bindings/gpio/gpio.txt

   - Online:

      - Linux:  https://e2e.ti.com/support/processors-group/processors/f/processors-forum/1494485/faq-processor-sdk-getting-started-with-gpios-in-linux-using-the-am62-and-am64-family-processors
      - U-Boot: https://e2e.ti.com/support/processors-group/processors/f/processors-forum/1398803/faq-processor-sdk-am62x-how-to-toggle-gpios-and-leds-from-u-boot-command-prompt
      - GPIO on Sitara: https://www.ti.com/lit/ab/spradk0/spradk0.pdf
      - https://e2e.ti.com/support/processors-group/processors/f/processors-forum/1398198/faq-am62x-how-to-allocate-use-gpios-from-different-device-domains
      - https://support.criticallink.com/redmine/projects/mitysom_am62x/wiki/Example\_-_User_level_GPIO_Access
      - https://software-dl.ti.com/processor-sdk-linux/esd/AM64X/latest/exports/docs/linux/How_to_Guides/FAQ/How_to_Check_Device_Tree_Info.html
      - https://docs.kernel.org/devicetree/usage-model.html
      - (*Note: AM62P-specific, but similar to AM62x*): https://software-dl.ti.com/processor-sdk-linux/esd/AM62PX/latest/exports/docs/linux/Foundational_Components/Tools/GPIO_Tools.html

.. rubric:: Consuming Drivers
   :name: consuming-drivers

The GPIO Driver can also be easily leveraged by other drivers to "consume" a GPIO.

- For an example of a driver using a GPIO pin, examine this entry in a dts file for how the MMC/SD interface could use a GPIO as a card detect pin:

   - ti-processor-sdk-linux-am62xx-evm-<sdk version>/board-support/ti-linux-kernel-<kernel version>+git-ti/arch/arm/boot/dts/ti/omap/am335x-bone-common.dtsi.

|

.. rubric:: Features
   :name: features

-  Access GPIO from user space as input or output
-  Leverage GPIO from another "consumer" driver

|

.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family')

    .. rubric:: Power Management

    | GPIO pins to be used to wake the system from low-power sleep states
      must be configured as a wake source in the device tree. Verify
      low-power wake capability in the device Technical Reference Manual.
      Some devices map specific wake capabilities to each GPIO bank.

    | To configure a GPIO pin as a wake up source, setup a gpio-key instance
      in the device tree. This will associate a GPIO pin with wake up
      capability and an interrupt.

    | For example, look at the ``gpio_keys: volume_keys@0`` node in the
      device tree ``LINUX/arch/arm/boot/dts/am335x-evm.dts`` as a reference.
      GPIO0\_31 is configured as a wake source below:

    `` @am33xx_pinmux { ``

    ::

         pinctrl-names = "default";
         pinctrl-0 = <&test_keys>;
         ...
         test_keys: test_keys {
           0x74 (PIN_INPUT_PULLDOWN | MUX_MODE7);  /* gpmc_wpn.gpio0_31 */
         };
         ...
         keys: test_keys@0 {
           compatible = "gpio-keys";
           #address-cells = <1>;
           #size-cells = <0>;
           autorepeat;
           test@0 {
             label = "J4-pin21";
             linux,code = <155>;
             gpios = <&gpio0 31 GPIO_ACTIVE_LOW>;
             gpio-key,wakeup;
           };
          };
         ...

    };

    |
