

This note explains how to develop an example using a General-Purpose Input/Output (GPIO) pin to capture an external input event and generate an interrupt by modifying an existing RTOS GPIO driver LED blinking example. The hardware setup, software development procedures and testing are done using TI AM572x IDK EVM. The same process can be extended to other TI Sitara devices, TI EVMs or custom platforms as well.

Hardware
---------
`The AM572x Industrial Development
Kit (IDK) <http://www.ti.com/tool/TMDXIDK5728>`__ is used here for developing the example. The same expect to work with the `AM574x
IDK <http://www.ti.com/tool/TMDSIDK574>`__ as well.

From the `AM572x IDK EVM hardware
user guide <http://www.ti.com/lit/ug/sprui64c/sprui64c.pdf>`__, the card has 3 push buttons: SW1, SW2 and SW3, but they all are used for different purposes. However, the card has a 60-pin female expansion connector J21, pins that are not used may be dedicated for GPIO input test purpose. Here J21 pin 4 is selected based on the following analysis:

•	The Pin 4 signal is labeled as GPMC_CS0 and is connected to AM572x chip ball T1 as shown in the schematic:

.. Image:: /images/J21_gpio_input.png
.. Image:: /images/gpmc_cs0_t1.png

•	From the AM5728 datasheet, T1 ball can be configured as GPMC_CS0 or GPIO2_19 based on different PINMUX modes.

Software
---------
The GPIO LED blink example is served as the reference example and the test is developed on the ARM A15 core, it should work for other cores. This section discusses several typical steps involved in the software development work:

•	PinMux configuration
•	PRCM setup
•	Re-build board library
•	Application software development

**PinMux configuration**

The default PinMux file has to be modified for GPIO2_19 pin usage:

•	Use the PinMux Utility to open the default PinMux file pdk_am57xx_1_0_x\\packages\\ti\\board\\src\\idkAM572x\\idkAM572x_SR2.0.pinmux (for the latest Rev 1.3B EVM)
•	Select GPIO, then MyGPIO2:

.. Image:: /images/pinmux_gpio_1.png

•	Then, scroll down, set gpio2_19 with ball #T1, pull up and Rx direction.
•	Finally, select Category filter as “SR2.0 – Platform Development Kit (PDK) and download the generated files.

.. Image:: /images/pinmux_gpio_2.png

•	Four new files should be generated, with the only difference  being a new pin configuration added in boardPadDelayInit.c file:

.. code-block:: c

      /* GPIO2 - gpio2_19 on T1 - MyGPIO2 */
     {0x14B4, 0x6000E, {0x0, 0, 0}, {0x0, 0, 0}, {0x0, 0, 0}},

•	Replace the same files under pdk_am57xx_1_0_x\\packages\\ti\\board\\src\\idkAM572x with the new ones.

**PRCM setup**

Setup of the Power, Reset and Clock Management (PRCM) domain for newly added GPIO2 is required. The application code calls Board_init() API with a BOARD_INIT_MODULE_CLOCK flag to enable the clock domain. It is implemented in the Board_moduleClockInit() function inside pdk_am57xx_1_0_x\\packages\\ti\\board\\source\\idkAM572x\\idkAM572x_clock.c. It is found that GPIO2 is enabled already and no further code needed.

**Re-build board library**

The board library must be recompiled for the changes to take effect. This has several major steps:

•	Setup the build environment by running setupenv script
•	Build the library with make command (e.g. “make board”) and the output will be under pdk_am57xx_1_0_x\\packages\\ti\\board\\lib\\idkAM572x\\a15\\release

Application software development
-----------------------------------
The GPIO LED blinking example (GPIO_LedBlink_idkAM572x_armTestProject) is used as the reference. The CCS project can be created by using pdkprojectcreate script, such as “pdkprojectcreate AM572x idkAM572x little gpio all arm”. Check `PDK Example and Test Project Creation <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index_overview.html#rebuilding-components>`_ for details.

This LED blink example uses 2 GPIO pins. The first pin is used to periodically generate an interrupt. The second pin is an output pin connected to an onboard LED, which toggles between low and high inside the interrupt ISR, thus driving the LED. Note the first pin doesn’t accept any external input, but using software to write a register (GPIO_IRQSTATUS_RAW_n) to generate interrupt.

Also note from GPIO_idkAM572x_board.c, the rising edge is configured to generate interrupt:

.. code-block:: c

  GPIO_PinConfig gpioPinConfigs_1p3[] = {
    /* Input pin with interrupt enabled */
    GPIO_DEVICE_CONFIG(GPIO_GRN_LED_PORT_NUM_1P3, GPIO_GRN_LED_PIN_NUM_1P3) |
    GPIO_CFG_IN_INT_RISING | GPIO_CFG_INPUT,
   }

After understanding how the reference example works, the code can be modified to use the first pin to receive external input and trigger the interrupt, then the second pin works the same way to toggle the LED, visualizing the event input.

Code modifications:
•	GPIO_board.h: this file defines the GPIO pins for the test, the first pin needs to be updated

.. code-block:: c

  #define GPIO_INTR_LED_BASE_ADDR_1P3      (CSL_MPU_GPIO2_REGS)
  #define GPIO_LED_PIN_NUM_1P3             (0x13U)

•	GPIO_idkAM572x_board.c: this file also defines the GPIO pins for the test, the first pin needs to be updated

.. code-block:: c

  /* GPIO Definitions specific Rev1p3 Board */
  /* GPIO pin number connected to the green LED */
  #define GPIO_GRN_LED_PIN_NUM_1P3    (0x13)

  /* GPIO port number connected to the green LED */
  #define GPIO_GRN_LED_PORT_NUM_1P3   (0x02)

•	main_led_blink.c: this is the main test program. The change is high-lighted in black, while the original code is in grey.

1) Inside void gpio_test(UArg arg0, UArg arg1) routine there is a while(1) loop that continuously triggers the interrupt by software write. Since the new example relies on the external input event to trigger it, one can simply add another while(1) in front of it to block the original loop:

.. code-block:: c

    while(1);  //New added loop
    while(1)
	{
		if defined(SOC_AM574x) || defined(SOC_AM572x) || defined(SOC_AM571x)|| defined(SOC_AM335x) || defined(SOC_AM437x)
		#if defined (idkAM572x) || defined (idkAM574x)
                  ….
    }

2) Also inside the same void gpio_test(UArg arg0, UArg arg1) routine, one may add a debounce control before the test loop:

.. code-block:: c

    /* Write high to gpio pin to control LED1 */
    GPIO_write((USER_LED1), GPIO_PIN_VAL_HIGH);

    /* Add new debounce code here */
    GPIOAppUpdateConfig(&gpioBaseAddr, &gpioPin);
    GPIODebounceFuncControl(gpioBaseAddr, gpioPin, 1);
    GPIODebounceTimeConfig(gpioBaseAddr, 255);

    AppDelay(DELAY_VALUE);

    GPIO_log("\n GPIO Led Blink Application \n");

After all the code changes, rebuild the test application. A GPIO_LedBlink_idkAM572x_armTestProject.out should be generated.

Test
---------

**Test Setup**
The test setup using AM572x IDK EVM is depicted below:

.. Image:: /images/gpio_test.png

•	The EVM is powered with a +5V power supply
•	A micro USB cable is connected to the host PC for on-board XDS100v2 JTAG connection and UART console.
•	A wire is connected to J21 pin4 as the event input. Another wire is connected to J21 pin 60 as the digital ground. When the two wires touch each other, pin 4 goes low, creating a GPIO falling edge. On the other hand, when the two wires are not touching, pin 4 goes high, creating a GPIO rising edge.

**Test Procedure**

•	Connect to the A15_0 with a JTAG emulator and use the default GEL file to initialize the SOC.
•	Load the test application (GPIO_LedBlink_idkAM572x_armTestProject.out) and run.
•	Touch the two wires, then un-touch, the LED should flip the status and keep steady until next touch, un-touch cycle.

