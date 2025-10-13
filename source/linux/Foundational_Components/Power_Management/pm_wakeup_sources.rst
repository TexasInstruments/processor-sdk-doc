.. _pm_wakeup_sources:

##############
Wakeup Sources
##############

This section talks about the multiple ways in which we can wakeup the |__PART_FAMILY_DEVICE_NAMES__| SoC from various low power modes.
The |__PART_FAMILY_DEVICE_NAMES__| SoC support various wakeup sources like GP Timers, RTC Timer, UART, I2C, WKUP GPIO, and I/O Daisy Chain.

The table below lists the wakeup sources supported in this SDK release and whether that source is
valid for given low power modes:

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   +------------------------------------------------+------------+----------+-------------+
   |  Wakeup Source                                 | Deep Sleep | MCU Only | Partial I/O |
   +================================================+============+==========+=============+
   | Real-Time Clock (RTC)                          | Yes        | Yes      | No          |
   +------------------------------------------------+------------+----------+-------------+
   | MCU (WKUP) GPIO                                | Yes        | Yes      | No          |
   +------------------------------------------------+------------+----------+-------------+
   | Main I/O Daisy Chain (Main GPIO and Main UART) | Yes        | Yes      | No          |
   +------------------------------------------------+------------+----------+-------------+
   | USB Wakeup                                     | Yes        | Yes      | No          |
   +------------------------------------------------+------------+----------+-------------+
   | WKUP UART                                      | Yes        | Yes      | No          |
   +------------------------------------------------+------------+----------+-------------+
   | MCU IPC (for MCU Only mode)                    | No         | Yes      | No          |
   +------------------------------------------------+------------+----------+-------------+
   | CAN UART I/O Daisy Chain                       | Yes        | Yes      | Yes         |
   +------------------------------------------------+------------+----------+-------------+

.. ifconfig:: CONFIG_part_variant in ('AM62AX', 'AM62PX')

   +------------------------------------------------+-------+------+---------+----------+
   |  Wakeup Source                                 | Deep  | MCU  | Partial | I/O Only |
   |                                                | Sleep | Only | I/O     | Plus DDR |
   +================================================+=======+======+=========+==========+
   | Real-Time Clock (RTC)                          | Yes   | Yes  | No      | No       |
   +------------------------------------------------+-------+------+---------+----------+
   | MCU (WKUP) GPIO                                | Yes   | Yes  | No      | No       |
   +------------------------------------------------+-------+------+---------+----------+
   | Main I/O Daisy Chain (Main GPIO and Main UART) | Yes   | Yes  | No      | No       |
   +------------------------------------------------+-------+------+---------+----------+
   | USB Wakeup                                     | Yes   | Yes  | No      | No       |
   +------------------------------------------------+-------+------+---------+----------+
   | WKUP UART                                      | Yes   | Yes  | No      | No       |
   +------------------------------------------------+-------+------+---------+----------+
   | MCU IPC (for MCU Only mode)                    | No    | Yes  | No      | No       |
   +------------------------------------------------+-------+------+---------+----------+
   | CAN UART I/O Daisy Chain                       | Yes   | Yes  | Yes     | Yes      |
   +------------------------------------------------+-------+------+---------+----------+

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   +----------------------------------+------------+----------------+
   |  Wakeup Source                   | Deep Sleep | RTC Only + DDR |
   +==================================+============+================+
   | Real-Time Clock (RTC)            | Yes        | Yes            |
   +----------------------------------+------------+----------------+
   | Main I/O Daisy Chain (Main UART) | Yes        | No             |
   +----------------------------------+------------+----------------+
   | USB Wakeup                       | Yes        | No             |
   +----------------------------------+------------+----------------+
   | RTC Ext Pin                      | Yes        | Yes            |
   +----------------------------------+------------+----------------+

*********************
Real-Time Clock (RTC)
*********************

It's possible to use the SoC's internal RTC to wakeup the system using the command rtcwake:

.. code-block:: console

   rtcwake

   - Show whether an alarm is set or not:
      rtcwake -m show -v

   - Suspend to RAM and wakeup after 10 seconds:
      rtcwake -m mem -s {{10}}

   - Disable a previously set alarm:
      rtcwake -m disable

   - Perform a dry run to wakeup the computer at a given time. (Press Ctrl + C to abort):
      rtcwake -m on --date {{hh:ss}}

For example, to wakeup from Deep Sleep in 10 seconds, use the command like this:

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   .. note::

      An additional :code:`-d rtc1` option is required on BeaglePlay as the SoC's
      internal RTC gets probed as rtc1

   .. code-block:: console

      root@am62xx-evm:~# rtcwake -s 10 -m mem
      rtcwake: wakeup from "mem" using /dev/rtc0 at Thu Jan 1 00:00:45 1970
      [ 28.038332] PM: suspend entry (deep)
      [ 28.042057] Filesystems sync: 0.000 seconds
      [ 28.050312] Freezing user space processes
      [ 28.052137] Freezing user space processes completed (elapsed 0.001 seconds)
      [ 28.052162] OOM killer disabled.
      [ 28.052166] Freezing remaining freezable tasks
      [ 28.053557] Freezing remaining freezable tasks completed (elapsed 0.001 seconds)
      [ 28.053571] printk: Suspending console(s) (use no_console_suspend to debug)
      [ 28.138190] ti-sci 44043000.system-controller: ti_sci_cmd_set_device_constraint: device: 179: state: 1: ret 0
      [ 28.148680] ti-sci 44043000.system-controller: ti_sci_cmd_set_device_constraint: device: 178: state: 1: ret 0
      [ 29.911265] omap8250 2800000.serial: PM domain pd:146 will not be powered off
      [ 29.923288] ti-sci 44043000.system-controller: ti_sci_cmd_set_device_constraint: device: 117: state: 1: ret 0
      [ 30.789584] remoteproc remoteproc0: stopped remote processor 5000000.m4fss
      [ 30.981215] Disabling non-boot CPUs ...
      [ 30.983394] psci: CPU1 killed (polled 0 ms)
      [ 30.986714] psci: CPU2 killed (polled 0 ms)
      [ 30.990028] psci: CPU3 killed (polled 0 ms)
      [ 30.991437] Enabling non-boot CPUs ...
      [ 31.011850] Detected VIPT I-cache on CPU1
      [ 31.011909] GICv3: CPU1: found redistributor 1 region 0:0x00000000018a0000
      [ 31.011972] CPU1: Booted secondary processor 0x0000000001 [0x410fd034]
      [ 31.013028] CPU1 is up
      [ 31.033291] Detected VIPT I-cache on CPU2
      [ 31.033322] GICv3: CPU2: found redistributor 2 region 0:0x00000000018c0000
      [ 31.033365] CPU2: Booted secondary processor 0x0000000002 [0x410fd034]
      [ 31.034221] CPU2 is up
      [ 31.054487] Detected VIPT I-cache on CPU3
      [ 31.054524] GICv3: CPU3: found redistributor 3 region 0:0x00000000018e0000
      [ 31.054573] CPU3: Booted secondary processor 0x0000000003 [0x410fd034]
      [ 31.055431] CPU3 is up
      [ 31.058242] ti-sci 44043000.system-controller: ti_sci_resume: wakeup source: 0x50
      [ 33.771971] am65-cpsw-nuss 8000000.ethernet: set new flow-id-base 19
      [ 34.177716] am65-cpsw-nuss 8000000.ethernet eth0: PHY [8000f00.mdio:00] driver [TI DP83867] (irq=POLL)
      [ 34.177741] am65-cpsw-nuss 8000000.ethernet eth0: configuring for phy/rgmii-rxid link mode
      [ 34.184415] am65-cpsw-nuss 8000000.ethernet eth1: PHY [8000f00.mdio:01] driver [TI DP83867] (irq=POLL)
      [ 34.184425] am65-cpsw-nuss 8000000.ethernet eth1: configuring for phy/rgmii-rxid link mode
      [ 34.400791] OOM killer enabled.
      [ 34.403934] Restarting tasks ... done.
      [ 34.408982] random: crng reseeded on system resumption
      [ 34.555214] k3-m4-rproc 5000000.m4fss: Core is off in resume
      [ 34.560924] remoteproc remoteproc0: powering up 5000000.m4fss
      [ 34.566695] remoteproc remoteproc0: Booting fw image am62-mcu-m4f0_0-fw, size 55016
      [ 34.595350] rproc-virtio rproc-virtio.2.auto: assigned reserved memory node m4f-dma-memory@9cb00000
      [ 34.605831] virtio_rpmsg_bus virtio1: rpmsg host is online
      [ 34.611540] rproc-virtio rproc-virtio.2.auto: registered virtio1 (type 7)
      [ 34.618396] remoteproc remoteproc0: remote processor 5000000.m4fss is now up
      [ 34.619659] virtio_rpmsg_bus virtio1: creating channel ti.ipc4.ping-pong addr 0xd
      [ 34.633257] virtio_rpmsg_bus virtio1: creating channel rpmsg_chrdev addr 0xe
      [ 34.645777] PM: suspend exit
      root@am62xx-evm:~#

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

   .. code-block:: console

      root@am62axx-evm:~# rtcwake -s 10 -m mem
      rtcwake: wakeup from "mem" using rtc1 at Thu Jan  1 00:01:31 1970
      [   68.915144] PM: suspend entry (deep)
      [   68.918851] Filesystems sync: 0.000 seconds
      [   68.926581] Freezing user space processes
      [   68.932192] Freezing user space processes completed (elapsed 0.001 seconds)
      [   68.939174] OOM killer disabled.
      [   68.942402] Freezing remaining freezable tasks
      [   68.948218] Freezing remaining freezable tasks completed (elapsed 0.001 seconds)
      [   68.955615] printk: Suspending console(s) (use no_console_suspend to debug)
      [   68.967023] ti-sci 44043000.system-controller: ti_sci_cmd_set_device_constraint: device: 179: state: 1: ret 0
      [   68.967177] ti-sci 44043000.system-controller: ti_sci_cmd_set_device_constraint: device: 178: state: 1: ret 0
      [   68.975296] ti-sci 44043000.system-controller: ti_sci_cmd_set_device_constraint: device: 117: state: 1: ret 0
      [   68.982165] remoteproc remoteproc0: stopped remote processor 7e000000.dsp
      [   68.007805] remoteproc remoteproc1: stopped remote processor 79000000.r5f
      [   68.010972] Disabling non-boot CPUs ...
      [   68.013268] psci: CPU1 killed (polled 0 ms)
      [   68.016262] psci: CPU2 killed (polled 4 ms)
      [   68.019303] psci: CPU3 killed (polled 4 ms)
      [   68.020139] Enabling non-boot CPUs ...
      [   68.020472] Detected VIPT I-cache on CPU1
      [   68.020515] GICv3: CPU1: found redistributor 1 region 0:0x00000000018a0000
      [   68.020568] CPU1: Booted secondary processor 0x0000000001 [0x410fd034]
      [   68.021670] CPU1 is up
      [   68.021915] Detected VIPT I-cache on CPU2
      [   68.021943] GICv3: CPU2: found redistributor 2 region 0:0x00000000018c0000
      [   68.021982] CPU2: Booted secondary processor 0x0000000002 [0x410fd034]
      [   68.022911] CPU2 is up
      [   68.023158] Detected VIPT I-cache on CPU3
      [   68.023188] GICv3: CPU3: found redistributor 3 region 0:0x00000000018e0000
      [   68.023233] CPU3: Booted secondary processor 0x0000000003 [0x410fd034]
      [   68.024279] CPU3 is up
      [   68.024692] ti-sci 44043000.system-controller: ti_sci_resume: wakeup source: 0x50
      [   68.037668] am65-cpsw-nuss 8000000.ethernet: set new flow-id-base 19
      [   68.053755] am65-cpsw-nuss 8000000.ethernet eth0: PHY [8000f00.mdio:00] driver [TI DP83867] (irq=POLL)
      [   68.053779] am65-cpsw-nuss 8000000.ethernet eth0: configuring for phy/rgmii-rxid link mode
      [   68.214438] OOM killer enabled.
      [   68.217581] Restarting tasks ... done.
      [   68.222831] random: crng reseeded on system resumption
      [   68.228121] k3-dsp-rproc 7e000000.dsp: Core is off in resume
      [   68.233990] remoteproc remoteproc0: powering up 7e000000.dsp
      [   68.239783] remoteproc remoteproc0: Booting fw image am62a-c71_0-fw, size 8391984
      [   68.254785] k3-dsp-rproc 7e000000.dsp: booting DSP core using boot addr = 0x9a000000
      [   68.262806] rproc-virtio rproc-virtio.7.auto: assigned reserved memory node c7x-dma-memory@99800000
      [   68.273026] virtio_rpmsg_bus virtio0: rpmsg host is online
      [   68.274647] virtio_rpmsg_bus virtio0: creating channel ti.ipc4.ping-pong addr 0xd
      [   68.278683] rproc-virtio rproc-virtio.7.auto: registered virtio0 (type 7)
      [   68.286349] virtio_rpmsg_bus virtio0: creating channel rpmsg_chrdev addr 0xe
      [   68.292879] remoteproc remoteproc0: remote processor 7e000000.dsp is now up
      [   68.307022] platform 79000000.r5f: Core is off in resume
      [   68.312378] remoteproc remoteproc1: powering up 79000000.r5f
      [   68.318064] remoteproc remoteproc1: Booting fw image am62a-mcu-r5f0_0-fw, size 53172
      [   68.326761] rproc-virtio rproc-virtio.8.auto: assigned reserved memory node r5f-dma-memory@9b800000
      [   68.336811] virtio_rpmsg_bus virtio1: rpmsg host is online
      [   68.337372] virtio_rpmsg_bus virtio1: creating channel ti.ipc4.ping-pong addr 0xd
      [   68.342463] rproc-virtio rproc-virtio.8.auto: registered virtio1 (type 7)
      [   68.350242] virtio_rpmsg_bus virtio1: creating channel rpmsg_chrdev addr 0xe
      [   68.356706] remoteproc remoteproc1: remote processor 79000000.r5f is now up
      [   68.370906] PM: suspend exit

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   .. code-block:: console

      root@am62pxx-evm:~# rtcwake -s 10 -m mem
      rtcwake: wakeup from "mem" using /dev/rtc0 at Thu Jan  1 00:01:06 1970
      [   34.312057] PM: suspend entry (deep)
      [   34.315781] Filesystems sync: 0.000 seconds
      [   34.333057] Freezing user space processes
      [   34.338700] Freezing user space processes completed (elapsed 0.001 seconds)
      [   34.345697] OOM killer disabled.
      [   34.348924] Freezing remaining freezable tasks
      [   34.354679] Freezing remaining freezable tasks completed (elapsed 0.001 seconds)
      [   34.362078] printk: Suspending console(s) (use no_console_suspend to debug)
      [   34.377118] ti-sci 44043000.system-controller: ti_sci_cmd_set_device_constraint: device: 179: state: 1: ret 0
      [   34.377267] ti-sci 44043000.system-controller: ti_sci_cmd_set_device_constraint: device: 178: state: 1: ret 0
      [   34.378162] am65-cpsw-nuss 8000000.ethernet eth0: Link is Down
      [   34.387141] omap8250 2800000.serial: PM domain pd:146 will not be powered off
      [   34.387736] ti-sci 44043000.system-controller: ti_sci_cmd_set_device_constraint: device: 117: state: 1: ret 0
      [   34.416958] remoteproc remoteproc0: stopped remote processor 79000000.r5f
      [   34.420565] Disabling non-boot CPUs ...
      [   34.422781] psci: CPU1 killed (polled 0 ms)
      [   34.426363] psci: CPU2 killed (polled 0 ms)
      [   34.429526] psci: CPU3 killed (polled 0 ms)
      [   34.430459] Enabling non-boot CPUs ...
      [   34.430798] Detected VIPT I-cache on CPU1
      [   34.430841] GICv3: CPU1: found redistributor 1 region 0:0x00000000018a0000
      [   34.430895] CPU1: Booted secondary processor 0x0000000001 [0x410fd034]
      [   34.431987] CPU1 is up
      [   34.432232] Detected VIPT I-cache on CPU2
      [   34.432262] GICv3: CPU2: found redistributor 2 region 0:0x00000000018c0000
      [   34.432306] CPU2: Booted secondary processor 0x0000000002 [0x410fd034]
      [   34.433233] CPU2 is up
      [   34.433485] Detected VIPT I-cache on CPU3
      [   34.433515] GICv3: CPU3: found redistributor 3 region 0:0x00000000018e0000
      [   34.433557] CPU3: Booted secondary processor 0x0000000003 [0x410fd034]
      [   34.434504] CPU3 is up
      [   34.434948] ti-sci 44043000.system-controller: ti_sci_resume: wakeup source: 0x50
      [   34.447824] am65-cpsw-nuss 8000000.ethernet: set new flow-id-base 19
      [   34.463954] am65-cpsw-nuss 8000000.ethernet eth0: PHY [8000f00.mdio:00] driver [TI DP83867] (irq=POLL)
      [   34.463980] am65-cpsw-nuss 8000000.ethernet eth0: configuring for phy/rgmii-rxid link mode
      [   34.477401] am65-cpsw-nuss 8000000.ethernet eth1: PHY [8000f00.mdio:01] driver [TI DP83867] (irq=POLL)
      [   34.477414] am65-cpsw-nuss 8000000.ethernet eth1: configuring for phy/rgmii-rxid link mode
      [   34.661705] OOM killer enabled.
      [   34.664848] Restarting tasks ... done.
      [   34.670624] random: crng reseeded on system resumption
      [   34.676468] platform 79000000.r5f: Core is off in resume
      [   34.681906] remoteproc remoteproc0: powering up 79000000.r5f
      [   34.687692] remoteproc remoteproc0: Booting fw image am62p-mcu-r5f0_0-fw, size 58344
      [   34.699283] rproc-virtio rproc-virtio.5.auto: assigned reserved memory node mcu-r5fss-dma-memory-region@9b800000
      [   34.710642] virtio_rpmsg_bus virtio0: rpmsg host is online
      [   34.716279] virtio_rpmsg_bus virtio0: creating channel ti.ipc4.ping-pong addr 0xd
      [   34.717435] rproc-virtio rproc-virtio.5.auto: registered virtio0 (type 7)
      [   34.724381] virtio_rpmsg_bus virtio0: creating channel rpmsg_chrdev addr 0xe
      [   34.731147] remoteproc remoteproc0: remote processor 79000000.r5f is now up
      [   34.754176] PM: suspend exit

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   .. code-block:: console

      root@am62lxx-evm:~# rtcwake -m mem -s 10
      rtcwake: assuming RTC uses UTC ...
      rtcwake: wakeup from "mem" using /dev/rtc0 at Thu Jan  1 00:00:46 1970
      [   28.138624] PM: suspend entry (deep)
      [   28.142400] Filesystems sync: 0.000 seconds
      [   28.159141] Freezing user space processes
      [   28.169800] Freezing user space processes completed (elapsed 0.002 seconds)
      [   28.176909] OOM killer disabled.
      [   28.180168] Freezing remaining freezable tasks
      [   28.186015] Freezing remaining freezable tasks completed (elapsed 0.001 seconds)
      [   28.193484] printk: Suspending console(s) (use no_console_suspend to debug)
      ERROR:   Wake up src 0x10000
      [   28.229712] Disabling non-boot CPUs ...
      [   28.232172] psci: CPU1 killed (polled 0 ms)
      [   28.233437] Enabling non-boot CPUs ...
      [   28.233757] Detected VIPT I-cache on CPU1
      [   28.233811] GICv3: CPU1: found redistributor 1 region 0:0x0000000001860000
      [   28.233875] CPU1: Booted secondary processor 0x0000000001 [0x410fd034]
      [   28.235241] CPU1 is up
      [   28.257825] am65-cpsw-nuss 8000000.ethernet: set new flow-id-base 96
      [   28.271845] am65-cpsw-nuss 8000000.ethernet eth0: PHY [8000f00.mdio:00] driver [TI DP83867] (irq=POLL)
      [   28.271880] am65-cpsw-nuss 8000000.ethernet eth0: configuring for phy/rgmii-rxid link mode
      [   28.285658] am65-cpsw-nuss 8000000.ethernet eth1: PHY [8000f00.mdio:01] driver [TI DP83867] (irq=POLL)
      [   28.285678] am65-cpsw-nuss 8000000.ethernet eth1: configuring for phy/rgmii-rxid link mode
      [   28.364033] OOM killer enabled.
      [   28.367181] Restarting tasks ... done.
      [   28.378392] random: crng reseeded on system resumption
      [   28.384269] PM: suspend exit

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX')

   .. note::

      The system will enter the mode selected by DM on the basis on existing constraints.

********
MCU GPIO
********

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   MCU GPIO wakeup is not supported on AM62LX.

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX')

   One of the most common ways to wakeup a system is by using some I/O activity.
   I/O activity on the MCU GPIOs can wakeup the system when the MCU GPIO
   controller is configured as a wakeup source. In ideal scenarios, the firmware
   running on MCU core is responsible for configuring MCU GPIOs as a wakeup
   source. However, if the application design doesn't rely on the MCU firmware
   then Linux can be used to configure the MCU GPIOs as a wakeup source. Refer
   to the mcu_gpio_key node in
   `k3-am62x-sk-lpm-wkup-sources.dtso <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62x-sk-lpm-wkup-sources.dtso?h=11.01.05>`__
   to use as a template to configure the desired MCU GPIO as a wakeup capable
   GPIO.

   A brief guide to configuring an MCU GPIO as wakeup:

   First, add gpio-keys as a compatible string, refer to
   `gpio_keys kernel documentation <https://www.kernel.org/doc/Documentation/devicetree/bindings/input/gpio-keys.txt>`__
   for details.

   .. code-block:: dts

      compatible = "gpio-keys";


   Set the desired pinctrl,

   .. code-block:: dts

      pinctrl-names = "default";
      pinctrl-0 = <&wake_mcugpio1_pins_default>;

   Setup the interrupt parent and interrupt as MCU_GPIO0,

   .. code-block:: dts

      interrupt-parent = <&mcu_gpio0>;
      interrupts = <4 IRQ_TYPE_EDGE_RISING>;

   Now, under the switch node, add the following:

   .. code-block:: dts

      switch {
                  label = "MCUGPIO";
                  linux,code = <143>;
                  gpios = <&mcu_gpio0 4 GPIO_ACTIVE_LOW>;
                  wakeup-source;
      };

   #. label: Descriptive name of the switch node. If the MCU GPIO node is setup
      correctly, the label will appear under /proc/interrupts:

       .. code-block:: console

           root@<machine>:~# cat /proc/interrupts | grep "MCUGPIO"
           273:          0          0          0          0      GPIO  4 Edge    -davinci_gpio  MCUGPIO

   #. linux,code: Keycode to emit.
   #. gpios: the gpio required to be used as the gpio-key.
   #. wakeup-source:
      `wakeup-source <https://www.kernel.org/doc/Documentation/devicetree/bindings/power/wakeup-source.txt>`__
      property describes devices which have wakeup capability.

   This indicates that gpio_keys can wake-up the system from Deep Sleep or MCU Only mode.

   The MCU GPIOs can be used to wakeup the system from Deep Sleep because MCU
   GPIOs are in a power domain that stays ON even when the SoC is in Deep Sleep.
   Hence, the GPIO controller is able to act as a wakeup source and send a
   wakeup interrupt to the Device Manager. To understand the role of Device
   Manager, refer to
   :ref:`S/W Architecture of System Suspend<pm_sw_arch>`

   MCU GPIO wakeup can only be tested when
   `k3-am62x-sk-lpm-wkup-sources.dtso <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62x-sk-lpm-wkup-sources.dtso?h=11.01.05>`__
   overlay is loaded. Refer to :ref:`How to enable DT overlays<howto_dt_overlays>` for more details.

   Once the system has entered Deep Sleep or MCU Only mode as shown in the
   :ref:`LPM section<lpm_modes>`, wakeup from MCU_SPI0_D1 can be triggered
   by grounding Pin 4 on J8 MCU Header.

********************
Main I/O Daisy Chain
********************

The main domain is powered-off when the SoC enters low power mode. This includes controllers like
Main UART, GPIO, I2C, etc. The question then arises how to wakeup the SoC from peripherals connected
to these controllers (for example main UART)? Here's where the role of I/O Daisy Chaining comes in.
At the hardware level, all the pads in an SoC have to be pinmuxed to dedicated controllers like UART or GPIO.

For example, if a key press on Main UART (which is used for Linux console logs)
were to wakeup the system from Deep Sleep then simply configuring the Main UART controller as a
wakeup source wouldn't suffice. This is because the UART controller is powered off and wouldn't be able to
register any key press as such. However, at the "pad" level we are still connected, and the pads have
a specific way to be configured as wakeup sources.

For detailed information and sequence please refer to
I/O Power Management and Daisy Chaining section in the TRM.

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX')

   .. note::

      |__PART_FAMILY_DEVICE_NAMES__| supports the ability to wakeup using pad based wake event ONLY in Deep Sleep or MCU Only Mode.
      During active system usage, even if the wake_enable bit is set the system will be unresponsive to any wakeup
      activity on that pad.

   To demonstrate I/O daisy chain wakeup as part of |__PART_FAMILY_DEVICE_NAMES__| offering, two reference examples are provided:

   #. main_uart0 is used where a key press on the Linux console can wakeup the system.
   #. main_gpio is used where activity on configured GPIO pin can wakeup the system.

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   .. note::

      |__PART_FAMILY_DEVICE_NAMES__| supports the ability to wakeup using pad based wake event ONLY in Deep Sleep.
      During active system usage, even if the wake_enable bit is set the system will be unresponsive to any wakeup
      activity on that pad.

   To demonstrate I/O daisy chain wakeup as part of |__PART_FAMILY_DEVICE_NAMES__| offering, a reference example is provided:

   #. main_uart0 is used where a key press on the Linux console can wakeup the system.


Main UART
=========

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   To configure UART as an I/O daisy chain wakeup, refer to the
   main_uart0 node in `k3-am62x-sk-common.dtsi <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62x-sk-common.dtsi?h=11.01.16>`_

   .. code-block:: dts

      &main_pmx0 {
         main_uart0_tx_pins_default: main-uart0-tx-default-pins {
            bootph-all;
            pinctrl-single,pins = <
               AM62X_IOPAD(0x1cc, PIN_OUTPUT, 0) /* (E14/E11) UART0_TXD */
            >;
         };

         main_uart0_rx_pins_default: main-uart0-rx-default-pins {
            bootph-all;
            pinctrl-single,pins = <
               AM62X_IOPAD(0x1c8, PIN_INPUT, 0) /* (D14/A13) UART0_RXD */
            >;
         };

         main_uart0_rx_pins_wakeup: main-uart0-rx-wakeup-pins {
            pinctrl-single,pins = <
               AM62X_IOPAD(0x1c8, PIN_INPUT | PIN_WKUP_EN, 0) /* (D14/A13) UART0_RXD */
            >;
         };
      };

      &main_uart0 {
         bootph-all;
         status = "okay";
         pinctrl-names = "default", "wakeup";
         pinctrl-0 = <&main_uart0_tx_pins_default>, <&main_uart0_rx_pins_default>;
         pinctrl-1 = <&main_uart0_tx_pins_default>, <&main_uart0_rx_pins_wakeup>;
         wakeup-source = <&system_deep_sleep>,
               <&system_mcu_only>,
               <&system_standby>;
      };

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

   To configure UART as an I/O daisy chain wakeup, refer to the
   main_uart0 node in `k3-am62a7-sk.dts <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62a7-sk.dts?h=11.01.16>`_

   .. code-block:: dts

      &main_pmx0 {
         main_uart0_tx_pins_default: main-uart0-tx-default-pins {
            pinctrl-single,pins = <
               AM62AX_IOPAD(0x1cc, PIN_OUTPUT, 0) /* (D15) UART0_TXD */
            >;
            bootph-all;
         };

         main_uart0_rx_pins_default: main-uart0-rx-default-pins {
            pinctrl-single,pins = <
               AM62AX_IOPAD(0x1c8, PIN_INPUT, 0) /* (E14) UART0_RXD */
            >;
            bootph-all;
         };

         main_uart0_rx_pins_wakeup: main-uart0-rx-wakeup-pins {
            pinctrl-single,pins = <
               AM62AX_IOPAD(0x1c8, PIN_INPUT | PIN_WKUP_EN, 0) /* (E14) UART0_RXD */
            >;
         };
      };

      &main_uart0 {
         status = "okay";
         pinctrl-names = "default", "wakeup";
         pinctrl-0 = <&main_uart0_tx_pins_default>, <&main_uart0_rx_pins_default>;
         pinctrl-1 = <&main_uart0_tx_pins_default>, <&main_uart0_rx_pins_wakeup>;
         wakeup-source = <&system_deep_sleep>,
               <&system_mcu_only>,
               <&system_standby>;
         bootph-all;
      };

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   To configure UART as an I/O daisy chain wakeup, refer to the
   main_uart0 node in `k3-am62p5-sk.dts <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62p5-sk.dts?h=11.01.16>`_

   .. code-block:: dts

      &main_pmx0 {
         main_uart0_tx_pins_default: main-uart0-tx-default-pins {
            pinctrl-single,pins = <
               AM62PX_IOPAD(0x1cc, PIN_OUTPUT, 0) /* (B22) UART0_TXD */
            >;
            bootph-all;
         };

         main_uart0_rx_pins_default: main-uart0-rx-default-pins {
            pinctrl-single,pins = <
               AM62PX_IOPAD(0x1c8, PIN_INPUT, 0) /* (A22) UART0_RXD */
            >;
            bootph-all;
         };

         main_uart0_rx_pins_wakeup: main-uart0-rx-wakeup-pins {
            pinctrl-single,pins = <
               AM62PX_IOPAD(0x1c8, PIN_INPUT | PIN_WKUP_EN, 0) /* (A22) UART0_RXD */
            >;
         };
      };

      &main_uart0 {
         pinctrl-names = "default", "wakeup";
         pinctrl-0 = <&main_uart0_tx_pins_default>, <&main_uart0_rx_pins_default>;
         pinctrl-1 = <&main_uart0_tx_pins_default>, <&main_uart0_rx_pins_wakeup>;
         wakeup-source = <&system_deep_sleep>,
               <&system_mcu_only>,
               <&system_standby>;
         status = "okay";
         bootph-all;
      };

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   To configure UART as an I/O daisy chain wakeup, refer to the
   main_uart0 node in `k3-am62l3-evm.dts <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62l3-evm.dts?h=11.01.16>`_

   .. code-block:: dts

      &main_pmx0 {
         main_uart0_tx_pins_default: main-uart0-tx-default-pins {
            pinctrl-single,pins = <
               AM62LX_IOPAD(0x01b8, PIN_OUTPUT, 0) /* (C13) UART0_TXD */
            >;
            bootph-all;
         };

         main_uart0_rx_pins_default: main-uart0-rx-default-pins {
            pinctrl-single,pins = <
               AM62LX_IOPAD(0x01b4, PIN_INPUT, 0) /* (D13) UART0_RXD */
            >;
            bootph-all;
         };

         main_uart0_rx_pins_wakeup: main-uart0-rx-wakeup-pins {
            pinctrl-single,pins = <
               AM62LX_IOPAD(0x01b4, PIN_INPUT | PIN_WKUP_EN, 0) /* (D13) UART0_RXD */
            >;
         };
      };

      &main_uart0 {
         pinctrl-names = "default", "wakeup";
         pinctrl-0 = <&main_uart0_tx_pins_default>, <&main_uart0_rx_pins_default>;
         pinctrl-1 = <&main_uart0_tx_pins_default>, <&main_uart0_rx_pins_wakeup>;
         wakeup-source = <&system_deep_sleep>;
         status = "okay";
         bootph-all;
      };

In the above code, a "wakeup" pinctrl state is defined for main_uart0. The
"wakeup" pinctrl state sets the  WKUP_EN flag on the desired padconfig register,
which allows the pad to act as a wakeup source. During suspend, the Linux
8250_omap serial driver switches from the "default" pinctrl state to the "wakeup"
pinctrl state.

This configures UART to act as a wakeup source, and a *key press* on same
terminal should trigger a wakeup from LPM.

Any UART can be chosen according to application requirements.


Main GPIO
=========

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   Main GPIO wakeup is not yet supported on AM62LX.

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX')

   Configuring Main GPIO as an I/O daisy chain wakeup source requires a
   combination of gpio-keys with chained IRQ in the pinctrl driver. To briefly
   explain, setting the 29th bit in the desired padconfig register, allows the
   pad to act as a wakeup source by triggering a wake IRQ to the DM R5 in Deep
   Sleep states.

   The reference configuration for Main GPIO wakeup can be found under
   gpio_key node in `k3-am62x-sk-lpm-wkup-sources.dtso <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62x-sk-lpm-wkup-sources.dtso?h=11.01.05#n21>`__

   .. code-block:: console

      gpio_key {
	      compatible = "gpio-keys";
	      autorepeat;
	      pinctrl-names = "default";
	      pinctrl-0 = <&main_gpio1_pins_default>;
	      switch {
		      label = "WKGPIO";
		      linux,code = <KEY_WAKEUP>;
		      interrupts-extended = <&main_gpio1 10 IRQ_TYPE_EDGE_RISING>,
		   	   <&main_pmx0 0x1a0>;
		      interrupt-names = "irq", "wakeup";
	      };
      };

   Here, we chain the IRQ to the pinctrl driver using the second
   interrupts-extended entry. The wake IRQ framework in Linux works in such a
   way that the second entry gets marked as a wakeup source, and then the
   pinctrl driver is informed that the pad 0x1a0 in this case is to be
   configured as a wakeup pad when system enters Deep Sleep.

   Main GPIO wakeup can only be tested when
   `k3-am62x-sk-lpm-wkup-sources.dtso <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62x-sk-lpm-wkup-sources.dtso?h=11.01.05>`__
   overlay is loaded. Please refer to :ref:`How to enable DT overlays<howto_dt_overlays>` for more details.

   To use main_gpio as a wakeup source, ensure gpio is a wake-irq in /proc/interrupts:

   .. code-block:: console

      root@<machine>:~# grep wakeup /proc/interrupts
      531:          0          0          0          0   pinctrl 416 Edge      WKGPIO:wakeup

   Once the system has entered Deep Sleep or MCU Only mode as shown in the
   :ref:`LPM section<lpm_modes>`, wakeup from MAIN GPIO1_10 can be triggered
   by grounding Pin 33 on J3 User Expansion Connector.

*********
WKUP UART
*********

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   WKUP UART wakeup is not yet supported on AM62LX.

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX')

   The UART in WKUP domain is capable of waking up the system from Deep
   Sleep and MCU Only modes.

   In order to use WKUP UART as a wakeup source, it needs to be configured
   in a generic way using the ti-sysc interconnect target module driver.
   The reference configuration can be found under target-module in
   `k3-am62-wakeup.dtsi <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62-wakeup.dtsi?h=11.01.05#n46>`__

   WKUP UART is generally available on the third serial port
   (/dev/ttyUSB2) and by default it only shows output from DM R5.

   Once the system has entered Deep Sleep or MCU Only mode as shown in the
   :ref:`LPM section<lpm_modes>`, wakeup from WKUP UART can be triggered
   by doing *any key press* on the WKUP UART terminal. No output will be
   visible on the WKUP UART terminal, but Linux resume messages will be
   printed on the MAIN UART terminal.


******************
USB Wakeup methods
******************

System wakeup is possible through the USB events in both Host and Device mode.

Host Mode Wakeup Events
=======================

The USB wakeup events in Host mode are described below:

Wakeup via a device connect event
---------------------------------

Follow the steps described in :ref:`LPM section<lpm_modes>` to enter desired
low power mode.

Now plug in a USB device to one of the port on the board and the system should wakeup. Post wakeup, the device would show up enumerated.
This can be checked by below command before and after suspending and waking up the system.

.. code-block:: console

  # lsusb -t

Wakeup via a device disconnect event
------------------------------------

Plug in a USB device to one of the port on the board and check that the device is enumerated by executing the below command.

.. code-block:: console

  # lsusb -t

Follow the steps described in :ref:`LPM section<lpm_modes>` to enter desired
low power mode.

Once the system is suspended, disconnect the USB device from the board and this should wakeup the system.
The device will not show up in list of USB enumerated devices. This can be verified by executing

.. code-block:: console

  # lsusb -t

Via Remote wakeup event
-----------------------

Use a device that supports USB suspend/resume and ensure that the USB device can suspend and resume correctly.
For a example a Logitech USB keyboard that supports suspend/resume. Follow below steps to check whether the keyboard is capable
to trigger a remote wakeup event to system.

Assuming the USB keyboard device is at /sys/bus/usb/devices/1-1/, enable USB autosuspend and wakeup

.. code-block:: console

   # echo auto > /sys/bus/usb/devices/1-1/power/control
   # echo enabled > /sys/bus/usb/devices/1-1/power/wakeup

Allow for two seconds of inactivity and check the runtime power status of the keyboard.
It should show "suspended", indicating that the keyboard has entered into suspend state.

.. code-block:: console

   # cat /sys/bus/usb/devices/1-1/power/runtime_status

Now press a key on the keyboard and check the runtime power status and it would come back to "active".

.. code-block:: console

   # cat /sys/bus/usb/devices/1-1/power/runtime_status

Follow the steps described in :ref:`LPM section<lpm_modes>` to enter desired
low power mode.

And once in suspended state, trigger system wakeup via remote wakeup event by typing keys on the keyboard. The system would wakeup.
And USB keyboard would still be present in the system's list of USB enumerated devices and this can be verified by executing

.. code-block:: console

   # lsusb -t

Device Mode Wakeup Events
=========================

Wakeup via connect event
------------------------

Load a USB gadget driver such as g_zero

.. code-block:: console

   # modprobe g_zero

Follow the steps described in :ref:`LPM section<lpm_modes>` to put the system enter desired
low power mode.

Once the system has entered the suspend state, plug a cable from a different Host system to the board's USB DRP port.
This should wakeup the system and gadget will be enumerated on the Host. Enumeration of the gadget on the Host system can be verified by executing the
below command on the Host system

.. code-block:: console

   # lsusb -t


********************
MCU IPC based Wakeup
********************

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   MCU IPC wakeup is not supported on AM62LX.

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX')

   It's possible to use IPC based wakeup events from the MCU core. For details on how to implement this
   from the firmware side, please refer to the relevant documentation:

   .. ifconfig:: CONFIG_part_variant in ('AM62X')

      `MCU+ SDK for AM62x <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62X/latest/exports/docs/api_guide_am62x/index.html>`__

   .. ifconfig:: CONFIG_part_variant in ('AM62AX')

      `MCU+ SDK for AM62Ax <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62AX/11_01_00_16/exports/docs/api_guide_am62ax/index.html>`__

   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

      `MCU+ SDK for AM62Px <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62PX/latest/exports/docs/api_guide_am62px/index.html>`__

   To use MCU IPC based wakeup, system should be placed into MCU Only mode
   as shown in the :ref:`LPM section<pm_mcu_only>`.

   Once the SoC enters MCU Only mode, the following log should be printed
   on the MCU UART (in most cases it will be /dev/ttyUSB3)

   .. code-block:: text

      [IPC RPMSG ECHO] Next MCU mode is 1
      [IPC RPMSG ECHO] Suspend request to MCU-only mode received
      [IPC RPMSG ECHO] Press a single key on this terminal to resume the kernel from MCU only mode

   Any *key press* on the same terminal should trigger a wakeup from MCU Only
   mode and the following message printed:

   .. code-block:: text

      [IPC RPMSG ECHO] Main domain resumed due to MCU UART

************************
CAN UART I/O Daisy Chain
************************

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   CAN UART wakeup is not supported on AM62LX.

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX')

   It is possible to wakeup the system from CAN UART pins in all supported low
   power modes. This is possible once CAN UART is configured.

   To set CAN UART as a wakeup source, a pinctrl state called "wakeup" needs to be
   added to the device tree. The "wakeup" pinctrl state will set the  WKUP_EN flag
   on the desired padconfig register. When the WKUP_EN flag (29th bit) is set, it
   allows the pad to act as a wakeup source. If CAN UART has the "wakeup" pinctrl
   state defined, then the Linux mcan driver is able to switch to the pinctrl
   "wakeup" state during suspend which enables CAN UART wakeup.

   The mcan_uart0 and mcan_uart1 nodes in
   `k3-am62x-sk-lpm-io-ddr-wkup-sources.dtso <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62x-sk-lpm-io-ddr-wkup-sources.dtso?h=11.01.05>`__
   can be used as a reference for enabling CAN UART wakeup.

   .. code-block:: text

      &mcu_pmx0 {
           mcu_mcan0_tx_pins_default: mcu-mcan0-tx-pins-default {
                   pinctrl-single,pins = <
                           AM62X_IOPAD(0x034, PIN_OUTPUT, 0) /* (D6) MCU_MCAN0_TX */
                   >;
           };

           mcu_mcan0_rx_pins_default: mcu-mcan0-rx-pins-default {
                   pinctrl-single,pins = <
                           AM62X_IOPAD(0x038, PIN_INPUT, 0) /* (B3) MCU_MCAN0_RX */
                   >;
           };

           mcu_mcan0_rx_pins_wakeup: mcu-mcan0-rx-pins-wakeup {
                   pinctrl-single,pins = <
                           AM62X_IOPAD(0x038, PIN_INPUT | WKUP_EN, 0) /* (B3) MCU_MCAN0_RX */
                   >;
           };
      };

      &mcu_mcan0 {
           pinctrl-names = "default", "wakeup";
           pinctrl-0 = <&mcu_mcan0_tx_pins_default>, <&mcu_mcan0_rx_pins_default>;
           pinctrl-1 = <&mcu_mcan0_tx_pins_default>, <&mcu_mcan0_rx_pins_wakeup>;
           status = "okay";
      };

   CAN UART wakeup can be tested by using either the
   `k3-am62x-sk-lpm-wkup-sources.dtso <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62x-sk-lpm-wkup-sources.dtso?h=11.01.05>`__
   or
   `k3-am62x-sk-lpm-io-ddr-wkup-sources.dtso <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62x-sk-lpm-io-ddr-wkup-sources.dtso?h=11.01.05>`__
   overlays. Please refer to :ref:`How to enable DT overlays<howto_dt_overlays>`
   for more details.

   Once the system has entered any low power mode as shown in the
   :ref:`LPM section<lpm_modes>`, wakeup from MCU_GPIO0_16 or MCU_MCAN0_RX can be
   triggered by grounding Pin 11 or Pin 22 on J8 MCU Header, respectively.

***********
RTC Ext Pin
***********

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX')

   This is not applicable for |__PART_FAMILY_DEVICE_NAMES__|.

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   To resume using RTC Ext pin wakeup, press the following button on the EVM:

   .. image:: /images/am62l_lpm_wakeup_evm_pin.jpg

********************************
Confirming the Wakeup event type
********************************

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   This is not applicable for AM62LX.

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX')

   When the SoC wakes up from any Low Power Mode, the Device Manager logs the wake
   reason, the pin number that triggered the wakeup, and the last low power mode
   entered. This wake reason and low power mode can be queried by Linux using the
   `TISCI LPM API <https://downloads.ti.com/tisci/esd/latest/2_tisci_msgs/pm/lpm.html>`__.
   The wakeup pin can be found in the datasheet by converting the pin number from
   hex to decimal and finding the corresponding PADCONFIG register.

   This wake reason is printed as part of the Linux suspend/resume log:

   .. code-block:: console

      [  249.471725] CPU3 is up
      [  249.472314] ti-sci 44043000.system-controller: ti_sci: wakeup source:0x80, pin:0x72, mode:0x1

   In the above example, the wakeup source of 0x80 is MAIN_IO. The 0x72 pin refers
   to PADCONFIG114. This means the cause of the wakeup event is UART0_RXD. The
   mode of 0x1 is the last low power mode entered which was MCU_ONLY.
