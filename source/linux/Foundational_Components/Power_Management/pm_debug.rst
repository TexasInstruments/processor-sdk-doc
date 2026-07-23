.. _pm_debug:

#################
Debug Information
#################

***************
Low Power Modes
***************

As described in the :ref:`S/W Architecture section<pm_sw_arch>`,
implementing Low Power Modes like DeepSleep requires a synchronization
between multiple software components. Debugging a LPM issue
requires finding out which component (Linux, TF-A, TIFS or DM R5) might
be at fault.

The comprehensive way of debugging DeepSleep starts by looking at all
the commands that have been executed by the DM R5. The steps for getting
this trace and interpreting the logs has been documented in the following FAQ:
`How can we debug DeepSleep on AM62x/AM62A/AM62P using SYSFW Trace?
<https://e2e.ti.com/support/processors-group/processors/f/processors-forum/1323581/faq-processor-sdk-am62x-a-p-how-can-we-debug-deep-sleep-on-am62x-am62a-am62p-using-sysfw-trace/5103851#5103851>`__

Decoding set constraint debug messages
======================================

The logs after resume can be used to debug the constraints sent during suspend. Alternatively, the console
suspend can be delayed to get these logs at suspend time using the below command:

.. code-block:: console

        root@<machine>:~# echo N | sudo tee /sys/module/printk/parameters/console_suspend

.. rubric:: Device constraints

Example of setting device constraint is shown below.

.. code-block:: dmesg

        [   45.640758] ti-sci 44043000.system-controller: ti_sci_cmd_set_device_constraint: device: 179: state: 1: ret 0

The above log implies that the device constraint has been set (state: 1) on device 179 successfully (ret: 0)
The device can be found using

.. rubric:: Interpreting the device number

The :code:`device: X` contains information about which device the constraint is set on. This will
essentially be the same as the number in front of :code:`k3_pds` as shown below: (It's 179 for usb1)

.. code-block:: dts

                usbss1: dwc3-usb@f910000 {
                        compatible = "ti,am62-usb";
                        reg = <0x00 0x0f910000 0x00 0x800>,
                              <0x00 0x0f918000 0x00 0x400>;
                        clocks = <&k3_clks 162 3>;
                        clock-names = "ref";
                        ti,syscon-phy-pll-refclk = <&usb1_phy_ctrl 0x0>;
                        #address-cells = <2>;
                        #size-cells = <2>;
                        power-domains = <&k3_pds 179 TI_SCI_PD_EXCLUSIVE>;
                        ranges;
                        status = "disabled";

                        usb1: usb@31100000 {
                                compatible = "snps,dwc3";
                                reg =<0x00 0x31100000 0x00 0x50000>;
                                interrupts = <GIC_SPI 226 IRQ_TYPE_LEVEL_HIGH>,
                                             <GIC_SPI 226 IRQ_TYPE_LEVEL_HIGH>;
                                interrupt-names = "host", "peripheral";
                                maximum-speed = "high-speed";
                                dr_mode = "otg";
                        };
                };

.. rubric:: Latency constraint

.. code-block:: dmesg

        [   45.648993] cpu cpu3: ti_sci_suspend: sending max CPU latency=100
        [   45.649033] ti-sci 44043000.system-controller: ti_sci_cmd_set_latency_constraint: latency: 100: state: 1: ret 0

The above log implies that the latency constraint has been set (state: 1) by system CPUs successfully (ret: 0)

