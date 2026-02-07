#########################
RTC-Only and RTC+DDR Mode
#########################

AM437x supports two RTC modes, RTC+DDR and RTC-Only mode. RTC+DDR Mode is similar to the
Suspend/Resume above but only supports wake by the Power Button present
on the board or from an RTC ALARM2 Event. RTC-Only mode supports the
same wake sources, however DDR context is not maintained so a wake event
causes a cold boot.

RTC-Only mode is supported on:

-  AM437x GP EVM
-  AM437x SK EVM

RTC+DDR mode is supported on:

-  AM437x GP EVM

.. rubric:: RTC+DDR Mode

The first step in using RTC+DDR mode is to enable off mode by typing the
following at the command line:

.. code-block:: console

        $ echo 1 > /sys/kernel/debug/pm_debug/enable_off_mode

With off-mode enabled, a command to enter DeepSleep0 will now enter
RTC-Only mode:

.. code-block:: console

        $ echo mem > /sys/power/state

This method of entry only supports Power button as the wake source.

To use the rtc as a wake source, after enabling off mode use the
following command:

.. code-block:: console

        $ rtcwake -s <NUMBER OF SECONDS TO SLEEP> -d /dev/rtc0 -m mem

Whether or not your board enters RTC-Only mode or RTC+DDR mode depends
on the regulator configuration and whether or not the regulator that
supplies the DDR is configured to remain on during suspend. This is
supported by the TPS65218 in use of the AM437x boards but not the
TPS65217 or TPS65910 present on AM335x boards.

.. code-block:: dts

    tps65218: tps65218@24 {
            reg = <0x24>;
            compatible = "ti,tps65218";
            interrupts = <GIC_SPI 7 IRQ_TYPE_NONE>; /* NMIn */
            interrupt-parent = <&gic>;
            interrupt-controller;
            #interrupt-cells = <2>;

            ...

            dcdc3: regulator-dcdc3 {
                    compatible = "ti,tps65218-dcdc3";
                    regulator-name = "vdcdc3";
                    regulator-suspend-enable;
                    regulator-min-microvolt = <1500000>;
                    regulator-max-microvolt = <1500000>;
                    regulator-boot-on;
                    regulator-always-on;
            };

            ...

    };

Another important thing to make sure of is that you are using the proper
u-boot. A certain u-boot is required in order to support RTC+DDR mode
otherwise the following message appears during boot of the kernel:

``PM: bootloader does not support rtc-only!``

When building u-boot, rather than using ``am43xx_evm_config`` you must
use ``am43xx_evm_rtconly_config`` to support either RTC mode.

.. rubric:: RTC-Only Mode

RTC-Only mode does not maintain DDR context so placing a board into
RTC-only mode allows for very low power consumption after which a
supported wake source will cause a cold boot. RTC-Only mode is entered
via the poweroff command.

To wakeup from RTC-Only mode via an RTC alarm, a separate tool must be
used to program an RTC alarm prior to entering poweroff.
