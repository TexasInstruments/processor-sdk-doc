##############
Suspend/Resume
##############

********
Overview
********

The user can deliberately force the system to low power state. There are
various levels: Suspend to memory(RAM), Suspend to disk, etc. Certains
parts support different levels of idle, such as DeepSleep0 or standby,
which allow additional wake-up sources to be used with less wake latency
at the expense of less power savings.

.. rubric:: Source Location

The files that provide suspend/resume differ from part to part however
they generally reside in arch/arm/mach-omap2/pm\*\*\*\*.c for the
higher-level code and arch/arm/mach-omap2/sleep\*\*\*\*.S for the
lower-level code.

.. rubric:: Kernel Configuration Options

Suspend/resume can be enable or disabled within the kernel using the
same method for all parts. To configure suspend/resume, enter the kernel
configuration tool using:

.. code-block:: console

   $ make menuconfig

Select *Power management options* from the main menu.

.. code-block:: menuconfig

   ...
   ...
   Kernel Features  --->
   Boot options  --->
   CPU Power Management  --->
   Floating point emulation  --->
   Userspace binary formats  --->
   Power management options  --->
   [*] Networking support  --->
   Device Drivers  --->
   ...
   ...

Select *Suspend to RAM and standby* to toggle the power management
support.

.. code-block:: menuconfig

   [*] Suspend to RAM and standby
   -*- Run-time PM core functionality
   ...
   < > Advanced Power Management Emulation

And then build the kernel as usual.

|

.. rubric:: IO Pad Configuration

In order to optimize power on the I/O supply rails, each pin can be
given a "sleep" configuration in addition to it's run-time
configuration. This can be handled with the pinctrl states defined in
the board device tree for each peripheral. These values are used to
configure the PAD\_CONF registers found in the control module of the
device which allow for selection of the MUXMODE of the pin and the
operation of the internal pull resistor. Typically a device defines it's
pinctrl state for normal operation:

.. code-block:: dts

   davinci_mdio_default: davinci_mdio_default {
      pinctrl-single,pins = <
         /* MDIO */
         0x148 (PIN_INPUT_PULLUP | SLEWCTRL_FAST | MUX_MODE0)    /* mdio_data.mdio_data */
         0x14c (PIN_OUTPUT_PULLUP | MUX_MODE0)                   /* mdio_clk.mdio_clk */
      >;
   };

In order to define a sleep state for the same device, another pinctrl
state can be defined:

.. code-block:: dts

   davinci_mdio_sleep: davinci_mdio_sleep {
      pinctrl-single,pins = <
         /* MDIO reset value */
         0x148 (PIN_INPUT_PULLDOWN | MUX_MODE7)
         0x14c (PIN_INPUT_PULLDOWN | MUX_MODE7)
      >;
   };

The driver then defines the sleep state in addition to the default
state:

.. code-block:: dts

   &davinci_mdio {
      pinctrl-names = "default", "sleep";
      pinctrl-0 = <&davinci_mdio_default>;
      pinctrl-1 = <&davinci_mdio_sleep>;
      ...

Although the driver core handles selection of the default state during
the initial probe of the driver, some extra work may be needed within
the driver to make sure the sleep state is selected during suspend and
the default state is re-selected at resume time. This is accomplished by
placing calls to ``pinctrl_pm_select_sleep_state`` at the end of the
suspend handler of the driver and ``pinctrl_pm_select_default_state`` at
the start of the resume handler. These functions will not cause failure
if the driver cannot find a sleep state so even with them added the
sleep state is still default. Some drivers rely on the default
configuration of the pins without any need for a default pinctrl entry
to be set but if a sleep state is added a default state must be added as
well in order for the resume path to be able to properly reconfigure the
pins. Most TI drivers included with the 3.12 release already have this
done.

The required pinctrl states will differ from board to board;
configuration of each pin is dependent on the specific use of the pin
and what it is connected to. Generally the most desirable configuration
is to have an internal pull-down and GPIO mode set which gives minimal
leakage. However, in a case where there are external pull-ups connected
to the line (like for I2C lines) it makes more sense to disable the pull
on the pin. The pins are supplied by several different rails which are
described in the data manual for the part in use. By measuring current
draw on each of these rails during suspend it may be possible to fine
tune the pin configuration for maximum power savings. The AM335x EVM has
pinctrl sleep states defined for its peripheral and serves as a good
example.

Even pins that are not in use and not connected to anything can still
leak some power so it is important to consider these pins as well when
implementing the pad configuration. This can be accomplished by defining
a pinctrl state for unused pins and then assigning it directly the the
pinctrl node itself in the board device tree so the state is configured
during boot even though there is no specific driver for these pins:

.. code-block:: dts

   &am43xx_pinmux {
      pinctrl-names = "default";
      pinctrl-0 = <&unused_wireless>;
      ...
      unused_pins: unused_pins {
         pinctrl-single,pins = <
            0x80    (PIN_INPUT_PULLDOWN | MUX_MODE7) /* gpmc_csn1.mmc1_clk */
            ...

CM3 Firmware
============

Suspend on am335x and am437x depends on interaction between the Linux
kernel and the wkup\_m3, so there are several requirements when building
the Linux kernel to ensure this will work. The following config options
are required when building a kernel to support suspend:

.. code-block:: kconfig

   # Firmware Loading from rootfs
   CONFIG_FW_LOADER_USER_HELPER=y
   CONFIG_FW_LOADER_USER_HELPER_FALLBACK=y

   # AMx3 Power Config Options
   CONFIG_MAILBOX=y
   CONFIG_OMAP2PLUS_MBOX=y
   CONFIG_WKUP_M3_RPROC=y
   CONFIG_SOC_TI=y
   CONFIG_WKUP_M3_IPC=y
   CONFIG_TI_EMIF_SRAM=y
   CONFIG_AMX3_PM=y

   CONFIG_RTC_DRV_OMAP=y

Note that it is also possible to build all of the options under
`` AMx3 Power Config Options `` as modules if desired. Finally, do not
forget the steps mentioned in the `CM3 Firmware <#cm3-firmware>`__
section of the guide to make sure the proper firmware binary is
available.

The LCPD release supports mem sleep and standby sleep. On both AM335 and
AM437 mem sleep corresponds to DeepSleep0. The following wake sources
are supported from DeepSleep0

-  UART
-  GPIO0
-  Touchscreen (AM335x only)

To enter DeepSleep0 enter the following at the command line:

.. code-block:: console

   $ echo mem > /sys/power/state

From here, the system will enter DeepSleep0. At any point, triggering
one of the aforementioned wake-up sources will cause the kernel to
resume and the board to exit DeepSleep0. A successful suspend/resume
cycle should look like this:

.. code-block:: console

   $ echo mem > /sys/power/state
     PM: Syncing filesystems ... done.
     Freezing user space processes ... (elapsed 0.007 seconds) done.
     Freezing remaining freezable tasks ... (elapsed 0.006 seconds) done.
     Suspending console(s) (use no_console_suspend to debug)
     PM: suspend of devices complete after 194.787 msecs
     PM: late suspend of devices complete after 14.477 msecs
     PM: noirq suspend of devices complete after 17.849 msecs
     Disabling non-boot CPUs ...
     PM: Successfully put all powerdomains to target state
     PM: Wakeup source UART
     PM: noirq resume of devices complete after 39.113 msecs
     PM: early resume of devices complete after 10.180 msecs
     net eth0: initializing cpsw version 1.12 (0)
     net eth0: phy found : id is : 0x4dd074
     PM: resume of devices complete after 368.844 msecs
     Restarting tasks ... done
   $

It is also possible to enter standby sleep with the possibility to use
additional wake sources and have a faster resume time while using
slightly more power. To enter standby sleep, enter the following at the
command line:

.. code-block:: console

   $ echo standby > /sys/power/state

A successful cycle through standby sleep should look the same as
DeepSleep0.

In the event that a cycle fails, the following message will be present
in the log:

.. code-block:: text

   PM: Could not transition all powerdomains to target state

This is usually due to clocks that have not properly been shut off
within the PER powerdomain. Make sure that all clocks within CM\_PER are
properly shut off and try again.


A small ARM Cortex-M3 co-processor is present on these parts that helps
the SoC to get to the lowest power mode. This processor requires
firmware to be loaded from the kernel at run-time for all low-power
features of the SoC to be enabled. The name of the binary file
containing this firmware is am335x-pm-firmware.elf for both SoCs. The
git repository containing the source and pre-compiled binaries of this
file can be found here:
https://git.ti.com/processor-firmware/ti-amx3-cm3-pm-firmware/commits/ti-v4.1.y
.

There are two options for loading the CM3 firmware. If using the
CoreSDK, the firmware will be included in /lib/firmware and the root
filesystem should handle loading it automatically. Placing any version
of ``am335x-pm-firmware.elf`` at this location will cause it to load
automatically during boot. However, due to changes in the upstream
kernel it is now required that
CONFIG\_FW\_LOADER\_USER\_HELPER\_FALLBACK be enabled if the
CONFIG\_WKUP\_M3\_IPC is being built-in to the kernel so that the
firmware can be loaded once userspace and the root filesystem becomes
avaiable. It is also possible to manually load the firmware by following
the instructions below:

The final option is to build the binary directly into the kernel. Note
that if the firmware binary is built into the kernel it cannot be loaded
using the methods above and will be automatically loaded during boot. To
accomplish this, first make sure you have placed
``am335x-pm-firmware.elf`` under ``<KERNEL SOURCE>/firmware``. Then
enter the kernel configuration by typing:

.. code-block:: console

   $ make menuconfig

Select *Device Drivers* from the main menu.

.. code-block:: menuconfig

   ...
   ...
   Kernel Features  --->
   Boot options  --->
   CPU Power Management  --->
   Floating point emulation  --->
   Userspace binary formats  --->
   Power management options  --->
   [*] Networking support  --->
   Device Drivers  --->
   ...
   ...

Select Generic Driver Options

.. code-block:: menuconfig

   Generic Driver Options
   CBUS support
   ...
   ...

Configure the name of the PM firmware and the location as shown below

.. code-block:: menuconfig

   ...
   -*- Userspace firmware loading support
   [*] Include in-kernel firmware blobs in the kernel binary
   (am335x-pm-firmware.elf) External firmware blobs to build into the kernel binary
   (firmware) Firmware blobs root directory

The CM3 firmware is needed for all idle low power modes on am335x and
am437x and for cpuidle on am335x. During boot, if the CM3 firmware has
been properly loaded, the following message will be displayed:

.. code-block:: text

   PM: CM3 Firmware Version = 0x191

CM3 Firmware Linux Kernel Interface
-----------------------------------

The kernel interface to the CM3 firmware is through the wkup\_m3\_rproc
driver, which is used to load and boot the CM3 firmware, and the
wkup\_m3\_ipc driver, which exposes an API to be used by the PM code to
communicate with the CM3 firmware.

.. rubric:: wkup\_m3\_rproc Driver

This driver is responsible for loading and booting the CM3 firmware on
the wkup\_m3 inside the SoC using the remoteproc framework.

Source Location:

`` drivers/remoteproc/wkup_m3_rproc.c ``

.. rubric:: wkup\_m3\_ipc Driver

This driver exposes an API to be used by the PM code to provide board
and SoC specific data from the kernel to the CM3 firmware, request
certain power state transitions, and query the status of any previous
power state transitions performed by the CM3 firmware.

Source Location:

`` drivers/soc/ti/wkup_m3_ipc.c `` - provides the wkup\_m3\_ipc driver
responsible for communicating with the CM3 firmware.

Debugging Techniques
--------------------

Debugging suspend and resume issues can be inherently difficult because
by nature portions of the processor may be clock gated or powered down,
making traditional methods difficult or impossible.

To aid your debugging efforts, the following resources are available:

-  `Debugging AM335x Suspend Resume
   Issues <http://processors.wiki.ti.com/index.php/Debugging_AM335x_Suspend-Resume_Issues>`__
   (wiki article)
-  `AM335x Low Power Design
   Guide <http://www.ti.com/lit/an/sprac74a/sprac74a.pdf>`__
-  `E2E support forums <https://e2e.ti.com>`__

|

RTC-Only and RTC+DDR Mode
-------------------------

RTC-Only and RTC+DDR modes are only supported on AM437x devices.

.. rubric:: DDR3 VTT Regulator Toggling

Some boards using DDR3 have a VTT Regulator that must be shut off during
suspend to further conserve power. There are two methods that can be
used to toggle DDR3 VTT regulators (or any GPIO for that matter) during
suspend on am335x and am437x, through the use of GPIO0 (AM335x and
AM437x) or IO Isolation (AM437x only).

.. rubric:: GPIO0 Toggling

An example of a board with this regulator is the AM335X EVM SK. On
AM335x and AM437x, GPIO0 remains powered during DS0 so it is possible to
use this to toggle a pin to control the VTT regulator. This is handled
by the wakeup M3 processor and gets defined inside the device node
within the board device tree file.

.. code-block:: dts

   &wkup_m3_ipc {
      ti,needs-vtt-toggle;
      ti,vtt-gpio-pin = <7>;
   };

``ti,needs-vtt-toggle`` is used to indicate that the vtt regulator must
be toggled and ``ti,vtt-gpio-pin`` indicates which pin within GPIO0 is
connected to the VTT regulator to control it.

IO Isolation Control
--------------------

Many of the pins on AM437x have the ability to configure both normal and
sleep states. Because of this it is possible to use any pin with a
corresponding CTRL\_CONF\_\* register in the control module and the
DS\_PAD\_CONFIG bits to toggle the VTT regulator enable pin. The DS
state of the pin must be configured such that the pin disables the VTT
regulator. The normal state of the pin must be configured such that the
VTT regulator is enabled by the state alone. This is because the VTT
regulator must be enabled before context is restored to the controlling
GPIO.

Example:

On the AM437x GP EVM, the VTT enable line must be held low to disable
VTT regulator and held high to enable, so the following pinctrl entry is
used. The DS pull is enabled which uses a pull down by default and DS
off mode is used which outputs a low by default. For the normal state, a
pull up is specified so that the VTT enable line gets pulled high
immediately after the DS states are removed upon exit from DeepSleep0.

The ``ti,set-io-isolation`` flag below in the ``wkup_m3_ipc`` node tells
the CM3 firmware to place the IO's in isolation and actually trigger the
value provided in the ``ddr3_vtt_toggle_default`` pinctrl entry.

.. code-block:: dts

   &am43xx_pinmux {
      pinctrl-names = "default";
      pinctrl-0 = <&ddr3_vtt_toggle_default>;

      ddr3_vtt_toggle_default: ddr_vtt_toggle_default {
      pinctrl-single,pins = <
         0x25C (DS0_PULL_UP_DOWN_EN | PIN_OUTPUT_PULLUP |
                DS0_FORCE_OFF_MODE | MUX_MODE7)>;
      };
      ...
   };

   wkup_m3_ipc: wkup_m3_ipc@1324 {
      compatible = "ti,am4372-wkup-m3-ipc";
      ...
      ...
      '''ti,set-io-isolation;'''
      ...
   };

Deep Sleep Voltage Scaling
--------------------------

It is possible to scale the voltages on both the MPU and CORE supply
rails down to 0.95V while we are in DeepSleep once powerdomains are shut
off. The i2c sequences needed to scale voltage vary from board to board
and are dependent on which PMIC is in use, so we use board specific
binaries that are passed to the CM3 firmware to define the sequences
needed during the sleep and wake paths. The CM3 firmware is then able to
write these sequences out at the proper location in the Deep Sleep path
on i2c0.

The CM3 firmware at
https://git.ti.com/processor-firmware/ti-amx3-cm3-pm-firmware/ti-v4.1.y/bin
contains scale data binaries for these platforms:

**am335x-evm-scale-data.bin**

-  AM335x EVM
-  AM335x Starter kit

**am335x-bone-scale-data.bin**

-  AM335x Beaglebone
-  AM335x Beaglebone Black

**am43x-evm-scale-data.bin**

-  AM437x GP EVM
-  AM437x EPOS EVM
-  AM437x SK EVM

The name of the binary to use is specified in the wkup\_m3\_ipc node
with the ``ti,scale-data-fw`` property of a board file like so:

.. code-block:: dts

   /* From arch/arm/boot/dts/am437x-gp-evm.dts */
   &wkup_m3_ipc {
      ...
      ti,scale-data-fw = "am43x-evm-scale-data.bin";
   };

The wkup\_m3\_ipc driver at\ ``drivers/soc/ti/wkup_m3_ipc.c`` handles
loading this binary to the proper data region of the CM3 and then
passing the offsets to the wake and sleep sequences through IPC register
5 to the firmware. As long as the format of the binary is proper the
driver will handle this automatically.

.. rubric:: Binary Data Format

Each binary file contains a small header with a magic number and offsets
to the sleep wand wake sections and then the sleep and wake sections
themsevles which consist of two bytes to specify the i2c bus speed for
the operation and then blocks of bytes that specify the message. The
header is 4 bytes long and is shown here:

+----------------+-------------------------+
| Size (bytes)   | Field                   |
+================+=========================+
| 2              | Magic Number (0x0c57)   |
+----------------+-------------------------+
| 1              | Offset to sleep data    |
+----------------+-------------------------+
| 1              | Offset to wake data     |
+----------------+-------------------------+

Table:  Scale data binary header

The offsets to the sleep and wake are counted from the first byte after
the header starting at zero and point to the first of the two bytes in
little-endian order that specify the bus speed in kHz. In all scale data
provided by TI the i2c bus speed is specified as 0x6400, which
corresponds to 100kHz. After these two bytes are the message blocks
which can have a variable length. A standard message block is defined
as:

+----------------+---------------------------------------------------------------------------+
| Size (bytes)   | Field                                                                     |
+================+===========================================================================+
| 1              | Message size, counting from first byte \*after\* I2C Bus address below.   |
+----------------+---------------------------------------------------------------------------+
| 1              | I2C Bus Address                                                           |
+----------------+---------------------------------------------------------------------------+
| 1              | First byte of message (typically I2C register address)                    |
+----------------+---------------------------------------------------------------------------+
| 1              | Second byte of message (typically value to write to register)             |
+----------------+---------------------------------------------------------------------------+
| 1              | Nth byte of message                                                       |
+----------------+---------------------------------------------------------------------------+
| ...            | ...                                                                       |
+----------------+---------------------------------------------------------------------------+

Table:  Scale data message block

Each block is a single I2C transaction, and multiple blocks can be
placed one after the other to send multiple messages, as is needed in
the case of PMICs which have GO bits to actually apply the programmed
voltage to the rail.

|

Simple Example
--------------

Single message for both sleep and wake sequence (from
bin/am335x-evm-scale-data.bin).

Raw binary data using xxd:

.. code-block:: console

   a0274052local@uda0274052:~/git-repos/amx3-cm3$ xxd bin/am335x-evm-scale-data.bin
   0000000: 0c57 0006 0034 022d 251f 0034 022d 252b  .W...4.-%..4.-%+

Explanation of values:

.. code-block:: text

   0c57        # Magic number
   00      # Offset from first byte after header to sleep section
   06      # Offset from first byte after header to wake section

   0034        # Sleep sequence section, starts with two bytes to describe i2c bus in khz (100)
   02 2d 25 1f # Length of message, evm i2c bus addr, then message (i2c reg 0x25, write value 0x1f)

   0034        # Wake sequence section, starts with two bytes to describe i2c bus in khz (100)
   02 2d 25 2b # Length of message, evm i2c bus addr, then message (i2c reg 0x25, write value 0x2b)

Advanced Example
----------------

Multiple messages on sleep and wake sequence (from
bin/am43x-evm-scale-data.bin).

Raw binary data using xxd:

.. code-block:: console

   amx3-cm3$ xxd bin/am43x-evm-scale-data.bin
   0000000: 0c57 0012 0034 0224 106b 0224 168a 0224  .W...4.$.k.$...$
   0000010: 1067 0224 1a86 0034 0224 106b 0224 1699  .g.$...4.$.k.$..
   0000020: 0224 1067 0224 1a86                      .$.g.$..

Explanation of values:

.. code-block:: text

   0C 57           # Magic number 0x0C57
   00          # Offset, starting after header, to sleep sequence
   12          # Offset, starting after header, to wake sequence

   0034            # Sleep sequence section, starts with two bytes to describe i2c bus in khz (100)
   02 24 10 6b     # msg length 0x02, to i2c addr 0x24, message is (i2c reg 0x10, write 0x6b)
   02 24 16 8a     # msg length 0x02, to i2c addr 0x24, message is (i2c reg 0x16, write 0x8a)
   02 24 10 67     # msg length 0x02, to i2c addr 0x24, message is (i2c reg 0x10, write 0x67)
   02 24 1a 86     # msg length 0x02, to i2c addr 0x24, message is (i2c reg 0x1a, write 0x86)

   0034            # Wake sequence section, starts with two bytes to describe i2c bus in khz (100)
   02 24 10 6b     # msg length 0x02, to i2c addr 0x24, message is (i2c reg 0x10, write 0x6b)
   02 24 16 99     # msg length 0x02, to i2c addr 0x24, message is (i2c reg 0x16, write 0x99)
   02 24 10 67     # msg length 0x02, to i2c addr 0x24, message is (i2c reg 0x10, write 0x67)
   02 24 1a 86     # msg length 0x02, to i2c addr 0x24, message is (i2c reg 0x1a, write 0x86)

|


